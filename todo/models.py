from django.db import models

# Create your models here.


class ToDo(models.Model):
    added_date = models.DateTimeField()
    text = models.CharField(max_length=200)
    is_urgent = models.BooleanField()

    class Meta:
        verbose_name_plural = "Todo's"
