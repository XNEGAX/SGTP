from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.generic import View,TemplateView,FormView

from general.forms.login_form import LoginForm

class LoginFormView(FormView):
    template_name = 'login/index.html'
    form_class = LoginForm

    def get_context_data(self, **kwargs):
        context = super(LoginFormView, self).get_context_data(**kwargs)
        #context["testing_out"] = "this is a new context var"
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        #form.send_email()
        #print "form is valid"
        return super(LoginFormView, self).form_valid(form)