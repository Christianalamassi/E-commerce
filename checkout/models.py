import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from drinks.models import Drink


class ToPay(models.Model):

    states = (
            ("London","London"),("Bradford","Bradford"),
            ("Wakefield","Wakefield"),("Nottingham","Nottingham"),
            ("Westminster","Westminster"),("Coventry","Coventry"),
            ("Birmingham","Birmingham"),("Liverpool","Liverpool"),
            ("Leeds","Leeds"),("Bristol","Bristol"),
            ("Manchester","Manchester"),("Leicester","Leicester"),
        )

    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=75, null=False, blank=False)
    email = models.EmailField(max_length=300, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    states =  models.CharField(choices=states, max_length=40, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    

    def _generate_order_number(self):
        """ 
        Generate a random, unique order number using UUID 
        """
        
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum']
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(ToPay, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    drink = models.ForeignKey(Drink, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.drink.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.order.order_number}'