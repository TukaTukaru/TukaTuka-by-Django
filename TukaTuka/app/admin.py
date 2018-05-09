from django.contrib import admin
from .models import Company,Ad,Comment,RatingAd,Complaint,News
# from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# class MerchantInline(admin.StackedInline):
#     model = Merchant
#     can_delete = False
#     verbose_name_plural = 'Merchants'

# # Define a new User admin
# class UserAdmin(UserAdmin):
#     inlines = (MerchantInline, )

# # Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)

admin.site.register(News)
admin.site.register(Complaint)
admin.site.register(RatingAd)
admin.site.register(Comment)
admin.site.register(Company)
admin.site.register(Ad)


