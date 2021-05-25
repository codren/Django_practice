from django.contrib import admin
from django.utils.html import format_html
from .models import Order
class OrderAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    list_display = ('user', 'product', 'styled_status')

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
