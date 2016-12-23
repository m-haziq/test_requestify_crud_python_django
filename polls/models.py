from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Sampletable(models.Model):
    name = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
