from django.urls import path
from .views import list_venda, create_venda, update_venda, delete_venda

urlpatterns = [
    path('', list_venda, name='list_venda'),
    path('new', create_venda, name='create_venda'),
    path('update/<int:id>/', update_venda, name='update_venda'),
    path('delete/<int:id>/', delete_venda, name='delete_venda'),


]