from django.shortcuts import render

from django.views.generic import TemplateView

class Home(TemplateView):
  template_name = "home.html"

from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from .models import *

class QuestionCreateView(CreateView):
  model = Question
  template_name = "question/question_form.html"
  fields = ['title', 'description']
  success_url = reverse_lazy('home')

  def form_valid(self, form):
       form.instance.user = self.request.user
       return super(QuestionCreateView, self).form_valid(form)
