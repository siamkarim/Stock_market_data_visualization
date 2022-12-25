from django.shortcuts import render
from stock_market import forms
from stock_market.models import Stock
from stock_market.forms import StockForm
from django.contrib import messages
from .utils import get_plot
# Create your views here.
import pyodbc


def index(request):
        #   with open('janatawifi/data/stock_market_data.json', encoding='utf-8') as data_file:
        #       json_data = json.loads(data_file.read())
      conn = pyodbc.connect('Driver={sql server};'
                           'Server=DESKTOP-QU9OGJQ;'
                           'Database=test;'
                           'Trusted_Connection=yes;')   
      cursor=conn.cursor()
      cursor.execute("select * from stock_market_data")  
      result= cursor.fetchall()

      return render(request,'home/index.html',{'data':result})



def edit(request):
      conn = pyodbc.connect('Driver={sql server};'
                           'Server=DESKTOP-QU9OGJQ;'
                           'Database=test;'
                           'Trusted_Connection=yes;') 
      # display = Stock.objects.order_by(id)
      if request.method=="POST":
            if request.POST.get('date') and request.POST.get('trade_code') and request.POST.get('high') and request.POST.get('low') and request.POST.get('open')and request.POST.get('close') and request.POST.get('volume'):
                  insertValue = Stock()
                  insertValue.date=request.POST.get('')
                  insertValue.trade_code=request.POST.get('')
                  insertValue.high=request.POST.get('')
                  insertValue.low=request.POST.get('')
                  insertValue.open=request.POST.get('')
                  insertValue.close=request.POST.get('')
                  insertValue.volume=request.POST.get('')
                  cursor=conn.cursor()
                  cursor.execute("insert into stock_market_data values('"+insertValue.date+"','"+insertValue.trade_code+"','"+insertValue.high+"','"+insertValue.low+"','"+insertValue.open +"','"+insertValue.close+"','"+insertValue.volume+ "')")  
                  cursor.commit()
                  return render(request,"home/edit.html")

      else:

         return render(request,"home/edit.html")


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