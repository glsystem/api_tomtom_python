# Biblioteca de ajuda sobre a API https://www.twilio.com/docs/python/install
# Cadastre-se: www.twilio.com/referral/IYYIHw
from flask import Flask, render_template, request, Blueprint, jsonify
import requests
from geopy.geocoders import Nominatim

class TOMTOM:
    def __init__(self):
        # Your Account Sid and Auth Token from twilio.com/console
        self.__api_key = 'r81RuqjQVs1tOxkZS9v3FE0RdR0a8x0j'
        self.__geolocator = Nominatim(user_agent="Organic Shop")
        self.__apiURL= "https://api.tomtom.com/routing/1/calculateRoute/"
        self.__contextURL = "?computeBestOrder=false&&callback=Json&routeType=fastest&avoid=unpavedRoads&key=r81RuqjQVs1tOxkZS9v3FE0RdR0a8x0j"
        #HAS HTEMPORARIA

    def resolve_distancia(self, usuario_destino, usuario_distante):
        #criando um novo objeto da Classe Cliente do Twilio.
        destino = self.obtemLatitudeLongitude(usuario_destino)
        distante = self.obtemLatitudeLongitude(usuario_distante)
        if(distante != 'ERRO' and destino !='ERRO'):
            print('DESTINO')
            print(destino.latitude)
            print(destino.longitude)
            print('REMETENTE')
            print(distante.latitude)
            print(distante.longitude)
            tomtom_url = "%s,%s:%s,%s/json"%(str(destino.latitude), str(destino.longitude), str(distante.latitude), str(distante.longitude))
            url_final = self.__apiURL+tomtom_url+self.__contextURL
            print('\n URL FINAL')
            print(url_final)
            print('\n NOVO======')
            # print(url_final)
            dados = requests.get(url_final).json()
            km = int(dados['routes'][0]['summary']['lengthInMeters'])/1000
            # print(type(dados['routes'][0]['summary']['departureTime']))
            # print(dados['routes'][0]['summary']['arrivalTime'].strftime('%H:%M:%S - %m/%d/%Y'))
            return "%.2f KM"%(km)
        return 'ERRO'
        
    def obtemLatitudeLongitude(self, usuario):
        print(str(usuario.nome))
        print(str(usuario.numero))
        print(str(usuario.logradouro))
        print(str(usuario.cidade))
        print(str(usuario.bairro))
        print(str(usuario.estado))
        try:
            location = self.__geolocator.geocode(str(usuario.numero)+' '+str(usuario.logradouro)+' '+str(usuario.cidade))
            print(location.address)
            return location
        except Exception as e:
            try:
                # print('\n')
                # print(str(usuario.numero)+' '+str(usuario.logradouro)+' '+str(usuario.bairro))
                location = self.__geolocator.geocode(str(usuario.numero)+' '+str(usuario.logradouro)+' '+str(usuario.bairro))
                print(location.address)
                return location
            except Exception as e:
                try:
                    # print(str(usuario.numero)+' '+str(usuario.logradouro)+' '+str(usuario.estado))
                    location = self.__geolocator.geocode(str(usuario.numero)+' '+str(usuario.logradouro)+' '+str(usuario.estado))
                    print(location.address)
                    return location
                except Exception as e:
                    return 'ERRO'


#print(message.sid)
