import os

# This configures the settings for the project, you have to do this before you manipulate models
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_django_project.settings')

import django
django.setup()

import random
from first_app.models import AccessRecord,Webpage,Topic, Users
from faker import Faker

fakegen = Faker()

topics = ['Search','Social','Marketplace','News','Games','Sports']


def firstName():
    full_name = fakegen.name()
    first_name = full_name.split()[0]
    return first_name

def lastName():
    full_name = fakegen.name()
    last_name = full_name.split()[1]
    return last_name

def addUsers():
    user = Users.objects.get_or_create(first_name=firstName(),last_name=lastName(),email=fakegen.email())[0]
    return user



def populateUsers(N=5):
    for entry in range(N):
        addUsers()
        print("adding users")


# def addTopic():
#     t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
#     t.save()
#     return t

#
# def populate(N=5):
#     for entry in range(N):
#         top = addTopic()
#
#         fake_url = fakegen.url()
#         fake_date = fakegen.date()
#         fake_name = fakegen.company()
# you must pass down attributes from the other models here so there is relational data.
        # webpg = Webpage.objects.get_or_create(topic=top,url=fake_url, name=fake_name)[0]
        # print(webpg)
        #
        # acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]
        # print(acc_rec)

if __name__ == '__main__':
    print("user populating")
    populateUsers(20)
    print("it worked")
