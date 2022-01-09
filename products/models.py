from django.db import models
from django import forms
from django.http.response import HttpResponse
from django.shortcuts import  render

# Create your models here.
from markets.models import Market

class ProductCategory(models.Model):
    name = models.CharField('이름',max_length=50)

class Product(models.Model):
    reg_date = models.DateTimeField('등록날짜', auto_now_add=True)
    update_date = models.DateTimeField('갱신날짜', auto_now=True)
    is_deleted = models.BooleanField('삭제여부', default=False)
    delete_date = models.DateTimeField('삭제날짜', null=True, blank=True)
    market = models.ForeignKey(Market, on_delete=models.DO_NOTHING)
    name = models.CharField('상품명(내부용)', max_length=100)
    display_name = models.CharField('상품명(고객용)', max_length=100)
    price = models.PositiveIntegerField('권장판매가')
    sale_price = models.PositiveIntegerField('실제판매가')
    is_hidden = models.BooleanField('노출여부', default=False)
    is_sold_out = models.BooleanField('품절여부', default=False)
    category = models.ForeignKey(ProductCategory, on_delete=models.DO_NOTHING)
    hit_count = models.PositiveIntegerField('조회수', default=0)
    review_count = models.PositiveIntegerField('리뷰수', default=0)
    review_point = models.PositiveIntegerField('리뷰평점', default=0)
    image = models.ImageField(upload_to=f"products/",null=True)

    def thumb_img_url(self):
        if self.image:
            return self.image.url
        else:
            try:
                return f"http://site1.honeycombpizza.link/media/products/{self.id}.jpg"
                #return f"http://localhost:8000/media/products/{self.id}.jpg"
            except:
                return "이미자없음"


    def colors(self):
        colors = []
        product_reals = self.productreal.all()
        for product_real in product_reals:
            colors.append(product_real.option_2_name)
        html = ''
        colors=list(set(colors))
        for color in colors:
            if color == "와인":
                _color = "purple"
            elif color == "그린":
                _color = "green"
            elif color == "레드":
                _color = "red"
            elif color == "핑크":
                _color = "pink"
            else:
                return f"{_color} 가 출력되었음"
            html += f"""<span style="width:10px; height:10px; display:inline-block; border-radius:50%; margin:0 3px; background-color:{_color};"></span>"""

        html = html
        return html

    def __str__(self):
        try:
            return self.display_name + self.image.upload_to
        except:
            return self.display_name


class ProductReal(models.Model):
    reg_date = models.DateTimeField('등록날짜', auto_now_add=True)
    update_date = models.DateTimeField('갱신날짜', auto_now=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="productreal")
    option_1_type = models.CharField('옵션1 타입', max_length=10, default='SIZE')
    option_1_name = models.CharField('옵션1 이름(내부용)', max_length=50)
    option_1_display_name = models.CharField('옵션1 이름(고객용)', max_length=50)
    option_2_type = models.CharField('옵션2 타입', max_length=10, default='COLOR')
    option_2_name = models.CharField('옵션2 이름(내부용)', max_length=50)
    option_2_display_name = models.CharField('옵션2 이름(고객용)', max_length=50)
    option_3_type = models.CharField('옵션3 타입', max_length=10, default='', blank=True)
    option_3_name = models.CharField('옵션3 이름(내부용)', max_length=50, default='', blank=True)
    option_3_display_name = models.CharField('옵션3 이름(고객용)', max_length=50, default='', blank=True)
    is_sold_out = models.BooleanField('품절여부', default=False)
    is_hidden = models.BooleanField('노출여부', default=False)
    add_price = models.IntegerField('추가가격', default=0)
    stock_quantity = models.PositiveIntegerField('재고개수', default=0)
    
    def color(self):
        color = self.option_2_name
        html = ""
        if color == "와인":
            _color = "purple"
        elif color == "그린":
            _color = "green"
        elif color == "레드":
            _color = "red"
        elif color == "핑크":
            _color = "pink"
        html += f"<span style=\"color:{_color}\">{self.option_2_display_name}</span><br>"
        return html
        
    def c(self):
        color = self.option_2_name
        html = ""
        if color == "와인":
            _color = "purple"
        elif color == "그린":
            _color = "green"
        elif color == "레드":
            _color = "red"
        elif color == "핑크":
            _color = "pink"
        html =_color
        return html

    def __str__(self):
        return f"{self.product}상품 사이즈 : {self.option_1_display_name} 컬러 : {self.option_2_display_name} 추가됨"