from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)
    tin_number = models.CharField(max_length=100, blank=True)
    vrn_number = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    address = models.TextField(max_length=50)
    date_created = models.DateTimeField(auto_created=True, auto_now_add=True)

    class Meta:
        # Table's name
        db_table = "Customer"
        verbose_name_plural = "Customer"

    def __str__(self):
        return self.name
