import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient 
import multiprocessing
import time
import datetime

def connectDB():
    try: 
        conn = MongoClient("localhost:27017",connect=False)
        print("Connected successfully!!!") 
    except:   
        print("Could not connect to MongoDB")

    # database 
    db = conn.motoGP_db
     
    # database 
    db = conn.motoGP_db 
    global collectionCampeonatos
    collectionCampeonatos = db.campeonatos

    global collectionCarreras
    collectionCarreras = db.carreras 

def getResumenMotosAnual():
    connectDB()
    campeonatosPorTemporadaOrder=collectionCarreras.aggregate([
                    { "$match": { "temporada":2019} },


        {
            "$project": {
                "temporada":"$temporada",
                "categoria":"$categoria",
                "moto":"$moto",
                "fecha":"$fecha",
                "puntos":"$puntos",
                "victorias":{  
                "$cond": [ { "$eq": ["$pos", 1 ] }, 1, 0]
            },
                "podios": {  
                "$cond": [ { "$in": [ "$pos", [1,2,3] ] }, 1, 0]
            },
            }
        },
        {
            "$group": {
                "_id": {"temporada":"$temporada","categoria":"$categoria","moto":"$moto"},
                "victorias":{"$sum":"$victorias"},
                "podios":{"$sum":"$podios"}



            }
        },
        {"$sort":{"_id.fecha":1,"id_categoria":1}},

    ])
    for n in campeonatosPorTemporadaOrder:
        print(n)


def getResumenPilotosAnual():
    connectDB()
    campeonatosPorTemporadaOrder=collectionCarreras.aggregate([
                    { "$match": { "temporada":2019} },


        {
            "$project": {
                "temporada":"$temporada",
                "categoria":"$categoria",
                "piloto":"$piloto",
                "fecha":"$fecha",
                "puntos":"$puntos",
                "victorias":{  
                "$cond": [ { "$eq": ["$pos", 1 ] }, 1, 0]
            },
                "podios": {  
                "$cond": [ { "$in": [ "$pos", [1,2,3] ] }, 1, 0]
            },
            }
        },
        {
            "$group": {
                "_id": {"temporada":"$temporada","categoria":"$categoria","piloto":"$piloto"},
                "victorias":{"$sum":"$victorias"},
                "podios":{"$sum":"$podios"}



            }
        },
        {"$sort":{"_id.fecha":1,"id_categoria":1}},

    ])


    listaTemporadas=list(campeonatosPorTemporadaOrder)
    for n in listaTemporadas:
        print(n)


    return None
#Para la vista de piloto: Circuito favorito

#3 piloto_record_puntos_campeonato= fields.StringField(required=False) Done
#3 pilotos_mas_temporadas_corriendo= fields.StringField(required=False) Done
#3 pilotos_mas_puntos_historia= fields.StringField(required=False)  Done
#3 motos_mas_victoriosas=fields.StringField(required=False) Done
#  nacionalidad_historica_pilotos=fields.ListField(required=False) Done
#  ultima_carrera_disputada=fields.StringField(required=False)
#  resumen_ultima_carrera_disputada=fields.ListField(required=False)

def getRecordPuntosPiloto():
    connectDB()
    recordPuntosCampeonato=collectionCampeonatos.aggregate([
        {
            "$project": {
                "piloto":"$piloto",
                "puntos":"$puntos"
            }
        },
        {
            "$group": {
                "_id": {"piloto":"$piloto",},
                "puntos":{"$sum":"$puntos"},
            }
        },
        {"$sort":{"puntos":-1,}},
        {"$limit":5},
    ])

    recordPuntosCampeonatoList=list(recordPuntosCampeonato)
    for t in recordPuntosCampeonatoList:
        print(t)




def getRecordPuntosPilotoCampeonato():
    connectDB()
    recordPuntosCampeonato=collectionCampeonatos.aggregate([



        {
            "$project": {
                "temporada":"$temporada",
                "piloto":"$piloto",
                "puntos":"$puntos"
            }
        },
        {
            "$group": {
                "_id": {"piloto":"$piloto","temporada":"$temporada"},
                "puntos":{"$max":"$puntos"},
            }
        },
        {"$sort":{"puntos":-1,}},
        {"$limit":5},

    ])

    recordPuntosCampeonatoList=list(recordPuntosCampeonato)
    for t in recordPuntosCampeonatoList:
        print(t)

