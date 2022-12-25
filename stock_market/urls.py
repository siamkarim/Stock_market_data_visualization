from django.urls import path
from . import views

app_name = "stock_market"
urlpatterns = [
  path('', views.index, name='index'),
  path('graph', views.graph, name='graph'),
  path('update/<int:id>/',views.update, name='update'),
  path('edit',views.edit, name='edit')

]
 
