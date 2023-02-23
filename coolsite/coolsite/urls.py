from django.urls import handler400, handler403, handler404, handler500
from django.conf.urls import url
from . import views

# Обработка ошибок 400, 403, 404 и 500
handler400 = 'myapp.views.handler400'
handler403 = 'myapp.views.handler403'
handler404 = 'myapp.views.handler404'
handler500 = 'myapp.views.handler500'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    # Добавляем маршруты для других страниц в вашем приложении
]

