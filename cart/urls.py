from django.urls import path, re_path
from . import views

app_name = 'cart'

urlpatterns=[
    path('detail/',views.detail,name='detail'),
    path('add_product/',views.add_product,name='add_product'),
    path('detail/modify/<int:cartitem_id>',views.modify_quantity,name="modify"),
    path('detail/delete/<int:cartitem_id>',views.delete_cartitem,name="delete"),
]