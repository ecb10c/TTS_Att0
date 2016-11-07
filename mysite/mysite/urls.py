"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from mysite1 import views as view1
from mysite2 import views as view2
from django.contrib import admin


urlpatterns = [
    url(r'^test/', view2.test, name='test'),
    url(r'^mysite1/', view1.bootstraps, name='bootstrap'),
    url(r'^listPick/', view2.listPick, name='listPick'),
    url(r'^list0/', view2.list0, name='list0'),
    url(r'^list1/', view2.list1, name='list1'),
    url(r'^inputExcel/', view2.inputExcel, name='inputExcel'),
    url(r'^uploadExcel/', view2.uploadExcel, name='uploadExcel'),
    url(r'^admin/', admin.site.urls),
]

# def i18n_javascript(request):
#     return admin.site.i18n_javascript(request)
# 这个函数是为了解决调用django日历,普通用户无法访问admin的jsi18n，如果要用要放在urlpatterns上面
#这个函数是配合上方解决调用日历问题的，添加在url里
# url(r'^admin/jsi18n', i18n_javascript),


