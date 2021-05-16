from django.db import transaction
from django import forms
from .models import Order
from product.models import Product
from user.models import User

class RegisterForm(forms.Form):
   
    def __init__(self,request, *args, **kwargs):  
        super().__init__(*args,**kwargs)          
        self.request = request                    
                      
    product = forms.IntegerField(error_messages={'required': '상품명을 입력해주세요.'},
        label='상품명', widget=forms.HiddenInput)
    quantity = forms.IntegerField(error_messages={'required': '수량을 입력해주세요.'}, label='수량')

    def clean(self):
        cleaned_data = super().clean()      
        quantity = cleaned_data.get('quantity')
        product = cleaned_data.get('product')

        if not (quantity and product):                              
            self.add_error('quantity', '값이 없습니다.')
            self.add_error('product', '값이 없습니다.')




