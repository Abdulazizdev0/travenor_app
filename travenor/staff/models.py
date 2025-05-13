from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.firstname}  {self.lastname} "




