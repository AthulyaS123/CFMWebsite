from django.db import models

#test
class Book(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField("date published")

class Bank(models.Model):
    email = models.EmailField('something@mail.com')
#real code
