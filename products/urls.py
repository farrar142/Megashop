from django.urls import path,include
from products import views


app_name = 'products'


urlpatterns = [
    path('list/', views.list, name="list"),
    path('<int:product_id>/', views.detail, name='detail'),
    path('question/create/<int:product_id>/', views.question_create, name='question_create'),
    path('<int:product_id>/question/<int:question_id>/modify',views.question_modify, name='question_modify'),
    path('<int:product_id>/question/<int:question_id>/delete',views.question_delete, name='question_delete'),
]
