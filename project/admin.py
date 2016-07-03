from django.contrib import admin
from .models import User,Orders,RateList

# Register your models here.
class OrdersAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "email_id","amount_paid","timestamp"]
	class Meta:
		model = Orders



admin.site.register(User)
admin.site.register(Orders,OrdersAdmin)
admin.site.register(RateList)

