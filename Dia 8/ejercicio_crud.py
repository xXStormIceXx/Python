#OPCIONAL : CREAR UN CRUD (CREACION,LECTURA,ACTUALIZACIÓN Y ELIMINACIÓN) DE LOS 3 CONJUNTOS DE DATOS ADENTRO DE DATA.JSON, LOS CUALES DEBEN SER PERSISTENTES DONDE APLIQUE.

import  json
import os

MY_DATABASE = ''  
def NewFile(*param):
    with open (MY_DATABASE,"w") as wf:
        json.dump(param[0],wf,indent=4)
        
        
        
def AddData(*param):
 with open(MY_DATABASE,"r+") as rwf:
    data_file=json.load(rwf)
    if(len(param)>1):
     data_file.update({  param[0]:param[1]})
    else:
     data_file.update({param[0]})
     rwf.seek(0)
     json.dump(data_file,rwf,indent=4)
     rwf.close()  
                    
                    
                    
def Eliminar(*param):
    data=list(param)
    data[1].pop(data[0])
    NewFile(data[1])
                        
                        
                        
def ReadFile():
    with open(MY_DATABASE,"r") as rf:
        return json.load(rf)
                            
                            
                            
def checkFile(*param):
    data = list(param)
    if(os.path.isfile(MY_DATABASE)):
     if(len(param)):
       data[0].update(ReadFile())
    else:
     if(len(param)):
       NewFile(data[0])
       
       
    
import importar.impordata as imp
general = "data/peliculas.json"
genero= "data/genero.json"
def NewFile(**param):
    with open(general,"w")as wf :
        json.dump(param,wf)
        
def NewFileG(**param):
    with open(genero,"w")as wfT :
        json.dump(param,wfT)