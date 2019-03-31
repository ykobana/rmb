from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=100, default='nobody')
#    password = models.CharField(max_length=100)


class Character(models.Model):
    name = models.CharField(max_length=100, default='heartless')
    graffiti_image = models.ImageField('graffiti',upload_to='uploads/graffiti/')
    rate = models.IntegerField(default=1000)
    level = models.IntegerField(default=1)
    experience_point = models.IntegerField(default=0)
    hit_point = models.IntegerField(default=1000)
    magic_point = models.IntegerField(default=1000)
    attack_point = models.IntegerField(default=150)
    defence_point = models.IntegerField(default=150)
    speed_point = models.IntegerField(default=150)
    luck_point = models.IntegerField(default=150)
    skill1 = models.IntegerField(default=1)
    skill2 = models.IntegerField(default=0)
    skill3 = models.IntegerField(default=0)
    skill4 = models.IntegerField(default=0)


class UserAndCharacterLink(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    character_id = models.ForeignKey(Character, on_delete=models.CASCADE)


class BattleResult(models.Model):
    characterA = models.ForeignKey(UserAndCharacterLink, on_delete=models.CASCADE, related_name='A')
    characterB = models.ForeignKey(UserAndCharacterLink, on_delete=models.CASCADE, related_name='B')
    result = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(2)])  # 勝ち/負け


class Skill(models.Model):
    power = models.IntegerField(default=10)
    magic_point_consumption = models.IntegerField(default=0)
