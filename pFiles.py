# Pfile file acces
ConfFile = "pFiles1.conf"
Version = "0.90 Alpha"

#imports:
import os, sys, re
from datetime import datetime
#from os import walk


#opdracht = "CV"
#opdracht = "LinkedIn"
#opdracht = "Motivatie"

#Declarations:
devider = "#"
deviderFull = " # "
geldigeParam = ["Reorder","reorder","Strip","strip", "Rebuild","rebuild","Rename","rename"]
#Conftype geeft type records in confurationfile
ConfType = ["pFiles.conf","Current Path:","Working Directories:","End"]
subject = []       #List voor lessen/onderwrpen
subjectdir =[]    #bijnehorende directory waar de files staan


#Lists for files and directories
files = []
dirnames = []
dirpaths = []
currentPath = ""
#LIsts for part of the filename (eg Reorder)
part0 = []
part1 = []
part2 = []
part3 = []
part4 = []
volgorde = []

###### CLS()
def cls(param): # Clearscreen en vast header (programname en datetime
    # param 0 geen actie, param 1 "hit any key"
    if param == 1:
        g = input("Hit any key")
    os.system('cls' if os.name=='nt' else 'clear')
    Header = "Pfile {:<50} {:<}\n"
    now = datetime.now()
    timestamp = now.strftime("%m/%d/%Y, %H:%M:%S")
    print (Header.format(Version, str(timestamp)))

        
def ConfLine(file,keyword,content): #Wegschrijven regel in bestand (config)
    confline = "{:<20} {:<}\n"
    file.write(confline.format(keyword, content))

def MakeConf(): #Aanmaken configfile
    print("makeConf")
    f = open(ConfFile,"w+")
    ConfLine(f,ConfFile, Version)
    ConfLine(f,"Current Path:",str(os.getcwd()))
    ConfLine(f,"Directories:",str(dirs))
    ConfLine(f,"Files",str(files))
    ConfLine(f,"testing","inhoud")
    f.close()

def ReadConf(): 
    f = open(ConfFile,"r")
    fl = f.readlines()
    for x in fl:
        firstPart = x[0:29].rstrip()
        secondPart = ""
        if len(x) > 30:
            secondPart = x[29:len(x)].rstrip()
        if firstPart in ConfType:
            Typesrt = firstPart
        if Typesrt == "pFiles.conf": 
            Version = secondPart
        elif Typesrt == "Current Path:":
            currentPath = secondPart
        elif Typesrt == "End":
            pass
        elif Typesrt == "Working Directories:" and firstPart == "Working Directories:":
            pass
        elif Typesrt == "Working Directories:":
            subject.append(firstPart)
            subjectdir.append(secondPart)
        
                

def AppendConf():
    f=open(ConfFile,"a+")
    for i in range(10):
        f.write("This is line %d\n" % (i+1))
    f.close()

###### STRIP
def Strip():
    mypath = os.getcwd()
    for (dirpath, dirnames, filenames) in os.walk(mypath):
        #files.extend(filenames)
        dirnames.extend(dirnames)
        break
    for x in dirnames:
        work = str(mypath)+"\\"+str(x)+ "\\"
        first = x.find(" - ")+ 3 # eerste ' - ' vinden + 3 prefix weglaten
        last = x.rfind(" - ") # laatste ' - ' vinden (datum)om af te splitsen
        renwork = str(mypath)+"\\"+ opdracht + deviderFull + str(x[first:last]) + deviderFull + str(x[last+3:])
        for (pathy, diry, filey) in os.walk(work):
            files.extend(filey)
            for filenm in filey:
                renamefile= str(work) + str(filenm)
                newname = str(renwork) + deviderFull + str(filenm)
                print ("renamefile" , renamefile)
                print ("newname" , newname)
                os.renames(renamefile,newname)
        files.clear()
    cls(1)

###### RESULTORDER
def ResultOrder(order):
    if order == "0":
        return(2)
    elif len(order)==3 and "1" in order and "2" in order and "3" in order:
        volgorde.clear()
        for i in range(3):
            volgorde.append(order[i])
        return(1)
    else:
        return(0)

