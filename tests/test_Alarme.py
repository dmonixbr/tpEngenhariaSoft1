from src.Alarme import Alarme

def testSetIdentificouUmFocoDeIncendio():
    a1 = Alarme()

    # Testar valor padrão
    assert a1.getIdentificouUmFocoDeIncendio()

def testSetIdentificouUmFocoDeIncendio():
    a1 = Alarme()

    # Testar valor padrão
    assert a1.getIdentificouUmFocoDeIncendio() == False

    # Testar set True
    a1.setIdentificouUmFocoDeIncendio(True)
    assert a1.getIdentificouUmFocoDeIncendio() == True

    # Testar set False
    a1.setIdentificouUmFocoDeIncendio(False)
    assert a1.getIdentificouUmFocoDeIncendio() == False

def testEnviarAlertaParaAreaCentral():
    a1 = Alarme()
    assert a1.enviarAlertaParaAreaCentral() == print("Alertar Area Central! Incendio Detectado!!")

def testLigarParaEmergencia():
    a1 = Alarme()
    assert a1.ligarParaEmergencia() == print("Esta é uma zona critica e não deve passar pela centra. Ligando para emergência imediatamente!!")

def testLigarIndicadoresLuminosos():
    a1 = Alarme()  
    assert a1.ligarIndicadoresLuminosos() == print("Ligando indicadores luminosos")