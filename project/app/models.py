from django.db import models
from django.utils import timezone

# Create your models here.

GENDER_CHOICES = [
    ('M','Male'),
    ('F','Female'),
]

class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    birth_date = models.DateField(default=timezone.now)
    phone_number = models.CharField(max_length=255) #because of that 0 start of the integer field it won't count, we could use one of two choices: register phonenumber field as string(CharField) or use plugin(PhoneNumberField)
    email = models.EmailField(null=False, blank=False)
    notes = models.TextField()
    status = models.BooleanField(default=True)
    profile_image = models.ImageField(upload_to='members/images/')

    def __str__(self) -> str:
        return self.first_name

    class Meta:
        verbose_name_plural = 'Members List'