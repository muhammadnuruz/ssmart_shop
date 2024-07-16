from django.db import models


class Types(models.Model):
    name = models.CharField(max_length=255)
    warranty_years = models.IntegerField(default=0)
    warranty_months = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"

    def __str__(self):
        return f"{self.name} ({self.warranty_years} years, {self.warranty_months} months)"
