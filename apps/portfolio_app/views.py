from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"  # templates/home.html

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = []
        return context


class AboutPageView(TemplateView):
    template_name = "about.html"  # templates/about.html

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = []
        return context
