#!/usr/bin/python
# coding: utf8
import sys
import time
import datetime
import re
import shutil
from os import makedirs
from os import listdir
import win32com.client
from win10toast import ToastNotifier

class sap:
  def __init__(self, instancia=0) -> None:
      self.DESTAQUE_AMARELO = 3
      self.DESTAQUE_VERMELHO = 2
      self.DESTAQUE_VERDEJANTE = 4
      self.DESTAQUE_AUSENTE = 0
      self.instancia = instancia
      self.SapGui = win32com.client.GetObject("SAPGUI").GetScriptingEngine
      self.session = self.SapGui.FindById(f"ses[{self.instancia}]")
      self.toaster = ToastNotifier()
  def relatorio(self, dia=7) -> str:
      self.session.StartTransaction(Transaction="ZSVC20")
      self.session.FindById("wnd[0]/usr/btn%_SO_QMART_%_APP_%-VALU_PUSH").Press()
      self.session.FindById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,0]").text = "B1"
      self.session.FindById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,1]").text = "BL"
      self.session.FindById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,2]").text = "BR"
      self.session.FindById("wnd[1]/tbar[0]/btn[8]").Press()
      hoje = datetime.date.today()
      semana = hoje - datetime.timedelta(days=dia)
      self.session.FindById("wnd[0]/usr/ctxtSO_QMDAT-LOW").text = semana.strftime("%d.%m.%Y")
      self.session.FindById("wnd[0]/usr/ctxtSO_QMDAT-HIGH").text = hoje.strftime("%d.%m.%Y")
      self.session.FindById("wnd[0]/usr/btn%_SO_USUAR_%_APP_%-VALU_PUSH").Press()
      self.session.FindById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,0]").text = "ENVI"
      self.session.FindById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,1]").text = "LIBE"
      self.session.FindById("wnd[1]/tbar[0]/btn[8]").Press()
      self.session.FindById("wnd[0]/usr/ctxtSO_BEBER-LOW").text = "RB"
      self.session.FindById("wnd[0]/usr/ctxtP_LAYOUT").text = "/MANSERVRELC"
      self.session.FindById("wnd[0]/tbar[1]/btn[8]").Press()
      if (dia > 0):
        self.toaster.show_toast("Relatório está pronto!")
      filepath = "S:\\ADM\\RUAN CAMELLO\\" + hoje.strftime("%d.%m.%Y")
      filename = datetime.datetime.now().strftime("%H;%M") + ".XLSX"
      try:
        self.session.FindById("wnd[0]/usr/cntlCONTAINER_100/shellcont/shell").pressToolbarContextButton("&MB_EXPORT")
        self.session.FindById("wnd[0]/usr/cntlCONTAINER_100/shellcont/shell").selectContextMenuItem("&XXL")
        return "O relatorio esta pronto"
      except:
        raise Exception("O relatório de notas em aberto está vazio!")
      #TODO: make interation with fileDialog
      # https://answers.sap.com/questions/7761287/pasting-filename-in-a-panel-using-script.html
      if (dia > 0):
        self.manobra(dia)
  def manobra(self, dia=0) -> str:
      self.session.StartTransaction(Transaction="ZSVC20")
      self.session.FindById("wnd[0]/usr/btn%_SO_QMART_%_APP_%-VALU_PUSH").Press()
      self.session.FindById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,0]").text = "BP"
      self.session.FindById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,1]").text = "BB"
      self.session.FindById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,2]").text = "BD"
      self.session.FindById("wnd[1]/tbar[0]/btn[8]").Press()
      hoje = datetime.date.today()
      semana = hoje - datetime.timedelta(days=dia)
      self.session.FindById("wnd[0]/usr/ctxtSO_QMDAT-LOW").text = semana.strftime("%d.%m.%Y")
      self.session.FindById("wnd[0]/usr/ctxtSO_QMDAT-HIGH").text = hoje.strftime("%d.%m.%Y")
      self.session.FindById("wnd[0]/usr/btn%_SO_FECOD_%_APP_%-VALU_PUSH").Press()
      self.session.FindById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,0]").text = "AP04"
      self.session.FindById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,1]").text = "AP99"
      self.session.FindById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,2]").text = "AP11"
      self.session.FindById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,3]").text = "AP25"
      self.session.FindById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,4]").text = "AP79"
      self.session.FindById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,5]").text = "APRA"
      self.session.FindById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,6]").text = "APRT"
      self.session.FindById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,7]").text = "APTC"
      self.session.FindById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE").verticalScrollbar.position = 1
      self.session.FindById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,7]").text = "APCI"
      self.session.FindById("wnd[1]/tbar[0]/btn[8]").Press()
      self.session.FindById("wnd[0]/usr/btn%_SO_USUAR_%_APP_%-VALU_PUSH").Press()
      self.session.FindById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,0]").text = "ENVI"
      self.session.FindById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,1]").text = "LIBE"
      self.session.FindById("wnd[1]/tbar[0]/btn[8]").Press()
      self.session.FindById("wnd[0]/usr/ctxtSO_BEBER-LOW").text = "RB"
      self.session.FindById("wnd[0]/usr/ctxtP_LAYOUT").text = "/MANSERVRELC"
      self.session.FindById("wnd[0]/tbar[1]/btn[8]").Press()
      try:
        self.session.FindById("wnd[0]/usr/cntlCONTAINER_100/shellcont/shell").pressToolbarContextButton("&MB_EXPORT")
        self.session.FindById("wnd[0]/usr/cntlCONTAINER_100/shellcont/shell").selectContextMenuItem("&XXL")
        return "O relatorio de manobra esta pronto!"
      except:
        raise Exception("O relatório de notas em aberto está vazio!")
  def leiturista(self, nota, retry=False) -> str:
      instalacao = self.instalacao(nota)
      self.session.StartTransaction(Transaction="ES32")
      self.session.FindById("wnd[0]/usr/ctxtEANLD-ANLAGE").text = instalacao
      self.session.findById("wnd[0]/tbar[0]/btn[0]").Press()
      unidade = self.session.FindById("wnd[0]/usr/tblSAPLES30TC_TIMESL/ctxtEANLD-ABLEINH[9,0]").text
      self.session.StartTransaction(Transaction="ZMED89")
      livro = f"{unidade[0]}{unidade[1]}"
      local = f"{unidade[2]}{unidade[3]}{unidade[4]}{unidade[5]}"
      if (local == "L645"): centro = "017"
      elif (local == "L644"): centro = "017"
      elif (local == "L643"): centro = "017"
      elif (local == "L624"): centro = "017"
      elif (local == "L622"): centro = "017"
      elif (local == "L613"): centro = "017"
      elif (local == "L616"): centro = "015"
      elif (local == "L615"): centro = "015"
      elif (local == "L614"): centro = "015"
      elif (local == "L612"): centro = "015"
      elif (local == "L610"): centro = "014"
      elif (local == "L623"): centro = "014"
      elif (local == "L611"): centro = "014"
      elif (local == "L620"): centro = "015"
      elif (local == "L617"): centro = "015"
      elif (local == "L625"): centro = "013"
      elif (local == "L635"): centro = "013"
      elif (local == "L636"): centro = "013"
      elif (local == "L637"): centro = "013"
      elif (local == "L630"): centro = "012"
      elif (local == "L632"): centro = "012"
      elif (local == "L731"): centro = "016"
      elif (local == "L749"): centro = "016"
      elif (local == "L762"): centro = "016"
      elif (local == "L747"): centro = "016"
      else: raise Exception(f"A localidade {local} pesquisada é desconhecida")
      mes = datetime.date.today()
      mes = mes.replace(day=1)
      mes = mes - datetime.timedelta(days=1)
      self.session.FindById("wnd[0]/usr/txtP_ABL_Z-LOW").text = centro
      self.session.FindById("wnd[0]/usr/ctxtP_LOTE-LOW").text = livro
      self.session.FindById("wnd[0]/usr/ctxtP_MESANO").text = mes.strftime("%m/%Y")
      self.session.FindById("wnd[0]/usr/ctxtP_UNID-LOW").text = unidade
      self.session.FindById("wnd[0]/tbar[1]/btn[8]").Press()
      try:
        self.session.FindById("wnd[0]/tbar[1]/btn[33]").Press()
      except:
        raise Exception("Não há relatório de leitura para o período especificado!")
      self.session.FindById("wnd[1]/usr/ssubD0500_SUBSCREEN:SAPLSLVC_DIALOG:0501/cntlG51_CONTAINER/shellcont/shell").setCurrentCell(0,"DEFAULT")
      self.session.FindById("wnd[1]/usr/ssubD0500_SUBSCREEN:SAPLSLVC_DIALOG:0501/cntlG51_CONTAINER/shellcont/shell").clickCurrentCell()
      self.session.FindById("wnd[0]/tbar[0]/btn[71]").Press()
      self.session.FindById("wnd[1]/usr/txtGS_SEARCH-VALUE").text = instalacao
      self.session.FindById("wnd[1]/usr/cmbGS_SEARCH-SEARCH_ORDER").key = "0"
      self.session.FindById("wnd[1]/tbar[0]/btn[0]").Press()
      # statusBar = self.session.FindById("/app/con[0]/ses[{self.instancia}]/wnd[0]/sbar").text
      # if(statusBar == "Nenhuma ocorrência encontrada"):
        # raise Exception("A instalação não foi encontrada no relatório!")
      self.session.FindById("wnd[1]").Close()
      celula = self.session.FindById("wnd[0]/usr/cntlGRID1/shellcont/shell").currentCellRow
      if(celula == 0):
        raise Exception("A instalação não foi encontrada no relatório!")
      linhas = self.session.FindById("wnd[0]/usr/cntlGRID1/shellcont/shell").RowCount
      # se a linhaAtual é menor que 14, a primeiraVisivel é 0 e offset é igual a linha atual
      # se a linhaAtual é maior que linhasTotais - 14, então primeiraVisivel é linhasTotais - 28 e offset é igual a
      apontador = 0
      limite = 0
      offset = 0
      # Se a instalação foi encontrada no início do relatório
      if (celula <= 14):
        self.session.FindById("wnd[0]/usr/cntlGRID1/shellcont/shell").firstVisibleRow = 0
        apontador = 0
        limite = 28
        offset = celula + 1
      # Se a instalação foi encontrada no meio do relatório
      if (celula > 14 and celula < (linhas - 14)):
        self.session.FindById("wnd[0]/usr/cntlGRID1/shellcont/shell").firstVisibleRow = celula - 14
        apontador = celula - 14
        limite = celula + 14
        offset = 14 + 1
      # Se a instalação foi encontrada no final do relatório
      if(celula > 14 and celula >= (linhas - 14)):
        self.session.FindById("wnd[0]/usr/cntlGRID1/shellcont/shell").firstVisibleRow = linhas - 28
        apontador = celula - 28
        limite = linhas
        offset = (28 - (linhas - celula)) + 1
      self.session.FindById("wnd[0]/usr/cntlGRID1/shellcont/shell").selectedRows = celula
      leitString = "Cor|Seq|Instalacao|Endereco|Bairro|Medidor|Hora|Cod\n"
      tamanhos = [0,4,10,0,0,8,8,4]
      while (apontador < limite and apontador < linhas):
        destaque = self.DESTAQUE_AMARELO if(apontador == celula) else self.DESTAQUE_AUSENTE
        sequencia = self.session.FindById("wnd[0]/usr/cntlGRID1/shellcont/shell").getCellValue(apontador,"ZZ_NUMSEQ")
        instalRoteiro = self.session.FindById("wnd[0]/usr/cntlGRID1/shellcont/shell").getCellValue(apontador,"ANLAGE")
        endereco = self.session.FindById("wnd[0]/usr/cntlGRID1/shellcont/shell").getCellValue(apontador,"ZENDERECO")
        tamanhos[3] = len(endereco) if (len(endereco) > tamanhos[3]) else tamanhos[3]
        subbairro = self.session.FindById("wnd[0]/usr/cntlGRID1/shellcont/shell").getCellValue(apontador,"BAIRRO")
        tamanhos[4] = len(subbairro) if (len(subbairro) > tamanhos[4]) else tamanhos[4]
        medidor = self.session.FindById("wnd[0]/usr/cntlGRID1/shellcont/shell").getCellValue(apontador,"GERAET")
        horaleit = self.session.FindById("wnd[0]/usr/cntlGRID1/shellcont/shell").getCellValue(apontador,"ZHORALEIT")
        codleit = self.session.FindById("wnd[0]/usr/cntlGRID1/shellcont/shell").getCellValue(apontador,"ABLHINW")
        leitString = f"{leitString}{destaque}|{sequencia}|{instalRoteiro}|{endereco}|{subbairro}|{medidor}|{horaleit}|{codleit}\n"
        apontador = apontador + 1
      tamanhosString = f"{tamanhos[0]}|{tamanhos[1]}|{tamanhos[2]}|{tamanhos[3]}|{tamanhos[4]}|{tamanhos[5]}|{tamanhos[6]}|{tamanhos[7]}\n"
      leitString = tamanhosString + leitString
      return leitString
  def debito(self, nota) -> None:
    instalacao = self.instalacao(nota)
    contrato = self.session.FindById("wnd[0]/usr/txtEANLD-VERTRAG").text
    self.session.StartTransaction(Transaction="ZARC140")
    self.session.FindById("wnd[0]/usr/ctxtP_PARTNR").text = ""
    self.session.findById("wnd[0]/usr/ctxtP_VERTRG").text = contrato
    self.session.FindById("wnd[0]/usr/ctxtP_ANLAGE").text = instalacao
    self.session.FindById("wnd[0]/tbar[1]/btn[8]").Press()
  def escrever(self, nota) -> str:
    self.debito(nota)
    linhas = self.session.FindById("wnd[0]/usr/tabsTAB_STRIP_100/tabpF110/ssubSUB_100:SAPLZARC_DEBITOS_CCS_V2:0110/cntlCONTAINER_110/shellcont/shell").RowCount
    debString = 'Cor|Mes ref.|Vencimento|Valor|Tipo|Status\n'
    apontador = 1
    tamanhos = [0,7,10,12,0,0]
    while (apontador < linhas):
      referencia = self.session.FindById("wnd[0]/usr/tabsTAB_STRIP_100/tabpF110/ssubSUB_100:SAPLZARC_DEBITOS_CCS_V2:0110/cntlCONTAINER_110/shellcont/shell").getCellValue(apontador,"BILLING_PERIOD")
      vencimento = self.session.FindById("wnd[0]/usr/tabsTAB_STRIP_100/tabpF110/ssubSUB_100:SAPLZARC_DEBITOS_CCS_V2:0110/cntlCONTAINER_110/shellcont/shell").getCellValue(apontador,"FAEDN")
      valorPendente = self.session.FindById("wnd[0]/usr/tabsTAB_STRIP_100/tabpF110/ssubSUB_100:SAPLZARC_DEBITOS_CCS_V2:0110/cntlCONTAINER_110/shellcont/shell").getCellValue(apontador,"TOTAL_AMNT")
      tipoDebito = self.session.FindById("wnd[0]/usr/tabsTAB_STRIP_100/tabpF110/ssubSUB_100:SAPLZARC_DEBITOS_CCS_V2:0110/cntlCONTAINER_110/shellcont/shell").getCellValue(apontador,"TIP_FATURA")
      tamanhos[4] = len(tipoDebito) if (len(tipoDebito) > tamanhos[4]) else tamanhos[4]
      statusFat = self.session.findById("wnd[0]/usr/tabsTAB_STRIP_100/tabpF110/ssubSUB_100:SAPLZARC_DEBITOS_CCS_V2:0110/cntlCONTAINER_110/shellcont/shell").getCellValue(apontador, "STATUS")
      if(statusFat == "@5B@"): # Status no prazo de vencimento da fatura
        destaque = self.DESTAQUE_VERDEJANTE
        textStatus = "Fat. no prazo"
      elif(statusFat == "@5C@"): # Status prazo de pagamento vencido
        destaque = self.DESTAQUE_VERMELHO
        textStatus = "Fat. vencida"
      elif(statusFat == "@06@"): # Status prazo de pagamento vencido
        destaque = self.DESTAQUE_AMARELO
        textStatus = "Fat. Retida"
      else:
        destaque = self.DESTAQUE_AUSENTE
        textStatus = "Consultar"
      tamanhos[5] = len(textStatus) if (len(textStatus) > tamanhos[5]) else tamanhos[5]
      debString = f"{debString}{destaque}|{referencia}|{vencimento}|R$:{valorPendente}|{tipoDebito}|{textStatus}\n"
      apontador = apontador + 1
    tamanhosString = f"{tamanhos[0]}|{tamanhos[1]}|{tamanhos[2]}|{tamanhos[3]}|{tamanhos[4]}|{tamanhos[5]}\n"
    debString = tamanhosString + debString
    return debString
  def imprimir(self, documento):
    self.session.StartTransaction(Transaction="ZATC73")
    shutil.rmtree("C:\\Users\\ruan.camello\\Documents\\Temporario")
    makedirs("C:\\Users\\ruan.camello\\Documents\\Temporario")
    self.session.FindById("wnd[0]/usr/chkP_LOCL").selected = True
    self.session.FindById("wnd[0]/usr/chkP_IMPLOC").selected = True
    apontador = 0
    while(apontador < len(documento)):
      self.session.FindById("wnd[0]/usr/ctxtP_OPBEL").text = documento[apontador]
      self.session.FindById("wnd[0]/tbar[1]/btn[8]").Press()
      apontador = apontador + 1
  def fatura_novo(self, nota) -> str:
    debitos = []
    apontador = 0
    self.debito(nota)
    linhas = self.session.FindById("wnd[0]/usr/tabsTAB_STRIP_100/tabpF110/ssubSUB_100:SAPLZARC_DEBITOS_CCS_V2:0110/cntlCONTAINER_110/shellcont/shell").RowCount
    while(apontador < linhas):
      if not (self.analisar(apontador)):
        apontador = apontador + 1
        continue
      debitos.append(self.session.FindById("wnd[0]/usr/tabsTAB_STRIP_100/tabpF110/ssubSUB_100:SAPLZARC_DEBITOS_CCS_V2:0110/cntlCONTAINER_110/shellcont/shell").getCellValue(apontador,"ZIMPRES"))
      apontador = apontador + 1
    if(len(debitos)> 5):
      raise Exception("Cliente possui muitas faturas pendentes")
    self.imprimir(debitos)
    return self.monitorar(len(debitos))
  def instalacao(self, arg: str) -> str:
    arg = str(arg)
    if re.search("[0-9]{10}", arg):
      self.session.StartTransaction(Transaction="IW53")
      self.session.FindById("wnd[0]/usr/ctxtRIWO00-QMNUM").text = arg
      try:
        self.session.FindById("wnd[0]/tbar[1]/btn[5]").Press()
      except:
        raise Exception("A nota informada é inválida!")
      self.session.FindById("wnd[0]/usr/tabsTAB_GROUP_10/tabp10\TAB09").Select()
      instalacao = self.session.FindById("wnd[0]/usr/tabsTAB_GROUP_10/tabp10\TAB09/ssubSUB_GROUP_10:SAPLIQS0:7217/subSUBSCREEN_1:SAPLIQS0:7900/subUSER0001:SAPLXQQM:0102/ctxtVIQMEL-ZZINSTLN").text
      self.instalacao(instalacao)
      return instalacao
    elif re.search("[0-9]{9}", arg):
      self.session.StartTransaction(Transaction="ES32")
      self.session.FindById("wnd[0]/usr/ctxtEANLD-ANLAGE").text = arg
      self.session.FindById("wnd[0]/tbar[0]/btn[0]").Press()
      return arg
    else:
      return ""
  def historico(self, nota) -> str:
    instalacao = self.instalacao(nota)
    self.session.StartTransaction(Transaction="ZSVC20")
    self.session.FindById("wnd[0]/usr/ctxtSO_ANLAG-LOW").text = instalacao
    self.session.FindById("wnd[0]/usr/ctxtSO_QMART-LOW").text = ""
    self.session.FindById("wnd[0]/usr/ctxtSO_QMDAT-LOW").text = ""
    self.session.FindById("wnd[0]/usr/ctxtSO_QMDAT-HIGH").text = ""
    self.session.FindById("wnd[0]/usr/ctxtP_LAYOUT").text = "/WILLIAM"
    self.session.FindById("wnd[0]/tbar[1]/btn[8]").Press()
    linhas = self.session.FindById("wnd[0]/usr/cntlCONTAINER_100/shellcont/shell").RowCount
    apontador = 0
    tamanhos = [0,10,0,0,10]
    historico = "Cor|Nota|Texto breve para dano|Texto breve para code|Data\n"
    while(apontador < linhas and apontador < 10):
      destaque = 0
      notaServico = self.session.FindById("wnd[0]/usr/cntlCONTAINER_100/shellcont/shell").getCellValue(apontador,"QMNUM")
      textoDano = self.session.FindById("wnd[0]/usr/cntlCONTAINER_100/shellcont/shell").getCellValue(apontador, "KURZTEXT")
      tamanhos[2] = len(textoDano) if (len(textoDano) > tamanhos[2]) else tamanhos[2]
      textoCode = self.session.FindById("wnd[0]/usr/cntlCONTAINER_100/shellcont/shell").getCellValue(apontador,"MATXT")
      tamanhos[3] = len(textoCode) if (len(textoCode) > tamanhos[3]) else tamanhos[3]
      FimAvaria = self.session.FindById("wnd[0]/usr/cntlCONTAINER_100/shellcont/shell").getCellValue(apontador,"AUSBS")
      historico = f"{historico}{destaque}|{notaServico}|{textoDano}|{textoCode}|{FimAvaria}\n"
      apontador = apontador + 1
    tamanho = f"{tamanhos[0]}|{tamanhos[1]}|{tamanhos[2]}|{tamanhos[3]}|{tamanhos[4]}\n"
    return tamanho + historico
  def agrupamento(self, nota): #TODO: Implementar análise de débitos
    instalacao = self.instalacao(nota)
    self.session.StartTransaction(Transaction="ES32")
    self.session.FindById("wnd[0]/usr/ctxtEANLD-ANLAGE").text = instalacao
    self.session.FindById("wnd[0]/tbar[0]/btn[0]").Press()
    consumo = self.session.FindById("wnd[0]/usr/ctxtEANLD-VSTELLE").text
    self.session.StartTransaction(Transaction="ES61")
    self.session.findById("wnd[0]/usr/ctxtEVBSD-VSTELLE").text = consumo
    self.session.FindById("wnd[0]/tbar[0]/btn[0]").Press()
    ligacao = self.session.FindById("wnd[0]/usr/ctxtEVBSD-HAUS").text
    self.session.StartTransaction(Transaction="ES57")
    self.session.FindById("wnd[0]/usr/ctxtEHAUD-HAUS").text = ligacao
    self.session.FindById("wnd[0]/tbar[0]/btn[0]").Press()
    logradouro = self.session.findById("wnd[0]/usr/subADDRESS:SAPLSZA1:0300/subCOUNTRY_SCREEN:SAPLSZA1:0301/txtADDR1_DATA-NAME_CO").text
    numero = self.session.findById("wnd[0]/usr/subADDRESS:SAPLSZA1:0300/subCOUNTRY_SCREEN:SAPLSZA1:0301/txtADDR1_DATA-HOUSE_NUM1").text
    self.session.StartTransaction(Transaction="ZMED95")
    self.session.FindById("wnd[0]/usr/ctxtADRSTREET-STRT_CODE").text = logradouro
    self.session.FindById("wnd[0]/tbar[0]/btn[0]").Press()
    self.session.FindById("wnd[0]/tbar[1]/btn[9]").Press()
    if (numero == "1SN" or numero == "SN"):
      raise Exception("O agrupamento não pode ser analizado automaticamente")
    linhas = self.session.FindById("wnd[0]/usr/tblSAPLZMED_ENDERECOSTC_NUMSX").RowCount
    numero_sem_letra = re.search("[0-9]{1,5}", numero)
    if(numero_sem_letra == None):
      raise Exception("O agrupamento não pode ser analizado automaticamente")
    apontador = 0
    while (apontador < linhas):
      num10 = self.session.FindById(f"wnd[0]/usr/tblSAPLZMED_ENDERECOSTC_NUMSX/txtTI_NUMSX-NUMERO[0,10]").text
      num10_sem_letra = re.search("[0-9]{1,5}", num10)
      if ((num10_sem_letra != None) and (int(num10_sem_letra.group()) < int(numero_sem_letra.group()))):
        apontador = apontador + 10
        self.session.FindById("wnd[0]/usr/tblSAPLZMED_ENDERECOSTC_NUMSX").verticalScrollbar.position = apontador
        continue
      num = self.session.FindById(f"wnd[0]/usr/tblSAPLZMED_ENDERECOSTC_NUMSX/txtTI_NUMSX-NUMERO[0,0]").text
      if num == numero:
        self.session.FindById("wnd[0]/usr/tblSAPLZMED_ENDERECOSTC_NUMSX").verticalScrollbar.position = apontador
        self.session.FindById(f"wnd[0]/usr/tblSAPLZMED_ENDERECOSTC_NUMSX").GetAbsoluteRow(apontador).selected = True
        self.session.FindById("wnd[0]/usr/btn%#AUTOTEXT005").Press()
        break
      apontador = apontador + 1
      self.session.FindById("wnd[0]/usr/tblSAPLZMED_ENDERECOSTC_NUMSX").verticalScrollbar.position = apontador
    apontador = 0
    linhas = self.session.FindById("wnd[0]/usr/tblSAPLZMED_ENDERECOSTC_INSTALX").RowCount
    return linhas
    enderecos = []
    instalacoes = []
    nomeCliente = []
    tipoinstal = []
    while (apontador < linhas):
      pass
  def coordenadas(self, nota) -> str:
    instalacao = self.instalacao(nota)
    self.session.StartTransaction(Transaction="ES32")
    self.session.FindById("wnd[0]/usr/ctxtEANLD-ANLAGE").text = instalacao
    self.session.findById("wnd[0]/tbar[0]/btn[0]").Press()
    consumo = self.session.FindById("wnd[0]/usr/ctxtEANLD-VSTELLE").text
    self.session.StartTransaction(Transaction="ES61")
    self.session.findById("wnd[0]/usr/ctxtEVBSD-VSTELLE").text = consumo
    self.session.FindById("wnd[0]/tbar[0]/btn[0]").Press()
    self.session.FindById("wnd[0]/usr/ssubSUB:SAPLXES60:0100/tabsTS0100/tabpTAB1/ssubSUB1:SAPLXES60:0101/ctxtEVBSD-ZZ_TPCAIXA").text = ""
    self.session.FindById("wnd[0]/usr/ssubSUB:SAPLXES60:0100/tabsTS0100/tabpTAB1/ssubSUB1:SAPLXES60:0101/ctxtEVBSD-ZZ_MDCAIXA").text = ""
    self.session.FindById("wnd[0]/usr/ssubSUB:SAPLXES60:0100/tabsTS0100/tabpTAB1/ssubSUB1:SAPLXES60:0101/txtEVBSD-ZZ_NUMCAIXA").text = ""
    self.session.FindById("wnd[0]/usr/ssubSUB:SAPLXES60:0100/tabsTS0100/tabpTAB2").Select()
    coordenada = self.session.FindById("wnd[0]/usr/ssubSUB:SAPLXES60:0100/tabsTS0100/tabpTAB2/ssubSUB1:SAPLXES60:0201/txtEVBSD-ZZ_COORDENADAS").text
    if (len(coordenada) > 0):
      coordenada = re.sub(',', '.', coordenada)
      coordenada = re.findall("-[0-9]{2}.[0-9]*", coordenada)
      return f"https://www.google.com/maps?z=12&t=m&q=loc:{coordenada[0]}+{coordenada[1]}"
    else:
      raise Exception("A instalação não possui coordenada cadastrada!")
  def telefone(self, info) -> str:
    telefone = []
    nome_solicitante = ""
    if re.search("[0-9]{10}", str(info)):
      self.session.StartTransaction(Transaction="IW53")
      self.session.FindById("wnd[0]/usr/ctxtRIWO00-QMNUM").text = info
      try:
        self.session.FindById("wnd[0]/tbar[1]/btn[5]").Press()
      except:
        raise Exception("Número da nota é inválido!")
      self.session.FindById("wnd[0]/usr/tabsTAB_GROUP_10/tabp10\TAB09").Select()
      nome_solicitante = self.session.FindById("wnd[0]/usr/tabsTAB_GROUP_10/tabp10\TAB09/ssubSUB_GROUP_10:SAPLIQS0:7217/subSUBSCREEN_1:SAPLIQS0:7900/subUSER0001:SAPLXQQM:0102/txtVIQMEL-ZZ_NOME_SOLICIT").text
      telefone.append(self.session.FindById("wnd[0]/usr/tabsTAB_GROUP_10/tabp10\TAB09/ssubSUB_GROUP_10:SAPLIQS0:7217/subSUBSCREEN_1:SAPLIQS0:7900/subUSER0001:SAPLXQQM:0102/txtVIQMEL-ZZ_TEL_SOLICIT").text)
      telefone.append(self.session.FindById("wnd[0]/usr/tabsTAB_GROUP_10/tabp10\TAB09/ssubSUB_GROUP_10:SAPLIQS0:7217/subSUBSCREEN_1:SAPLIQS0:7900/subUSER0001:SAPLXQQM:0102/txtVIQMEL-ZZ_CEL_SOLICIT").text)
      info = self.session.FindById("wnd[0]/usr/tabsTAB_GROUP_10/tabp10\TAB09/ssubSUB_GROUP_10:SAPLIQS0:7217/subSUBSCREEN_1:SAPLIQS0:7900/subUSER0001:SAPLXQQM:0102/ctxtVIQMEL-ZZINSTLN").text
    self.session.StartTransaction(Transaction="ES32")
    self.session.FindById("wnd[0]/usr/ctxtEANLD-ANLAGE").text = info
    self.session.FindById("wnd[0]/tbar[0]/btn[0]").Press()
    cliente = self.session.FindById("wnd[0]/usr/txtEANLD-PARTNER").text
    self.session.StartTransaction(Transaction="BP")
    try:
      self.session.FindById("wnd[0]/usr/subSCREEN_3000_RESIZING_AREA:SAPLBUS_LOCATOR:2000/subSCREEN_1010_RIGHT_AREA:SAPLBUPA_DIALOG_JOEL:1000/subSCREEN_1000_HEADER_AREA:SAPLBUPA_DIALOG_JOEL:1510/ctxtBUS_JOEL_MAIN-CHANGE_NUMBER").text = cliente
    except:
      self.session.FindById("wnd[0]/tbar[1]/btn[9]").Press()
      self.session.FindById("wnd[0]/usr/subSCREEN_3000_RESIZING_AREA:SAPLBUS_LOCATOR:2000/subSCREEN_1010_RIGHT_AREA:SAPLBUPA_DIALOG_JOEL:1000/subSCREEN_1000_HEADER_AREA:SAPLBUPA_DIALOG_JOEL:1510/ctxtBUS_JOEL_MAIN-CHANGE_NUMBER").text = cliente
    self.session.FindById("wnd[0]/tbar[0]/btn[0]").Press()
    nome_cliente = self.session.FindById("wnd[0]/usr/subSCREEN_3000_RESIZING_AREA:SAPLBUS_LOCATOR:2000/subSCREEN_1010_RIGHT_AREA:SAPLBUPA_DIALOG_JOEL:1000/subSCREEN_1000_HEADER_AREA:SAPLBUPA_DIALOG_JOEL:1510/txtBUS_JOEL_MAIN-CHANGE_DESCRIPTION").text
    self.session.FindById("wnd[0]/usr/subSCREEN_3000_RESIZING_AREA:SAPLBUS_LOCATOR:2000/subSCREEN_1010_RIGHT_AREA:SAPLBUPA_DIALOG_JOEL:1000/ssubSCREEN_1000_WORKAREA_AREA:SAPLBUPA_DIALOG_JOEL:1100/ssubSCREEN_1100_MAIN_AREA:SAPLBUPA_DIALOG_JOEL:1101/tabsGS_SCREEN_1100_TABSTRIP/tabpSCREEN_1100_TAB_01").Select()
    def coletor(self):
      try:
        coleta = []
        coleta.append(self.session.FindById("wnd[1]/usr/tblSAPLSZA6T_CONTROL2/txtADTEL-TEL_NUMBER[2,0]").text)
        coleta.append(self.session.FindById("wnd[1]/usr/tblSAPLSZA6T_CONTROL2/txtADTEL-TEL_NUMBER[2,1]").text)
        coleta.append(self.session.FindById("wnd[1]/usr/tblSAPLSZA6T_CONTROL2/txtADTEL-TEL_NUMBER[2,2]").text)
        coleta.append(self.session.FindById("wnd[1]/usr/tblSAPLSZA6T_CONTROL2/txtADTEL-TEL_NUMBER[2,3]").text)
        self.session.FindById("wnd[1]").Close()
        return coleta
      except:
        return ""
    self.session.FindById("wnd[0]/usr/subSCREEN_3000_RESIZING_AREA:SAPLBUS_LOCATOR:2000/subSCREEN_1010_RIGHT_AREA:SAPLBUPA_DIALOG_JOEL:1000/ssubSCREEN_1000_WORKAREA_AREA:SAPLBUPA_DIALOG_JOEL:1100/ssubSCREEN_1100_MAIN_AREA:SAPLBUPA_DIALOG_JOEL:1101/tabsGS_SCREEN_1100_TABSTRIP/tabpSCREEN_1100_TAB_01/ssubSCREEN_1100_TABSTRIP_AREA:SAPLBUSS:0028/ssubGENSUB:SAPLBUSS:7016/subA05P01:SAPLBUA0:0400/subADDRESS:SAPLSZA7:0600/subCOUNTRY_SCREEN:SAPLSZA7:0601/btnG_ICON_TEL").Press()
    telefone.extend(coletor(self))
    self.session.FindById("wnd[0]/usr/subSCREEN_3000_RESIZING_AREA:SAPLBUS_LOCATOR:2000/subSCREEN_1010_RIGHT_AREA:SAPLBUPA_DIALOG_JOEL:1000/ssubSCREEN_1000_WORKAREA_AREA:SAPLBUPA_DIALOG_JOEL:1100/ssubSCREEN_1100_MAIN_AREA:SAPLBUPA_DIALOG_JOEL:1101/tabsGS_SCREEN_1100_TABSTRIP/tabpSCREEN_1100_TAB_01/ssubSCREEN_1100_TABSTRIP_AREA:SAPLBUSS:0028/ssubGENSUB:SAPLBUSS:7016/subA05P01:SAPLBUA0:0400/subADDRESS:SAPLSZA7:0600/subCOUNTRY_SCREEN:SAPLSZA7:0601/btnG_ICON_MOB").Press()
    telefone.extend(coletor(self))
    self.session.FindById("wnd[0]/usr/subSCREEN_3000_RESIZING_AREA:SAPLBUS_LOCATOR:2000/subSCREEN_1010_RIGHT_AREA:SAPLBUPA_DIALOG_JOEL:1000/ssubSCREEN_1000_WORKAREA_AREA:SAPLBUPA_DIALOG_JOEL:1100/ssubSCREEN_1100_MAIN_AREA:SAPLBUPA_DIALOG_JOEL:1101/tabsGS_SCREEN_1100_TABSTRIP/tabpSCREEN_1100_TAB_01/ssubSCREEN_1100_TABSTRIP_AREA:SAPLBUSS:0028/ssubGENSUB:SAPLBUSS:7016/subA06P01:SAPLBUA0:0700/subADDR_ICOMM:SAPLSZA11:0100/btnG_ICON_TEL").Press()
    telefone.extend(coletor(self))
    self.session.FindById("wnd[0]/usr/subSCREEN_3000_RESIZING_AREA:SAPLBUS_LOCATOR:2000/subSCREEN_1010_RIGHT_AREA:SAPLBUPA_DIALOG_JOEL:1000/ssubSCREEN_1000_WORKAREA_AREA:SAPLBUPA_DIALOG_JOEL:1100/ssubSCREEN_1100_MAIN_AREA:SAPLBUPA_DIALOG_JOEL:1101/tabsGS_SCREEN_1100_TABSTRIP/tabpSCREEN_1100_TAB_01/ssubSCREEN_1100_TABSTRIP_AREA:SAPLBUSS:0028/ssubGENSUB:SAPLBUSS:7016/subA06P01:SAPLBUA0:0700/subADDR_ICOMM:SAPLSZA11:0100/btnG_ICON_MOB").Press()
    telefone.extend(coletor(self))
    # Remove duplicadas do array
    telefone = list(dict.fromkeys(telefone))
    try:
      telefone.remove("______________________________")
    except:
      pass
    texto = nome_solicitante + " " if (len(nome_solicitante) > 0) else nome_cliente + " "
    for tel in telefone:
      texto += tel + " " if (len(tel) > 0) else ""
    return texto
  def medidor(self, nota) -> str:
    instalacao = self.instalacao(nota)
    self.session.StartTransaction(Transaction="ZATC66")
    self.session.FindById("wnd[0]/usr/ctxtP_ANLAGE").text = instalacao
    self.session.FindById("wnd[0]/tbar[1]/btn[8]").Press()
    try:
      self.session.FindById("wnd[0]/usr/subSUB1:SAPLZATC_INFO_CRM:0900/radXSCREEN-HEADER-RB_LEIT").Select()
    except:
      raise Exception(f"A instalação {instalacao} não possui histórico de consumo para o contrato atual.")
    linhas = self.session.FindById("wnd[0]/usr/cntlCONTROL/shellcont/shell").RowCount
    apontador = 0
    while(apontador < linhas):
      codigo = self.session.FindById("wnd[0]/usr/cntlCONTROL/shellcont/shell").getCellValue(apontador,"OCORRENCIA")
      if ((codigo == "3201") or (codigo == "3202") or (codigo == "3203") or (codigo == "3251")):
        medidor = int(self.session.FindById("wnd[0]/usr/cntlCONTROL/shellcont/shell").getCellValue(apontador,"GERNR"))
        leitura = self.session.FindById("wnd[0]/usr/cntlCONTROL/shellcont/shell").getCellValue(apontador,"ADATSOLL")
        return f"Medidor {medidor} com código de retirado pelo leiturista desde {leitura}"
      apontador = apontador + 1
    return "Medidor *não* consta como retirado"
  def analisar(self, apontador=0, verificar_15_dias=False) -> bool:
    if(apontador == 0): return False
    if (self.session.findById("wnd[0]/usr/tabsTAB_STRIP_100/tabpF110/ssubSUB_100:SAPLZARC_DEBITOS_CCS_V2:0110/cntlCONTAINER_110/shellcont/shell").getCellValue(apontador, "STATUS") != "@5C@"): return False
    if(verificar_15_dias):
      vencimento = self.session.findById("wnd[0]/usr/tabsTAB_STRIP_100/tabpF110/ssubSUB_100:SAPLZARC_DEBITOS_CCS_V2:0110/cntlCONTAINER_110/shellcont/shell").getCellValue(apontador,"FAEDN")
      vencimento = datetime.datetime.strptime(vencimento, f"%d.%m.%Y").date()
      prazo_mais_15_dias = vencimento + datetime.timedelta(days=15)
      if (datetime.date.today() > prazo_mais_15_dias): return False
    return True
  def monitorar(self, qnt) -> str:
    while(len(listdir("C:\\Users\\ruan.camello\\Documents\\Temporario")) < qnt):
      time.sleep(3)
    return "\n".join(listdir("C:\\Users\\ruan.camello\\Documents\\Temporario"))

