from greedy import Greedy
import concurrent.futures 
import json

def interface(start, end):
    """
    runs Greedy class, makes it easier to interact with the front end interface
    """
    max_path_length = 18

    # instantiating greedy algo obj
    wiki_path = Greedy()
    wiki_path.set_max_path(max_path_length)
    
    # returning path
    return wiki_path.find_path(start, end) 

# print(interface("KIPP Texas Public Schools", "Colorado River"))



def thread(starts, ends):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(interface, starts, ends))
    return results


with open("100games.txt", "r") as file:
    games = json.loads(file.read())
    
print(games)

pages = [("KIPP Texas Public Schools", "Colorado River") , ("Pomona College", "Apple pie"), ("Apple pie", "Pomona College"), ("Pomona College", "Albert Einstein"), ("Culver City, California", "Fifty Shades of Grey (film)")]
# starts = [page[0] for page in games]
# ends = [page[1] for page in games]

# print("\nRESULTS")
# results = thread(starts, ends)
# for result in results:
#     print(result)