from django.shortcuts import render
from stock_market import forms
from stock_market.models import Stock
from stock_market.forms import StockForm
from django.contrib import messages
from .utils import get_plot
# Create your views here.

import json

def index(request):
        #   with open('janatawifi/data/stock_market_data.json', encoding='utf-8') as data_file:
        #       json_data = json.loads(data_file.read())
        
          sql_data = Stock.objects.all()
          context = {'data': sql_data}
        
          return render(request,'home/index.html',context)



def edit(request,id):
      # display = Stock.objects.order_by(id)
      displayStock = Stock.objects.get(id=id )
      return render(request,"home/edit.html",{"stock":displayStock})


def update(request,stock_id):
    stock_info = Stock.objects.get(pk=stock_id)

    form = StockForm(request.POST, instance=stock_info)
    
  
      
    if form.is_valid():
            form.save()
            messages.success(request,"Record Updated Successfully...!!")
            return render(request,"home/edit.html",{"stock": stock_info})




def graph(request):
      # display = Stock.objects.order_by(id)
      axis = Stock.objects.all()
      x = [x.id for x in axis]
      y = [y.close for y in axis]
      chart = get_plot(x,y)
      return render(request,"home/graph.html",{"chart":chart})