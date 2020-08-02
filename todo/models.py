from django.db import models

# Create your models here.


class ToDo(models.Model):
    added_date = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=200)
    is_urgent = models.BooleanField(default=False)

    def __str__(self):
        return self.text + " and is it urgnet: " + str(self.is_urgent) + " and it was created: " + str(self.added_date)

    class Meta:
        verbose_name_plural = "Todo's"
