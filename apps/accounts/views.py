from django.shortcuts import render

# Create your views here.
from django.views import View


class Login(View):
    template_name = "account/index.html"

    def get(self, request):
        return render(request, template_name=self.template_name)
