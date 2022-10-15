import requests 
import time as t
import os
from colorama import Fore


if True:
    os.system("cls||clear")
    print("\033[32mCriado pelo canal: " + Fore.RED + "Jovem Dev")
    t.sleep(2)
    os.system("cls||clear")
    print("\033[32mMe chame no Whats:" + Fore.RED + "+55 (45) 99812-8850\n" + "\033[32mSiga no Instagram: " + Fore.RED + "@carvalho_ricarddo")
    t.sleep(5)
    os.system("clear||cls")
    print("\033[32m========================= DEV PRO =========================")
    t.sleep(0.5)
    print("\033[32mBY: " + Fore.RED + "Henrique")
    t.sleep(0.5)
    print("\033[32mYOUTUBE: " + Fore.RED + "Jovem Dev")
    t.sleep(0.5)
    print("\033[32mINSTAGRAM: " + Fore.RED + "@carvalho_ricarddo")
    t.sleep(0.5)
    print("\033[32mWHATSAPP: " + Fore.RED  + "+55 (45) 99812-8850")
    t.sleep(0.5)
    print("\033[32m===========================================================\n")
    t.sleep(0.5)
    print("Ideias bacanas?" + Fore.RED + "ENTRE EM CONTATO!!")
    t.sleep(2)
    c=1


