from django.db import models

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=200)
    emp_id=models.CharField(max_length=200)
    phone=models.CharField (max_length=10)
    address=models.CharField(max_length=200)
    working=models.BooleanField(default=False)
    department=models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
    
class Testimonial(models.Model):
    name=models.CharField(max_length=200)
    testimonial=models.TextField()
    picture=models.ImageField(upload_to="testimonials/")
    rating=models.IntegerField(max_length=1)
    
    def __str__(self):
        return self.name
    
    