from django.db import models

class Curriculum(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '커리큘럼 : ' + self.name

