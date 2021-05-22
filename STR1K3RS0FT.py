import requests
import os
import time

def consult_CEP():
    def consult_cep():
        os.system("clear")
        print("\033[1;31mSeja bem vindo Painel by:STR1K3RS0FT×᷼×\033[0m")
        print("\033[1;33m--------------------------------------\033[0m")
        cep = input("\033[1;34mCEP>>> ")
        return cep

    def go_consult(cep):
        r = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep));data = r.json( )
        print("\n\n\033[32mconsulta realizada: ")
        print( )
        print('CEP: {} '.format(data['cep' ]))
        print('Logradoura: {}'.format(data['logradouro']))
        print('Cidade: {}'.format(data['bairro' ]))
        print('Localidade: {}'.format(data['localidade']))
        print('complemento: {}'.format(data['complemento']))
        print('Ibge: {}'.format(data['ibge' ]))
        print('Uf: {}'.format(data['uf' ]))
        print('DDD: {}'.format(data['ddd' ]))
        print('Gia: {}'.format(data['gia']))
        print('Siafi: {}'.format(data['siafi']))
        print( )

    cep = consult_cep()
    go_consult(cep)
    back = str(input("\n\033[0mnova consulta?[\033[32mS\033[0m/\033[31mN\033[0m]: "))

    while back == "s" or back == "S":
        cep = consult_cep()
        go_consult(cep)
        back = str(input("\n\033[0mnova consulta?[\033[32mS\033[0m/\033[31mN\033[0m]: "))

    return False


def consult_IP():
    def consult_ip():
        os.system('clear')
        print('\033[01;35mSeja Bem Vindo Consulta IP By:STR1K3RS0FT')
        print('\033[01;36m=========================================')
        ip = input('\033[01;34m>>> ')
        return ip

    def go_consult(ip):
        r = requests.get('http://ip-api.com/json/{}'.format(ip));data = r.json( )
        print('\033[01;33mConsulta Realizada!!')
        print( )
        print("IP: {}".format(data['query']))
        print("Status: {}".format(data['status']))
        print("País: {}".format(data['country']))
        print("Código_País: {}".format(data['countryCode']))
        print("Código_Região: {}".format(data['region']))
        print("Nome_Região: {}".format(data['regionName']))
        print("Cidade: {}".format(data['city']))
        print("Zip: {}".format(data['zip']))
        print("Lat: {}".format(data['lat']))
        print("Lon: {}".format(data['lon']))
        print("TimeZone: {}".format(data['timezone']))
        print("Isp: {}".format(data['isp']))
        print("Org: {}".format(data['org']))
        print("As: {}".format(data['as']))
        print("\033[01;32mby:T34M D@rkpr0j3ct.py\n")

    ip = consult_ip()
    go_consult(ip)
    back = str(input("\n\033[0mnova consulta?[\033[32mS\033[0m/\033[31mN\033[0m]: "))

    while back == "s" or back == "S":
        ip = consult_ip()
        go_consult(ip)
        back = str(input("\n\033[0mnova consulta?[\033[32mS\033[0m/\033[31mN\033[0m]: "))
        
    return False
    
        
def consult_ifo():
	print('\033[01;33mInformações do script')
	print('\033[01;31m>>>>©copyright2021<<<<')
	print('\033[01;34mCriado Do Script:')
	print('\033[01;32m---STR1K3RS0FT---')
	print('\033[01;34mObgd por ajuda na Script')
	print('\033[01;31m>>>@Dreifus-404/@MyDickXD<<<')
	print('\033[01;36mScript feita para consultas!! obgd pela ajuda @Dreifus-404/@MyDickXd tmj')
	print('\033[01;37mYT:Dreifus-404/YT:STR1KER S0FT')    
	print('\033[01;32mT34M d@rkpr0j3ct.py')  
	
	return False


def options_consult():
    while True:
        os.system("clear")
        print("\033[1;31mSeja bem vindo Painel by:STR1K3RS0FT×᷼×\033[0m"), print("\033[1;33m--------------------------------------\033[0m\n")
        print(">\033[34m01\033[0m Consultar\033[31m CEP\033[0m\n>\033[34m02\033[0m Consultar \033[31mIP\033[0m\n\033[0m>\033[34m03\033[0m Informações\033[31mScript\033[0m\n>\033[34m00\033[\ Sair\n")
        try:
            option = int(input("\033[0m: "))
            return option
        except ValueError:
            print("\033[31mdigite apenas numeros!!")
            time.sleep(1)

option = options_consult()

if option == 1:
    cond = consult_CEP()
    while cond == True:
        consult_CEP()

elif option == 2:
    cond = consult_IP()

    while cond == True:
        cond = consult_IP()
        
elif option == 3:
 	cond = consult_ifo()
 	
 	while cond == True:
 	    cond = consult_ifo()

elif option == 0:
    os.system("clear")
    print("\033[32mexit sucessfull!")
