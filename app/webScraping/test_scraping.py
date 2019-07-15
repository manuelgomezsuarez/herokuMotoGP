# Python code to illustrate 
# inserting data in MongoDB 
from pymongo import MongoClient 
from pymongo import ASCENDING  
from pymongo import DESCENDING
from pymongo import collation
import unittest


try: 
    conn = MongoClient("localhost:27017",connect=False)
    print("Connected successfully!!!") 
except:   
    print("Could not connect to MongoDB")

# database 
db = conn.motoGP_db 
collectionCarreras = db.carreras
ano=2014
categoria="MotoGP"

class TestStringMethods(unittest.TestCase):
    
    def testDatabase(self):
        validaciones=[] #anoTemporada, categoriaTemporada,validacion
        cursorTemporadas = collectionCarreras.find({}).distinct("temporada");
        contadorTrue=0
        contadorFalse=0
        #cursorTemporadas=[2017,2018]
        for anoTemporada in cursorTemporadas:          
            if anoTemporada is not 2004:
                try:
                    cursorCategorias = collectionCarreras.find({"temporada":anoTemporada}).distinct("categoria");
                    for categoriaTemporada in cursorCategorias:              
                        primero=db.campeonatos.find({"temporada":anoTemporada,"categoria":categoriaTemporada}, {"puntos":1, "piloto":1,'_id':0}).sort("puntos",DESCENDING).collation({'locale':'es','numericOrdering':True})[0]
                        primer_piloto=(primero["piloto"])
                        primer_puntos=int(primero["puntos"])

                        cursorCarrerasPrimero=collectionCarreras.find({"temporada":anoTemporada,"categoria":categoriaTemporada,"piloto__icontains":primer_piloto}, {"puntos":1, '_id':0})
                        TotalPuntosPrimero=0;
                        for n in cursorCarrerasPrimero:
                            if n["puntos"] != '':
                                TotalPuntosPrimero=TotalPuntosPrimero+int((n["puntos"]))

                        quinto= db.campeonatos.find({"temporada":anoTemporada,"categoria":categoriaTemporada}, {"puntos":1, "piloto":1,'_id':0}).sort("puntos",DESCENDING).collation({'locale':'es','numericOrdering':True})[5]

                        quinto_piloto=(quinto["piloto"])
                        quinto_puntos=int(quinto["puntos"])

                        cursorCarrerasQuinto=collectionCarreras.find({"temporada":anoTemporada,"categoria":categoriaTemporada,"piloto__icontains":quinto_piloto}, {"puntos":1, '_id':0})
                        TotalPuntosQuinto=0;
                        for n in cursorCarrerasQuinto:
                            if n["puntos"] != '':
                                TotalPuntosQuinto=TotalPuntosQuinto+int((n["puntos"]))
                        if (TotalPuntosPrimero!=0) and primer_puntos != TotalPuntosPrimero:
                            validacion=False
                        elif(TotalPuntosQuinto!=0) and quinto_puntos != TotalPuntosQuinto:
                           validacion=False
                        else:
                            validacion=True
                        validaciones.append([anoTemporada,categoriaTemporada,validacion])
                except:
                    contadorFalse=contadorFalse+1
                    pass


        for check in validaciones:
            print(check)
            if check[2]==False:
                contadorFalse=contadorFalse+1
            if check[2]==True:
                contadorTrue=contadorTrue+1
        total=contadorTrue+contadorFalse
        porcentajeExito=(contadorTrue/total)*100
        print("Validaciones realizas: "+str(total))
        print("Validaciones exitosas: "+str(contadorTrue))
        print("validaciones fallidas: "+str(contadorFalse))
        print("Porcentaje de éxito: "+str(porcentajeExito))
        assert(porcentajeExito>90)

    

if __name__ == '__main__':
    unittest.main()

