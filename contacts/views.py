from django.urls import reverse_lazy
from django.views.generic import CreateView

from contacts.forms import ContactForm
from contacts.models import Contact
from base.models import ExtendedFlatPage


class AddContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = "contacts/consult.html"
    success_url = reverse_lazy("success")

    def get_context_data(self, *args, **kwargs):
        context = super(AddContactView, self).get_context_data(**kwargs)
        context["flatpage"], created = ExtendedFlatPage.objects.get_or_create(url="/consult/")
        return context
