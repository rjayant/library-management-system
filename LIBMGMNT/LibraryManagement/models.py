from django.db import models

# Create your models here.
class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):              # __unicode__ on Python 2
        return self.title

    class Meta:
        ordering = ('title',)

class ArticleManyToMany(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    def __str__(self):              # __unicode__ on Python 2
        return self.headline

    class Meta:
        ordering = ('id',)

class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person)
    group = models.ForeignKey(Group)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):              # __unicode__ on Python 2
        return "%s %s" % (self.first_name, self.last_name)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter)

    def __str__(self):              # __unicode__ on Python 2
        return self.headline

    class Meta:
        ordering = ('headline',)
        
class Blog(models.Model):
    name    = models.CharField(max_length=50)
    tagline = models.TextField()
    
    def __unicode__(self):
        return self.name

class Author(models.Model):
    name  = models.CharField(max_length=50)
    email = models.EmailField()

class Entry(models.Model):
    blog     = models.ForeignKey(Blog)
    headline = models.CharField(max_length=50)
    body_text = models.TextField()
    pub_date  = models.DateField()
    mod_date  = models.DateField()
    authors  = models.ManyToManyField(Author)
    n_coment = models.IntegerField()
    n_pingback = models.IntegerField()
    rating  = models.IntegerField()
    
    def __unicode__(self):
        return  self.headline

class ThemeBlog(Blog):
    theme = models.CharField(max_length=200)

class UserLink(models.Model):
    anchor = models.CharField(max_length=50)
    url = models.URLField(max_length=50)
    
class UserInfo(models.Model):
    GENDER_CHOICES = (('M', 'Male'),
                      ('F', 'Female'))
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email   = models.EmailField(max_length=20)
    address = models.CharField(max_length=30)
    city  =  models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    aadhar_no = models.CharField(max_length=20, unique=True, editable=False)
    age = models.IntegerField()
    state= models.CharField(max_length=20)

