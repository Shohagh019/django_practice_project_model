from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField(max_length=10, primary_key= True)
    email = models.EmailField()
    address = models.TextField()
    father_name = models.CharField(default='Rahim', max_length=20)

    def __str__(self):
        return f'Roll: {self.roll} - {self.name}'