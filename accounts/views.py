from django.shortcuts import render
from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class ProfileView(LoginRequiredMixin, View):
    template_name = 'accounts/profile.html'
    def get(self, request):
        
        # context = {
            
        # }
        return render(request, self.template_name)
