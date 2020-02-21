from django.db import models

# Create your models here.
class Courses(models.Model):
    course_name = models.TextField()
    course_id = models.TextField()
    image_number = models.TextField()

    def __str__(self):
        return self.course_name