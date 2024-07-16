class GestionCptB :
    def __init__(self,nCompt,nomClient,soldeCompt=0):
        self._nCompt=nCompt
        self._nomClient=nomClient
        self._soldeCompt=soldeCompt
    def Versement (self,montant):
        if montant <= 0:
            print('le montant doit etre positive !')
        else:
            self._soldeCompt += montant
            
    def Retrait (self,montant):
        if montant <= 0:
            print('le montant doit etre positive !')
        else:
            if self._soldeCompt < montant :
                print('solde insuffisant')
            else:
                self._soldeCompt -= montant
                
    def affichageinfo (self):
        return f'le solde de compte de Mr/Mme {self._nomClient} ayant le numero {self._nCompt} est : {self._soldeCompt}'