from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models

# import할 때 좋은 coding 방식 => 가장 상위 패키지부터 위에서부터 나열한다. python > django > django 하위 패키지> 3rd party app 순으로 점점 작게


### 이곳에서는 Room에 대한 데이터 타입과 필요한 데이터들을 정의한다.
### 여기에서 정의하는 것은 Room에 대한 공통 모델을 정의한 것이지, 만약 admin 패널에서 사용하려면 admin.py에다가 등록해줘야 사용할 수 있다.
### 공통 모델이기 때문에 admin 패널이던, 사용자가 사용하는 ui에서건 여기를 참조할 수 있다.

# Abstract를 하는 이유는 DB에 넣지는 않을 것이지만 화면에 리스트를 표현하기 위한 아이템들을 정의하기 위해 사용한다.
# 예를들어 집 종류, 어메니티, 퍼실리티 목록 등을 정의하기 위해 사용된다. 이것들이 고객이 데이터를 주입하거나 해서 db에 순차적으로 기입될 필요는 없다.
class AbstractItem(core_models.TimeStampedModel):
    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


# 위에서 정의한 abstract를 상속받아 사용한다.
class RoomType(AbstractItem):
    pass

    class Meta:
        verbose_name = "Room Type"


# 위에서 정의한 abstract를 상속받아 사용한다.
class Amenity(AbstractItem):
    pass

    class Meta:
        verbose_name_plural = "Amenities"


# 위에서 정의한 abstract를 상속받아 사용한다.
class Facility(AbstractItem):
    pass

    class Meta:
        verbose_name_plural = "Facilites"


# 위에서 정의한 abstract를 상속받아 사용한다.
class HouseRule(AbstractItem):
    pass

    class Meta:
        verbose_name = "House Rule"


class Room(core_models.TimeStampedModel):
    """ ROOM MODEL DEFINITION """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guest = models.IntegerField()
    bed = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    # host는 User이기도 하니까 User 정의한 어플리케이션과 연결을 해야 함으로 이렇게 작성함
    # host는 여러개의 room을 가질 수 있기 때문에 일대 다의 관계이다.
    # CASCADE를 걸어준 이유는 user가 삭제될 경우에 그와 연관된 room을 모두 삭제시키기 위해서임
    # related_name 은 User가 room을 어떻게 찾을건지 그 이름을 정의한다. OneToMany의 관계
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
    )
    room_type = models.ForeignKey(
        "RoomType", related_name="rooms", on_delete=models.SET_NULL, null=True
    )
    # 다대다의 관계는 아래처럼 기술함
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    def __str__(self):
        return self.name + "'s room"


class Photo(core_models.TimeStampedModel):
    caption = models.CharField(max_length=80)
    file = models.ImageField()
    # Room이 지워질 경우 관련된 사진도 모두 지워진다는 ForeignKey이다.
    # 파이썬은 위에서 아래로 인식하기 때문에 Room Class 밑에다가 Photo Class를 위치시켰다.
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
