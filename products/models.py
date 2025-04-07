from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField(blank=True)  # Se puede cambiar a ImageField más adelante
    power = models.IntegerField(help_text="Potencia en Watts")
    efficiency = models.DecimalField(max_digits=4, decimal_places=2, help_text="Porcentaje de eficiencia")
    panel_type = models.CharField(
        max_length=50,
        choices=[
            ('Monocristalino', 'Monocristalino'),
            ('Policristalino', 'Policristalino'),
            ('Amorfo', 'Amorfo'),
        ]
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

