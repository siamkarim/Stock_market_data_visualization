from django.db import models
from datetime import datetime
import json


 # Create your models here.
class Stock (models.Model):
    date = models.DateTimeField(blank=True, default=datetime.now)
    trade_code = models.CharField(max_length=100)
    high = models.FloatField()
                      
    low = models.FloatField()
    open = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()

    # class Meta:
    #     db_table="stock_market_data"

    def __str__(self):
        return str(self.pk)+ " " + self.date+ " "+ self.trade_code+ " "+ self.high+" "+ self.low+" "+ self.open+" "+ self.close+" "+ self.volume
    