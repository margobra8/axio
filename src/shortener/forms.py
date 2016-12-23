from django import forms


# from django.core.validators import URLValidator


class SubmitUrlForm(forms.Form):
    url = forms.URLField(label="Submit URL")

    # def clean(self):
    #     cleaned_data = super(SubmitUrlForm, self).clean()
    #     url = cleaned_data.get("url")
    #     print(url)
    #
    # def clean_url(self):
    #     url = self.cleaned_data.get("url")
    #     print(url)
    #     try:
    #         URLValidator(url)
    #     except:
    #         raise forms.ValidationError("Invalid URL")
    #     return url
