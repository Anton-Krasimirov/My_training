from django.core.validators import MinLengthValidator
from django.db import models

from Expenses_tracker.web.validators import validate_only_letters


class Profile(models.Model):
    NAME_MIN_LENGTH = 2
    NAME_MAX_LENGTH = 15

    BUDGET_MIN_VALUE = 0
    BUDGET_DEFOULT = 0

    IMAGE_MAX_SIZE_IN_MB = 5
    IMAGE_UPLOAD_TI_DIR = 'profiles/'

    first_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(NAME_MIN_LENGTH),
            validate_only_letters,
        )
     )

    last_name = models.CharField(

    )
    budget = models.FloatField(

    )
    profile_image = models.ImageField(

    )


class Expense(models.Model):

    title = models.CharField(

    )
    expense_image = models.URLField(

    )
    description = models.TextField(

    )
    price = models.FloatField(

    )