from django.conf.urls import url
from django.conf.urls import patterns

from . import views

urlpatterns = patterns('',
                       url(r'^$', views.contactView.as_view()),
                       url(r'^(?P<year>\d{4})/$', views.ArticleYearArchiveView.as_view(), name="article_year_archive"),
                       url(r'^(?P<year>\d{4})/week/(?P<week>\d+)/$', views.ArticleWeekArchiveView.as_view()),
                       url(r'^(user/(?P<pk>\d+))/$', views.UserDetailView.as_view()),
                       url(r'^(modify_user)/$', views.AddLinksToProfile)
                       )
