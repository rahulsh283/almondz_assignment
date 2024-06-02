from django.db import models

class SplitType(models.TextChoices):
    EQUAL = "EQUAL"
    EXACT = "EXACT"
    PERCENT = "PERCENT"
