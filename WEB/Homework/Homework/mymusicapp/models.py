from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


def validatorusername(value):
    for char in value:
        if not char.isdigit() and not char.isalpha() and not char == '_':
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


class Profile(models.Model):
    NAME_MIN_LEN = 2
    NAME_MAX_LEN = 15
    MIN_AGE = 0

    username = models.CharField(max_length=NAME_MAX_LEN, validators=(MinLengthValidator(NAME_MIN_LEN), validatorusername,))

    email = models.EmailField()

    age = models.IntegerField(null=True, blank=True, validators=(MinValueValidator(MIN_AGE),),)

class Album(models.Model):

    STILES_MUSIC = (
        ("Pop Music", "Pop Music"),
        ("Jazz Music", "Jazz Music"),
        ("R&B Music", "R&B Music"),
        ("Rock Music","Rock Music"),
        ("Country Music", "Country Music"),
        ("Dance Music", "Dance Music"),
        ("Hip Hop Music", "Hip Hop Music"),
        ("Other", "Other"),
    )

    album_name = models.CharField(max_length=30, unique=True,)

    artist = models.CharField(max_length=30,)

    genre = models.CharField(max_length=30, choices=STILES_MUSIC,)

    description = models.TextField(null=True, blank=True,)

    image_url = models.URLField()

    price = models.FloatField(validators=(MinValueValidator(0),)
)
