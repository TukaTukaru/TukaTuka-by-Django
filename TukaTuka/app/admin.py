from django.contrib import admin
from .models import Company,Ad,Comment,RatingAd,Complaint

# class CompanyAdmin(admin.ModelAdmin):
# 	pass


admin.site.register(Complaint)
admin.site.register(RatingAd)
admin.site.register(Comment)
admin.site.register(Company)
admin.site.register(Ad)


