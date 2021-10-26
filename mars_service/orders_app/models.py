from django.db import models

# Create your models here.
from django.db import models


def status_validator(order_status):
    return order_status in ["open", "closed", "in progress", "need info"]


class Order(models.Model):
    order_description = models.TextField(verbose_name="Описание")
    created_dt = models.DateTimeField(verbose_name="Создано", auto_created=True)
    updated_dt = models.DateTimeField(verbose_name="Изменено", blank=True, null=True)
    order_status = models.TextField(validators=[status_validator])
