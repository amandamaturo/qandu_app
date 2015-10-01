from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
   url(r'^$', Home.as_view(), name='home'),
   url(r'^user/', include('registration.backends.simple.urls')),
   url(r'^user/', include('django.contrib.auth.urls')),
   url(r'^question/create/$', QuestionCreateView.as_view(), name='question_create'),
   url(r'^question/$', QuestionListView.as_view(), name='question_list'),
   url(r'^question/(?P<pk>\d+)/$', QuestionDetailView.as_view(), name='question_detail'),
   url(r'^question/update/(?P<pk>\d+)/$', QuestionUpdateView.as_view(), name='question_update'),
   url(r'^question/delete/(?P<pk>\d+)/$', QuestionDeleteView.as_view(), name='question_delete'),
   url(r'^question/(?P<pk>\d+)/answer/create/$', AnswerCreateView.as_view(), name='answer_create'),
)