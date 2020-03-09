# Airbnb-Clone

[초기 접속]
pipenv --three
pipenv shell
pipenv install django==2.2.5 (초기에 django 설치시에만)
그리고 앞으로 무슨 패키지를 설치하더라도 pip install이 아닌 pipenv install을 사용해야 버블 안에서 설치가 가능하다.

이후에 각 폴더(어플리케이션)에 데이터 모델링을 정의하고 실제 적용해 구동시키려면 아래 명령어를 활용한다.

[프로젝트 폴더 생성]

- 초기 기본 세팅
  django-admin startproject xxxx

- 여러가지 폴더(어플리케이션 생성)
  django-admin startapp xxxx
  이를 통해 Users, converstaions, lists, reviews, reservatiomns, rooms 폴더를 동일한 방식으로 만들어 준다.
  users 폴더를 새로 만드는 이유는 장고는 기본적으로 제공하는 데이터 모델들이 있지만 우리가 커스텀을 해야하기 때문에 별도 생성해 사용한다.

[실행]
python manage.py makemigration
python manage.py migrate
python manage.py runserver
python manage.py createsuperuser -> 초기 admin 접속 계정을 만들기 위함

[에러 종류 확인]
가끔 보면 Migrate할 때 에러가 나는 경우가 이는데, 이 경우에 각 폴더(어플리케이션)의 Migration을 다 지워버리고 새 migration 폴더로 갈아주면 된다.

캐시 파일은 지워도 무방하긴하다.
