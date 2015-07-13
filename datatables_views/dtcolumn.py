# coding=utf-8
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


class DTColumn(object):
    template_path = 'core/filters/field.jinja2'

    def __init__(
            self,
            name,
            searching=True,
            hidden=False,
            field_type="html",
            orderable=True,
            className = "",
            cellType = "td",
            search_choices = None,
            render_func=lambda m: str(m)
    ):
        self.name = name
        self.searching=True if searching else False
        self.hidden = True if hidden else False
        self.field_type=field_type
        self.orderable = True if orderable else False
        self.render_func = render_func
        self.className = str(className)
        self.cellType = str(cellType)

        if searching and search_choices:
            self.search_choices = search_choices or None
        else:
            self.search_choices = None

    def render(self, item):
        return self.render_func(item)

    def render_filter(self, column_counter=0):
        rendered = render_to_string(self.template_path, {'field': self, 'counter': column_counter})
        return mark_safe(rendered)

