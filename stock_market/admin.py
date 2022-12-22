from django.contrib import admin
from stock_market.models import Stock

# Register your models here.
class StockAdmin(admin.ModelAdmin):
    list_display = ('id','date')
   
admin.site.register(Stock,StockAdmin)

