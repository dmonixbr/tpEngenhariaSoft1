from src.AreaEdificio import AreaEdificio
from src.Alarme import Alarme

def testSetNomeArea():
    a1 = AreaEdificio()

    #Testar valor padrão
    assert a1.getNomeArea() == ""

    #Testar valor setado por "area1"
    a1.setNomeArea("area1")
    assert a1.getNomeArea() == "area1"

    #Testar setter para string vazia ""
    a1.setNomeArea("")
    assert a1.getNomeArea() == ""


def testSetZona():
    a1 = AreaEdificio()    
    
    #Testar valor padrão
    assert a1.getZona() == []
    
    #Testar cada possibilidade para o setter
    a1.setZona(['amarelo', 'azul'])
    assert a1.getZona() == ['amarelo', 'azul']

    a1.setZona([])
    assert a1.getZona() == []
    
    a1.setZona(['amarelo'])
    assert a1.getZona() == ['amarelo']
    
    a1.setZona(['azul'])
    assert a1.getZona() == ['azul']
  

def testSetPessoasPresentes():
    a1 = AreaEdificio() 
    
    #Testar valor padfrom src.AreaEdificio import AreaEdificio
from src.Alarme import Alarme

def testSetNomeArea():
    a1 = AreaEdificio()

    #Testar valor padrão
    assert a1.getNomeArea() == ""

    #Testar valor setado por "area1"
    a1.setNomeArea("area1")
    assert a1.getNomeArea() == "area1"

    #Testar setter para string vazia ""
    a1.setNomeArea("")
    assert a1.getNomeArea() == ""


def testSetZona():
    a1 = AreaEdificio()    
    
    #Testar valor padrão
    assert a1.getZona() == []
    
    #Testar cada possibilidade para o setter
    a1.setZona(['amarelo', 'azul'])
    assert a1.getZona() == ['amarelo', 'azul']

    a1.setZona([])
    assert a1.getZona() == []
    
    a1.setZona(['amarelo'])
    assert a1.getZona() == ['amarelo']
    
    a1.setZona(['azul'])
    assert a1.getZona() == ['azul']
  

def testSetPessoasPresentes():
    a1 = AreaEdificio() 
    
    #Testar valor padrão        
    assert a1.getPessoasPresentes() == 0
    
    #Testar numero positivo
    a1.setPessoasPresentes(10)
    assert a1.getPessoasPresentes() == 10
    
    #Testar zero
    a1.setPessoasPresentes(0)
    assert a1.getPessoasPresentes() == 0
    
    #Testar numero negativo    
    a1.setPessoasPresentes(-2)
    assert a1.getPessoasPresentes() == 0


def testSetAlarmesDoEdificio():
    a1 = AreaEdificio()

    #Testar valor padrao
    assert a1.getAlarmesDoEdificio() == []

    #Testar valor para [a2, a3, a4]
    a2 = Alarme()
    a3 = Alarme()
    a4 = Alarme()
    a1.setAlarmesDoEdificio([a2, a3, a4])
    assert a1.getAlarmesDoEdificio() == [a2, a3, a4]


def testSetIndicadoresLuminososLigados():
    #Testar valor padrao
    a1 = AreaEdificio()
    assert a1.getIndicadoresLuminososLigados() == False

    #Testar valor True
    a2 = AreaEdificio()
    a2.setIndicadoresLuminososLigados(True)
    assert a2.getIndicadoresLuminososLigados() == True

    #Testar valor False
    a3 = AreaEdificio()
    a3.setIndicadoresLuminososLigados(False)
    assert a3.getIndicadoresLuminososLigados() == False


def testSetZonaCritica():
    a1 = AreaEdificio()

    #Teste para o valor padrão
    assert a1.getZonaCritica() == False
    
    #Teste para valor True
    a1.setZonaCritica(True) 
    assert a1.getZonaCritica() == True

    #Teste para valor False
    a1.setZonaCritica(False) 
    assert a1.getZonaCritica() == False


