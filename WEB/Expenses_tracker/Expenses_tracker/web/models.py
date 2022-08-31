from django.core.validators import MinLengthValidator
from django.db import models

from Expenses_tracker.web.validators import validate_only_letters, MaxSizeInMB


class Profile(models.Model):
    NAME_MIN_LENGTH = 2
    NAME_MAX_LENGTH = 15

    BUDGET_MIN_VALUE = 0
    BUDGET_DEFAULT = 0

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
        max_length=NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )
    budget = models.FloatField(
        default=BUDGET_DEFAULT,
        validators=(
            MinLengthValidator(BUDGET_MIN_VALUE),
        ),

    )
    profile_image = models.ImageField(
        upload_to=IMAGE_UPLOAD_TI_DIR,
        null=True,
        blank=True,
        validators=(
            MaxSizeInMB(IMAGE_MAX_SIZE_IN_MB),
        )

    )


class Expense(models.Model):

    title = models.CharField(
        max_length=30,

    )
    image = models.URLField(
        verbose_name='Link to image',
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    price = models.FloatField()