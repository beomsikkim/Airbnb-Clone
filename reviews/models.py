from django.db import models

# 아래 core는 모든 폴더(어플리케이션)에서 공통적으로 사용함
from core import models as core_models


# Create your models here.
class Review(core_models.TimeStampedModel):
    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    # 아래 ForeignKey에서 user는 폴더(어플리케이션)이고, User는 user 폴더 아래에서 models에 정의된 class임
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    """
    여기서 return 값으로 정해주지 않으면 django에서 default 값으로 정해진 값이 목록 이름으로 표기된다.
    아니라면 
    def __str__(self):
        return self.~~ 로 해주면 해당 값으로 표기함
    """

    def __str__(self):
        return f"{self.review} - {self.room}"

