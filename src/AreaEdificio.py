class AreaEdificio:
  def __init__(self):
    self.nomeArea = ""
    self.zona = []
    self.alarmesDoEdificio = []
    self.zonaCritica = False
    self.pessoasPresentes = 0
    self.indicadoresLuminososLigados = False
    
  def setNomeArea(self, _nomeArea):
    self.nomeArea = _nomeArea
  
  def setZona(self, _zona):
    self.zona = _zona
  
  def setPessoasPresentes(self, _pessoasPresentes):
      self.pessoasPresentes = max(0, _pessoasPresentes)

  def setAlarmesDoEdificio(self, _alarmesDoEdificio):
    self.alarmesDoEdificio = _alarmesDoEdificio

  def setIndicadoresLuminososLigados(self, _indicadoresLuminososLigados):
    self.indicadoresLuminososLigados = _indicadoresLuminososLigados
  
  def setZonaCritica(self, _zonaCritica):
    self.zonaCritica = _zonaCritica

  def getNomeArea(self):
    return self.nomeArea
  
  def getZona(self):
    return self.zona
  
  def getPessoasPresentes(self):
    return self.pessoasPresentes

  def getAlarmesDoEdificio(self):
    return self.alarmesDoEdificio

  def getIndicadoresLuminososLigados(self):
    return self.indicadoresLuminososLigados

  def getZonaCritica(self):
    return self.zonaCritica
    
  def ehAlarmeFalso(self):
    if len(self.alarmesDoEdificio) == 0:
      return True

    aux = 0
    alarmeFalso = False
    
    for i in range(0, len(self.alarmesDoEdificio)):
      if(self.alarmesDoEdificio[i].getIdentificouUmFocoDeIncendio()):
        aux = aux + 1

    if(aux < (len(self.alarmesDoEdificio) / 2.0)):
      alarmeFalso = True
    
    return alarmeFalso
    
  def fecharPortas(self):
    fecharPortas = False
    for i in range(0, len(self.zona)):
      if self.zona[i] == "amarelo" and self.pessoasPresentes == 0:
        fecharPortas = True
        break

    return fecharPortas

  def desligarSistemaEletrico(self):
    desligarSistemaEletrico = False

    for i in range(0, len(self.zona)):
      if self.zona[i] == "azul" and self.pessoasPresentes == 0:
        desligarSistemaEletrico = True
        break

    return desligarSistemaEletrico

  def alertarAreaCentral(self):
    alarmeFalso = self.ehAlarmeFalso()

    if alarmeFalso and len(self.alarmesDoEdificio)!=0:
        return self.alarmesDoEdificio[0].enviarAlertaParaAreaCentral()
    
    else:
      return False
      
  def chamarServicosEmergencia(self):
    if self.zonaCritica and len(self.alarmesDoEdificio) != 0:
        return self.alarmesDoEdificio[0].ligarParaEmergencia()
    
    else:
      return False

  def ligarIndicadoresLuminosos(self):
    alarmeFalso = self.ehAlarmeFalso()
    
    if not alarmeFalso:
      self.indicadoresLuminososLigados = True
      
      if len(self.alarmesDoEdificio) != 0:
        self.alarmesDoEdificio[0].ligarIndicadoresLuminosos()
    
      else:
        return False
    else:
      return False