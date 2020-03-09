from django.contrib import admin
from . import models

# Register your models here.
# 아래 @를 통해 models.py에 정의한 class를 가지고 온다.
@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
