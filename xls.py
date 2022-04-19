#!/usr/bin/python
# coding: utf8

import win32com.client

class xls:
  def __init__(self):
    self.excel = win32com.client.gencache.EnsureDispatch('Excel.Application')
    self.excel.Visible = True
  def inicia(self):
    self.wb = self.excel.Workbooks.Add()
    self.ws1 = self.wb.Worksheets('Planilha1')
    self.ws1.Name = 'DEBITOS'
    cabecalho = list(['Ano/Mes', 'Vencimento', 'Valor', 'Tipo'])
    self.ws1.Range(self.ws1.Cells(1,1),self.ws1.Cells(1,4)).Value = cabecalho
    self.wb.Worksheets.Add()
    self.ws2 = self.wb.Worksheets('Planilha2')
    self.ws2.Name = 'LEITURISTA'
    cabecalho = list(['Seq', 'Endereço', 'Bairro', 'Medidor', 'Hora', 'Cod'])
    self.ws2.Range(self.ws2.Cells(1,1),self.ws2.Cells(1,6)).Value = cabecalho
    # print(dir(self.ws1))
  def debito(self, arg):
    self.ws1.Select()
  def leitura(self, arg):
    self.ws2.Select()
    conteudo = arg.split(':')
    a = 2
    for c in conteudo:
      if c == ';':
        a =+ 1
      self.ws2.Range(self.ws2.Cells(a,c),self.ws2.Cells(a,c)).Copy()
a = xls()
a.inicia()