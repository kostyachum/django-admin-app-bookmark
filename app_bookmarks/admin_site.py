from django.contrib.admin import AdminSite
from django.template.response import TemplateResponse
from django.urls import path

from . import models, views


class BookmarkedAdminSite(AdminSite):


    def get_app_list(self, request):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        order_apps = {o.app_label: o.order for o in models.AppBookmark.objects.filter(user_id=request.user.pk).only('app_label', 'order')}

        app_dict = self._build_app_dict(request)
        app_list = sorted(app_dict.values(), key=lambda x: self.get_app_order_index(x, order_apps))

        # Sort the models alphabetically within each app.
        for index, app in enumerate(app_list):
            app['models'].sort(key=lambda x: x['name'])
            app['is_marked'] = app['app_label'] in order_apps
            app['order'] = order_apps.get(app['app_label'])
            app['can_up'] = index > 0
            app['can_down'] = (index + 1) < len(order_apps)

        return app_list


    def index(self, request, extra_context=None):
        """
        Display the main admin index page, which lists all of the installed
        apps that have been registered in this site.
        """
        app_list = self.get_app_list(request)
        context = {
            **self.each_context(request),
            'title': self.index_title,
            'subtitle': None,
            'app_list': app_list,
            'allow_order': True,
            **(extra_context or {}),
        }
        request.current_app = self.name
        return TemplateResponse(request, self.index_template or 'admin/index.html', context)

    def get_app_order_index(self, app, marked_apps):
        if app['app_label'] in marked_apps:
            return marked_apps[app['app_label']]
        return len(marked_apps) + ord(app['app_label'][0])

    def get_urls(self):
        urls_patters = super().get_urls()
        urls_patters.append(
            path('bookmarks/update', views.UpdateAppBookmarkView.as_view(), name='admin-app-bookmarks-update-endpoint')
        )
        return urls_patters
