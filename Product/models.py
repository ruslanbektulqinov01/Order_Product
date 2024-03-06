from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.price}'
