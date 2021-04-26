import re
import dicionario
from datetime import datetime

def whriteInLog(log, li_num):
  arquivo = open("log_programa.txt", "a")
  arquivo.write(" -> line ")
  arquivo.write(str(li_num))
  arquivo.write(": ")
  arquivo.write(log)  
  return arquivo.write("\n")
  arquivo.close()

def whriteInLogF(log, li_num, result):
  arquivo = open("log_programa.txt", "a")
  arquivo.write(" -> line ")
  arquivo.write(str(li_num))
  arquivo.write(": ")
  arquivo.write(log)  
  arquivo.write(" - ")
  arquivo.write(result)
  return arquivo.write("\n")
  arquivo.close()

def dateTimeInLog():
  now = datetime.now()
  arquivo = open("log_programa.txt", "a")
  arquivo.write("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
  arquivo.write("Date: ")
  arquivo.write(str(now.day))
  arquivo.write("-")
  arquivo.write(str(now.month))
  arquivo.write("-")
  arquivo.write(str(now.year))
  arquivo.write(" -- Time: ")
  arquivo.write(str(now.hour))
  arquivo.write(":")
  arquivo.write(str(now.minute))
  arquivo.write(":")
  arquivo.write(str(now.second))
  arquivo.write("\n")
  arquivo.close()

# Abre o arquivo txt e percorre seu conteúdo. O With faz com que 
# o arquivo seja fechado sozinho depois do uso
dateTimeInLog()
with open('programa_fonte.txt') as f:
  for l_num, l in enumerate(f, 1): # percorrer linhas e enumera-las a partir de 1

    # Testa os caracteres para verificar a ação das linhas
    # e chama a função que escreve o retorno em um arquivo de log chamado log_programa.txt
    if dicionario.tk01 in l:
       whriteInLog(dicionario.log001, l_num)
    if dicionario.tk02 in l:
       whriteInLog(dicionario.log002, l_num)
    if dicionario.tk03 in l:
      whriteInLog(dicionario.log003, l_num)
    if dicionario.tk04 in l:
      whriteInLog(dicionario.log004, l_num)
    if dicionario.tk05 in l:
      whriteInLog(dicionario.log005, l_num)
    if dicionario.tk06 in l:
      whriteInLog(dicionario.log006, l_num)
    if dicionario.tk07 in l:
      whriteInLog(dicionario.log007, l_num)
    if dicionario.tk08 in l:
      whriteInLog(dicionario.log008, l_num)
    if dicionario.tk09 in l:
      whriteInLog(dicionario.log009, l_num)
    if dicionario.tk10 in l:
      whriteInLog(dicionario.log010, l_num)
    if dicionario.tk11 in l:
      whriteInLog(dicionario.log011, l_num)
    if dicionario.tk12 in l:
      whriteInLog(dicionario.log012, l_num)
    if dicionario.tk13 in l:
      whriteInLog(dicionario.log013, l_num)
    if dicionario.tk14 in l:
      whriteInLog(dicionario.log014, l_num)
    if dicionario.tk15 in l:
      whriteInLog(dicionario.log015, l_num)
    if dicionario.tk16 in l:
      whriteInLog(dicionario.log016, l_num)
    if dicionario.tk17 in l:
      whriteInLog(dicionario.log017, l_num)
    if dicionario.tk18 in l:
      whriteInLog(dicionario.log018, l_num)
    if dicionario.tk19 in l:
      whriteInLog(dicionario.log019, l_num)
    if dicionario.tk20 in l:
      whriteInLog(dicionario.log020, l_num)
    if dicionario.tk21 in l:
      whriteInLog(dicionario.log021, l_num)
    if dicionario.tk22 in l:
      whriteInLog(dicionario.log022, l_num)
    if dicionario.tk23 in l:
      whriteInLog(dicionario.log023, l_num)
    if dicionario.tk24 in l:
      whriteInLog(dicionario.log024, l_num)
    if dicionario.tk25 in l:
      whriteInLog(dicionario.log025, l_num)
    if dicionario.tk26 in l:
      whriteInLog(dicionario.log026, l_num)
    if dicionario.tk27 in l:
      whriteInLog(dicionario.log027, l_num)
    if dicionario.tk28 in l:
      whriteInLog(dicionario.log028, l_num)
    if dicionario.tk29 in l:
      result = re.findall(r'def \w+',l)
      whriteInLogF(dicionario.log029, l_num, str(result))        
    if dicionario.tk30 in l:
      whriteInLog(dicionario.log030, l_num)
    if dicionario.tk31 in l:
      whriteInLog(dicionario.log031, l_num)
    if dicionario.tk32 in l:
      whriteInLog(dicionario.log032, l_num)
    if dicionario.tk33 in l:
      whriteInLog(dicionario.log033, l_num)
 
    