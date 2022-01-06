import string

from django.db import migrations, models
import django.db.models.deletion

from products.models import ProductCategory, Product, ProductReal


def gen_master_product_category(apps, schema_editor):
    ProductCategory(name='구두').save()
    ProductCategory(name='니트').save()
    ProductCategory(name='롱스커트').save()
    ProductCategory(name='숏스커트').save()
    ProductCategory(name='청바지').save()
    ProductCategory(name='청자켓').save()
    ProductCategory(name='청치마').save()
    ProductCategory(name='코트').save()
    ProductCategory(name='백').save()
    ProductCategory(name='블라우스').save()


def gen_product(market_id: int, name: string, display_name: string, price: int, opt_1_names: (string), is_hidden: bool, is_sold_out: bool, hit_count: int, review_count: int, review_point: int,image=""):
    category_id = ProductCategory.objects.filter(name=name).first().id

    opt_2_names = ('레드', '와인', '그린', '핑크',)
    opt_2_display_names = ('감성레드', '감성와인', '감성그린', '감성핑크',)

    product = Product(market_id=market_id, name=name, display_name=display_name, price=price, sale_price=price - 1000,
                      category_id=category_id, is_hidden=is_hidden, is_sold_out=is_sold_out, hit_count=hit_count,
                      review_count=review_count, review_point=review_point)
    product.save()

    for opt_1_name in opt_1_names:
        opt_1_display_name = opt_1_name
        for opt_2_index, opt_2_name in enumerate(opt_2_names):
            opt_2_display_name = opt_2_display_names[opt_2_index]
            ProductReal(product=product, option_1_name=opt_1_name, option_1_display_name=opt_1_display_name,
                        option_2_name=opt_2_name, option_2_display_name=opt_2_display_name).save()


