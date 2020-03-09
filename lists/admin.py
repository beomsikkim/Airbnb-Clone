from django.contrib import admin

# 아래 처럼 가져옴으로써 현재 폴더(어플리케이션)에 위치한 model.py 내용을 참조한다.
from . import models

# Register your models here.
@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):
    pass
