from django.db import models

class student(models.Model):
    name = models.CharField(max_length=30)
    regno=models.PositiveBigIntegerField()
    branch=models.CharField(max_length=30)
    year=models.PositiveBigIntegerField()
    # image = models.ImageField(upload_to='images')


    # def __int__(self):
    #     return self.regno

    def __str__(self):
        return self.name    

class faculty(models.Model):
    namef=models.CharField(max_length=30)
    branchf=models.CharField(max_length=30)

    def __str__(self):
        return self.namef



class message(models.Model):
    toname=models.CharField(max_length=30,default='abc')
    fromw=models.CharField(max_length=30)
    # to_name=models.ForeignKey(faculty,on_delete=models.CASCADE)
    # fromw=models.ForeignKey(student, on_delete=models.CASCADE)
    regno1= models.CharField(max_length=50)
    messageis=models.CharField(max_length=30)

    def __str__(self):
        return self.messageis
    

class reply(models.Model):
    fromr=models.ForeignKey(faculty,on_delete=models.CASCADE)
    to=models.ForeignKey(student,on_delete=models.CASCADE)
    message=models.CharField(max_length=50)
    def __str__(self):
        return self.to

    def __str__(self):
        return self.message

class register(models.Model):
    name=models.CharField(max_length=30)
    regno=models.PositiveIntegerField()
    complaint=models.CharField(max_length=100)

   