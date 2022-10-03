from django.db import models

class Orders(models.Model):
    spreadsheet_id = '1d7adBBgWfXdm6vtUqA1FO8XMWSp2D4Jsu52VAP4IQS0'
    order_id = models.IntegerField(max_length=127, default=None)
    order_number = models.IntegerField(max_length=127, default=None)
    cost = models.IntegerField(max_length=127, default=None)
    date_delivery = models.DateTimeField()
    cost_rub = models.IntegerField(max_length=127, default=None)

    def __str__(self):
        return self.order_id

    def save(self, *args, **kwargs):
        self.cost_rub += self.cost * get_dollar_currency_from_cb()

        super(Orders, self).save(*args, **kwargs)
# Create your models here.
