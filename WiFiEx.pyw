# -*- Coding: UTF-8 -*-
# Python 3.X
# Windows
# WiFiEx

import datetime
import locale
import sys
import os

Version = "v1.2.4"
Autor = "LawlietJH"

#=======================================================================


# Función Que Comprueba si el SO es Windows, Devuelve TRUE/FALSE
def isWindows():
	
	osver = os.popen("ver").read()
	
	if osver.find("Windows") > 0: return True
	else: return False



def Pause(Quiet=True):
	
	if Quiet: os.system("Pause > Nul")
	else: os.syste("Pause")



#=======================================================================



def getESSIDs():
	
	global Redes
	
	ESSID = []
	
	Cadena = os.popen("netsh wlan show profiles").read()
	
	#~ print(Cadena)
	
	Cadena = Cadena.split("Perfil de todos los usuarios")
	
	for x in Cadena:
		
		if " " in x: x = x.replace(" ","á")
		if "¡" in x: x = x.replace("¡","í")
		if "¢" in x: x = x.replace("¢","ó")
		if "£" in x: x = x.replace("£","ú")
		
		x = x.replace("\n", "").strip().replace(": ", "").split("Perfiles de directiva de grupo")[0]
		ESSID.append(x)
	
	Redes["Interfaz"] = ESSID[:1]
	Redes["ESSID"] = ESSID[1:]



def getPass():
	
	global Redes
	
	Seguridad = ""
	Passwd = ""
	Seg = []
	Pwd = []
	
	for x in Redes["ESSID"]:
		
		Cadena = os.popen("netsh wlan show profiles name=" + x + " key=clear").read()
		
		if "Ç­­­" in Cadena: Cadena = Cadena.replace("Ç­", "á")
		if "Ç¸" in Cadena: Cadena = Cadena.replace("Ç¸", "é")
		if "Çð" in Cadena: Cadena = Cadena.replace("Çð", "í")
		if "Çü" in Cadena: Cadena = Cadena.replace("Çü", "ó")
		if "Ç§" in Cadena: Cadena = Cadena.replace("Ç§", "ú")
		if " " in Cadena: Cadena = Cadena.replace(" ","á")
		if "¡" in Cadena: Cadena = Cadena.replace("¡","í")
		if "¢" in Cadena: Cadena = Cadena.replace("¢","ó")
		if "£" in Cadena: Cadena = Cadena.replace("£","ú")
		
		Cadena = Cadena.split("Configuración de seguridad")[-1]
		Cadena = Cadena.split("Configuración de costos")[0]
		Cadena = Cadena.split("\n")[2:]
		
		for y in Cadena:
			
			if "Autenticación" in y: Seguridad = y.split("Autenticación")[-1]
			elif "Contenido de la clave" in y: Passwd = y.split("Contenido de la clave")[-1]
		
		Seguridad = Seguridad.strip().replace(": ", "").replace("-Personal", "").replace("Abierta","WEP")
		Passwd = Passwd.strip().replace(": ", "")
		
		Seg.append(Seguridad)
		Pwd.append(Passwd)
		
		Redes["SEG"] = Seg
		Redes["PWD"] = Pwd



def SavePasswd():
	
	global Redes
	
	Cont = len(Redes["ESSID"])
	Nombres = []
	Cad = ""
	xD = ""
	
	open("📶 Pass.ZioN","a")
	Eny = open("📶 Pass.ZioN","r+")
	
	Lineas = Eny.readlines()
	
	if Lineas == []: Eny.write("\n [+] Por: LawlietJH - WiFiEx "+Version)
	
	Usuario = os.popen("echo %UserName%").read().strip()
	
	dt = datetime.datetime.now()
	FH = dt.strftime(" %A %d de %B del %Y - %H:%M ").title()
	
	xD += "\n\n" + "\\"*62
	xD += "\n" + "/"*17 + " Nombre de Usuario: " + Usuario + " " + "/"*(23-len(Usuario)) + r"\\"
	xD += "\n" + "\\"*11 + FH + "\\"*(50-len(FH)) + "//"
	xD += "\n" + "/"*62 + "\n"
	
	Eny.write(xD)
	
	for x in Lineas:
		
		x = x.split("\n")[0]
		
		if "ESSID: " in x:
			
			x = x.split(": ")[1]
			Nombres.append(x)
	
	for x in range(Cont):
		
		Cad = "\n\t============================================" +\
				"\n\t [+] --------- ESSID: " + Redes["ESSID"][x] + " " + "-"*(20-len(Redes["ESSID"][x])) +\
				"\n\t  |  ---- Contraseña: " + Redes["PWD"][x] + " " + "-"*(20-len(Redes["PWD"][x])) +\
				"\n\t [+] ----- Seguridad: " + Redes["SEG"][x] + " " + "-"*(20-len(Redes["SEG"][x])) +\
				"\n\t============================================"
		
		Eny.write(Cad)
		
	Eny.close()



def Main():
	
	locale.setlocale(locale.LC_ALL, "esp")
	
	getESSIDs()
	getPass()
	SavePasswd()



Redes = {}



if __name__ == "__main__":
	
	if isWindows(): Main()
	else:
		print("\n\n\t Compatible Solo Con Windows.")
		Pause()

	
