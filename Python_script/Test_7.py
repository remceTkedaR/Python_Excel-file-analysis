#  ------------------------------------------------------------
# Downloading data from a csv file (social survey file)
# Analysis of votes by age group. Saving the analysis
# results in a csv file. Result of votes cast and percentage share
# by Radosław Tecmer
# radek69tecmer@gmail.com
# 2023 -02-28 ( ok)
#  --------------------------------------------------------------
#


import csv
from csv import reader
from csv import DictReader
import numpy

pyt_1_grupa_1 = []
pyt_2_grupa_1 = []
pyt_3_grupa_1 = []
pyt_4_grupa_1 = []
pyt_5_grupa_1 = []
pyt_6_grupa_1 = []
pyt_7_grupa_1 = []
pyt_8_grupa_1 = []
pyt_9_grupa_1 = []
pyt_10_grupa_1 = []
pyt_11_grupa_1 = []
pyt_12_grupa_1 = []
pyt_13_grupa_1 = []
pyt_14_grupa_1 = []
pyt_15_grupa_1 = []

# Grupy respondentów
grupa_1 = "18-23 lat"
grupa_2 = "24-39 lat"
grupa_3 = "40-55 lat"

header_ask = [' narzędzi niezbędnych do wykonywania pracy i/lub właściwych warunków bhp','odpowiednich do Twoich potrzeb warunków socjalnych'
              'możliwości awansu i/lub przejrzystych warunków jego uzyskania', 'satysfakcjonującego wynagrodzenia i/lub przejrzystych zasad jego podwyżek',
              'szansy na rozwój osobisty wykraczający poza zajmowane stanowisko', 'możliwości udziału w szkoleniach rozwijających kwalifikacje na zajmowanym stanowisku',
              'bezpieczeństwa zatrudnienia, tj. stałej umowy o pracę', 'samodzielności w pracy adekwatnej do posiadanych kwalifikacji i doświadczenia',
              'dopasowanego do potrzeb systemu motywacyjnego', 'równowagi pomiędzy pracą a życiem osobistym (work life balance)',
              'przejrzystego systemu oceny pracy', 'równego traktowania pracowników (brak dyskryminacji i brak faworyzowania wybranych pracowników)',
              'regularnego otrzymywania informacji zwrotnych dotyczących oceny jakości pracy',
              'szacunku i poszanowania godności', 'dbałości o klimat sprzyjający zadowoleniu z pracy']

# lista dostępnych odpowiedzi
narzedzia_niezbedne = 'narzędzi niezbędnych do wykonywania pracy i/lub właściwych warunków bhp'
warunki_socjalne = 'odpowiednich do Twoich potrzeb warunków socjalnych'
mozliwosci_awansu = 'możliwości awansu i/lub przejrzystych warunków jego uzyskania'
satysfakcja_wynagraodzenia = 'satysfakcjonującego wynagrodzenia i/lub przejrzystych zasad jego podwyżek'
szansa_rozwoj ='szansy na rozwój osobisty wykraczający poza zajmowane stanowisko'
mozliwosc_udzialu = 'możliwości udziału w szkoleniach rozwijających kwalifikacje na zajmowanym stanowisku'
bezpieczenstwo_zatrudnienia = 'bezpieczeństwa zatrudnienia, tj. stałej umowy o pracę'
samodzielnosc = 'samodzielności w pracy adekwatnej do posiadanych kwalifikacji i doświadczenia'
dopasowany = 'dopasowanego do potrzeb systemu motywacyjnego'
rownowaga = 'równowagi pomiędzy pracą a życiem osobistym (work life balance)'
przejrzystosc = 'przejrzystego systemu oceny pracy'
rownego_traktowania = 'równego traktowania pracowników (brak dyskryminacji i brak faworyzowania wybranych pracowników)'
regularnego = 'regularnego otrzymywania informacji zwrotnych dotyczących oceny jakości pracy'
szatsunku = 'szacunku i poszanowania godności'
dbalosci = 'dbałości o klimat sprzyjający zadowoleniu z pracy'


def get_dates_header(one_file, encoding='utf-8'):
    # variable initiation
    header = []
    header_1 = []

    with open(one_file, 'r', newline='', encoding='utf-8') as the_file:
        reader = csv.reader(the_file)
        line_csv_dict = DictReader(the_file, delimiter=';')
        header_title = line_csv_dict.fieldnames
        for line in header_title:
            header_1.append(line)
            header = header_1
            header = header[0]
    the_file.close()
    return header

# header from file


header_title = (get_dates_header("../Pytanie_6_1.csv"))


# Grupa 1

def get_dates_answer_grup_1(one_file, header_ask,  grup_nb,  encoding='utf-8'):
    # variable initiation

    with open(one_file, 'r', newline='', encoding='utf-8') as the_file:

        csv_line_dict = DictReader(the_file)
        for line1 in csv_line_dict:
            if line1['Twój wiek?'] == grup_nb:
                #print(line1)
                pyt_1_grupa_1.append(line1[header_ask[0]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_2_grupa_1.append(line1[header_ask[1]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_3_grupa_1.append(line1[header_ask[2]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_4_grupa_1.append(line1[header_ask[3]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_5_grupa_1.append(line1[header_ask[4]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_6_grupa_1.append(line1[header_ask[5]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_7_grupa_1.append(line1[header_ask[6]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_8_grupa_1.append(line1[header_ask[7]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_9_grupa_1.append(line1[header_ask[8]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_10_grupa_1.append(line1[header_ask[9]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_11_grupa_1.append(line1[header_ask[10]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_12_grupa_1.append(line1[header_ask[11]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_13_grupa_1.append(line1[header_ask[12]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_14_grupa_1.append(line1[header_ask[13]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_15_grupa_1.append(line1[header_ask[14]])
    the_file.close()
    return


# get_dates_answer_grup_1('Pytanie_6_1.csv',header_ask, grupa_1)













