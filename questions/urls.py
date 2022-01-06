from django.urls import path,include
from products import views


app_name = 'questions'

##
urlpatterns = [
    # path('question/create/<int:product_id>/', views.question_create, name='create'),
    # path('question/<int:question_id>/modify',views.question_modify, name='modify'),
    # path('question/<int:question_id>/delete',views.question_delete, name='delete'),
    # path('<int:product_id>/question/<int:question_id>/',include('question.urls'))
]