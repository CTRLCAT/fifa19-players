from django import forms
from players.models import LogMessage

class LogMessageForm(forms.ModelForm):
    class Meta:
        model=LogMessage
        fields=('message',)