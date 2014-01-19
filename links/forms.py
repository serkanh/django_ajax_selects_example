from django.db import models
from django.forms import ModelForm
from .models import Link
from ajax_select import make_ajax_field
from ajax_select.fields import AutoCompleteSelectField

class LinkForm(ModelForm):
    tags = make_ajax_field(Link, 'tags', 'taglookup', help_text="Please enter up to 5 software products you are authorized to sell.")
    class Meta:
        model = Link

