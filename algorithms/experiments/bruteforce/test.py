
import os.path
from database import Database

# sdow_database= './server.py'
# print(os.path.isfile(sdow_database))

database = Database(sdow_database='.\sdow.sqlite')
print(database.fetch_page("Apple"))
print(database.fetch_page("Banana"))

page1 = 18978754
page2 = 38940
print(database.compute_shortest_paths(page1, page2))