###### SHOWPARTS    
def ShowParts():  
#def Reorder():
    # Opnieuw opbreken in delen van de filenaam en in nieuwe volgorde aan alekaar plakken (voor sorteringen)
    mypath = os.getcwd()
    for (dirpath, dirnames, filenames) in os.walk(mypath):
        files.extend(filenames)
        #dirnames.extend(dirnames)
        break
    for x in filenames:
        # check if filenaam has al least three sepertors (4 parts)
        if (len(x.split(deviderFull)) - 1) > 2:
            #save the original filename
            part0.append(x)
            tempX = x.split(deviderFull)
            #if there are more than 4 parts, concat the later ones.
            if len(tempX) > 6:
                tempX[5] = tempX[5] + deviderFull + tempX[6]
                tempX[6] = ""
            elif len(tempX) > 5:
                tempX[4] = tempX[4] + deviderFull + tempX[5]
                tempX[5] = ""
            elif len(tempX) > 4:
                tempX[3] = tempX[3] + deviderFull + tempX[4]
                tempX[4] = ""
            x1 = tempX[0]
            part1.append(tempX[0])
            part2.append(tempX[1])
            part3.append(tempX[2])
            part4.append(tempX[3])
    # if no found files than quit 
    if len(part0) < 1:
        return()
    #show al parts and the origional
    print ("")
   
    x = "{p1:<25} | {p2:<25} | {p3:<25} | {p4:<25}"
    print(x.format(p1="Part 1",p2="Part 2",p3="Part 3",p4=""))
    print ("")
 
    for i in range(len(part0)):
        print(x.format(p1=str(part1[i] [:25]),p2=str(part2[i] [:25]),p3=str(part3[i] [:25]),p4=str(part4[i] [:25])))
    print ("")
# op scherm stan nu de verschillende delen

###### REORDER
def ReOrder():
    ShowParts()
    #opvragen nieuwe volgord en wegschrijven filenaam in nieuwe vologord    
    order = ""
    while ResultOrder(order) == 0:
        order = input("Geef de nieuwe volgorde (Alleen cijfers 1, 2 en 3 aan elkaar vast, 0 voor geen actie): ")
    if order is not "0":
        for i in range(len(part0)):
            if volgorde[0] == "1":
                y = part1[i]
            elif volgorde[0] == "2":
                y = part2[i]
            elif volgorde[0] == "3":
                y = part3[i]
                
            if volgorde[1] == "1":
                y = y + deviderFull + part1[i]
            elif volgorde[1] == "2":
                y = y + deviderFull + part2[i]
            elif volgorde[1] == "3":
                y = y + deviderFull + part3[i]

            if volgorde[2] == "1":
                y = y + deviderFull + part1[i] + deviderFull + part4[i]
            elif volgorde[2] == "2":
                y = y + deviderFull + part2[i] + deviderFull + part4[i]
            elif volgorde[2] == "3":
                y = y + deviderFull + part3[i] + deviderFull + part4[i]
            #print (" old: ", part0[i])
            #print (" new: ", y)
            os.renames(part0[i],y)
        cls(1)

        
###### RENAME
def ReName():
    ShowParts()
    #opvragen kolomnummer en nieuwe tekst (of 0 voor geen wijziging)
    order = 0
    kolom = input("Geef nummer van de te wijzigen kolom (0 = geen wijziging): ")
    while order == 0:
        if kolom == "0" or kolom == "1" or kolom == "2" or kolom == "3":
            order = 1
        else:
            kolom = input("Geef nummer van de te wijzigen kolom (0 = geen wijziging): ")
    
    if kolom is not "0":
        newTekst = ""
        while newTekst == "":
            newTekst = input("Wat is de nieuwe tekst voor kolom " + kolom + " (spatie niet toegestaan): ")
        for i in range(len(part0)):
            if kolom == "1":
                y = newTekst + deviderFull + part2[i] + deviderFull + part3[i] + deviderFull + part4[i]
            elif kolom == "2":
                y = part1[i] + deviderFull + newTekst + deviderFull + part3[i] + deviderFull + part4[i]
            elif kolom == "3":
                y = part1[i] + deviderFull + part2[i] + deviderFull + newTekst + deviderFull + part4[i]
            os.renames(part0[i],y)
###### MAIN
if __name__== "__main__":
# Iteration over all arguments:
# Parse arguments Strip Sort Rebuild
    if len(sys.argv) > 1:
        if sys.argv[1] in geldigeParam:
            x = sys.argv[1]
            action = x.upper()
        else: #Default action is STRIP
            action = "STRIP"
    else:
        action = "STRIP"

    if len (sys.argv) > 2:  #Als tweede argument mag alleen devider medeegegeven worden.
        # tweede argument is de devider (1 positie)
        if len(sys.argv[2]) == 1:
            devider = sys.argv[2]
            deviderFull = " " + sys.argv[2] + " "
            
    
#    mypath = os.getcwd()
#    print (mypath)
#    cls(1)

    if action == "STRIP":
        opdracht = input("Welke opdracht ? ")
        Strip()
    elif action == "REORDER":
        ReOrder()
    elif action == "RENAME":
        ReName()
        
#    MakeConf()
#    cls(1)
#    ReadConf()
#    AppendConf()

#    cls(0)
#    ReadConf()
#    cls(1)

