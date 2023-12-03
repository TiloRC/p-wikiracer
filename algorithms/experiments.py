from wikiracer import WikiRacer, FailedPath
from typing import List, Tuple
from dataclasses import dataclass
from greedy import Greedy
from helper import get_random_page
import concurrent.futures
import functools 
import json

@dataclass
class EvaluationResults():
    def __init__(self, paths: List[List[str]], failedGames: List[Tuple[str, str]], numGames):
        assert numGames == len(paths) + len(failedGames)

        self.path_lengths = [len(path) for path in paths] + len(failedGames)*[None]
        self.failedGames = failedGames
        self.successfulGames = [(path[0], path[-1])  for path in paths]

    @staticmethod
    def combineResults(result1, result2):
        res = EvaluationResults([], [], 0)
        res.path_lengths =  result1.path_lengths + result2.path_lengths
        res.failedGames  = result1.failedGames + result2.failedGames
        res.successfulGames  = result1.successfulGames + result2.successfulGames
        return res



def evaluate_racer(racer: WikiRacer, games):
    """
    Returns `EvaluationResults`.
    """
    racers = []
    for i in games:
        racers.append(racer)

    with concurrent.futures.ThreadPoolExecutor(max_workers = 10) as executor:
        results = []
        for result in executor.map(runGame, games):
            results.append(result)

    

    # game_results = [run_game(racer, game) for game in games]
    
    return functools.reduce(EvaluationResults.combineResults, results)
        
def runGame(game):
    racer = Greedy()
    racer.set_max_path(10)
    run_game(racer,game)

def run_game(racer: WikiRacer, game):
    """
    Runs one game with the given Wikiracer
    """
    startPage = game[0]
    endPage = game[1]
    paths = []
    failed = []
    try:
        paths = [racer.find_path(startPage, endPage)]
    except FailedPath:
        failed = [(startPage, endPage)]
    
    return EvaluationResults(paths, failed, 1)

def generate_game_pair(num) :
    return (get_random_page(), get_random_page())

def generate_games(num_games):
    """
    Returns a List[Tuple[str, str]] where each tuple contains a start and destination 
    page which represents a game.
    """
    nums = []
    for i in range(num_games):
        nums.append(i)

    with concurrent.futures.ThreadPoolExecutor(max_workers = 10) as executor:
        games = []
        for result in executor.map(generate_game_pair, nums) :
            games.append(result)

    return games
        

