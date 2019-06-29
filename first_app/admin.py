from django.contrib import admin
from first_app.models import AccessRecord,Topic,Webpage,Users
# Register model, create admin interface, super powerful and useful

# Super User, this allows only the person who created the project to interact with the database.

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(Users)

# Register your models here.