def testEhAlarmeFalso():
    #Teste para o caso em que nenhum alarme identificou incêndio
    a1 = AreaEdificio()
    al1 = Alarme()
    al2 = Alarme()
    al3 = Alarme()
    a1.setAlarmesDoEdificio([al1, al2, al3])
    assert a1.ehAlarmeFalso() == True

    #Teste para o caso em que um de três alarme identificou incêndio
    a2 = AreaEdificio()
    al4 = Alarme(True)
    al5 = Alarme()
    al6 = Alarme()
    a2.setAlarmesDoEdificio([al4, al5, al6])
    assert a2.ehAlarmeFalso() == True

    #Teste para o caso em que dois de três alarmes identificaram incêndio
    a3 = AreaEdificio()
    al7 = Alarme(True)
    al8 = Alarme(True)
    al9 = Alarme()
    a3.setAlarmesDoEdificio([al7, al8, al9])
    assert a3.ehAlarmeFalso() == False

    #Teste para o caso em que três de três alarmes identificaram incêndio
    a4 = AreaEdificio()
    al10 = Alarme(True)
    al11 = Alarme(True)
    al12 = Alarme(True)
    a4.setAlarmesDoEdificio([al10, al11, al12])
    assert a4.ehAlarmeFalso() == False

    # Teste para o caso em que AreaEdificio nao possui alarmes
    a5 = AreaEdificio()
    assert a5.ehAlarmeFalso() == True

    # Testes para um unico alarme
    a6 = AreaEdificio()
    al13 = Alarme()
    a6.setAlarmesDoEdificio([al13])
    assert a6.ehAlarmeFalso() == True

    # Testes para um unico alarme
    a7 = AreaEdificio()
    al14 = Alarme(True)
    a7.setAlarmesDoEdificio([al14])
    assert a7.ehAlarmeFalso() == False
    
    
def testFecharPortas():
    #Teste para o caso em que AreaEdificio nao possui zonas
    a1 = AreaEdificio()
    assert a1.fecharPortas() == False

    #Teste para o caso em que AreaEdificio possui uma zona amarela e nao tem pessoas
    a2 = AreaEdificio()
    a2.setZona(['amarelo'])
    assert a2.fecharPortas() == True

    #Teste para o caso em que AreaEdificio possui uma zona amarela e tem pessoas
    a3 = AreaEdificio()
    a3.setZona(['amarelo'])
    a3.setPessoasPresentes(10)
    assert a3.fecharPortas() == False

    #Teste para o caso em que AreaEdificio possui uma zona azul e nao tem pessoas
    a4 = AreaEdificio()
    a4.setZona(['azul'])
    assert a4.fecharPortas() == False

    #Teste para o caso em que AreaEdificio possui uma zona azul e tem pessoas
    a5 = AreaEdificio()
    a5.setZona(['azul'])
    a5.setPessoasPresentes(10)
    assert a5.fecharPortas() == False

    #Teste para o caso em que AreaEdificio possui uma zona azul e uma amarela e nao tem pessoas
    a6 = AreaEdificio()
    a6.setZona(['azul','amarelo'])
    assert a6.fecharPortas() == True

    #Teste para o caso em que AreaEdificio possui uma zona amarela e uma azul e nao tem pessoas
    a7 = AreaEdificio()
    a7.setZona(['amarelo','azul'])
    assert a7.fecharPortas() == True

    #Teste para o caso em que AreaEdificio possui uma zona azul e uma amarela e tem pessoas
    a8 = AreaEdificio()
    a8.setZona(['azul', 'amarelo'])
    a8.setPessoasPresentes(10)
    assert a8.fecharPortas() == False

    #Teste para o caso em que AreaEdificio possui uma zona amarela e uma azul e tem pessoas
    a9 = AreaEdificio()
    a9.setZona(['amarelo', 'azul'])
    a9.setPessoasPresentes(10)
    assert a9.fecharPortas() == False

