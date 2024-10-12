from django.db import models

# Create your models here.
class ddos_dataset(models.Model):
    ddos_data=models.CharField(max_length=500)
    attack_result=models.CharField(max_length=500)