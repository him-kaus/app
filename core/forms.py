from django import forms
from .models import Meeting, Slot, CustomerQueries, Shop


class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        exclude = ('created_at', 'updated_at', 'Client', 'Link', 'Status', 'PaymentLink')
        widgets = {
            'Date': forms.DateInput(
                attrs={'onchange': 'check()', 'class': 'datepicker form-control shadow', 'placeholder': 'MM/DD/YY'}),
            'Slot': forms.Select(attrs={'class': 'form-control shadow', 'disabled': 'disabled'}),
            'AlgoTradingPlatform': forms.Select(attrs={'class': 'form-control shadow'}),
            'Comment': forms.Textarea(attrs={'class': 'form-control shadow'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['Slot'] = Slot.objects.none()


class QueriesForm(forms.ModelForm):
    class Meta:
        model = CustomerQueries
        fields = '__all__'


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = (
            'UploaderName', 'UploaderEmail', 'UploaderPhone', 'StrategyName', 'CapitalRequired', 'Segment', 'Price',
            'Image', 'Youtube', 'Website', 'Tradingview', 'Telegram', 'Platform')
        widgets = {
            'Segment': forms.Select(attrs={'class': 'form-control shadow'}),
        }

    def __init__(self, *args, **kwargs):
        super(ShopForm, self).__init__(*args, **kwargs)
        self.fields['UploaderName'].widget.attrs = {'class': 'form-control shadow ', }
        self.fields['UploaderEmail'].widget.attrs = {'class': 'form-control shadow', }
        self.fields['UploaderPhone'].widget.attrs = {'class': 'form-control shadow', }
        self.fields['StrategyName'].widget.attrs = {'class': 'form-control shadow ', }
        self.fields['Image'].widget.attrs = {'class': 'form-control shadow ', }
        self.fields['CapitalRequired'].widget.attrs = {'class': 'form-control shadow', }
        self.fields['Price'].widget.attrs = {'class': 'form-control shadow', }
        self.fields['Youtube'].widget.attrs = {'class': 'form-control shadow', }
        self.fields['Website'].widget.attrs = {'class': 'form-control shadow', }
        self.fields['Tradingview'].widget.attrs = {'class': 'form-control shadow', }
        self.fields['Telegram'].widget.attrs = {'class': 'form-control shadow', }
        self.fields['Platform'].widget.attrs = {'class': 'form-control shadow', }
