from algorithms.wikiracer import WikiRacer, MaxPathLengthExceeded
from algorithms.helper import get_random_page

class RandomRacer(WikiRacer):
    """
    Tries to find a path between two wikipedia pages by guessing
    randomly.

    Not a very good WikiRacer as it is incredibly unlikely to find
    a path between wikipedia pages. And if it does somehow find
    a path to the destination page by ridiculous luck, then that
    path most likely not a valid path; every page should be
    linked to from the previous page.
    """
    def __init__(self):
        self.max_path_length = 50

    def set_max_path_length(self, max_path_length: int):
        if max_path_length < 1:
            raise ValueError("Max path length must be at least 1")
        self.max_path_length = max_path_length

    def find_path(self, start_page, dest_page):
        path = [start_page]
        # Note that the length of a path is
        # the number of pages minus 1.
        while len(path) - 1 <= self.max_path_length:
            rand_page = get_random_page()
            path.append(rand_page)

            # incredibly unlikely to actually occur
            if rand_page == dest_page:
                return path

        raise MaxPathLengthExceeded(f"Path of length less than or equal to {self.max_path_length} could not be found")

if __name__ == '__main__':
    a = RandomRacer()
    a.find_path("Wikiracing", "Pomona College")