# games = generate_games(100)
# print(games)
# print(json.dumps([('Pirates of the Coast', "Steve Jackson's Sorcery!"), ('David Ogrin', 'Long Xiaohua'), ('Bothriembryon praecelcus', 'Montréal–Jeanne-Mance'), ('Umarete kara Hajimete Mita Yume', 'Hans Hoffmann (painter)'), ('Preston Dock', 'Jurk'), ("Uruguay women's national under-17 basketball team", 'Wu Rongrong'), ('The Murder Capital', 'Heaven Music'), ('Azerbaijan Cycling Federation', 'Al Najaf International Airport'), ('List of ship launches in 1772', 'Donald Stanley'), ('Pratt Institute', 'Emarat, East Azerbaijan'), ('Heinrich Jost', 'Barry Houston'), ('Tooth Protectors', 'Thomas Meißner'), ('Gmina Rytwiany', 'Choriner Musiksommer'), ('1984 Open Championship', 'Tabanus marginalis'), ('Loss of citizenship', 'Thomas Hannan (activist)'), ('Marfino District', 'Android-x86'), ('Harchandpur, Mainpuri', '2018 Dakar Rally'), ('Pussihukat', 'Mislav Karoglan'), ('USS Guam (CB-2)', 'Vega de Poja'), ('KWHQ-FM', 'Burrton, Kansas'), ('Ángel Pindado', '3rd Open Russian Festival of Animated Film'), ('Protected area mosaic (Brazil)', 'Der Ackermann aus Böhmen'), ('Dorian Lord', 'History of Åland'), ('Flemming Rose', 'Golokganj railway station'), ('Stopnik, Tolmin', 'Breagh gas field'), ('Sthapit', 'De ortolaan'), ('Kamma Mountains', 'Chellal'), ('Profoundemonium', 'Bunny Pearce'), ('Émile Gontier', 'Daniel Lorenz Salthenius'), ('Amazing Race Suomi', 'Inchekeh, Ziviyeh'), ('Danielle Fishel', 'Lenin, Transnistria'), ('Kinda baboon', 'Richard Elmore'), ('Tafa (disambiguation)', '64th Cavalry Division (United States)'), ('Glucagon-like peptide-1', 'Charles Horwood'), ('Bankura Zilla School', 'Monotygma lauta'), ('Madhyapur Thimi', 'Paul McGann'), ('Democratic Party (Malta)', 'Walt Kyle'), ('Han Xuan (disambiguation)', 'Coat of arms of Rhineland-Palatinate'), ('The Soundtrack of My Life', 'Florido River'), ('Kevin Kendall', 'Hector Morison'), ('Kenneth Callow', 'Gera (Egypt)'), ('Captain Lightfoot', 'Bud Delp'), ('Perceptual Speech Quality Measure', 'Pillerton Hersey'), ('Laura Domínguez', 'Extrajudicial prisoners of the United States'), ('Sport climbing at the 2023 Pan American Games', 'Mecklenburg cuisine'), ('Anupama', 'Cabo Verde International Film Festival'), ('Jailbait', 'Evan Lysacek'), ('May 1915 Greek legislative election', 'Fish species of Aravaipa Canyon'), ('Konstal 13N', 'Berridale, New South Wales'), ('Karamba!', 'The L.A. Riot Spectacular'), ('Robert Emil Hansen', 'Neil Currie'), ('Kalinga Park', 'Kigeli V Ndahindurwa'), ('Fluke; or, I Know Why the Winged Whale Sings', 'Integer function'), ('Maiden Way', 'John Burgess (host)'), ('Courquetaine', 'Distributed file system for cloud'), ('Plaza de Toros Cañaveralejo', 'Zarjaz'), ('Dan Quirke', 'Ruth Stephan'), ('Samaje Perine', 'Mina Waxin'), ('Muérdete La Lengua', 'Lunella jungi'), ('O-phosphoserine sulfhydrylase', '2023 Serbian protests'), ('Lea County Correctional Center', 'Viola caiçara'), ('Berkshire County, Massachusetts', 'Yuri Kuleshov'), ('Évelyne Pagès', 'Bruno Zeltner'), ('Rupandehi 1 (constituency)', 'Pinheirinho River'), ('United Nations Security Council Resolution 697', 'Duncan Wright'), ('Chamber of Representatives of Burkina Faso', 'Lobophylliidae'), ('Catalonia in the Senate', 'Acanthomysis microps'), ('Tom Butime', '1952 NCAA track and field championships'), ('Ballstorp Runestone', 'Storable votes'), ('Luke Montz', 'David Taylor'), ('David Kemp (Australian scientist)', 'Euxoa serricornis'), ('Lowly Worm', 'HMS Whirlwind (D30)'), ('Qaleh Gah, Ravansar', '1992–93 Deportivo de La Coruña season'), ('Døstrup', 'Greed Mask'), ('Maimoona Sultan', '2019 FIL European Luge Championships – Doubles'), ('Westminster (Liverpool ward)', 'Kalwa, Thane'), ('Terkel in Trouble', 'Henry Ryland'), ('Paul Grewal', 'Andrew Hayward'), ('Carson Mansion', "Lost Dutchman's Gold"), ('Teratocephalidae', 'Xu Fan'), ('Khalil-ur-Rehman (politician)', 'Jameh Mosque of Semnan'), ('1984 Sovran Bank Classic – Doubles', 'Washoe Valley (Nevada)'), ('FC Gütersloh', 'Battle of Wisternitz'), ('John IV, Count of Nassau-Siegen', 'Sajid Hussain (journalist)'), ('Okinawa Times', 'Chemehuevi'), ('João Lopes (footballer)', 'Loolkade'), ('DermAtlas', "2021–22 Holy Cross Crusaders men's ice hockey season"), ('1992 Nairn District Council election', 'Catherine Mabillard'), ('Jacques Le Fèvre', 'Newport High School (Pennsylvania)'), ('Fruta del Norte mine', "Hold On It's Easy"), ('City of Derry Jazz and Big Band Festival', 'Saitama Wild Knights'), ('Barony and Castle of Kilbirnie', 'Macbeth'), ('Star of Bombay', 'Topsy Turvy (Guitar Shorty album)'), ('Dumitru Marcu', 'Toppeladugård Castle'), ('Nacoleia fuscifusalis', 'Java (cigarette)'), ('Jan Scheere', 'Alone in the Dark (1982 film)'), ('Le Ray, New York', 'DramaQueen'), ('A Thing About Machines', 'Lyn Macdonald'), ('Lurlean Hunter', 'Hector Island'), ('Kostrzyn nad Odrą', 'Jeremy Blaustein')]))
with open("algorithms/100games.txt", "r") as file:
    games = json.loads(file.read())


racer = Greedy()
racer.set_max_path(20)
racerResults = evaluate_racer(racer, games)
print(racerResults.failedGames, racerResults.path_lengths, racerResults.successfulGames)