if __name__ == "__main__":
  if (len(sys.argv) < 3):
    raise Exception("Falta argumentos para relizar alguma ação!")
  if (len(sys.argv) > 4):
    raise Exception("Script não foi programado para essa quantidade de argumentos!")
  try:
    robo = sap() if (len(sys.argv) == 3) else sap(int(sys.argv[3]))
  except:
    raise Exception("ERRO: Não pode se conectar ao sistema SAP!")
  try:
    if ((sys.argv[1] == "coordenada") or (sys.argv[1] == "localização")):
      print(robo.coordenadas(int(sys.argv[2])))
    elif ((sys.argv[1] == "telefone") or (sys.argv[1] == "contato")):
      print(robo.telefone(int(sys.argv[2])))
    elif (sys.argv[1] == "medidor"):
      print(robo.medidor(int(sys.argv[2])))
    elif ((sys.argv[1] == "leiturista") or (sys.argv[1] == "roteiro")):
      print(robo.leiturista(int(sys.argv[2])))
    elif ((sys.argv[1] == "debito") or (sys.argv[1] == "fatura") or (sys.argv[1] == "débito")):
      print(robo.fatura_novo(int(sys.argv[2])))
    elif (sys.argv[1] == "relatorio"):
      robo.relatorio(int(sys.argv[2]))
    elif ((sys.argv[1] == "historico") or (sys.argv[1] == "histórico")):
      print(robo.historico(sys.argv[2]))
    elif (sys.argv[1] == "agrupamento"):
      print(robo.agrupamento(sys.argv[2]))
    elif (sys.argv[1] == "pendente"): #or (sys.argv[1] == "consulta")):
      print(robo.escrever(int(sys.argv[2])))
    elif (sys.argv[1] == "manobra"):
      print(robo.manobra(int(sys.argv[2])))
    elif (sys.argv[1] == "conecao"):
      print("Status: online")
    else:
      raise Exception("Não entendi o comando, verifique se está correto!")
  except Exception as erro:
    print(f"ERRO: {erro.args[0]}")