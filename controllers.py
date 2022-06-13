from unittest import result
from models import Players

def ask_player_infos():
    l_name = input("Entrez nom : ")
    f_name = input("Entrez prénom : ")
    b_day = input("Date d'anniversaire : ")
    gender = input("Genre : ")
    rank = input("Rang : ")
    return l_name,f_name,b_day,gender,rank #return list of 5

def ask_tounament_infos():
    t_name = input("Entrez nom : ")
    t_place = input("Entrez lieu : ")
    t_date = input("Entrez date : ")
    t_round = 4
    t_tourne = input("Entrez instances rondes : ")
    t_players = [3042972155808, 2520259116960, 2835596394400, 2498757410720, 2123311234976, 1988607754144, 1384106246048, 2187293245344]
    t_time = input("Bullet/Blitz/coup rapide : ")
    t_desc = input("Entrez description : ")
    return t_name, t_place, t_date, t_round, t_tourne, t_players, t_time, t_desc #return list of 8


class Tournament():
    ''' 
       Deroulé d'un tournoi:
    1- Créer un nouveau tournoi => ok
    2- Ajouter huit joueurs. => ok 
    3- L'ordinateur génère des paires de joueurs pour le premier tour.
    4- Lorsque le tour est terminé, entrez les résultats.
    5- Répétez les étapes 3 et 4 pour les tours suivants jusqu'à ce que 
       tous les tours soient joués, et que le tournoi soit terminé.
    '''
    def __init__(self,list_paires, t_round):
        self.list_paires = list_paires
        self.t_round = t_round

    def first_round(self):
        nb_loop = len(self.list_paires)
        self.complete_result = []
        for i in range(nb_loop):
            print("Round 1 :", 
                self.list_paires[i][0]['Nom'],
                self.list_paires[i][0]['Prenom'], "contre",
                self.list_paires[i][1]['Nom'],
                self.list_paires[i][1]['Prenom'])
            score_p1 = input(f"Score joueur {self.list_paires[i][0]['Nom']} {self.list_paires[i][0]['Prenom']}: ")
            score_p2 = input(f"Score joueur {self.list_paires[i][1]['Nom']} {self.list_paires[i][1]['Prenom']}: ")
            tour1 = [self.list_paires[i][0]['id_player'],score_p1],[self.list_paires[i][1]['id_player'],score_p2]
            simple_result = (tour1)
            self.complete_result.append(simple_result)
            print(simple_result)
        print("Résultats du round : ", self.complete_result)

    def sort_paire(self):
        self.complete_result
        

it = ask_tounament_infos()
infos = Players()
mes_paires = infos.pairing(it[5], it[3])


mon_tournois = Tournament(mes_paires)
zembrozate = mon_tournois.first_round()

#print(zembrozate)
