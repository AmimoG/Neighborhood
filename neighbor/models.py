from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from pyuploadcare.dj.models import ImageField
import datetime as dt



class Neighborhood(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    occupants_count = models.IntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)
    Admin = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    
        
    def save_neighborhood(self):
        self.save()
    
    def delete_neighborhood(self):
        self.delete()
        
    @classmethod
    def get_neighborhoods(cls):
        projects = cls.objects.all()
        return projects
    
    @classmethod
    def search_neighborhoods(cls, search_term):
        projects = cls.objects.filter(name__icontains=search_term)
        return projects
    
    
    @classmethod
    def get_by_admin(cls, Admin):
        projects = cls.objects.filter(Admin=Admin)
        return projects
    
    
    @classmethod
    def get_neighborhood(request, neighborhood):
        try:
            project = Neighborhood.objects.get(pk = id)
            
        except ObjectDoesNotExist:
            raise Http404()
        
        return project
    
    def __str__(self):
        return self.name
    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='images/', default='default.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=60, blank=True)
    contact = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Post(models.Model):
    title = models.CharField(max_length=155)
    url = models.URLField(max_length=255)
    description = models.TextField(max_length=255)
    technologies = models.CharField(max_length=200, blank=True)
    photo = ImageField(manual_crop='1280x720')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    def delete_post(self):
        self.delete()

    @classmethod
    def search_project(cls, title):
        return cls.objects.filter(title__icontains=title).all()

    @classmethod
    def all_posts(cls):
        return cls.objects.all()

    def save_post(self):
        self.save()


class Business(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    Admin = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    admin_profile = models.ForeignKey(Profile,on_delete=models.CASCADE, blank=True, default='1')
    address = models.TextField()
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE, blank=True, default='1')

    
    def save_business(self):
        self.save()
    
    def delete_business(self):
        self.delete()
        
    @classmethod
    def get_allbusiness(cls):
        business = cls.objects.all()
        return business
    
    @classmethod
    def search_business(cls, search_term):
        business = cls.objects.filter(name__icontains=search_term)
        return business
    
    @classmethod
    def get_by_neighborhood(cls, neighborhoods):
        business = cls.objects.filter(neighborhood__name__icontains=neighborhoods)
        return business
    
    @classmethod
    def get_businesses(request, id):
        try:
            business = Business.objects.get(pk = id)
            
        except ObjectDoesNotExist:
            raise Http404()
        
        return business
    
    def __str__(self):
        return self.name
    
