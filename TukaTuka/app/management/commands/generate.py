from django.core.management.base import BaseCommand, CommandError
from app.models import *
from random import randint, choice

DEFAULT_AD=50000
BATCH_SIZE = 5000
DEFAULT = 100000




class Command(BaseCommand):
    help = 'Generates the 100000 objects of my models'

    def handle(self, *args, **options):

        adss = [Ad(title=f'{i} Ad',description ='Descrip' + str(i),
            category=randint(0,4)) for i in range(DEFAULT)]
        Ad.objects.bulk_create(adss, batch_size=BATCH_SIZE)
        ad_ids=[Ad.objects.all()[_].id for _ in range(DEFAULT_AD)]

        ratings = [RatingAd(rating=randint(0,4),
            ad_id=choice(ad_ids),) for i in range(DEFAULT)]
        RatingAd.objects.bulk_create(ratings, batch_size=BATCH_SIZE)

        complaints = [Complaint(complaint_text=f'{i}some',complaint_type=randint(0,4),
            ad_id=choice(ad_ids),) for i in range(DEFAULT)]
        Complaint.objects.bulk_create(complaints, batch_size=BATCH_SIZE)

        companies = [Company(first_name=f'first_name {i}',
            last_name=f'last_name {i}',
            middle_name=f'last_name {i}',
            phone_number ='+79857808761',
            position=f'position {i}',
            company_type=f'name {i}',
            company_adress=f'adress {i}',
            ad_id=choice(ad_ids)
            ) for i in range(DEFAULT)]
        Company.objects.bulk_create(companies, batch_size=BATCH_SIZE)
        

        





