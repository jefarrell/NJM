from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.template.defaultfilters import slugify

from tiles.forms import ProfileImageForm
from tiles.models import ProfileImage
import logging


class ProfileImageView(generic.FormView):
    template_name = 'tiles/profile_image_form.html'
    form_class = ProfileImageForm

    def form_valid(self, form):
        profile_image = ProfileImage(
            image=self.get_form_kwargs().get('files')['image'], description=form.cleaned_data['text'], date=timezone.now(), title=form.cleaned_data['title'], weblink=form.cleaned_data['weblink'])
        profile_image.save()
        self.id = profile_image.id
        self.s = profile_image.slug

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('tiles:profile_image', kwargs={"slug": self.s, "pk": self.id})

class ProfileDetailView(generic.DetailView):
    model = ProfileImage
    template_name = 'tiles/profile_image.html'
    context_object_name = 'image'

class ProfileImageIndexView(generic.ListView, generic.FormView):
    model = ProfileImage
    template_name = 'tiles/profile_image_view.html'
    context_object_name = 'images'
    form_class = ProfileImageForm

    def get_queryset(self):
        return ProfileImage.objects.filter(date__lte=timezone.now()).order_by('-date')[:]

    def form_valid(self, form):
        profile_image = ProfileImage(
            image=self.get_form_kwargs().get('files')['image'], description=form.cleaned_data['text'], date=timezone.now(), title=form.cleaned_data['title'], weblink=form.cleaned_data['weblink'])
        profile_image.save()
        self.id = profile_image.id
        self.s = profile_image.slug

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('tiles:profile_image', kwargs={"slug": self.s, "pk": self.id})


class ResultsView(generic.DetailView):
    model = ProfileImage;
    template_name = 'tiles/results.html'

class DetailView(generic.DetailView):
    model = ProfileImage
    template_name = 'tiles/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return ProfileImage.objects.filter(date__lte=timezone.now())



