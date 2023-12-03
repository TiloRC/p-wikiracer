from greedy import Greedy


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