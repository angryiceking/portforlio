from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

import random

def randomize(min, max):
    value = random.randrange(min, max)
    return value

# Create your models here.
class SkillSet(models.Model):
    skill_one = models.ForeignKey(
        'SkillOne', on_delete=models.CASCADE)
    skill_two = models.ForeignKey(
        'SkillTwo', on_delete=models.CASCADE)
    skill_three = models.ForeignKey(
        'SkillThree', on_delete=models.CASCADE)
    skill_ult = models.ForeignKey(
        'SkillUlt', on_delete=models.CASCADE)
    skill_passive = models.ForeignKey(
        'SkillPassive', on_delete=models.CASCADE)
    hidden_skill_potential = models.ForeignKey(
        'HiddenSkillPotential', on_delete=models.CASCADE)
    
class SkillOne(models.Model):
    skill_name = models.CharField(max_length=255)
    skill_damage = models.FloatField(default=randomize(30, 100))
    skill_effect = models.CharField(max_length=255)
    
    def __str__(self):
        return self.skill_name
    
class SkillTwo(models.Model):
    skill_name = models.CharField(max_length=255)
    skill_damage = models.FloatField(default=randomize(50, 200))
    skill_effect = models.CharField(max_length=255)
    
    def __str__(self):
        return self.skill_name

    
class SkillThree(models.Model):
    skill_name = models.CharField(max_length=255)
    skill_damage = models.FloatField(default=randomize(80, 300))
    skill_effect = models.CharField(max_length=255)
    
    def __str__(self):
        return self.skill_name

    
class SkillUlt(models.Model):
    skill_name = models.CharField(max_length=255)
    skill_damage = models.FloatField(default=randomize(120, 500))
    skill_effect = models.CharField(max_length=255)
    
    def __str__(self):
        return self.skill_name

    
class SkillPassive(models.Model):
    skill_name = models.CharField(max_length=255)
    skill_damage = models.FloatField(default=randomize(30, 100))
    skill_effect = models.CharField(max_length=255)
    
    def __str__(self):
        return self.skill_name

    
class HiddenSkillPotential(models.Model):
    skill_name = models.CharField(max_length=255)
    skill_damage = models.FloatField(default=randomize(300, 800))
    skill_effect = models.CharField(max_length=255)
    
    def __str__(self):
        return self.skill_name
