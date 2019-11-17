from django.db import models
from django.contrib.postgres.fields import ArrayField
import django_tables2 as tables
import django_filters as filters
from django import forms
import re
from django.db.models import F

# Create your models here.

class Bean(models.Model):
    """ The price and review_date fields are non-nullable although in practice all
     fields should be populated """
    blend_name = models.CharField(max_length=100,null=True,verbose_name="Bean")
    company_name = models.CharField(max_length=100,null=True,verbose_name="Company")
    roast = models.CharField(max_length=100,null=True)
    flavors = ArrayField(models.CharField(max_length=20),null=True,verbose_name="Flavor(s)")
    notes = ArrayField(models.CharField(max_length=20,blank=True),blank=True,null=True,verbose_name="Note(s)")
    description = models.TextField(null=True)
    origin = models.CharField(max_length=100,null=True)
    vendor_location = models.CharField(max_length=100,null=True,verbose_name="Location")
    price = models.CharField(max_length=100,null=True)
    vendor_website = models.CharField(max_length=100,null=True,verbose_name="Website")
    vendor_phone = models.CharField(max_length=50,null=True,verbose_name="Phone Number")
    review_date = models.CharField(max_length=50,null=True,verbose_name="Review Date")

    def __str__(self):
        return f"{self.blend_name} for {self.price} from {self.company_name} as of {self.review_date}"


class BeanTable(tables.Table):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def render_flavors(self,value):
        return ",\n".join(value)

    def render_notes(self, value):
        return ",\n".join(value)

    price = tables.Column(orderable=False)
    review_date = tables.Column(order_by="id")
    description = tables.Column(attrs={"td":{"class":"desc"}})

    class Meta:
        model = Bean
        template_name = "django_tables2/bootstrap.html"
        exclude = ['id','vendor_phone']

ROAST_CHOICES = (
    ('Light','Light'),
    ('Medium-Light','Medium-Light'),
    ('Medium','Medium'),
    ('Medium-Dark','Medium-Dark'),
    ('Dark','Dark')
)

FLAVOR_CHOICES = (
    ('Fruity','Fruity'),
    ('Floral','Floral'),
    ('Sweet','Sweet'),
    ('Earthy/Herbal','Earthy/Herbal'),
    ('Nutty','Nutty'),
    ('Spice','Spice'),
    ('Smoky','Smoky'),
    ('Chocolatey','Chocolatey')
)

class BeanFilter(filters.FilterSet):
    # blend_name = filters.CharFilter(lookup_expr="icontains")
    company_name = filters.CharFilter(lookup_expr="icontains")
    origin = filters.CharFilter(lookup_expr="icontains")
    vendor_location = filters.CharFilter(lookup_expr="icontains")
    review_date = filters.CharFilter(lookup_expr="icontains")
    notes = filters.CharFilter(method='notes_filter',widget=forms.TextInput)
    roast = filters.MultipleChoiceFilter(choices=ROAST_CHOICES,widget=forms.CheckboxSelectMultiple(),label="Roast")
    flavors = filters.MultipleChoiceFilter(method='flavors_filter',choices=FLAVOR_CHOICES,
                                           widget=forms.CheckboxSelectMultiple,label="Flavor(s)")

    class Meta:
        model = Bean
        # Had to keep fields in order to satisfy using Meta
        fields = {
            'blend_name': ['icontains'],
        }


    def flavors_filter(self, queryset, name, value):
        return queryset.filter(flavors__contains=value)

    def notes_filter(self, queryset, name, value):
        note_filters = re.findall("\\w+",value)
        for index in range(len(note_filters)):
            note_filters[index] = note_filters[index].capitalize()
        return queryset.filter(notes__contains=note_filters)