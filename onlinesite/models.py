from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.


class group1(models.Model):
    title = models.CharField(max_length=200)
    paragraph = models.CharField(max_length=200)
    buttons = models.CharField(max_length=200)
    svg_file = models.FileField(upload_to='svgs/')


    def __str__(self):
        return self.title


class group2(models.Model):
    icons=models.CharField(max_length=100)
    delay=models.IntegerField()
    topic = models.CharField(max_length=200)
    description=models.TextField(max_length=400)

   

class group3(models.Model):
    svg_file = models.FileField(upload_to='svgs/')

class group4(models.Model):
    title = models.CharField(max_length=200)
    paragraph = models.CharField(max_length=200)


class group5(models.Model):
    icons=models.CharField(max_length=100)
    topic = models.CharField(max_length=200)
    description=models.TextField(max_length=400)


class group6(models.Model):
    svg_file1 = models.FileField(upload_to='svgs/')
    svg_file2 = models.FileField(upload_to='svgs/')


class group7(models.Model):
    title = models.CharField(max_length=200)
    paragraph = models.CharField(max_length=200)
    SubHeading1 = models.CharField(max_length=200)
    description1=models.TextField(max_length=400)
    SubHeading2 = models.CharField(max_length=200)
    description2=models.TextField(max_length=400)
    SubHeading3 = models.CharField(max_length=200)
    description3=models.TextField(max_length=400)


class group80(models.Model):
    title = models.CharField(max_length=200)
    customer=models.BigIntegerField()

class group81(models.Model):
    offers = models.CharField(max_length=200)

class group9(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    quote = models.TextField(max_length=500)
    image=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class groups100(models.Model):
    name=models.CharField(max_length=100)
    total_number=models.CharField(max_length=100)

class groups101(models.Model):
    ticker_name=models.CharField(max_length=200)

class about1(models.Model):
    name=models.CharField(max_length=200)
    paragraph=models.TextField(max_length=400)


class about2(models.Model):
    images=models.ImageField(null=True,blank=True)

    @property
    def imageURL(self):
        try:
            url = self.images.url
        except:
            url = ''
        return url

class about3(models.Model):
    title=models.CharField(max_length=200)
    data_value=models.CharField(max_length=200,null=True,blank=True)
    data_suffix=models.CharField(max_length=200,default='+',blank=True)


class about4_video(models.Model):
    youtube_link = models.URLField()
    title=models.CharField(default='YouTube video player',max_length=200)




class about6(models.Model):
    title = models.CharField(max_length=200)
    dates=models.DateField()
    Editor = models.CharField(max_length=200)
    Comments_count = models.IntegerField()
    images=models.ImageField(null=True,blank=True)

    @property
    def imageURL(self):
        try:
            url = self.images.url
        except:
            url = ''
        return url

class service2(models.Model):
    title = models.CharField(max_length=200)
    paragraph = models.CharField(max_length=200)
    type1 = models.CharField(max_length=200)
    type2 = models.CharField(max_length=200)
    type3 = models.CharField(max_length=200)
    type4 = models.CharField(max_length=200)
    image=models.ImageField(null=True,blank=True)
    icons=models.CharField(max_length=100)
    buttons = models.CharField(max_length=200)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class contact1(models.Model):
    title=models.CharField(max_length=200)
    des=models.CharField(max_length=200)
    svg_file=models.FileField(upload_to='svg/')

class contact2(models.Model):
    street=models.CharField(max_length=200)
    state=models.CharField(max_length=200)


class contact3(models.Model):
    phone=models.CharField(max_length=200)




class contact4(models.Model):
    icons=models.CharField(max_length=200)

# Price Package
class prices1(models.Model):
    title=models.CharField(max_length=200)
    des=models.CharField(max_length=200)

class prices2(models.Model):
    package_type=models.CharField(max_length=200)
    price=models.FloatField(max_length=200)
    des=models.CharField(max_length=200)
    service1=models.CharField(max_length=200, blank=True)
    service2=models.CharField(max_length=200, blank=True)
    service3=models.CharField(max_length=200, blank=True)
    service4=models.CharField(max_length=200, blank=True)
    service5=models.CharField(max_length=200, blank=True)
    buttons=models.CharField(max_length=200)
    buttons_color=models.CharField(max_length=200)

# Challenge
class prices3(models.Model):
    title=models.CharField(max_length=200)
    des=models.CharField(max_length=200)

class prices4(models.Model):
    topic_number=models.CharField(max_length=200, blank=True)
    data_value=models.CharField(max_length=200,null=True,blank=True)
    topic_des=models.CharField(max_length=200, blank=True)
    

# Model Prices
class prices5(models.Model):
    title=models.CharField(max_length=200)
    sec_title=models.CharField(max_length=200)
    des=models.CharField(max_length=200)
    buttons=models.CharField(max_length=200)

class prices6(models.Model):
    model_number=models.CharField(max_length=200, blank=True)
    service=models.CharField(max_length=200, blank=True)
    plan_bill=models.CharField(max_length=200, blank=True)