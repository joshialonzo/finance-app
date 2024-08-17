from django.db import models

from tracker.models.categories import Category
from tracker.models.users import User


class Transaction(models.Model):
    """
    Transaction can be either income or expense.
    It has an amount.
    It has a category (FK).
    It is tied to a user (FK).
    It has a date.
    """
    TRANSACTION_TYPE_CHOICES = (
        ("income", "Income"),
        ("expense", "Expense"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.CharField(max_length=7, choices=TRANSACTION_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self) -> str:
        return f"{self.type} of {self.amount} on {self.date} by {self.user}"
