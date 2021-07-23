from numpy import true_divide
from custom_level_types.prompt.definition.prompt_object import PromptObject
from numpy.random import default_rng


class Moi(PromptObject):

    is_editable = True

    def __init__(self, common_dict: dict, custom_dict: dict, game_object_list: list) -> None:
        super().__init__(common_dict, custom_dict, game_object_list)
        self.mon_argent = 0
    
    def objectif_atteint(self):
        if self.mon_argent >= 600 :
            print("code : un pingouin sachant voler doit savoir voler sans le covid")
        elif self.mon_argent < -10000 :
            print("")
        return self.mon_argent >= 600 or self.mon_argent < -10000
    
    def __str__(self):
        return f"ma tunasse : {self.mon_argent}"
    
    def update(self):
        pass


class FileDePassager(PromptObject):

    name = "File d'attente des passagers"
    is_editable = True

    def __init__(self, common_dict: dict, custom_dict: dict, game_object_list: list) -> None:
        super().__init__(common_dict, custom_dict, game_object_list)
        self.covided_count = 0
        self.covid_intercept = 0
        self.generated_people = 0
        self.liste_de_passagers = []

    def update(self):
        pass

    def __str__(self):
        return f"personnes sorties de l'avion : {self.generated_people}\npersonnes interceptées : {self.covid_intercept}"

    # TODO : probabilité de faux positif / faux négatif
    def passager_suivant(self):

        for object in self.game_object_list :
            if object.id == "player" :
                if object.mon_argent < - 10000 :
                    print("Patron : bon t'es nul, dégage !")
                elif object.mon_argent >= 600 :
                    print(
                        "la clé : un pingouin sachant voler doit savoir voler sans le covid")


        p = Passager({ 'id' : None}, {}, self.game_object_list)
        self.generated_people += 1
        self.liste_de_passagers.append(p)


    def mettre_en_quarantaine(self, passager):
        for object in self.game_object_list :
            if object.id == "player" :
                if passager.is_covided is True :
                    self.covid_intercept += 1
                    object.mon_argent += 50
                else :
                    object.mon_argent -= 100
                tune = object.mon_argent
        if self.covided_count == 0 :
            print(f"taux de réussite : 0%\ngain d'argent depuis arrivée au poste : {tune}")
        else :
            print(f"taux de réussite : {(self.covid_intercept / self.covided_count)*100}%\ngain d'argent depuis arrivée au poste : {tune}")


class Passager(PromptObject):
    is_editable = True

    rng = default_rng()
    proba_covid = 0.01

    def __init__(self, common_dict: dict, custom_dict: dict, game_object_list: list) -> None:
        super().__init__(common_dict, custom_dict, game_object_list)
        self._is_covided = bool(self.rng.binomial(n=1, p=self.proba_covid))
        if self._is_covided :
            for object in self.game_object_list:
                if object.id == "file_de_passager":
                    object.covided_count += 1
        
    
    @property
    def is_covided(self):
        return self._is_covided
    
    @is_covided.setter
    def is_covided(self, value):
        print("la tentative de fraude est répréhensible !")
        for object in self.game_object_list:
            if object.id == "player":
                object.mon_argent -= 200
                print(f" solde avec pénalité : {object.mon_argent}")
    
    def __str__(self):
        return ""
    
    def update(self):
        pass
    
        
