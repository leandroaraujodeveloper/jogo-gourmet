from utils import NodoArvore

class Game:
    def __init__(self):
        self.raiz = None
        self.init_game()
    def init_game(self):
        MASSA, BOLO_CHOCOLATE, LASANHA = "massa", "Bolo de Chocolate", "Lasanha"
        self.raiz = NodoArvore(MASSA)
        self.raiz.esquerda = NodoArvore(BOLO_CHOCOLATE)
        self.raiz.direita  = NodoArvore(LASANHA)
    def reset_game(self):
        return self.raiz
    def insertLeft(self, raiz_game, chave, direita):
        if not raiz_game:
            root = NodoArvore(chave)
            return
        lista_auxiliar = []
        lista_auxiliar.append(raiz_game)

        while (len(lista_auxiliar)):
            raiz_game = lista_auxiliar[0]
            lista_auxiliar.pop(0)
    
            if (not raiz_game.esquerda):
                raiz_game.esquerda = NodoArvore(chave,direita=NodoArvore(direita))
                break
            else:
                lista_auxiliar.append(raiz_game.esquerda)
    def pergunta(self, prato_atual):
        return "O prato que voce pensou é " + str(prato_atual) + "?"
    def pergunta_novo_prato(self):
        return "Qual prato voce pensou?"
    def pergunta_diferenca(self, prato_recente):
        if prato_recente.direita:
            return "Este prato é ________ mas " + str(prato_recente.direita) + " não."
        else:
            return "Este prato é ________ mas " + str(prato_recente.chave) + " não."