from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=50)
    location = models.ForeignKey(Location, on_delete= models.CASCADE)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=50)
    course = models.ManyToManyField(Course)

    def __str__(self):
        return self.name

        