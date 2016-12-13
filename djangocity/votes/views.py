from django.views.generic import TemplateView

from .models import Voter


class DashboardView(TemplateView):
    template_name = 'votes/dashboard.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['voters'] = Voter.objects.all()
        return context_data