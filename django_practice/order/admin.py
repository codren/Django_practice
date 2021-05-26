from django.contrib import admin
from django.db.models import Q
from django.db import transaction
from django.contrib.admin.models import LogEntry, CHANGE
from django.contrib.contenttypes.models import ContentType
from django.utils.html import format_html
from .models import Order
from product.models import Product
class OrderAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    list_display = ('user', 'product', 'styled_status')
    change_list_template = 'admin/order_change_list.html'

    def refund(modeladmin, request, queryset):      
        with transaction.atomic():                 
            qs = queryset.filter(~Q(status='환불'))    
            ct = ContentType.objects.get_for_model(queryset.model)
            for obj in qs:
                product = Product.objects.get(pk=obj.product.id)
                if obj.product.stock == product.stock:
                    obj.product.stock += obj.quantity
                    obj.product.save()
                else:
                    product.stock += obj.quantity
                    product.save()

                LogEntry.objects.log_action(       
                    user_id = request.user.id,
                    content_type_id = ct.pk,
                    object_id = obj.pk,
                    object_repr = '주문 환불',
                    action_flag = CHANGE,
                    change_message = '주문 환불'
                )
            qs.update(status='환불')   
                     
    refund.short_description = '환불'  

    actions = [ refund ]

    def styled_status(self, obj):
        if obj.status == '환불':
            return format_html(f'<span style="color:red">{obj.status}</span>')
        if obj.status == '결제완료':
            return format_html(f'<span style="color:green">{obj.status}</span>')
        return obj.status
    
    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': '주문 목록'}   
        return super().changelist_view(request, extra_context)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        if object_id:
            order = Order.objects.get(pk=object_id)
            extra_context = {'title': f'{order.user.email}의 {order.product.name} 수정하기'}
        return super().changeform_view(request, object_id, form_url, extra_context)  

    styled_status.short_description = '상태'

admin.site.register(Order, OrderAdmin)
