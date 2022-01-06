from django.contrib.contenttypes.models import ContentType
from django.shortcuts import  render, get_object_or_404, redirect, resolve_url
from django.utils import timezone
from .models import Product,ProductReal
from .forms import QuestionForm
from questions.models import Question
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def index(request):
    """
    목록 출력
    """
    return render(request, 'welcome.html')

def list(request):
    """
    목록 출력
    """# 입력 파라미터
    page = request.GET.get('page', '1')  # page
    # 조회
    search = request.GET.get('search','')
    if search:
        product_list = Product.objects.all().filter(display_name__contains=search)
    else:
        product_list = Product.objects.all()
    # 페이징 처리
    paginator = Paginator(product_list, 4)  # 페이지당 10개씩 보여줌
    page_obj = paginator.get_page(page)
    context = {'product_list': page_obj}
    return render(request, 'products/products_list.html', context)

def detail(request, product_id):
    product = Product.objects.get(id=product_id)
    options = product.productreal.all()
    ##컨텐트타입과 프로덕트 id로 질문들을 조회
    questions = Question.objects.filter(
        object_id=product_id
    ).filter(
        content_type = ContentType.objects.get(model='product')
    )
    context = {'product': product,'questions':questions, 'options': options}
    return render(request, 'products/products_detail.html', context)


@login_required(login_url='accounts:signin')
def question_create(request, product_id):
    """
    질문등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.object_id = product_id
            question.content_type = ContentType.objects.get(app_label='products', model='product')
            question.save()
        else:
            form = QuestionForm()
    return redirect('products:detail', product_id=product_id)

@login_required(login_url='accounts:signin')
def question_modify(request, product_id,question_id):
    """
    pybo 질문댓글수정
    """
    question = get_object_or_404(Question, pk=question_id)
    product = get_object_or_404(Product, pk=product_id)
    if request.user != question.user:
        messages.error(request, '댓글 수정권한이 없습니다')
        return redirect('products:detail', product_id=product_id)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()
            question.save()
            
            context = {'form': form,'product': product}
            return redirect('products:detail', product_id=product.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form,'question':question,
                'product': product}
    return render(request, 'products/question_form.html', context)

@login_required(login_url='accounts:signin')
def question_delete(request, product_id,question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.user:
        messages.error(request, '댓글 삭제권한이 없습니다')
        return redirect('products:detail', product_id=product_id)
    question.delete()
    return redirect('products:detail', product_id=product_id)
    
@login_required(login_url='accounts:signin')
def question_create_save(request):

    form = QuestionForm()
    return render(request, 'products/products_form.html', {'form': form})




