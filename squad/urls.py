from django.contrib import admin
from django.utils import timezone
from django.urls import path, include
from .views import home_page
from . import settings
from django.views.decorators.http import last_modified
from django.views.i18n import JavaScriptCatalog
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

last_modified_date = timezone.now()

urlpatterns = [
	#path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
	path("jsi18n/",
        last_modified(lambda req, **kw: last_modified_date)(
            JavaScriptCatalog.as_view()
        ),
        name="javascript-catalog",
    ),
	path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('', include('users.urls')),
    path('robot/', include('pages.urls')),
	

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
