import requests
import re
import os
import time
from bs4 import BeautifulSoup

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"


def pegarUrl():
    while True:
        os.system('clear')
        var = input('Escolha uma das Opções de Busca no Workana abaixo: \n\nTI e Programação: \n [1] - Programação \n [2] - Web Design \n [3] - Data Science \n\nDesign e Multimedia: \n [4] - Web Design \n [5] - Landing Page \n\n')

        if(var == '1'):
            var = 'https://www.workana.com/jobs?category=it-programming&language=pt&subcategory=web-development'
            break
        elif(var == '2'):
            var = 'https://www.workana.com/jobs?category=it-programming&language=pt&subcategory=web-design'
            break
        elif(var == '3'):
            var = 'https://www.workana.com/jobs?category=it-programming&language=pt&subcategory=data-science-1'
            break
        elif(var == '4'):
            var = 'https://www.workana.com/jobs?category=design-multimedia&language=pt&subcategory=web-design-1'
            break
        elif(var == '5'):
            var = 'https://www.workana.com/jobs?category=design-multimedia&language=pt&subcategory=landing-page'
            break
        else:
            print('\nOpção Inválida!')
            time.sleep(1)

    return var

def listaTrabalhos(var):
    response = requests.get(var)
    site = BeautifulSoup(response.text, 'html.parser')
    trabalhos = site.findAll('div', attrs={'class': 'project-item'})

    os.system('clear')

    return trabalhos

def imprimirTrabalhos(trab):
    for trabalho in trab:
        titulo =  trabalho.find('h2', attrs={'class': 'project-title'})
        horario = trabalho.find('span', attrs={'class': 'date'})
        autor = trabalho.find('span', attrs={'class': 'author-info'})
        detalhes = trabalho.find('div', attrs={'class': 'expander'})
        valor = trabalho.find('span', attrs={'class': 'values'})

        detalhes = detalhes.text

        perguntas = ['Categoria', 'Subcategoria', 'Do que você precisa',
                    'Isso é um projeto ou uma posição de trabalho', 'Disponibilidade requerida',
                    'Integrações de API', 'Necesidad específica', 'Necesidade específica',
                    'Funções necessárias', 'Tenho, atualmente', 'Qual é o alcance do projeto',
                    'Tamanho do projeto']

        detalhes = re.sub(perguntas[0], '\n' + perguntas[0], detalhes)

        for i in range(0, len(perguntas)):
            detalhes = re.sub(perguntas[i], '\n' + BOLD + perguntas[i] + GREEN, detalhes)

        print(RED + '========================================================================================' + RESET)
        print(BLUE + titulo.text + BOLD)
        print(BOLD + 'Valor: ' + GREEN + valor.text + RESET)
        print(horario.text)
        print(autor.text, '\n' + CYAN)
        print(detalhes, '\n\n\n' + RESET)

def buscarTrabalhos():
    while True:
        url = pegarUrl()
        trabalhos = listaTrabalhos(url)
        imprimirTrabalhos(trabalhos)

        cont = input('Pressione Enter para realizar uma nova busca. Caso contrário digite qualquer coisa\n')
        if(cont == ''):
            cont = ''
        else:
            break

if __name__ == '__main__':
    buscarTrabalhos()