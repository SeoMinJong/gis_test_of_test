from .base import *


env_list = dict()

local_env = open(os.path.join(BASE_DIR, '.env'))

while True:
    line = local_env.readline()
    if not line:
        break
    line = line.replace('\\n', '')  # 한줄로
    start = line.find('=')  # = 이 있는 곳을 찾기
    key = line[:start]  # 왼쪽부분을 키  SECRET_KEY = 'django-insecure-ez14bcuso741!155ys$8h1v6kl-gs$ok-)8k56ll*6jz!cr404'
    value = line[start + 1:]  # 오른쪽을 밸류
    env_list[key] = value  # 반복문으로 라인을 부르고 파일의 끝에 도달하면 라인이 아니므로 멈춤

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$k_dl(kdp$tx3#mog9kxvqc4$!lknt00+kyqdbjh1l9)@6l+%9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'password1234',
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}