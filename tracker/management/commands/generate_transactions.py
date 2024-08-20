import random

from faker import Faker
from django.core.management.base import BaseCommand

from tracker.models.categories import Category
from tracker.models.transactions import Transaction
from tracker.models.users import User


class Command(BaseCommand):
    help = "Generates transactions for testing"

    def handle(self, *args, **options):
        fake = Faker()

        # create categories
        categories = [
            "Bills", "Food", "Clothes",
            "Medical", "Housing", "Salary",
            "Social", "Transport", "Vacation",
        ]
        for category in categories:
            Category.objects.get_or_create(name=category)

        # get the user
        user = User.objects.filter(username="josuealonzo").first()
        if not user:
            User.objects.create_superuser(
                username="josuealonzo",
                email="joshi.alonzo@gmail.com",
                password="admin",
            )

        # create transactions
        categories = Category.objects.all()
        types = [t[0] for t in Transaction.TRANSACTION_TYPE_CHOICES]
        for i in range(20):
            Transaction.objects.create(
                category=random.choice(categories),
                user=user,
                amount=random.uniform(1, 2500),
                date=fake.date_between(start_date="-1y", end_date="today"),
                type=random.choice(types),
            )
