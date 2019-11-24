from django.db import models
from PIL import Image
# Create your models here.


class Department(models.Model):
    deptName = models.CharField("Department Name", max_length=100)

    def __str__(self):
        return self.deptName
    
    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Department'

class Subject(models.Model):
    dept = models.ForeignKey(Department, on_delete=models.Model)
    subjectCode = models.CharField("subject Code", max_length=20)
    subjectName = models.CharField("Subject Name", max_length=200)

    def __str__(self):
        return self.subjectCode+'-'+self.subjectName
    
    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"

class Faculty(models.Model):
    dept = models.ForeignKey(Department, on_delete=models.Model)
    empName = models.CharField("Employee Name", max_length=200)

    def __str__(self):
        return str(self.empName)
    
    class Meta:
        verbose_name = "Faculty"
        verbose_name_plural = "Faculty"

class Rating(models.Model):
    ip = models.CharField("IP Address",max_length=50)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete =models.CASCADE)
    rating1 = models.IntegerField(default=0)
    rating2 = models.IntegerField(default=0)
    rating3 = models.IntegerField(default=0)
    rating4 = models.IntegerField(default=0)
    rating5 = models.IntegerField(default=0)
    review = models.TextField()

    def __str__(self):
        return self.faculty
    class Meta:
        verbose_name = "Rating Data"
        verbose_name_plural = "Rating Data"

class EntryCodes(models.Model):
    code = models.CharField("Entry Code", max_length=20)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=False)

    def __str__(self):
        return self.code
    
    class Meta:
        verbose_name= "Entry Code"
        verbose_name_plural = "Entry Code"