while c == 1:
    os.system("clear||cls")
    print("\033[32m========================= DEV PRO =========================")
    print("\033[32mBY: " + Fore.RED + "Henrique")
    print("\033[32mYOUTUBE: " + Fore.RED + "Jovem Dev")
    print("\033[32mINSTAGRAM: " + Fore.RED + "@carvalho_ricarddo")
    print("\033[32mWHATSAPP: " + Fore.RED  + "+55 (45) 99812-8850")
    print("\033[32m===========================================================\n")

    esc = int(input("\033[32m[1] TELEFONE\n[2] CNPJ\n[3] CEP\n[4] IP\n[5] BIN\n[6] SAIR\n"))
    
    if (esc<1 or esc>6):
        os.system("clear||cls")
        print("DIGITE UMA OPÇÃO VÁLIDA!!")
        t.sleep(3)
    	
    if esc == 3:
        os.system("clear||cls")
        cep = int(input("\033[32mDIGITE UM CEP:\n"))	
        digitos_cep = len(str(cep))
    	

        if digitos_cep == 8:    
            consultar_cep = requests.get("https://viacep.com.br/ws/" + str(cep) + "/json")
            consultar_cep = consultar_cep.json()
            logradouro = consultar_cep['logradouro']
            bairro = consultar_cep['bairro']
            localidade = consultar_cep['localidade']
            uf = consultar_cep['uf']
            ddd = consultar_cep['ddd']
            ibge = consultar_cep['ibge']
            siafi = consultar_cep['siafi']
            complemento = consultar_cep['complemento']
            gia = consultar_cep['gia']

            os.system("clear||cls")
            print("\033[32mCEP CONSULTADO: " + Fore.RED + str(cep))
            print("\033[32mUF: " + Fore.RED + uf)
            print("\033[32mLocalidade: " + Fore.RED + localidade)
            print("\033[32mBairro: " + Fore.RED + bairro)
            print("\033[32mLogradouro: " + Fore.RED + logradouro)
            print("\033[32mDDD: " + Fore.RED + ddd)
            print("\033[32mIBGE: " + Fore.RED + ibge)
            print("\033[32mSIAFI: " + Fore.RED + siafi)
            print("\033[32mComplemento: " + Fore.RED + complemento)
            print("\033[32mGia: " + Fore.RED + gia)
            
            homes = int(input("\033[32m[1] Voltar ao menu inicial\n[2] Sair\n"))
            if homes == 2:
                c=0
                os.system("clear||cls")
                print(Fore.RED + "Saindo ...")
                t.sleep(1)

            if homes == 1:
                os.system("clear||cls")
                print(Fore.RED + "Voltando ...")
                t.sleep(1)
            
            if (homes<1 or homes>2):
                os.system("clear||cls")
                print(Fore.RED + "Digite uma opção válida!!")
                t.sleep(3)

        else:
            os.system("clear||cls")
            print(Fore.RED + "CEP INVÁLIDO!!\nRequer 8 digitos")
            t.sleep(5)

    if esc == 4:
        os.system("clear||cls")
        print(Fore.RED + "É PRECISO DIGITAR O IP COM OS PONTOS!!")
        ip = input("\033[32mDigite um IP:\n")

        consultar_ip = requests.get("http://ip-api.com/json/" + ip)
        consultar_ip = consultar_ip.json()

        status = consultar_ip['status']

        if status == "fail":
            os.system("clear||cls")
            print(Fore.RED + "DIGITE UM IP VÁLIDO!!")
            t.sleep(3)
        
        if status == "success":
            os.system("clear||cls")
            pais = consultar_ip['country']
            estado = consultar_ip['regionName']
            cidade = consultar_ip['city']
            latitude = consultar_ip['lat']
            longitude = consultar_ip['lon']
            fuso_horario = consultar_ip['timezone']
            isp = consultar_ip['isp']
            org = consultar_ip['org']
            cod_as = consultar_ip['as']

            print("\033[32mIP CONSULTADO:" + Fore.RED +  ip)
            print("\033[32mPaís: " + Fore.RED + pais)
            print("\033[32mEstado: " + Fore.RED + estado)
            print("\033[32mCidade: " + Fore.RED + cidade)
            print("\033[32mLatitude: " + Fore.RED + str(latitude))
            print("\033[32mLongitude: " + Fore.RED + str(longitude))
            print("\033[32mFuso-Horário: " + Fore.RED + fuso_horario)
            print("\033[32mFornecedor de Internet: " + Fore.RED + isp)
            print("\033[32mOrganização: " + Fore.RED + org)
            print("\033[32mCódigo \"AS\": " + Fore.RED + cod_as)

            homes = int(input("\033[32m[1] Voltar ao menu inicial\n[2] Sair\n"))
            if homes == 2:
                c=0
                os.system("clear||cls")
                print(Fore.RED + "Saindo ...")
                t.sleep(3)

            if homes == 1:
                os.system("clear||cls")
                print(Fore.RED + "Voltando ...")
                t.sleep(3)

    if esc == 5:
        os.system("clear||cls")
        bin = int(input("Digite uma BIN:\n"))
        digitos_bin = len(str(bin))
        
        if digitos_bin == 6:
            os.system("clear||cls")
            consultar_bin = requests.get("https://lookup.binlist.net/" + str(bin))
            consultar_bin = consultar_bin.json()
            bandeira = consultar_bin['scheme']
            tipo = consultar_bin['type']
            dados_banco = consultar_bin['bank']
            banco = dados_banco['name']
            nivel = consultar_bin['brand']
            dados_pais = consultar_bin['country']
            pais = dados_pais['name']
            moeda = dados_pais['currency']

            print("\033[32mBIN CONSULTADA:" + Fore.RED +  str(bin))
            print("\033[32mBanco: " + Fore.RED + banco)
            print("\033[32mBandeira: " + Fore.RED + bandeira)
            print("\033[32mNível: " + Fore.RED + nivel)
            print("\033[32mTipo: " + Fore.RED + tipo)
            print("\033[32mPaís: " + Fore.RED + pais)
            print("\033[32mMoeda: " + Fore.RED + moeda)

            homes = int(input("\033[32m[1] Voltar ao menu inicial\n[2] Sair\n"))
            if homes == 2:
                c=0
                os.system("clear||cls")
                print(Fore.RED + "Saindo ...")
                t.sleep(1)

            if homes == 1:
                os.system("clear||cls")
                print(Fore.RED + "Voltando ...")
                t.sleep(1)


        
        else:
            os.system("clear||cls")
            print(Fore.RED + "BIN INVÁLIDA!!\nRe 6 Digitos!!")
            t.sleep(3)

    if esc == 1:
        os.system("clear||cls")
        print(Fore.RED + "Não requer o \"+55\" somente o DDD e o número!!")
        print("\033[32mDigite um número:")
        telefone = int(input("\033[32m"))
        tel_digitos = len(str(telefone))
        tel_lista = list(str(telefone))
        digit1 = tel_lista[4]
        digit2 = tel_lista[5]
        t_o = digit1 + digit2
        t_o = int(t_o)
        ddd1 = tel_lista[0]
        ddd2 = tel_lista[1]
        ddd = ddd1 + ddd2
        ddd = int(ddd)
        

        if (tel_digitos>11 or tel_digitos<10 or ddd>99 or ddd<11):
            os.system("cls")
            print(Fore.RED + "DIGITE UM TELEFONE VÁLIDO!!")
            t.sleep(3)
        
        else:            

            if tel_digitos==10:
                tel_fixo = 1
            else:
                tel_fixo = 0

            if tel_fixo == 0:
                

                os.system("clear||cls")
                def obter_estado():
                    global estado
                    global ddd
                    if (ddd==53 or ddd==55 or ddd==51 or ddd==54):
                        estado = "RIO GRANDE DO SUL - RS"

                    if (ddd==49 or ddd==48 or ddd==47):
                        estado = "SANTA CATARINA - SC"

                    if (ddd==41 or ddd==42 or ddd==46 or ddd==43 or ddd==44 or ddd==45):
                        estado = "PARANÁ - PR"

                    if (ddd==13 or ddd==15 or ddd==14 or ddd==18 or ddd==11 or ddd==19 or ddd==16 or ddd==17 or ddd==12):
                        estado = "SÃO PAULO - SP"

                    if (ddd==24 or ddd==21 or ddd==22):
                        estado = "RIO DE JANEIRO - RJ"

                    if (ddd==28 or ddd==27):
                        estado = "ESPIRÍTO SANTO - ES"

                    if (ddd==35 or ddd==32 or ddd==34 or ddd==37 or ddd==31 or ddd==33 or ddd==38):
                        estado = "MINAS GERAIS - MG"

                    if (ddd==67):
                        estado = "MATO GROSSO DO SUL - MS"

                    if (ddd==65 or ddd==66):
                        estado = "MATO GROSSO DO NORTE - MT"

                    if (ddd==62 or ddd==64):
                        estado = "GOIÁS - GO"

                    if (ddd==61):
                        estado = "DISTRITO FEDERAL - DF"

                    if (ddd==73 or ddd==77 or ddd==71 or ddd==75 or ddd==74):
                        estado = "BAHIA - BA"
                    
                    if (ddd==63):
                        estado = "TOCANTINS - TO"
                    
                    if (ddd==69):
                        estado = "RONDÔNIA - RO"

                    if (ddd==68):
                        estado = "ACRE - AC"

                    if (ddd==79):
                        estado = "SERGIPE - SE"

                    if (ddd==82):
                        estado = "ALAGOAS - AL"

                    if (ddd==81 or ddd==87):
                        estado = "PERNAMBUCO - PE"

                    if (ddd==83):
                        estado = "PARAÍBA - PE"

                    if (ddd==84):
                        estado = "RIO GRANDE DO NORTE - RN"
                    
                    if (ddd==88 or ddd==85):
                        estado = "CEARÁ - CE"

                    if (ddd==89 or ddd==86):
                        estado = "PIAUÍ - PI"

                    if (ddd==99 or ddd==98):
                        estado = "MARANHÃO - MA"

                    if (ddd==94 or ddd==93 or ddd==91):
                        estado = "PARÁ - PA"

                    if (ddd==96):
                        estado = "AMAPÁ - AP"

                    if (ddd==92 or ddd==97):
                        estado = "AMAZONAS - AM"

                    if (ddd==95):
                        estado = "RORAIMA - RR"

                def obter_cidades():
                    global cidades
                    puxar_ddd = requests.get("https://brasilapi.com.br/api/ddd/v1/" + str(ddd))
                    puxar_ddd = puxar_ddd.json()
                    cidades = puxar_ddd['cities']
                
                obter_cidades()

                obter_estado()

                def parte_1():
                    global parte_um
                    parte = tel_lista[2]
                    parte2 = tel_lista[3]
                    parte3 = tel_lista[4]
                    parte4 = tel_lista[5]
                    parte5 = tel_lista[6]
                    parte_um = parte + parte2 + parte3 + parte4 + parte5

                def parte_2():
                    global parte_dois
                    parte = tel_lista[7]
                    parte2 = tel_lista[8]
                    parte3 = tel_lista[9]
                    parte4 = tel_lista[10]
                    parte_dois = parte + parte2 + parte3 + parte4

                parte_1()
                parte_2()
                

            
                print("\033[32mTELEFONE CONSULTADO: " + Fore.RED + "+55 (" + str(ddd) + ") " + str(parte_um) + "-" + str(parte_dois))
                print("\033[32mTelefone Fixo: " + Fore.RED +  "NÃO")
                print("\033[32mEstado: " + Fore.RED + estado)
                num_cidades = len(cidades)
                print(Fore.RED + str(num_cidades) + "\033[32m Possíveis Cidades:")
                for cidade in cidades:
                    print(Fore.RED + cidade)
                    
                homes = int(input("\033[32m[1] Voltar ao menu inicial\n[2] Sair\n"))
                if homes == 2:
                    c=0
                    os.system("clear||cls")
                    print(Fore.RED + "Saindo ...")
                    t.sleep(1)

                if homes == 1:
                    os.system("clear||cls")
                    print(Fore.RED + "Voltando ...")
                    t.sleep(1)

            if tel_fixo == 1:
                def obter_estado():
                    global estado
                    global ddd
                    if (ddd==53 or ddd==55 or ddd==51 or ddd==54):
                        estado = "RIO GRANDE DO SUL - RS"

                    if (ddd==49 or ddd==48 or ddd==47):
                        estado = "SANTA CATARINA - SC"

                    if (ddd==41 or ddd==42 or ddd==46 or ddd==43 or ddd==44 or ddd==45):
                        estado = "PARANÁ - PR"

                    if (ddd==13 or ddd==15 or ddd==14 or ddd==18 or ddd==11 or ddd==19 or ddd==16 or ddd==17 or ddd==12):
                        estado = "SÃO PAULO - SP"

                    if (ddd==24 or ddd==21 or ddd==22):
                        estado = "RIO DE JANEIRO - RJ"

                    if (ddd==28 or ddd==27):
                        estado = "ESPIRÍTO SANTO - ES"

                    if (ddd==35 or ddd==32 or ddd==34 or ddd==37 or ddd==31 or ddd==33 or ddd==38):
                        estado = "MINAS GERAIS - MG"

                    if (ddd==67):
                        estado = "MATO GROSSO DO SUL - MS"

                    if (ddd==65 or ddd==66):
                        estado = "MATO GROSSO DO NORTE - MT"

                    if (ddd==62 or ddd==64):
                        estado = "GOIÁS - GO"

                    if (ddd==61):
                        estado = "DISTRITO FEDERAL - DF"

                    if (ddd==73 or ddd==77 or ddd==71 or ddd==75 or ddd==74):
                        estado = "BAHIA - BA"
                    
                    if (ddd==63):
                        estado = "TOCANTINS - TO"
                    
                    if (ddd==69):
                        estado = "RONDÔNIA - RO"

                    if (ddd==68):
                        estado = "ACRE - AC"

                    if (ddd==79):
                        estado = "SERGIPE - SE"

                    if (ddd==82):
                        estado = "ALAGOAS - AL"

                    if (ddd==81 or ddd==87):
                        estado = "PERNAMBUCO - PE"

                    if (ddd==83):
                        estado = "PARAÍBA - PE"

                    if (ddd==84):
                        estado = "RIO GRANDE DO NORTE - RN"
                    
                    if (ddd==88 or ddd==85):
                        estado = "CEARÁ - CE"

                    if (ddd==89 or ddd==86):
                        estado = "PIAUÍ - PI"

                    if (ddd==99 or ddd==98):
                        estado = "MARANHÃO - MA"

                    if (ddd==94 or ddd==93 or ddd==91):
                        estado = "PARÁ - PA"

                    if (ddd==96):
                        estado = "AMAPÁ - AP"

                    if (ddd==92 or ddd==97):
                        estado = "AMAZONAS - AM"

                    if (ddd==95):
                        estado = "RORAIMA - RR"

                def obter_cidades():
                    global cidades
                    puxar_ddd = requests.get("https://brasilapi.com.br/api/ddd/v1/" + str(ddd))
                    puxar_ddd = puxar_ddd.json()
                    cidades = puxar_ddd['cities']
                
                obter_cidades()

                obter_estado()

                def parte_1():
                    global parte_um
                    parte = tel_lista[2]
                    parte2 = tel_lista[3]
                    parte3 = tel_lista[4]
                    parte4 = tel_lista[5]
                    parte_um = parte + parte2 + parte3 + parte4

                def parte_2():
                    global parte_dois
                    parte = tel_lista[6]
                    parte2 = tel_lista[7]
                    parte3 = tel_lista[8]
                    parte4 = tel_lista[9]
                    parte_dois = parte + parte2 + parte3 + parte4

                parte_1()
                parte_2()


                os.system("clear||cls")
                print("\033[32mTELEFONE CONSULTADO: " + Fore.RED + "+55 (" + str(ddd) + ") " + str(parte_um) + "-" + str(parte_dois))
                print("\033[32mTelefone Fixo: " + Fore.RED +  "SIM")
                print("\033[32mEstado: " + Fore.RED + estado)
                num_cidades = len(cidades)
                print(Fore.RED + str(num_cidades) + "\033[32m Possíveis Cidades:")
                for cidade in cidades:
                    print(Fore.RED + cidade)
                    
                homes = int(input("\033[32m[1] Voltar ao menu inicial\n[2] Sair\n"))
                if homes == 2:
                    c=0
                    os.system("clear||cls")
                    print(Fore.RED + "Saindo ...")
                    t.sleep(1)

                if homes == 1:
                    os.system("clear||cls")
                    print(Fore.RED + "Voltando ...")
                    t.sleep(1)
            
    if esc == 2:
        os.system("clear||cls")
        print(Fore.RED + "SOMENTE O NÚMERO!!")
        cnpj = int(input("\033[32mDigite um CNPJ:\n"))
        consulta_cnpj = requests.get("https://www.receitaws.com.br/v1/cnpj/" + str(cnpj))
        dados_cnpj = consulta_cnpj.json()
        status = dados_cnpj['status']

        if status == "ERROR":
            os.system("clear||cls")
            print(Fore.RED + "DIGITE UM CNPJ VÁLIDO!!")
            t.sleep(3)
        
        if status == "OK":
            cnpj_formatado = dados_cnpj['cnpj']
            fantasia = dados_cnpj['fantasia']
            porte = dados_cnpj['porte']
            tipo = dados_cnpj['tipo']
            abertura = dados_cnpj['abertura']
            situacao = dados_cnpj['situacao']
            natureza_juridica = dados_cnpj['natureza_juridica']
            capital_social = dados_cnpj['capital_social']
            email = dados_cnpj['email']
            telefone = dados_cnpj['telefone']
            uf = dados_cnpj['uf']
            municipio = dados_cnpj['municipio']
            bairro = dados_cnpj['bairro']
            logradouro = dados_cnpj['logradouro']
            numero = dados_cnpj['numero']
            complemento = dados_cnpj['complemento']
            cep = dados_cnpj['cep']
            data_situacao = dados_cnpj['data_situacao']
            ultima_atualizacao = dados_cnpj['ultima_atualizacao']

            os.system("clear||cls")
            print("\033[32mCNPJ CONSULTADO: " + Fore.RED + cnpj_formatado)
            print("\033[32mFantasia: " + Fore.RED + fantasia)
            print("\033[32mPorte: " + Fore.RED + porte)
            print("\033[32mTipo: " + Fore.RED + tipo)
            print("\033[32mAbertura: " + Fore.RED + abertura)
            print("\033[32mSituação: " + Fore.RED + situacao)
            print("\033[32mNATUREZA JURÍDICA" + Fore.RED + natureza_juridica)
            print("\033[32mCapital Social: " + Fore.RED + capital_social)
            print("\033[32mEmail: " + Fore.RED + email)
            print("\033[32mTelefone: " + Fore.RED + telefone)
            print("\033[32mUF: " + Fore.RED + uf)
            print("\033[32mMunicípio: " + Fore.RED + municipio)
            print("\033[32mBairro: " + Fore.RED + bairro)
            print("\033[32mRua: " + Fore.RED + logradouro)
            print("\033[32mNúmero: " + Fore.RED + numero)
            print("\033[32mComplemento: " + Fore.RED + complemento)
            print("\033[32mCEP: " + Fore.RED + cep)
            print("\033[32mData Situação: " + Fore.RED + data_situacao)
            print("\033[32mUltima Atualização: " + Fore.RED + ultima_atualizacao)

            homes = int(input("\033[32m[1] Voltar ao menu inicial\n[2] Sair\n"))
            if homes == 2:
                c=0
                os.system("clear||cls")
                print(Fore.RED + "Saindo ...")
                t.sleep(1)

            if homes == 1:
                os.system("clear||cls")
                print(Fore.RED + "Voltando ...")
                t.sleep(1)

    if esc == 6:
        os.system("clear||cls")
        print(Fore.RED + "Saindo ...")
        t.sleep(1)
        c=0