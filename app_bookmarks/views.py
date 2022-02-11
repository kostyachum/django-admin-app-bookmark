from django.core.handlers.wsgi import WSGIRequest
from django.db.models import F
from django.http import HttpResponseRedirect
from django.views import View
from .models import AppBookmark


class UpdateAppBookmarkView(View):

    def post(self, request: WSGIRequest):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        app_label = request.POST.get('app')

        is_update = 'update' in  request.POST
        is_up = 'up' in  request.POST
        is_down = 'down' in  request.POST

        if is_update:
            if AppBookmark.objects.filter(user_id=request.user.pk, app_label=app_label).exists():
                AppBookmark.objects.filter(user_id=request.user.pk, app_label=app_label).delete()
            else:
                AppBookmark.objects.create(user_id=request.user.pk, app_label=app_label, order=AppBookmark.objects.filter(user_id=request.user.pk).count() + 1)

        if is_up:
            obj = AppBookmark.objects.get(user_id=request.user.pk, app_label=app_label)
            AppBookmark.objects.filter(user_id=request.user.pk, order__gte=obj.order - 1).update(order=F('order') + 1)
            obj.order = obj.order - 1
            obj.save()


        if is_down:
            obj = AppBookmark.objects.get(user_id=request.user.pk, app_label=app_label)
            AppBookmark.objects.filter(user_id=request.user.pk, order__lte=obj.order + 1).update(order=F('order') - 1)
            obj.order = obj.order + 1
            obj.save()


        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
