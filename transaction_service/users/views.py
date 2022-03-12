from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import UserRegisterForm


class SignUp(CreateView):
    form_class = UserRegisterForm
    # success_url = reverse_lazy('index')
    template_name = 'users/sign_up.html'
