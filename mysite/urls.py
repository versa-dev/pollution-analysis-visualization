from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls import url
from accounts import views as accounts_views

from django.contrib.auth import views as auth_views
from boards import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    # path('accounts/', include('accounts.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
   path('', views.home, name='home'), # 2nd home page
    # url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    # url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    path('boards/', include('boards.urls')),
    url(r'^reset/$',
    auth_views.PasswordResetView.as_view(
        template_name='password_reset.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt'
    ),
    name='password_reset'),
    url(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.topic_posts, name='topic_posts'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$', views.reply_topic, name='reply_topic'),
    path('pollution/', include('pollution.urls')),
    path('upload/', include('uploadfile.urls')),
    path('plotone/', include('plotone.urls')),
    path('plottwo/', include('plottwo.urls')),
    path('plotthree/', include('plotthree.urls')),
    path('plotfour/', include('plotfour.urls')),
    path('plotfive/', include('plotfive.urls')),
    path('plotsix/', include('plotsix.urls')),
    path('plotseven/', include('plotseven.urls')),
]