def gen_master_product(apps, schema_editor):
    price = 10000
    hit_count = 1000
    review_count = 100
    review_point = 3

    gen_product(1, '구두', '인스타 셀럽 구두', price, ('235, 3cm', '235, 6cm', '240, 3cm', '240, 6cm', '245, 3cm', '245, 6cm',),
                False, False, hit_count, review_count, review_point)
    gen_product(1, '구두', '아이돌 구두', price + 2000,
                ('235, 3cm', '235, 6cm', '240, 3cm', '240, 6cm', '245, 3cm', '245, 6cm',),
                False, False, hit_count + 500, review_count + 50, review_point + 1)

    price = 12000
    hit_count = 2000
    review_count = 200
    review_point = 4

    gen_product(1, '니트', '인스타 셀럽 니트', price, ('XS', 'S', 'M', 'L', 'XL',),
                False, False, hit_count, review_count, review_point,'products/3.jpg')
    gen_product(1, '니트', '아이돌 니트', price + 2000,
                ('XS', 'S', 'M', 'L', 'XL',),
                False, False, hit_count + 500, review_count + 50, review_point + 1)

    price = 14000
    hit_count = 2000
    review_count = 200
    review_point = 4

    gen_product(1, '롱스커트', '인스타 셀럽 롱스커트', price, ('FREE',),
                False, False, hit_count, review_count, review_point)
    gen_product(1, '롱스커트', '아이돌 롱스커트', price + 2000,
                ('FREE',),
                False, False, hit_count + 500, review_count + 50, review_point + 1)

    price = 10000
    hit_count = 1000
    review_count = 100
    review_point = 2

    gen_product(1, '숏스커트', '인스타 셀럽 숏스커트', price, ('FREE',),
                False, False, hit_count, review_count, review_point)
    gen_product(1, '숏스커트', '아이돌 숏스커트', price + 2000,
                ('FREE',),
                False, False, hit_count + 500, review_count + 50, review_point + 1)

    price = 20000
    hit_count = 1300
    review_count = 130
    review_point = 3

    gen_product(2, '청바지', '인스타 셀럽 청바지', price, ('XS', 'S', 'M', 'L', 'XL',),
                False, False, hit_count, review_count, review_point)
    gen_product(2, '청바지', '아이돌 청바지', price + 2000,
                ('XS', 'S', 'M', 'L', 'XL',),
                False, False, hit_count + 500, review_count + 50, review_point + 1)

    price = 30000
    hit_count = 1400
    review_count = 140
    review_point = 3

    gen_product(2, '청자켓', '인스타 셀럽 청자켓', price, ('34', '36',),
                False, False, hit_count, review_count, review_point)
    gen_product(2, '청자켓', '아이돌 청자켓', price + 2000,
                ('34', '36',),
                False, False, hit_count + 500, review_count + 50, review_point + 1)

    price = 15000
    hit_count = 700
    review_count = 50
    review_point = 2

    gen_product(2, '청치마', '인스타 셀럽 청치마', price, ('FREE',),
                False, False, hit_count, review_count,review_point)
    gen_product(2, '청치마', '아이돌 청치마', price + 2000, ('FREE',), False, False, hit_count + 500, review_count + 50, review_point + 1)

    price = 75000
    hit_count = 1700
    review_count = 150
    review_point = 4

    gen_product(3, '코트', '인스타 셀럽 코트', price, ('FREE',),
                False, False, hit_count, review_count, review_point)
    gen_product(3, '코트', '아이돌 코트', price + 2000,
                ('FREE',),
                False, False, hit_count + 500, review_count + 50, review_point + 1)

    price = 175000
    hit_count = 1800
    review_count = 190
    review_point = 4

    gen_product(3, '백', '인스타 셀럽 백', price, ('FREE',),
                False, False, hit_count, review_count, review_point)
    gen_product(3, '백', '아이돌 백', price + 2000,
                ('FREE',),
                False, False, hit_count + 500, review_count + 50, review_point + 1)

    price = 25000
    hit_count = 800
    review_count = 90
    review_point = 2

    gen_product(3, '블라우스', '인스타 셀럽 블라우스', price, ('XS', 'S', 'M', 'L', 'XL',),
                False, False, hit_count, review_count, review_point)
    gen_product(3, '블라우스', '아이돌 블라우스', price + 2000,
                ('XS', 'S', 'M', 'L', 'XL',),
                False, False, hit_count + 500, review_count + 50, review_point + 1)


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('markets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='이름')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='갱신날짜')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='삭제여부')),
                ('delete_date', models.DateTimeField(blank=True, null=True, verbose_name='삭제날짜')),
                ('name', models.CharField(max_length=100, verbose_name='상품명(내부용)')),
                ('display_name', models.CharField(max_length=100, verbose_name='상품명(고객용)')),
                ('price', models.PositiveIntegerField(verbose_name='권장판매가')),
                ('sale_price', models.PositiveIntegerField(verbose_name='실제판매가')),
                ('is_hidden', models.BooleanField(default=False, verbose_name='노출여부')),
                ('is_sold_out', models.BooleanField(default=False, verbose_name='품절여부')),
                ('hit_count', models.PositiveIntegerField(default=0, verbose_name='조회수')),
                ('review_count', models.PositiveIntegerField(default=0, verbose_name='리뷰수')),
                ('review_point', models.PositiveIntegerField(default=0, verbose_name='리뷰평점')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.productcategory')),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='markets.market')),
                ('image', models.ImageField(null=True, upload_to='products/')),
            ],
        ),
        migrations.CreateModel(
            name='ProductReal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='갱신날짜')),
                ('option_1_type', models.CharField(default='SIZE', max_length=10, verbose_name='옵션1 타입')),
                ('option_1_name', models.CharField(max_length=50, verbose_name='옵션1 이름(내부용)')),
                ('option_1_display_name', models.CharField(max_length=50, verbose_name='옵션1 이름(고객용)')),
                ('option_2_type', models.CharField(default='COLOR', max_length=10, verbose_name='옵션2 타입')),
                ('option_2_name', models.CharField(max_length=50, verbose_name='옵션2 이름(내부용)')),
                ('option_2_display_name', models.CharField(max_length=50, verbose_name='옵션2 이름(고객용)')),
                ('option_3_type', models.CharField(blank=True, default='', max_length=10, verbose_name='옵션3 타입')),
                ('option_3_name', models.CharField(blank=True, default='', max_length=50, verbose_name='옵션3 이름(내부용)')),
                ('option_3_display_name',
                 models.CharField(blank=True, default='', max_length=50, verbose_name='옵션3 이름(고객용)')),
                ('is_sold_out', models.BooleanField(default=False, verbose_name='품절여부')),
                ('is_hidden', models.BooleanField(default=False, verbose_name='노출여부')),
                ('add_price', models.IntegerField(default=0, verbose_name='추가가격')),
                ('stock_quantity', models.PositiveIntegerField(default=0, verbose_name='재고개수')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productreal', to='products.product')),
            ],
        ),
        migrations.RunPython(gen_master_product_category),
        migrations.RunPython(gen_master_product),
    ]