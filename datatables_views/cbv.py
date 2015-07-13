from django.views.generic import TemplateView
from amphetamine.shortcuts import jsonResp
from core.cbv_mixins import RequestContextMixin


class DataTableListView(RequestContextMixin, TemplateView):
    model = None
    queryset = None
    template_name = "core/datatablelist.jinja2"
    table_id = "dt_table"
    dt_fields = []

    def get_context_data(self, *a, **k):
        context = super(DataTableListView, self).get_context_data(*a, **k)
        context["table_fields"] = self.get_table_fields()
        context["table_id"] = self.table_id or "dt_table"
        return context

    def get_table_fields(self):
        return self.dt_fields

    def post_queryset(self):
        if self.queryset is not None:
            return self.queryset
        else:
            return self.model.objects.all()

    def post_list(self):
        return [self.post_serialize_item(m) for m in self.post_queryset()]

    def post_serialize_item(self, item):
        return map(
            lambda dtfield: dtfield.render(item),
            self.dt_fields
        )

    def post(self, request):
        return jsonResp({'data': self.post_list()})
