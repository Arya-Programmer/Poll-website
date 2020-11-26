from django.shortcuts import render, redirect, Http404
from django.views.generic import DetailView
from .models.form_model import Form
from .validations import getIp, validate
import json
from stats.models import Stat

# Create your views here.


class PollDetail(DetailView):
    template_name = "poll_detail.html"
    slug_url_kwarg = "pollId"
    queryset = Form.objects.all()

    def get_object(self):
        obj = self.queryset.get(id=self.kwargs[self.slug_url_kwarg])
        return obj

    def post(self, request, *args, **kwargs):

        userInfo = getIp(request)
        answers = validate(request, self.get_object())

        print(userInfo, answers)
        if type(answers) == str:
            raise Http404()

        print(self.kwargs[self.slug_url_kwarg])

        Stat.objects.create(
            ip=userInfo[0],
            is_valid=userInfo[1],
            answers=str(answers),
            poll_id=self.kwargs[self.slug_url_kwarg]
        )


        return redirect("poll_detail", 1)
