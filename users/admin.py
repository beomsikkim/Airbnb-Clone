from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.

# 바로 아래 @admin줄은 데코레이터로 바로 아래 클래스가 오면 참조해서 model을 컨트롤할 수 있다. 여기서는 class가 models.User를 컨트롤하게 한다.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    # 위의 클래스를 통해서 공통으로 사용할 models를 가져오고 admin 패널에서 해당 모델을 가져와서 커스텀 구성하고 거기에 있는 구성 값들을 가져와서 그에 맡게 패널을 구성하는 것
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "Avatar",
                    "Gender",
                    "bio",
                    "birthDate",
                    "language",
                    "currency",
                    "superHost",
                ),
            },
        ),
    )
