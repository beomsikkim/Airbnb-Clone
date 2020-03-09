from django.db import models


class TimeStampedModel(models.Model):
    """ Time Stamped Model """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # abstract를 설정해주면 위 모델이 데이터베이스에 등록되지 않는다.
    # 왜냐면 지금 모델은 다른 어플리케이션들이 참조하기 위한 공통 값이지, 이 값 자체를 등록하려는 의도가 아니기 때문이다.
    class Meta:
        abstract = True
