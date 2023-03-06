from django.db import models
from branches.models import Branch
from django.db.models import Sum
from staff.models import Staff



# class ExpenseCategory(models.Model):
#     name = models.CharField(max_length=256)
#     created = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         # Table's name
#         db_table = "ExpenseCategory"
#         verbose_name_plural = "ExpenseCategory"

#     def __str__(self) -> str:
#         return self.name


class Expense(models.Model):
    name = models.CharField(max_length=256)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=256)
    staff = models.ForeignKey(Staff, on_delete=models.PROTECT, null=True)
    branch = models.CharField(blank=True, null=True, max_length=200)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default=False)

    
    class Meta:
        verbose_name_plural = 'Expense'
        

    def __str__(self) -> str:
        return self.name
    


    @property
    def price_total_amount(self):
        return self.quantity * self.amount
    
    


