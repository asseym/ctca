from django.views.generic import DetailView
from pages.models import Page 

class PageDetailView(DetailView):

    context_object_name = "page"
    model = Page 

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PageDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_list'] = Page.objects.all()
        return context
