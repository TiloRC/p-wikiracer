from wikiracer import MaxPathLengthExceeded
from helper import PageRequestError, PathDeadend
from sentence_transformers import SentenceTransformer, util
import wikipediaapi
from stop_words import get_stop_words
from pyinstrument import Profiler 
import json

profiler = Profiler()
profiler.start()

class Greedy():
    def __init__(self):
        """
        Parameters
        ----------
        max_path_length : int 
        doc_sim_func : function
            Takes two wikipedia page titles and returns
            some measure of their similarity.
        """
        self.max_path_length = 18 
        # self.model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
        self.model = SentenceTransformer('average_word_embeddings_glove.6B.300d')
        self.wiki_access = wikipediaapi.Wikipedia('Aldo & Richard', 'en')



    def set_max_path(self, max_path_length):
        """
        Sets the max path length
        """
        if max_path_length < 1:
            raise ValueError("Max path length must be at least 1")
        self.max_path_length = max_path_length


    def find_path(self, start_page: str, dest_page: str):
        """
        Returns a list of Wikipedia page titles representing the path.
        The `start_page` should be included as the first page of the path
        and the `dest_page` should be included at the end of the path.

        Should raise `FailedPath` exception if it can't find a path for
        a reason other than an api call failure.
        """
        # accessing wikipedia api 
        self.wiki_access = wikipediaapi.Wikipedia('Aldo & Richard', 'en')
        wiki_start = self.wiki_access.page(start_page) # wiki page for start 
        wiki_dest = self.wiki_access.page(dest_page) # wiki page for dest
        dest_page_vector = self.model.encode(dest_page)

        if (wiki_start.exists() and wiki_dest.exists()):
            visited = [start_page] # list of visisted pages
            print(visited)
            count = 0 # # page visit count
            current_wiki = wiki_start # tracks current wiki page

            while count < self.max_path_length:
                # exception for dead pages
                # if not current_wiki.exists:
                #     raise PathDeadend
                
                # get Linked Pages - we will only once per title
                links = self.get_linked_pages(current_wiki, visited)

                # get link with highest cos sim and 'visit'
                most_sim_page = self.get_blended_sim(links, dest_page_vector)
                visited.append(most_sim_page)
                print(visited)
                
                # path completed
                if most_sim_page == dest_page:
                    return visited
                
                # updated current and count
                current_wiki = self.wiki_access.page(most_sim_page)
                count += 1
            
            raise MaxPathLengthExceeded(f"Path of length less than or equal to {self.max_path_length} could not be found.")
        
        # start doesn't exist
        elif (not wiki_start.exists()):
            raise PageRequestError("Start page does not exist as a wikipedia title")
        
        # dest doesn't exist
        else:
            raise PageRequestError("Destination page does not exist as a wikipedia title")
    
    def assign_alpha(self, value = 0.5):
        return value

    def assign_beta(self, value = 3):
        return value

    def get_linked_pages(self, page, visited):
        """
        returns the title of all the linked pages of a wikipedia page
        """
        #gets the raw pages
        links = page.links
        linked_pages = []
        for title in links.keys():
            if title not in visited: 
                linked_pages.append(title)

        return linked_pages
        

    def get_most_similar(self, links, target_page):
        """
        returns the t
        """
        # encoding target page

        link_ids = range(len(links))

        encoded_links = self.model.encode(links)

        sorted_links = sorted(link_ids,key = lambda title_id: util.cos_sim(encoded_links[title_id], target_page)[0][0].item(), reverse=True)
        sorted_links = [links[link_id] for link_id in sorted_links]
        
        # checking if page w/ highest cos sim exists
        wiki_page = self.wiki_access.page(sorted_links[0])


        while not wiki_page.exists(): 
            # checking to see if list exists
            if not sorted_links:
                raise PathDeadend
            
            # pop out pages that don't exist
            sorted_links.pop(0)

            wiki_page = self.wiki_access.page(sorted_links[0])
            
        return sorted_links[0]
    

    def binary_search(self, arr, x):
        low = 0
        high = len(arr) - 1
        mid = 0
    
        while low <= high:
    
            mid = (high + low) // 2
    
            # If x is greater, ignore left half
            if arr[mid] < x:
                low = mid + 1
    
            # If x is smaller, ignore right half
            elif arr[mid] > x:
                high = mid - 1
    
            # means x is present at mid
            else:
                return mid
    
        # If we reach here, then the element was not present
        return -1


    def avg_freq(self, rankings, tokens):

        freqs = [(1/(1 + self.binary_search(rankings, token)) if token not in get_stop_words('english') and self.binary_search(rankings, token) != -1 else 0) for token in tokens]

        return sum(freqs)/len(freqs)
    

    def get_blended_sim(self, links, target_page):
        """
        returns the page with the highest blended similarity value to the target page. 
        blended_sim = (1-α)cos_sim ** beta  + αgen
        gen = Avg(1/word_rank)

        1) Make a function for alpha
        2) Remove stop words from title
        3) Adding the exponent to cosine similarity (cube it)

        """
        #  open file and encode target
        in_file = open("wordrankings.txt", "r")


        # list of lines in (-1 + rank) asc. order

        # stripping \n
        ranked_lines = [line.rstrip("\n") for line in in_file.readlines()]

        in_file.close()
        print("here?")
        # link_freqs = [] # list of tuples (link, avg freq)

        # print(get_stop_words('english'))
        
        # for link in links:  
        #     # list of a freq's for each token in a link title

        #     trimmed_link = [token for token in link.split() if token not in get_stop_words('english')]
        
        #     freqs = [(1/(1 + ranked_lines.index(token)) if token in ranked_lines else 0) for token in trimmed_link]
        #     link_freqs.append((link, sum(freqs)/len(freqs)))


        # freq scaling factor
        alpha = self.assign_alpha()
        beta = self.assign_beta()

        print("here2")
        link_ids = range(len(links))
        encoded_links = self.model.encode(links)


        sorted_links = sorted(link_ids, key = lambda title_id: (1 - alpha) * ((util.cos_sim(encoded_links[title_id], target_page)[0][0].item()) ** beta) 
                              + (alpha * self.avg_freq(ranked_lines, links[title_id].split())), reverse=True)
        print("here$$")
        sorted_links = [links[link_id] for link_id in sorted_links]



        # sort by highest blended
        # blend_sorted = sorted(link_freqs,key = lambda tple: (1 - alpha) * ((util.cos_sim(self.model.encode(tple[0]), target_page)[0][0].item()) ** beta) + alpha * tple[1], reverse=True)
        

        wiki_page = self.wiki_access.page(sorted_links[0])

        print("here4")
        while not wiki_page.exists(): 
            # checking to see if list exists
            if not sorted_links:
                raise PathDeadend
            
            # pop out pages that don't exist
            sorted_links.pop(0)
            print("here5")
            wiki_page = self.wiki_access.page(sorted_links[0])
            
        return sorted_links[0]


if __name__ == "__main__":



    tester_1 = Greedy()
    # print(tester_1.find_path("Pomona College", "Albert Einstein"))
    print(tester_1.find_path("Apple pie", "Pomona College"))
    print("finished")



profiler.stop()
profiler.print()




