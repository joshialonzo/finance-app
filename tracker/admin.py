from django.contrib import admin
from tracker.models.categories import Category
from tracker.models.transactions import Transaction


# Register your models here.
admin.site.register(Category)
admin.site.register(Transaction)
