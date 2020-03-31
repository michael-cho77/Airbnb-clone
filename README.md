# Airbnb-clone

Cloneing airbnb using Python, Django, etc...

NOTE (2020.03)
일반적인 프로젝트상에서는 모두 정상구동 확인
social login Part 에러 수정

    해당 프로젝트는 다운로드 후
    터미널에서
    1) pipenv shell
    2) python manage.py migrate
    3) python manage.py runserver
       을 통하여 실행가능합니다.

    cf) admin 사이트는
        python manage.py createsuperuser 을 통해 생성가능합니다.
        aws상에서는 migration과 admin이 이미 생성되어 있으며 아이디와 암호는 아래 기재했습니다.

AWS Server :
http://airbnb-clone.cbfai3acf3.ap-northeast-2.elasticbeanstalk.com/

How to Login
Main Page
access
http://airbnb-clone.cbfai3acf3.ap-northeast-2.elasticbeanstalk.com/
ID : michael_cho77@naver.com
PWD: 123456

ADMIN PAGE
access
http://airbnb-clone.cbfai3acf3.ap-northeast-2.elasticbeanstalk.com/admin
ID : admin
PWD: 123456

cf)
소셜로그인의 정상 구동을 위해선 - 가입하려는 계정의 이메일이 public(공개)상태일것
