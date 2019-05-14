from django.db import models
from django.utils import timezone
from datetime import datetime
from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Todo(models.Model):
    description = models.CharField(max_length=180)
    due_date = models.DateField(default=date.today)
    done_percentage = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])

    def __str__(self):
        return self.description