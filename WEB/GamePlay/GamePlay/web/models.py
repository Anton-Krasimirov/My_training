from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models


class Profile(models.Model):
    MIN_AGE_VALUE = 12
    MAX_CHARACTER = 30

    email = models.EmailField()

    age = models.IntegerField(validators=(MinValueValidator(MIN_AGE_VALUE),), )

    password = models.CharField(max_length=MAX_CHARACTER,)

    first_name = models.CharField(null=True, blank=True, max_length=MAX_CHARACTER, )

    last_name = models.CharField(null=True, blank=True, max_length=MAX_CHARACTER, )

    profile_picture = models.URLField(null=True, blank=True, )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Game(models.Model):
    CHOICES = [('Action', 'Action'), ('Adventure', 'Adventure'), ('Puzzle', 'Puzzle'), ('Strategy', 'Strategy'),
               ('Sports', 'Sports'), ('Board/Card Game', 'Board/Card Game'), ('Other', 'Other')]

    title = models.CharField(max_length=30, unique=True, )

    category = models.CharField(max_length=15, choices=CHOICES, )

    rating = models.FloatField(validators=(MinValueValidator(0.1), MaxValueValidator(5.0)))

    max_level = models.IntegerField(null=True, blank=True, validators=(MinValueValidator(1),))

    image_url = models.URLField()

    summary = models.TextField(null=True, blank=True,)