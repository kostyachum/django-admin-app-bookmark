from django.contrib.admin.apps import AdminConfig

class BookmarkAdminConfig(AdminConfig):
    default_site = 'app_bookmarks.admin_site.BookmarkedAdminSite'
