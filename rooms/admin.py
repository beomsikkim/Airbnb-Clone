from django.contrib import admin
from . import models


# admin.py에 각 class에 적어 놓으면 admin 패널에서 보이는 컬럼 값들을 조정할 수 있다.
# 예를들어 내가 이름, 이메일, 주소 만 보고 싶은 경우


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    # ModelAdmin이라는 이름 자체가 admin 패널에 있는 데이터 모델에 대한 정보를 말함

    # 일단 admin.ModelAdmin으로 가져오고 pass 하게 되면 장고에서 제공하는 기본 모든 데이터 표현식과 내가 models.py에서 정의한 모델을 모두 분류없이 가져온다.
    # 하지만 아래와 같이 fieldsets을 다시 정의하면 그 중에서 내가 admin 패널에 실제 표현할 모델만 필드별로 나누는게 가능하다.
    fieldsets = (
        ("Basic Info", {"fields": ("name", "country", "city", "price",)},),
        ("Time", {"fields": ("check_in", "check_out")},),
        ("Spaces", {"fields": ("guest", "bed", "bedrooms", "baths",)},),
        (
            "More About the Spaces",
            {"fields": ("amenities", "facilities", "house_rules",)},
        ),
        ("Last Details", {"fields": ("host",)},),
    )

    # 아래 list를 작성함으로써 admin 패널의 컬럼을 내마음대로 커스텀 가능하다.
    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guest",
        "bed",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
    )

    ordering = ("name", "price")

    list_filter = (
        "instant_book",
        "city",
        "host__superhost",
        "country",
    )

    search_fields = ("=city", "^host__username")

    # horizontal filter는 ManyToMany 타입만 필터링 가능함
    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    # self는 위의 RoomAdmin class를 말함
    def count_amenities(self, obj):
        return obj.amenities.count()

    # self가 Room의 RoomAdmin class를 참조하고 있고, 해당 Room은 외래키로 Photo class랑 연결되어 있어서 링크 가능하다
    # return의 photose는 related_name이다.(models.py에 정의함)
    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
