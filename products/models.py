from django.db import models

class product(models.Model):
    title=models.CharField(max_length=120)
    description=models.TextField(blank=True,null=True)
    price=models.DecimalField(decimal_places=2,max_digits=10000)
    summery=models.TextField(blank=True,null=False)
    featured=models.BooleanField()