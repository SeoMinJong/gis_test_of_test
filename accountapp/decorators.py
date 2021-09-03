from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        target_user = User.objects.get(pk=kwargs['pk'])
        if target_user == request.user: # requset로 불러와진 user는 지금 요청을 보낸 user
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    return decorated