
from .models import Member, City, Country
import django_filters


class MemberFilter(django_filters.FilterSet):
    country = django_filters.ModelChoiceFilter(
        queryset=Country.objects.all().order_by('name'),
        empty_label='Country'
    )
    city = django_filters.ModelChoiceFilter(
        queryset=City.objects.all().order_by('name'),
        empty_label='City'
    )

    class Meta:
        model = Member
        fields = [
            'first_name',
            'last_name',
            'country',
            'city',
            'gender',
            'birth_date',
            'phone_number',
            'email',
            'notes',
            'status',
            'profile_image'
        ]