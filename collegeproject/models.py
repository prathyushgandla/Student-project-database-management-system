from django.db import models

# Create your models here.
class Project(models.Model):
    Title=models.CharField(null=True, blank=True,max_length=100)
    Academic=models.CharField(null=True, blank=True,max_length=100)
    ProjectType=models.CharField(null=True, blank=True,max_length=100)
    Department=models.CharField(null=True, blank=True,max_length=100)
    GroupSize=models.IntegerField(null=True, blank=True)
    StudentName1=models.CharField(null=True, blank=True,max_length=100)
    StudentRollno1=models.CharField(null=True, blank=True,max_length=100)
    StudentMobileNumber1 = models.IntegerField(null=True, blank=True)
    StudentEmail1 = models.EmailField(null=True, blank=True,max_length=100)
    StudentName2=models.CharField(null=True, blank=True,max_length=100)
    StudentRollno2=models.CharField(null=True, blank=True,max_length=100)
    StudentMobileNumber2 = models.IntegerField(null=True, blank=True)
    StudentEmail2 = models.EmailField(null=True, blank=True,max_length=100)
    StudentName3=models.CharField(null=True, blank=True,max_length=100)
    StudentRollno3=models.CharField(null=True, blank=True,max_length=100)
    StudentMobileNumber3 = models.IntegerField(null=True, blank=True)
    StudentEmail3 = models.EmailField(null=True, blank=True,max_length=100)
    StudentName4=models.CharField(null=True, blank=True,max_length=100)
    StudentRollno4=models.CharField(null=True, blank=True,max_length=100)
    StudentMobileNumber4 = models.IntegerField(null=True, blank=True)
    StudentEmail4 = models.EmailField(null=True, blank=True,max_length=100)
    StudentName5=models.CharField(null=True, blank=True,max_length=100)
    StudentRollno5=models.CharField(null=True, blank=True,max_length=100)
    StudentMobileNumber5 = models.IntegerField(null=True, blank=True)
    StudentEmail5 = models.EmailField(null=True, blank=True,max_length=100)
    Research=models.TextField(null=True, blank=True)
    Software=models.TextField(null=True, blank=True)
    GuideName=models.CharField(null=True, blank=True,max_length=100)
    GuideEmail =models.EmailField(null=True, blank=True,max_length=100)
    GuideNumber = models.IntegerField(null=True, blank=True)
    File=models.FileField(null=True, blank=True)
    def __str__(self):
        return self.Title