# CoffeeDB
This project contains a Django App that allows users to filter and search for specific coffee beans for the perfect home roast. It has a custom Django command that takes a data file that I've webscraped containing information on coffee beans and puts it into a PostgreSQL database. I then use django-tables2 and django-filters to display the dataset as a table and allow it to be filterable and sortable. I created the APIs that let me get different querysets from Postgres and navigate between the login page and the main webpage. Finally, I wrote the HTML and CSS that would be used to display the two pages. 

Try it out!

coffeebeandb.herokuapp.com

Login Info

User: coffeelover

Password: Coffee123!
