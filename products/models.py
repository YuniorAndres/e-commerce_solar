from django.db import models

# # Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField(blank=True)  # Luego se puede mejorar con ImageField
    power = models.IntegerField(help_text="Potencia en Watts")
    efficiency = models.DecimalField(max_digits=4, decimal_places=2, help_text="Porcentaje de eficiencia")
    panel_type = models.CharField(max_length=50, choices=[
        ('Monocristalino', 'Monocristalino'),
        ('Policristalino', 'Policristalino'),
        ('Amorfo', 'Amorfo')
    ])

    def __str__(self):
        return self.name

