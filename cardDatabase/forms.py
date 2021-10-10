from django import forms

from fowsim import constants as CONS


class SearchForm(forms.Form):
    generic_text = forms.CharField(label='', strip=True,
                                   widget=forms.TextInput(attrs={'placeholder': 'Search...'}))


class AdvancedSearchForm(forms.Form):
    generic_text = forms.CharField(label='', strip=True,
                                   widget=forms.TextInput(attrs={'placeholder': 'Search...'}), required=False)
    text_search_fields = forms.MultipleChoiceField(label='Search Card:', choices=CONS.TEXT_SEARCH_FIELD_CHOICES, required=False)
    colours = forms.MultipleChoiceField(label='Color(s):', choices=CONS.COLOUR_CHOICES, required=False)
    sets = forms.MultipleChoiceField(label='Set(s):', choices=CONS.SET_CHOICES, required=False)
    cost = forms.MultipleChoiceField(label='Total Cost(s):', choices=CONS.TOTAL_COST_CHOICES, required=False)
