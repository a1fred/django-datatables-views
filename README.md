# Installation
```pip install django-datatables-views```

# Usage example

views.py:
```python
# coding=utf-8
from datatables_views.cbv import DataTableListView


class MyModelListVIew(DataTableListView):
    template_name = 'list.html'
    queryset = models.Mymodel.objects.filter(deleted=False)
    dt_fields = [
        DTColumn(
            u"Name",
            searching=True,
            hidden=False,
            render_func=lambda m: "<a href='%s'>%s</a>" % (m.get_absolute_url(), unicode(m))
        ),
        DTColumn(
            u"Creation date",
            searching=False,
            hidden=False,
            render_func=lambda m: str(m.created)
        ),
        DTColumn(
            u"Type",
            searching=True,
            hidden=False,
            search_choices=["choice1", "choice2", "choice3"]
            render_func=lambda m: str(m.created)
        ),
```
