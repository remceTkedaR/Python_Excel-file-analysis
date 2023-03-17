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
pyt_16_grupa_1 = []

pyt_1_grupa_2 = []
pyt_2_grupa_2 = []
pyt_3_grupa_2 = []
pyt_4_grupa_2 = []
pyt_5_grupa_2 = []
pyt_6_grupa_2 = []
pyt_7_grupa_2 = []
pyt_8_grupa_2 = []
pyt_9_grupa_2 = []
pyt_10_grupa_2 = []
pyt_11_grupa_2 = []
pyt_12_grupa_2 = []
pyt_13_grupa_2 = []
pyt_14_grupa_2 = []
pyt_15_grupa_2 = []
pyt_16_grupa_2 = []

pyt_1_grupa_3 = []
pyt_2_grupa_3 = []
pyt_3_grupa_3 = []
pyt_4_grupa_3 = []
pyt_5_grupa_3 = []
pyt_6_grupa_3 = []
pyt_7_grupa_3 = []
pyt_8_grupa_3 = []
pyt_9_grupa_3 = []
pyt_10_grupa_3 = []
pyt_11_grupa_3 = []
pyt_12_grupa_3 = []
pyt_13_grupa_3 = []
pyt_14_grupa_3 = []
pyt_15_grupa_3 = []
pyt_16_grupa_3 = []

size_grup_1 = 15
size_grup_2 = 42
size_grup_3 = 37


grupa_1 = "18-23 lat"
grupa_2 = "24-39 lat"
grupa_3 = "40-55 lat"



def get_dates_header(one_file, encoding='utf-8'):
    # variable initiation
    header = []
    header_1 = []

    with open(one_file, 'r', newline='', encoding='utf-8') as the_file:
        reader = csv.reader(the_file, delimiter=',')
        line_csv_dict = DictReader(the_file)
        header_title = line_csv_dict.fieldnames
        for line in header_title:
            header_1.append(line)
            header = header_1[1:]
    the_file.close()
    return header

# header from file


header_ask = (get_dates_header("../Pytanie_9_1.csv"))

# Grupa 1

def get_dates_answer_grup_1(one_file, header_ask, grup_nb,  encoding='utf-8'):
    # variable initiation

    with open(one_file, 'r', newline='', encoding='utf-8') as the_file:

        csv_line_dict = DictReader(the_file)
        for line1 in csv_line_dict:
            print(line1)
            if line1[' Twój wiek?'] == grup_nb:
                pyt_1_grupa_1.append(line1[header_ask[0]])


    the_file.close()
    return

# Grupa 2


def get_dates_answer_grup_2(one_file, header_ask, grup_nb, encoding='utf-8'):
    # variable initiation

    with open(one_file, 'r', newline='', encoding='utf-8') as the_file:

        csv_line_dict = DictReader(the_file)
        for line2 in csv_line_dict:

            if line2[' Twój wiek?'] == grup_nb:
                pyt_1_grupa_2.append(line2[header_ask[0]])


    the_file.close()
    return

# Grupa 3


def get_dates_answer_grup_3(one_file, header_ask, grup_nb, encoding='utf-8'):
    # variable initiation

    with open(one_file, 'r', newline='', encoding='utf-8') as the_file:

        csv_line_dict = DictReader(the_file)
        for line3 in csv_line_dict:

            if line3[' Twój wiek?'] == grup_nb:
                pyt_1_grupa_3.append(line3[header_ask[0]])


    the_file.close()
    return

# Przetwarzanie danych dla wszystkich grup


def question_grup(question_number, nb_qustion, grupa_nb, header=[]):
    #---
    # lista dostępnych odpowiedzi
    label_yes = 'Tak (przejdź do pytania 11)'
    label_no = 'Nie'

    liczba_tak = 0
    liczba_nie = 0

    size_grup_1 = 15
    size_grup_2 = 42
    size_grup_3 = 37

    tak_procent = 0
    nie_procent = 0

    my_grupa_1 = "18-23 lat"
    my_grupa_2 = "24-39 lat"
    my_grupa_3 = "40-55 lat"

    if grupa_nb == my_grupa_1:
        size_grup_nb = size_grup_1
    if grupa_nb == my_grupa_2:
        size_grup_nb = size_grup_2
    if grupa_nb == my_grupa_3:
        size_grup_nb = size_grup_3

    l_range = len(question_number)

    for x in range(l_range):
        tak_tak = (question_number[x].count(label_yes))
        nie_nie = (question_number[x].count(label_no))

        # Suma wystąpień TAK
        liczba_tak = tak_tak + liczba_tak
        liczba_nie = nie_nie + liczba_nie

        # calculation "%"
        tak_procent = ((liczba_tak * 100) / size_grup_nb)
        tak_procent = '%-.2f' % tak_procent

        nie_procent = ((liczba_nie * 100) / size_grup_nb)
        nie_procent = '%-.2f' % nie_procent

    print(header)
    row_0 = (header)
    print('Grupa ', grupa_nb, ' = ', liczba_tak, '-- TAK--', '-', tak_procent, '%')
    row_1 = ('Grupa ', grupa_nb, ' = ', liczba_tak, '-- TAK--', '-', tak_procent, '%')
    print('Grupa ', grupa_nb, ' = ', liczba_nie, '-- NIE--', '-', nie_procent, '%')
    row_2 = ('Grupa ', grupa_nb, ' = ', liczba_nie, '-- NIE--', '-', nie_procent, '%')

    row_3 = ('Liczba respondentów = ', size_grup_nb,)
    file_out = []
    b = nb_qustion
    filename = str('number9_' + str(b) + ' _Grupa- ' + grupa_nb + '.csv')
    # file_out.append(row_0)
    file_out.append(row_1)
    file_out.append(row_2)
    file_out.append(row_3)
    f = open(filename, 'w')

    with f:
        fnames = [row_0]
        writer = csv.DictWriter(f, fieldnames = fnames)
        writer.writeheader()
        writer = csv.writer(f)
        writer.writerows(file_out)

    return file_out


get_dates_answer_grup_1('../Pytanie_9_1.csv', header_ask, grupa_1)

question_grup(pyt_1_grupa_1, 1, grupa_1, header_ask[0])


# -------- Grupa 2
get_dates_answer_grup_2('../Pytanie_9_1.csv', header_ask, grupa_2)

question_grup(pyt_1_grupa_2, 1, grupa_2, header_ask[0])


# -------- Grupa 3
get_dates_answer_grup_3('../Pytanie_9_1.csv', header_ask, grupa_3)

question_grup(pyt_1_grupa_3, 1, grupa_3, header_ask[0])

















