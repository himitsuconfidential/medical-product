from django.db import models

class ClinicManager(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class MedicalProduct(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.name
    
class Order(models.Model):
    time = models.DateTimeField()
    status = models.CharField(max_length=10)
    manager = models.ForeignKey(ClinicManager, on_delete=models.CASCADE)
    products = models.ManyToManyField(MedicalProduct, through='OrderItem')
    def __str__(self):
        return f'{self.manager.name} ({self.time})'
    
class OrderItem(models.Model):
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(MedicalProduct, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.product.name} x({self.quantity})'
