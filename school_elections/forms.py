from django import forms
from .models import Candidate

class VoteForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(VoteForm, self).__init__(*args, **kwargs)
        for position in Candidate.POSITION_CHOICES:
            candidates = Candidate.objects.filter(position=position[0])
            self.fields[position[0]] = forms.ModelChoiceField(
                queryset=candidates,
                widget = forms.RadioSelect,
                label=position[1],
                required= True
            )