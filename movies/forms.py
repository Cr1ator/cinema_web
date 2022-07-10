from django import forms

from movies.models import Reviews, Rating, RatingStar


class ReviewForm(forms.ModelForm):
    captcha = forms.CharField()

    class Meta:
        model = Reviews
        fields = ("name", "email", "text", "captcha")
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control border"}),
            "email": forms.EmailInput(attrs={"class": "form-control border"}),
            "text": forms.Textarea(attrs={"class": "form-control border"})
        }


class RatingForm(forms.ModelForm):
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ("star",)

class MovieCreateForm(forms.ModelForm):
    title = forms.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Названия"
        verbose_name_plural = "Названии"


class MovieUpdateForm(forms.ModelForm):
    update= forms.CharField()

    def __str__(self):
        return self.update
    
    class Meta:
        verbose_name = "Обновления"
        verbose_name_plural = "Обновлении"