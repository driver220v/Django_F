from django.forms import ModelForm, forms, fields

from scrapper.models import Film


class ScrapperDateField(fields.DateField):
    def to_python(self, value):
        value_parse(value)
        return value_parsed


# сдлелать под процент!!
class FilmForm(ModelForm):
    premier = ScrapperDateField()
    avg_tomatores = fields.DecimalField()

    class Meta:
        model = Film
        fields = '__all__'
