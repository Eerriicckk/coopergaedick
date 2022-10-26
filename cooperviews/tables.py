import django_tables2 as tables
from .models import Associados

class PersonTable(tables.Table):
    class Meta:
        model = Associados
        