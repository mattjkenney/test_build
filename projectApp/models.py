from django.db import models

# Create your models here.

class Test(models.Model):
    test = models.CharField(primary_key= True, unique=True, max_length=30)

class Parameter(models.Model):
    parameter = models.CharField(primary_key= True, unique=True, max_length=30)
    dimension = models.CharField(max_length= 30)

    def __str__(self):
        if self.unit == "None":
            u = ''
        else:
            u = '(' + self.unit + ')'
        return self.dimension + u

class Criteria(models.Model):
    types = [
        ("RANGE", 'range'),
        ("EXACT NUMBER", 'exact number'),
        ("EXACT TEXT", 'exact text'),
        ("MINIMUM", 'minimum'),
        ("MAXIMUM", 'maximum')
    ]

    conditions = [
        ("NONE", 'none'),
        ("NUMBER", 'number'),
        ("TEXT", 'text')
    ]

    test = models.CharField(max_length=30)
    criteria_type = models.CharField(choices= types, max_length=30)
    condition_type = models.CharField(choices= conditions, max_length=30)

    # range criteria
    range_min = models.FloatField()
    range_max = models.FloatField()

    # exact number
    exact_criteria = models.FloatField()

    # exact text
    exact_text = models.CharField(max_length= 30)

    # minimum criteria
    min_minimum = models.FloatField()

    # maximum criteria
    max_maximum = models.FloatField()

    # conditional number: all conditions must be true for the instance criteria to apply
    parameter_number = models.CharField(max_length=30)
    greater_than = models.FloatField()
    greater_than_or_equal_to = models.FloatField()
    less_than = models.FloatField()
    less_than_or_equal_to = models.FloatField()

    # conditional text
    parameter_text = models.CharField(max_length=30)
    parameter_is = models.CharField(max_length=30)
    

