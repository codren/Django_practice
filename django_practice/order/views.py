from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .models import Order
from .forms import RegisterForm
class OrderCreate(FormView):
    form_class = RegisterForm
    success_url = '/product/'
    
    def form_invalid(self, form):
        return redirect('/product/' + str(form.data.get('product'))) 

    def get_form_kwargs(self, **kwargs):    
        kw = super().get_form_kwargs(**kwargs)  
        kw.update({'request': self.request})
        print(kw)
        return kw

class OrderList(ListView):
    template_name = 'order.html'
    context_object_name = 'order_list'
    # model = Order

    def get_queryset(self, **kwargs):
        queryset = Order.objects.filter(user__email=self.request.session.get('user'))
        return queryset
