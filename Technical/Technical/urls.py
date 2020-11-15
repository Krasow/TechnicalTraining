from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pages.views import (
                home_view,
                account_view,
                registration_view,
                test_view,
                grade_view,
                week1_switch,
                week2_switch,
                week3_switch,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('home/', home_view),
    path('account/switch1', week1_switch, name='week1'),
    path('account/switch2', week2_switch, name='week2'),
    path('account/switch3', week3_switch, name='week3'),
    path('account/test', test_view, name='test'),
    path('account/grades', grade_view, name='grade'),
    path('account/', account_view, name='account'),
    path('account/register', registration_view, name='register'),
    #needed to be last since these are the default views and django sorts through the views in order. Once found, it returns without looking at the rest.
    #auth views include password changing/reset and login logout. Paths above are custom views for some of the default views.
    path('', include("django.contrib.auth.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG==True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)