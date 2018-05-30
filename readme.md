
## drf的安装
```
pip install djangorestframework
pip install markdown
pip install django-filter
pip install coreapi
pip install django-crispy-forms
pip install django-guardian
pip install Pillow

INSTALLED_APPS = (
    ...
    'rest_framework',
)

urlpatterns = [
    ...
    url(r'^api-auth/', include('rest_framework.urls'))
]
```