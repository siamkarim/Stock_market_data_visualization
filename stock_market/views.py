from django.shortcuts import render

# Create your views here.

import json

def index(request):
          with open('janatawifi/data/stock_market_data.json', encoding='utf-8') as data_file:
              json_data = json.loads(data_file.read())
  
          context = {'data': json_data}
        
          return render(request,'home/index.html',context)
