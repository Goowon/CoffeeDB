from dbapp.models import Bean
from django.core.management.base import BaseCommand
import pandas as pd
import re
import numpy as np

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        path = "./dbapp/static/dbapp/data/coffee_data.csv"
        # Since the CSV headers match the model fields,
        # you only need to provide the file's path (or a Python file object)
        # insert_count = Bean.objects.from_csv(path)
        # print("{} records inserted".format(insert_count))
        bean_df = pd.read_csv(path)
        bean_df = bean_df.replace(np.nan, '', regex=True)
        for index in range(len(bean_df)):
            row = bean_df.loc[index]
            blend_name = row['blend_name']
            company_name = row['company_name']
            roast = row['roast']
            flavors = re.findall("[\\w/]+",row['flavors'])
            notes = re.findall("\\w+",row['notes'])
            description = row['description']
            origin = row['origin']
            vendor_location = row['vendor_location']
            price = row['price']
            vendor_website = row['vendor_website']
            vendor_phone = row['vendor_phone']
            review_date = row['review_date']
            bean = Bean()
            bean.blend_name = blend_name
            bean.roast = roast
            bean.company_name = company_name
            bean.flavors = flavors
            bean.notes = notes
            bean.description = description
            bean.origin = origin
            bean.vendor_location = vendor_location
            bean.vendor_phone = vendor_phone
            bean.review_date = review_date
            bean.vendor_website = vendor_website
            bean.price = price
            bean.save()
        print("Successfully populated Coffee!")