from datetime import timedelta

from django.db import models

from apps.shops.models import Shops
from apps.telegram_users.models import TelegramUsers
from apps.types.models import Types


class Guarantees(models.Model):
    shop = models.ForeignKey(to=Shops, on_delete=models.CASCADE)
    type = models.ForeignKey(to=Types, on_delete=models.CASCADE)
    user = models.ForeignKey(to=TelegramUsers, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=255)
    date_of_purchase = models.DateField()
    validity_period = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Guarantee"
        verbose_name_plural = "Guarantees"

    def __str__(self):
        return self.serial_number

    def save(self, *args, **kwargs):
        if self.type.name == 'Televizor':
            self.validity_period = self.date_of_purchase + timedelta(
                days=self.type.warranty_years * 365 + self.type.warranty_months * 30)
        else:
            self.validity_period = self.date_of_purchase + timedelta(
                days=self.type.warranty_years * 365 + self.type.warranty_months * 30)
        super().save(*args, **kwargs)
