from django.db import models

# Create your models here.
class Teacher(models.Model):
    eid = models.CharField(max_length = 20)
    efirstName = models.CharField(max_length = 100)
    elastName = models.CharField(max_length = 100)
    epassword = models.CharField(max_length = 100)


    def __str__(self):
        return "%s" %(self.efirstName)
    
    class Meta:
        db_table = "teacher"
