from django.contrib import admin
from django.utils.timezone import now

from eventex.subscriptions.models import Subscription

class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'cpf', 'created_at', 'subscribe_today', 'hashid')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'phone', 'cpf', 'created_at')
    list_filter = ('created_at',)

    def subscribe_today(self, obj):
        return obj.created_at.date() == now().date()

    subscribe_today.short_description = 'inscrito hoje?'
    subscribe_today.boolean = True

admin.site.register(Subscription, SubscriptionModelAdmin)