def getRecordCampeonatosParticipados():
    connectDB()
    recordPuntosCampeonato=collectionCampeonatos.aggregate([



        {
            "$project": {
                "temporada":"$temporada",
                "piloto":"$piloto",
                "puntos":"$puntos"
            }
        },
        {
            "$group": {
                "_id": {"piloto":"$piloto"},
                "temporadas":{"$sum":1},

            }
        },
        {"$sort":{"temporadas":-1,}},
        {"$limit":5},

    ])

    recordPuntosCampeonatoList=list(recordPuntosCampeonato)
    for t in recordPuntosCampeonatoList:
        print(t)



def getNacionalidadPilotosUltimaTemporada():
    connectDB()
    recordPuntosCampeonato=collectionCampeonatos.aggregate([
        {"$match":{"temporada":2019}},


        {
            "$project": {
                "temporada":"$temporada",
                "categoria":"$categoria",
                "piloto":"$piloto",
                "pais":"$pais",

            }
        },

                {
            "$group": {
                "_id": {"temporada":"$temporada","categoria":"$categoria","pais":"$pais"},
                "suma":{"$sum":1},

            }
        },
               {"$sort":{"suma":-1,}},

        {
            "$group": {
                "_id": "$_id.categoria",
                "PaisGroup":{
                    "$push":{
                        "pais":"$_id.pais",
                        "suma":"$suma"
                        }
                    },
            }
        },
 

    ])

    recordPuntosCampeonatoList=list(recordPuntosCampeonato)
    for t in recordPuntosCampeonatoList:
        print(t)



def getMotoMasVictoriosaHistoria():
    connectDB()
    recordPuntosCampeonato=collectionCarreras.aggregate([
        {
            "$project": {
                "temporada":"$temporada",
                "moto":"$moto",
                "victorias":{  
                "$cond": [ { "$eq": ["$pos", 1 ] }, 1, 0]
            },
            }
        },
        {
            "$group": {
                "_id": {"moto":"$moto",},
                "victorias":{"$sum":"$victorias"},
            }
        },
        {"$sort":{"victorias":-1,}},
        {"$limit":3},

    ])

    recordPuntosCampeonatoList=list(recordPuntosCampeonato)
    for t in recordPuntosCampeonatoList:
        print(t)

def getUltimaFechaCarreraScrap():
    connectDB()
    carrerasPorFechaOrder=collectionCarreras.aggregate([
        {
            "$project": {
                "fecha":"$fecha",
                "temporada":"$temporada"
            }
        },



        {
            "$group": {
                "_id": {"fecha":"$fecha","temporada":"$temporada","titulo":"$titulo"}
            }
        },
        {"$sort":{"_id.fecha":-1}},
        {"$limit":1}

    ])
    listaCarrerasEscrapeada=list(carrerasPorFechaOrder)
    ultimaCarreraEscrapeada=listaCarrerasEscrapeada[0].get("_id").get("fecha")
    print(ultimaCarreraEscrapeada)



def getVitoriasPiloto():
    connectDB()
    carrerasPorFechaOrder=collectionCarreras.aggregate([
            {"$match":{"temporada":2019}},
            
        {
            "$project": {
                "temporada":"$temporada",
                "categoria":"$categoria",
                "piloto":"$piloto",
                "victorias":{  
                "$cond": [ { "$eq": ["$pos", 1 ] }, 1, 0]
            },
            }
        },

        {
            "$group": {
                "_id": {"piloto":"$piloto","categoria":"$categoria"},
               "victorias":{"$sum":"$victorias"},

            }
        },
        
               {"$sort":{"victorias":-1}},
        {
            "$group": {
                "_id": "$_id.categoria",
                "categoGroup":{
                    "$push":{
                        "piloto":"$_id.piloto",
                        "victorias":"$victorias"
                        }
                    },
            }
        },
        

      

    ])
    for n in carrerasPorFechaOrder:
        print(n)


#getResumenMotosAnual()
#getResumenPilotosAnual()
#getRecordPuntosPiloto()
#getRecordPuntosPilotoCampeonato()
#getRecordCampeonatosParticipados()
#getNacionalidadPilotosUltimaTemporada()
getVitoriasPiloto()
#getMotoMasVictoriosaHistoria()
#getUltimaFechaCarreraScrap()