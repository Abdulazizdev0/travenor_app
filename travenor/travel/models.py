from django.db import models
from core.models import Category
from user.models import User
from staff.models import Employee
from core.models import Region

class Travels(models.Model):
    level_type = [
        ('orta','orta'),
        ('orta qiyinlikda','orta qiyinlikda'),
        ('qiyin','qiyin')
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    level = models.CharField(max_length=50,choices=level_type,default='orta')
    region = models.ForeignKey(Region, on_delete=models.CASCADE,null=True,blank=True)
    birth_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    guests_count = models.IntegerField(default=1)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Travel from {self.start_date} to {self.end_date}"




class TravelImage(models.Model):
    travel = models.ForeignKey(Travels, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/travel_images/')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f"Image for {self.travel}"




class TravelCategory(models.Model):
    travel = models.ForeignKey(Travels, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.travel} - {self.category}"




class Review(models.Model):
    travel = models.ForeignKey(Travels, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user} for {self.travel}"




class TravelGuide(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    travel = models.ForeignKey(Travels, on_delete=models.CASCADE)
    assignment_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee} assigned to {self.travel}"

