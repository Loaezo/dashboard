import uuid
import random

"Django modules"

from django.db import models

def random_values():
    return str(random.sample(range(0, 10000), 50))

class Company(models.Model):
    """The model for the company, including name, description, how many stock it has and the current stock price"""
    company_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    company_name = models.CharField("Nombre", max_length=50)
    description = models.CharField("Descripción", max_length=100)
    stock_volume = models.IntegerField("Acciones en circulación")
    stock_price = models.IntegerField("Precio por acción")
    market_value = models.CharField("Valores a mercado", max_length=500000, default=random_values)

# esta es la tabla que es la referencia a la primera, pero no será necesaria
class Market_cap(models.Model):
    """Market capitalization for the company in a given period"""
    market_cap_id = models.AutoField(auto_created=True, default=1, primary_key=True)
    year = models.DateField()
    mkt_value = models.IntegerField()
    company = models.ForeignKey(
        'company',
        on_delete = models.CASCADE,
        default = None
    )