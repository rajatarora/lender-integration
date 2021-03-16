from django.contrib import admin
from django_json_widget.widgets import JSONEditorWidget

from .models import *
from base.admin import *
# Register your models here.



class LoanDataAdmin(JSONBaseAdmin, BaseAdmin, admin.ModelAdmin):
    search_fields = ('app__lmsid',)
    list_display = ('app', 'lender_api', 'response_code')
    list_filter = ('lender_api', 'lender_api__lender')

    fields = (('loan', 'lender_api', 'response_code'), ('request', 'response'))




class LoanDataInlineAdmin(JSONBaseAdmin, BaseAdmin, admin.TabularInline):
    model = LoanData
    exclude = ('app', 'request', 'response_code') + BaseAdmin.exclude
    ordering = ('lender_api__priority',)
    max_num = 0
    extra = 0

    def has_delete_permission(self, request, obj=None):
        return False



class LoanAdmin(BaseAdmin, admin.ModelAdmin):
    list_filter = ('lender', 'app__lms')
    search_fields = ('app__lmsid',)

    fields = (('app', 'lender',),)
    inlines = (LoanDataInlineAdmin,)



class LenderSystemAPIAdmin(APIBaseAdmin, JSONBaseAdmin, BaseAdmin, admin.ModelAdmin):
    towhom = 'lender'



class LenderSystemAPIInlineAdmin(APIBaseInlineAdmin, BaseAdmin, admin.TabularInline):
    model = LenderSystemAPI



class LenderSystemAdmin(ServiceBaseAdmin, JSONBaseAdmin, BaseAdmin, admin.ModelAdmin):
    inlines = (LenderSystemAPIInlineAdmin,)



admin.site.register(Loan, LoanAdmin)
admin.site.register(LoanData, LoanDataAdmin)
admin.site.register(LenderSystem, LenderSystemAdmin)
admin.site.register(LenderSystemAPI, LenderSystemAPIAdmin)
