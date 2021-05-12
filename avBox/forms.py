from django.forms import ModelForm
from avBox.models import *

class Form(ModelForm):
    class Meta:
        model = Article
        fields=['av_code', 'av_title', 'av_contents', 'av_url', 'cover_path', 'thum_path', 'actor_name', 'actor_code']
