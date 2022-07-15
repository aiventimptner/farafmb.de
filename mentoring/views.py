from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from .forms import ProgramForm, MentorForm
from .models import Program, Mentor


class ProgramCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Program
    form_class = ProgramForm
    success_url = reverse_lazy('mentoring:program-create')
    success_message = _("%(name)s was created successfully")


class MentorCreateView(LoginRequiredMixin, CreateView):
    model = Mentor
    form_class = MentorForm
    success_url = reverse_lazy('create-mentor-done')


class MentorCreateDoneView(LoginRequiredMixin, TemplateView):
    template_name = 'mentoring/mentor_form_done.html'


class MentorListView(LoginRequiredMixin, ListView):
    template_name = 'mentoring/mentor_list.html'
    model = Mentor
