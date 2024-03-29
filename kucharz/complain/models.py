from django.db import models

class Complain(models.Model):
      first_name = models.CharField(max_length=100)
      last_name = models.CharField(max_length=100)
      email = models.EmailField(max_length=254)
      message = models.TextField(max_length=254)

      def __str__(self):
          return self.email