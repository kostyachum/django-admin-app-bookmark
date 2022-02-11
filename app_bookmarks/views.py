from django.core.handlers.wsgi import WSGIRequest
from django.db.models import F
from django.http import HttpResponseRedirect
from django.views import View
from .models import AppBookmark


class UpdateAppBookmarkView(View):
    admin_site = None

    def post(self, request: WSGIRequest):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        app_label = request.POST.get('app')

        is_update = 'update' in  request.POST
        is_up = 'up' in  request.POST
        is_down = 'down' in  request.POST

        if is_update:
            self._update(app_label, request)

        if is_up:
            self._move_up(app_label, request)

        if is_down:
            self._move_down(app_label, request)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    def _update(self, app_label, request):
        if AppBookmark.objects.filter(user_id=request.user.pk, app_label=app_label).exists():
            AppBookmark.objects.filter(user_id=request.user.pk, app_label=app_label).delete()
        else:
            AppBookmark.objects.create(user_id=request.user.pk, app_label=app_label, order=AppBookmark.objects.filter(user_id=request.user.pk).count() + 1)

    def _move_down(self, app_label, request):
        obj = AppBookmark.objects.get(user_id=request.user.pk, app_label=app_label)
        AppBookmark.objects.filter(user_id=request.user.pk, order__lte=obj.order + 1).update(order=F('order') - 1)
        obj.order = obj.order + 1
        obj.save()

    def _move_up(self, app_label, request):
        obj = AppBookmark.objects.get(user_id=request.user.pk, app_label=app_label)
        AppBookmark.objects.filter(user_id=request.user.pk, order__gte=obj.order - 1).update(order=F('order') + 1)
        obj.order = obj.order - 1
        obj.save()
