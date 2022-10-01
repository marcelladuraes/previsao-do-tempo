import requests
import json
import sqlite3
import datetime

opcao = int(input('Você deseja realizar a busca por [1]-Cidade,UF ou [2]-Cidade?'))
if opcao == 1:
    cidade_uf = input('Informe a cidade e o estado [Padrão: Cidade, UF ]: ')
    requisicao = requests.get('https://api.hgbrasil.com/weather?key=4efea24f&city_name={}'.format(cidade_uf))
    localidade = json.loads(requisicao.text)
    #print(localidade)
    data_hora_consulta = datetime.datetime.now()
    temperatura = localidade['results']['temp']
    data =  localidade['results']['date']
    hora = localidade['results']['time']
    descricao_tempo_atual = localidade['results']['description']
    dia_noite = localidade['results']['currently']
    umidade = localidade['results']['humidity']
    velocidade_vento = localidade['results']['wind_speedy']
    nasce_sol = localidade['results']['sunrise']
    por_sol = localidade['results']['sunset']
    condicao_tempo_atual = localidade['results']['condition_slug']

    print('Temperatura atual em graus celsius: {}'.format(temperatura))
    print('Data: {}'.format(data)+' Hora: {}'.format(hora))
    print('Descrição do tempo atual: {}'.format(descricao_tempo_atual))
    print('Dia ou noite: {}'.format(dia_noite))
    print('Umidade: {}'.format(umidade))
    print('Velocidade do vento: {}'.format(velocidade_vento))
    print('Nascer do sol: {}'.format(nasce_sol)+' Pôr do sol: {}'.format(por_sol))
    print('Condição de tempo atual: {}'.format(condicao_tempo_atual))

    condicoes_semanais = json.loads(requisicao.text)
    #condicoes_semanais = list(requisicao.json())
    forecast = [condicoes_semanais['results']['forecast']]
    for p in forecast:
        print(p[0],p[1],p[2],p[3],p[4],p[5],p[6])
        #print('Temperaturas máximas semanal:')
        maximo = p[0]['max'],p[1]['max'],p[2]['max'],p[3]['max'],p[4]['max'],p[5]['max'],p[6]['max']
        #print(maximo)
        #print('Temperaturas mínimas semanal:')
        minimo = p[0]['min'],p[1]['min'],p[2]['min'],p[3]['min'],p[4]['min'],p[5]['min'],p[6]['min']
        #print(minimo)

    soma_maximo = 0
    soma_minimo = 0

    for p in forecast:
       soma_maximo = sum(maximo)
       #print(f'Soma das temperaturas máximas semanal: {soma_maximo}')

    for p in forecast:
        soma_minimo = sum(minimo)
        #print(f'Soma das temperaturas máximas semanal: {soma_minimo}')
    
    media_maximo = soma_maximo/7
    media_minimo = soma_minimo/7
    print(f'Média da temperatura máxima: {media_maximo}')
    print(f'Média da temperatura mínima: {media_minimo}')
  
elif opcao == 2:
    cidade = input('Informe a cidade: ')
    requisicao = requests.get('https://api.hgbrasil.com/weather?key=4efea24f&city_name={}'.format(cidade))
    localidade = json.loads(requisicao.text)
    #print(localidade)
    data_hora_consulta = datetime.datetime.now()
    temperatura = localidade['results']['temp']
    data =  localidade['results']['date']
    hora = localidade['results']['time']
    descricao_tempo_atual = localidade['results']['description']
    dia_noite = localidade['results']['currently']
    umidade = localidade['results']['humidity']
    velocidade_vento = localidade['results']['wind_speedy']
    nasce_sol = localidade['results']['sunrise']
    por_sol = localidade['results']['sunset']
    condicao_tempo_atual = localidade['results']['condition_slug']

    print('Temperatura atual em graus celsius: {}'.format(temperatura))
    print('Data: {}'.format(data)+' Hora: {}'.format(hora))
    print('Descrição do tempo atual: {}'.format(descricao_tempo_atual))
    print('Dia ou noite: {}'.format(dia_noite))
    print('Umidade: {}'.format(umidade))
    print('Velocidade do vento: {}'.format(velocidade_vento))
    print('Nascer do sol: {}'.format(nasce_sol)+' Pôr do sol: {}'.format(por_sol))
    print('Condição de tempo atual: {}'.format(condicao_tempo_atual))

    condicoes_semanais = json.loads(requisicao.text)
    #condicoes_semanais = list(requisicao.json())
    forecast = [condicoes_semanais['results']['forecast']]
    for p in forecast:
        print(p[0],p[1],p[2],p[3],p[4],p[5],p[6])
        #print('Temperaturas máximas semanal:')
        maximo = p[0]['max'],p[1]['max'],p[2]['max'],p[3]['max'],p[4]['max'],p[5]['max'],p[6]['max']
        #print(maximo)
        #print('Temperaturas mínimas semanal:')
        minimo = p[0]['min'],p[1]['min'],p[2]['min'],p[3]['min'],p[4]['min'],p[5]['min'],p[6]['min']
        #print(minimo)

    soma_maximo = 0
    soma_minimo = 0

    for p in forecast:
       soma_maximo = sum(maximo)
       #print(f'Soma das temperaturas máximas semanal: {soma_maximo}')

    for p in forecast:
        soma_minimo = sum(minimo)
        #print(f'Soma das temperaturas máximas semanal: {soma_minimo}')
    
    media_maximo = soma_maximo/7
    media_minimo = soma_minimo/7
    print(f'Média da temperatura máxima: {media_maximo}')
    print(f'Média da temperatura mínima: {media_minimo}')
    
   

conexao = sqlite3.connect('previsoes_tempo.db')
cursor = conexao.cursor()
#cursor.execute('CREATE TABLE previsao (data_hora_consulta text, temperatura, umidade, descricao_condicao_tempo, velocidade_vento)')
cursor.execute('INSERT INTO previsao (data_hora_consulta, temperatura, umidade, descricao_condicao_tempo, velocidade_vento) VALUES (?,?,?,?,?);', (data_hora_consulta, temperatura, umidade, descricao_tempo_atual, velocidade_vento))
conexao.commit()
cursor.execute("SELECT * FROM previsao")
print(cursor.fetchall())
