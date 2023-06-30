from django.forms import ModelForm
from myprops.models import Props


class PropsForm(ModelForm):

    class Meta:
        model = Props
        fields = [
            "item",
            "description",
            "recipient",
        ]
