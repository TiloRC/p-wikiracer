from greedy import Greedy
import threading

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




def greedyThread(func, args):
    threads = []
    for page in args:
        threads.append(threading.Thread(func, page[0], page[1]))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("done")



pages = [("KIPP Texas Public Schools", "Colorado River") , ("Pomona College", "Apple pie"), ("Apple pie", "Pomona College"), ("Pomona College, Albert Einstein"), ("Culver City, California", "Fifty Shades of Grey (film)")]
greedyThread(interface, pages)