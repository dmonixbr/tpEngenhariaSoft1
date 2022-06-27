class Alarme():
    def __init__(self, _identificou = False):
        self.identificouUmFocoDeIncendio = _identificou

    def setIdentificouUmFocoDeIncendio(self, foco_identificado = True):
        self.identificouUmFocoDeIncendio = foco_identificado

    def getIdentificouUmFocoDeIncendio(self):
        return self.identificouUmFocoDeIncendio
    def __init__(self, _identificou = False):
        self.identificouUmFocoDeIncendio = _identificou

    def setIdentificouUmFocoDeIncendio(self, foco_identificado = True):
        self.identificouUmFocoDeIncendio = foco_identificado

    def getIdentificouUmFocoDeIncendio(self):
        return self.identificouUmFocoDeIncendio

    def enviarAlertaParaAreaCentral(self):
        return print("Alertar Area Central! Incendio Detectado!!")

    def ligarParaEmergencia(self):
        return print("Esta é uma zona critica e não deve passar pela centra. Ligando para emergência imediatamente!!")

    def ligarIndicadoresLuminosos(self):
        return print("Ligando indicadores luminosos")

