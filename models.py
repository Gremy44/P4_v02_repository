import os
from tinydb import TinyDB, where

class Players():
    def __init__(self, l_name = "Doe", f_name = "Jhon", b_day = "00/00/0000", gender = "N", rank = "100"):
        self.l_name = l_name
        self.f_name = f_name
        self.b_day = b_day
        self.gender = gender
        self.rank = rank

        self.db = TinyDB("./chess_data_base/player_data_base.json") # obj creation and path
        self.db.default_table_name = "Players" # table name

    def player_db_reg(self,id): #enregistre les infos joueurs dans la base donnée
        # ----directory creation----
        try:
            os.makedirs("./chess_data_base")
        except FileExistsError:
            pass
        # ----.json creation----
        self.db.insert({"id_player": id,
                   "Nom" : self.l_name, 
                   "Prenom" : self.f_name, 
                   "Date de naissance" : self.b_day,
                   "Genre" : self.gender, 
                   "Rang" : self.rank})  
    
    def pairing(self,id_player_tournament):
        # --- ressort les joueurs stockés dans la base de données ---
        l_serialize_players = []
        for i in id_player_tournament:
            serialized_players = self.db.search(where('id_player')== i) 
            l_serialize_players.append(serialized_players)

        # --- tri par rang ---
        malist = []
        for i in l_serialize_players:#supprime 1 degré de liste
            malist.extend(i)
        tri_rang = sorted(malist, key=lambda k: k['Rang'])#tri par rang

        # --- fait les paires ---
        length_to_split = len(tri_rang)//2
        mes_paires = []
        for i in range(length_to_split):
            paires_1 = tri_rang[i], tri_rang[i+length_to_split]
            mes_paires.append(paires_1)
        return mes_paires
            

class TournamentInputInfos():
    def __init__(self, t_name, t_place, t_date, t_round, t_tourne, t_players, t_time, t_desc):
        self.t_name = t_name
        self.t_place = t_place
        self.t_date = t_date
        self.t_round = t_round
        self.t_tourne = t_tourne
        self.t_players = t_players
        self.t_time = t_time
        self.t_desc = t_desc

    def input_tournament_db_reg(self, id_tournament):
        # ----directory creation----
        try:
            os.makedirs("./chess_data_base")
        except FileExistsError:
            pass

        # ----.json creation----
        db = TinyDB("./chess_data_base/input_tournament_infos.json") # obj creation and path
        db.default_table_name = "Input_Tournament" # table name
        db.insert({"id_tournament" : id_tournament,
                   "Name": self.t_name,
                   "Place" : self.t_place, 
                   "Date" : self.t_date, 
                   "Round" : self.t_round,
                   "Tourne" : self.t_tourne, 
                   "Players" : self.t_players,
                   "Time" : self.t_time,
                   "Description" : self.t_desc})  

"""     
#Créer un joueur dans la DB
ji = ask_player_infos()
joueur = Players(ji[0],ji[1],ji[2],ji[3],ji[4])
joueur.player_db_reg(id(joueur))
"""

"""
#Créer les infos input tournois dans la db
ti = ask_tounament_infos()
tournois = TournamentInputInfos(ti[0],ti[1],ti[2],ti[3],ti[4],ti[5],ti[6],ti[7])
tournois.input_tournament_db_reg(id(tournois))
"""       