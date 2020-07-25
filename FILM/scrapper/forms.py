from django.forms import ModelForm, fields
from scrapper.models import Film
from time import strptime
from collections import namedtuple
from string import punctuation
from datetime import datetime


def trash_remover(date: list):
    for sign in punctuation:
        for idx, entry in enumerate(date):
            if sign in entry:
                raw_sign = entry.replace(sign, '')
                date[idx] = raw_sign

    return date


class ScrapperDateField(fields.DateField):
    def to_python(self, value):
        #
        date = value.split()
        date_clean: list = trash_remover(date)
        premier_sample = namedtuple('Buildings', 'month, day, year')
        premier_composed = premier_sample._make(date_clean)
        month_num = strptime(premier_composed.month, '%b').tm_mon
        str_time = f'{premier_composed.day}/{month_num}/{premier_composed.year}'
        to_date_convert = datetime.strptime(str_time, '%m/%d/%Y')
        # date_to_return  = 2017-12-05
        date_to_return = to_date_convert.date()
        return date_to_return


# сдлелать под процент!!
class FilmForm(ModelForm):
    # premier = May 12, 2017
    premier = ScrapperDateField(input_formats=['%Y-%m-%d'])
    # Expect 2017-05-12

    class Meta:
        model = Film
        fields = '__all__'
