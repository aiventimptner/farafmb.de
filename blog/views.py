import random

from blog.forms import ProtocolForm
from blog.models import Snippet, Post, Protocol, Link
from datetime import date
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from meetings.models import Meeting


class PostsView(ListView):
    template_name = 'blog/posts.html'
    model = Post
    ordering = ['-created']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['meetings'] = Meeting.objects.filter(date__gte=date.today())
        return context


class ContactView(TemplateView):
    template_name = 'blog/contact.html'


class ProtocolView(CreateView):
    model = Protocol
    template_name = 'blog/protocol_form.html'
    form_class = ProtocolForm
    success_url = reverse_lazy('blog:protocols-success')

    def form_valid(self, form):
        form.instance.file.name = hex(random.randrange(16 ** 8))[2:] + '.pdf'
        return super().form_valid(form)


class ProtocolSuccessView(TemplateView):
    template_name = 'blog/protocol_form_done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['snippet'] = get_object_or_404(Snippet, slug='protocol_submitted')
        return context


class LinksView(ListView):
    template_name = 'blog/links.html'
    model = Link
    queryset = Link.objects.filter(visible=True)
