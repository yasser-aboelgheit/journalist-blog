from django.contrib import admin
from .models import Article

# admin.site.register(Article)



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # list_display = ('first_name', 'email', 'phone_number', 'company', 'referrer_type',
    #                 'users_referred', 'closed_deals', 'money_paid', 'money_waiting_for_payment', 'money_pending',
    #                 'hubspot_url')
    search_fields = ('title',)
    # inlines = [
    #     UserInline,
    #     CodeInline,
    # ]
    # inactivated_fields = ['email', 'first_name', 'last_name', 'phone_number', 'company', 'referrer_type',
    #                       'internal_broker', 'send_email_notifications', 'send_whatsapp_notifications',
    #                       'signup_date', 'referral_fee_percentage', 'referral_fixed_payment',
    #                       ]
    # readonly_fields = ['hubspot_url']    # making sure it will remain a list (not a tuple) in future changes.
    list_filter = ('type', 'published_on')
    # autocomplete_fields = ['company', 'user_internal_broker']
    # raw_id_fields = ("cognito",)
