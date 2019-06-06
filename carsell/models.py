from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator 


# Create your models here.
class Car(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length = 300)
    image = models.ImageField(upload_to='carimage/', null=True)
    description = models.CharField(max_length = 300,default='car!!!')
    rating = models.CharField(max_length = 30, default = 0)
    av_usability = models.CharField(max_length = 30, default = 0)
    av_design = models.CharField(max_length = 30, default = 0)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profile/')
    pub_date_created = models.DateTimeField(auto_now_add=True, null=True)
 
    def __str__(self):
        return self.first_name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profiles(cls):
        profiles = cls.objects.all()
        return profiles

class Location(models.Model):
    name = models.CharField(max_length=30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.name


class Rating(models.Model):
    car_name = models.CharField(max_length = 30, default = '')
    poster = models.ForeignKey(User,on_delete=models.CASCADE)
    usability = models.IntegerField(choices=((1, 1),(2, 2),(3, 3),(4, 4),(5, 5),(6, 6), (7, 7),(8, 8), (9, 9), (10, 10)), blank=True)
    design = models.IntegerField(choices=((1, 1),(2, 2),(3, 3),(4, 4),(5, 5),(6, 6), (7, 7),(8, 8), (9, 9), (10, 10)), blank=True)

    def __str__(self):
        return self.poster
    average = models.IntegerField(blank = True, default=0)


class CarEvaluate(models.Model):

    evaluater = models.CharField(default='My Project', max_length = 80)
    evaluated = models.CharField(default='My Project', max_length = 80)
    published_date = models.DateField(auto_now_add=True, null=True)
    design = models.PositiveIntegerField(default=1, choices=((1, 1),(2, 2),(3, 3),(4, 4),(5, 5),(6, 6), (7, 7),(8, 8), (9, 9), (10, 10)))
    usability = models.PositiveIntegerField(default=1, choices=((1, 1),(2, 2),(3, 3),(4, 4),(5, 5),(6, 6), (7, 7),(8, 8), (9, 9), (10, 10)))

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f'{self.design} marks'
