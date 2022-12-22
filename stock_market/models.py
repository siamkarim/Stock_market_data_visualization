from django.db import models
from datetime import datetime
import json


 # Create your models here.
class Stock (models.Model):
    date = models.DateTimeField(blank=True, default=datetime.now)
    trade_code = models.CharField(max_length=100)
    high = models.DecimalField(max_digits = 5,decimal_places = 2)
                      
    low = models.DecimalField(max_digits = 5,decimal_places = 2)
    open = models.DecimalField(max_digits = 5,decimal_places = 2)
    close = models.DecimalField(max_digits = 5,decimal_places = 2)
    volume = models.CharField(max_length=100)

    class Meta:
        db_table="stockdb"

    # def __str__(self):
    #     return str(self.pk)+ " " + self.date+ " "+ self.trade_code+ " "+ self.high+" "+ self.low+" "+ self.open+" "+ self.close+" "+ self.volume
    @classmethod
    def create(cls, **kwargs):
        stock = cls.objects.create(  
            date = kwargs['date'],
            trade_code = kwargs['trade_code'],
            high = kwargs['high'],
            low = kwargs['low'],
            open = kwargs['open'],
            close = kwargs['close'],
            volume = kwargs['volume'])

        with open('janatawifi/data/stock_market_data.json', encoding='utf-8') as data_file:
              json_data = json.loads(data_file.read())
        for stock_market_data in json_data:
               stock = Stock.create(**stock_market_data)

        return stock
    