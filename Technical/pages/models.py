from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.contrib.auth.models import  User
#model related to a new user creation
class Week(models.Model):
    week          = models.CharField(max_length=100, null=True, blank=True, default=0)
    
    def __str__(self):
        return self.week
class Grade(models.Model):
    user             = models.ForeignKey(User, unique=None, on_delete=models.CASCADE, related_name="grade", null=True)
    pretest          = models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True, default=0)
    posttest         = models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True, default=0)
    codingProject    = models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True, default=0)
    finalGrade       = models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True, default=0)
   

    def __str__(self):
        return self.user.get_username()


#allows the creation of the Point model whenever a new user is created. Stackoverflow FTW.
def create_user_grades(sender, instance, created, **kwargs):
    if created:
        Grade.objects.create(user=instance)

post_save.connect(create_user_grades, sender=User)