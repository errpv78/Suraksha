from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()

    relations = (
        ('Father', 'Father'),
        ('Mother', 'Mother'),
        ('Brother', 'Brother'),
        ('Sister', 'Sister'),
        ('Husband', 'Husband'),
        ('Friend', 'Friend'),
        ('Relative', 'Relative'),
        ('Other', 'Other'),
    )
    relation = models.CharField(max_length=20, choices=relations)
    def __str__(self):
        return self.name
