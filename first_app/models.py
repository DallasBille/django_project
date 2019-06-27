from django.db import models

# you create a class, tell python its a model, use the Charfield method, and set a max length. And make sure the names are unique. Easy Peasy.


#  How relationships and ForeignKey works:



class Topic(models.Model):
    top_name = models.CharField(max_length=200,unique= True)
# this returns the name in string form.
    def __str__(self):
        return self.top_name

# This is how you have one model inherit from another, you must pass the model into the ForeignKey method of the model inheriting it.
class Webpage(models.Model):
    # When inheriting from other models, you must pass in an on_delete for python version 2.0 +.
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date = models.DateField()
# you can just return date as a string by using the str() method on self.date
    def __str__(self):
        return str(self.date)



# Store application data Models, Relationships etc.
# Create your models here.
