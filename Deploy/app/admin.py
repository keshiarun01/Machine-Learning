from django.contrib import admin
from .models import UserImageModel, DoctorFeedModel

# Register your models here.
admin.site.register(UserImageModel);
admin.site.register(DoctorFeedModel);