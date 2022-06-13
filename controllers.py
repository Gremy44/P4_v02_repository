from unittest import result
from models import Players

def ask_player_infos():
    l_name = input("Entrez nom : ")
    f_name = input("Entrez prénom : ")
    b_day = input("Date d'anniversaire : ")
    gender = input("Genre : ")
    rank = input("Rang : ")
    return l_name,f_name,b_day,gender,rank #return list of 5


class Tournament():
    ''' 
       Deroulé d'un tournoi:
    1- Créer un nouveau tournoi => ok
    2- Ajouter huit joueurs. => ok 
    3- L'ordinateur génère des paires de joueurs pour le premier tour. => ok
    4- Lorsque le tour est terminé, entrez les résultats. => ok
    5- Répétez les étapes 3 et 4 pour les tours suivants jusqu'à ce que 
       tous les tours soient joués, et que le tournoi soit terminé.
    '''
    def __init__(self,list_paires=[], t_name ="", t_place="", t_date ="", t_round=4, t_tourne="",t_players=[], t_time="", t_desc=""):
        self.t_name = t_name
        self.t_place = t_place
        self.t_date = t_date
        self.t_round = t_round 
        self.t_tourne = t_tourne
        self.t_players = t_players 
        self.t_time = t_time
        self.t_desc = t_desc

        self.list_paires = list_paires

    def ask_tounament_infos(self):
        self.t_name = input("Entrez nom : ")
        self.t_place = input("Entrez lieu : ")
        self.t_date = input("Entrez date : ")
        self.t_round = 4
        self.t_tourne = input("Entrez instances rondes : ")
        self.t_players = [3042972155808, 2520259116960, 2835596394400, 2498757410720, 2123311234976, 1988607754144, 1384106246048, 2187293245344]
        self.t_time = input("Bullet/Blitz/coup rapide : ")
        self.t_desc = input("Entrez description : ")
        return self.t_name, self.t_place, self.t_date, self.t_round, self.t_tourne, self.t_players, self.t_time, self.t_desc #return list of 8

    def round(self, paires_tri):
        
        nb_loop = len(paires_tri)
        self.complete_result = []
        for i in range(nb_loop):
            print("Round 1 :", 
                paires_tri[i][0]['Nom'],
                paires_tri[i][0]['Prenom'], "contre",
                paires_tri[i][1]['Nom'],
                paires_tri[i][1]['Prenom'])
            score_p1 = input(f"Score joueur {paires_tri[i][0]['Nom']} {paires_tri[i][0]['Prenom']}: ")
            score_p2 = input(f"Score joueur {paires_tri[i][1]['Nom']} {paires_tri[i][1]['Prenom']}: ")
            tour1 = [paires_tri[i][0]['id_player'],score_p1],[paires_tri[i][1]['id_player'],score_p2]
            simple_result = (tour1)
            self.complete_result.append(simple_result)
            print(simple_result)
        print("Résultats du round : ", self.complete_result)
        return self.complete_result

    def take_second(self, elem):
        return elem[1]

    def sort_paire(self, result_round):
        liste_pour_tri = []
        for i in result_round:
            for n in i:
                liste_pour_tri.append(n)
        liste_pour_tri.sort(key=self.take_second)
        print("Liste trié : ", liste_pour_tri)


mon_tournois = Tournament()        
infos = Players()

it = mon_tournois.ask_tounament_infos()

mes_paires = infos.pairing(it[5])
print("Mes paires : ", mes_paires)

resultats = mon_tournois.round(mes_paires)

tri_round_suivant = mon_tournois.sort_paire(resultats)