def testDesligarSistemaEletrico():
    a1 = AreaEdificio()
    
    #Teste para o caso em que não há pessoas presentes e a zona não é azul
    a1.setPessoasPresentes(0)
    a1.setZona(['amarelo'])
    assert a1.desligarSistemaEletrico() == False

    #Teste para o caso em que há pessoas presentes e a zona não é azul
    a1.setPessoasPresentes(5)
    a1.setZona([])
    assert a1.desligarSistemaEletrico() == False

    #Teste para o caso em que não há pessoas presentes e a zona é azul
    a1.setPessoasPresentes(0)
    a1.setZona(['azul'])
    assert a1.desligarSistemaEletrico() == True

    #Teste para o caso em que há pessoas presentes e a zona é azul
    a1.setPessoasPresentes(3)
    a1.setZona(['amarelo', 'azul'])
    assert a1.desligarSistemaEletrico() == False

def testAlertarAreaCentral():
    #Teste para o caso em que o alarme é falso
    a1 = AreaEdificio()
    al1 = Alarme()
    a1.setAlarmesDoEdificio([al1])
    assert a1.alertarAreaCentral() == print("Alertar Area Central! Incendio Detectado!!")

    #Teste para o caso em que alarme não é falso
    a2 = AreaEdificio()
    al2 = Alarme(True)
    a2.setAlarmesDoEdificio([al2])
    assert a2.alertarAreaCentral() == False

    #Teste para o caso em que não há alarmes
    a3 = AreaEdificio()
    assert a3.alertarAreaCentral() == False

def testChamarServicosEmergencia():
    #Teste para o caso em que a zona é crítica
    a1 = AreaEdificio()
    al1 = Alarme()
    a1.setAlarmesDoEdificio([al1])
    a1.setZonaCritica(True)
    assert a1.chamarServicosEmergencia() == print("Ligando indicadores luminosos")
    
    #Teste para o caso em que a zona não é crítica
    a2 = AreaEdificio()
    al2 = Alarme()
    a2.setAlarmesDoEdificio([al2])
    a2.setZonaCritica(False)
    assert a2.chamarServicosEmergencia() == False

    #Testes para o caso em que a zona não há alarmes
    a3 = AreaEdificio()
    a3.setZonaCritica(True)
    assert a3.chamarServicosEmergencia() == False

    a4 = AreaEdificio()
    a4.setZonaCritica(False)
    assert a4.chamarServicosEmergencia() == False

def testLigarIndicadoresLuminosos():
    #Teste onde não tem incendio
    a1 = AreaEdificio()
    al1 = Alarme()
    al2 = Alarme()
    al3 = Alarme()
    a1.setAlarmesDoEdificio([al1, al2, al3])
    a1.ligarIndicadoresLuminosos()
    assert a1.getIndicadoresLuminososLigados() == False
    
    #Teste de alarme falso
    a2 = AreaEdificio()
    al4 = Alarme(True)
    al5 = Alarme()
    al6 = Alarme()
    a2.setAlarmesDoEdificio([al4, al5, al6])
    a2.ligarIndicadoresLuminosos()
    assert a2.getIndicadoresLuminososLigados() == False

    #Teste de alarme verdadeiro
    a3 = AreaEdificio()
    al7 = Alarme(True)
    al8 = Alarme(True)
    al9 = Alarme(True)
    a3.setAlarmesDoEdificio([al7, al8, al9])
    a3.ligarIndicadoresLuminosos()
    assert a3.getIndicadoresLuminososLigados() == True

    #Testes para o caso em que a zona não há alarmes
    a3 = AreaEdificio()
    a3.ligarIndicadoresLuminosos()
    assert a3.getIndicadoresLuminososLigados() == False

    a4 = AreaEdificio()
    assert a4.getIndicadoresLuminososLigados() == False