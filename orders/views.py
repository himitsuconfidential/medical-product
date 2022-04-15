from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from orders.models import ClinicManager, Order

def hello(request):
    return HttpResponse('Hello, user!')
class ViewAll(TemplateView):
    template_name = "view_all.html"
    def get_context_data(self, **kwargs):
        context = { "orders": [
        { "time": "Feb. 1, 2022, 10:31 a.m.",
        "status": "Delivered"
        },
        { "time": "Feb. 2, 2022, 2:25 p.m.",
        "status": "Delivered"
        },
        { "time": "Feb. 2, 2022, 8:54 p.m.",
        "status": "Confirmed"
        },
        { "time": "Jan. 3, 2020, 6:01 a.m.",
        "status": "Confirmed"
        }
        ]}
        return context

class ManagerViewOrders(TemplateView):
    template_name = "order_list.html"
    def get_context_data(self, **kwargs):
        manager_id = self.kwargs['manager_id']

        context = super().get_context_data(**kwargs)
        context['order_list'] = Order.objects.filter(manager__pk = manager_id)
        context['manager'] = ClinicManager.objects.get(pk = manager_id)
        return context
