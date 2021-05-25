from django.contrib import admin
from .models import User
class UserAdmin(admin.ModelAdmin):
    list_display = ('email',)

    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': '사용자 목록'}   
        return super().changelist_view(request, extra_context)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        if object_id:
            user = User.objects.get(pk=object_id)
            extra_context = {'title': f'{user.email} 수정하기'}
        return super().changeform_view(request, object_id, form_url, extra_context)  

admin.site.register(User, UserAdmin)

# 관리자 페이지에서 ADD할 때 form 또한 changeform이 사용되는데 이때는 object_id가 없어서 오류가남 그것을 방지
