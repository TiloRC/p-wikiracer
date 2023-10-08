from algorithms.wikiracer import WikiRacer


class Greedy(WikiRacer):
    def __init__(self, max_path_length, doc_sim_func):
        """
        Parameters
        ----------
        max_path_length : int
        doc_sim_func : function
            Takes two wikipedia page titles and returns
            some measure of their similarity.
        """
        super().__init__(max_path_length)
        self.doc_sim = doc_sim_func


