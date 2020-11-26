from django.shortcuts import render
from django.views.generic import DetailView
from .models import Stat
from items.models.form_model import Form
from .poll_static import staticing

# Create your views here.
class PollStatDetail(DetailView):
    template_name = "poll_stats.html"
    queryset = Stat.objects.all()
    slug_url_kwarg = 'pollId'

    def get_object(self):
        obj = self.queryset.filter(poll_id=self.kwargs[self.slug_url_kwarg])
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        stats = staticing(self.object, Form.objects.filter(id=self.kwargs['pollId']))
        print(stats)

        context["users_number"] = len(self.queryset.filter(poll_id=self.kwargs['pollId']))
        context["questions"] = Form.objects.get(id=self.kwargs['pollId'])
        context["stats"] = stats

        return context
