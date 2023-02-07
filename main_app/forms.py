from django.forms import ModelForm
from .models import History

# Django's ModelForm class is designed 
# to create an HTML5 Form from a model

class HistoryForm(ModelForm):
    class Meta:
        model = History
        fields = ('date', 'status')