
#  ----------------------------------------------------------------
# Downloading data from a csv file (social survey file)
# Analysis of votes by age group. Saving the analysis
# results in a csv file. Result of votes cast and percentage share
# by Radosław Tecmer
# radek69tecmer@gmail.com
# 2023 -02-28 ( ok)
# -------------------------------------------------------------------
#

import csv
from csv import reader
from csv import DictReader
import numpy
import matplotlib

pyt_1_grupa_1 = []
pyt_2_grupa_1 = []
pyt_3_grupa_1 = []

pyt_1_grupa_2 = []
pyt_2_grupa_2 = []
pyt_3_grupa_2 = []

pyt_1_grupa_3 = []
pyt_2_grupa_3 = []
pyt_3_grupa_3 = []


grupa_1 = "18-23 lat"
grupa_2 = "24-39 lat"
grupa_3 = "40-55 lat"


# lista dostępnych odpowiedzi
zdecydowanie_zgadzam_się = 'zdecydowanie zgadzam się'
raczej_zgadzam_się = 'raczej zgadzam się'
raczej_się_nie_gadzam = 'raczej się nie zgadzam'
trudno_powiedzieć = 'trudno powiedzieć'


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


header_ask = (get_dates_header("Pytanie_15_1.csv"))

# Grupa 1


def get_dates_answer_grup_1(one_file, header_ask, grup_nb,  encoding='utf-8'):
    # variable initiation

    with open(one_file, 'r', newline='', encoding='utf-8') as the_file:

        csv_line_dict = DictReader(the_file)
        for line1 in csv_line_dict:
            if line1['Twój wiek?'] == grup_nb:
                pyt_1_grupa_1.append(line1[header_ask[0]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_2_grupa_1.append(line1[header_ask[1]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_3_grupa_1.append(line1[header_ask[2]])
    the_file.close()
    return

# Grupa 2


def get_dates_answer_grup_2(one_file, header_ask, grup_nb, encoding='utf-8'):
    # variable initiation

    with open(one_file, 'r', newline='', encoding='utf-8') as the_file:

        csv_line_dict = DictReader(the_file)
        for line1 in csv_line_dict:
            if line1['Twój wiek?'] == grup_nb:
                pyt_1_grupa_2.append(line1[header_ask[0]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_2_grupa_2.append(line1[header_ask[1]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_3_grupa_2.append(line1[header_ask[2]])
    the_file.close()
    return

# Grupa 3


def get_dates_answer_grup_3(one_file, header_ask, grup_nb, encoding='utf-8'):
    # variable initiation

    with open(one_file, 'r', newline='', encoding='utf-8') as the_file:

        csv_line_dict = DictReader(the_file)
        for line1 in csv_line_dict:
            if line1['Twój wiek?'] == grup_nb:
                pyt_1_grupa_3.append(line1[header_ask[0]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_2_grupa_3.append(line1[header_ask[1]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_3_grupa_3.append(line1[header_ask[2]])
    the_file.close()
    return

# Przetwarzanie danych dla wszystkich grup


def question_grup(question_number, nb_qustion, grupa_nb, header=[]):
    #---
    zdecydowanie_zgadzam_suma_grupa = 0
    raczej_zgadzam_suma_grupa = 0
    raczej_sie_niezgadzam_suma_grupa = 0
    trudno_powiedziec_suma_grupa = 0

    size_grup_1 = 15
    size_grup_2 = 42
    size_grup_3 = 37

    z_t_proc_grup_1 = 0
    r_n_proc_grup_1 = 0
    r_t_proc_grup_1 = 0
    t_p_proc_grup_1 = 0
    z_n_proc_grup_1 = 0

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
        z_t = (question_number[x].count(zdecydowanie_zgadzam_się))
        r_t = (question_number[x].count(raczej_zgadzam_się))
        r_n = (question_number[x].count(raczej_się_nie_gadzam))
        t_p = (question_number[x].count(trudno_powiedzieć))

        zdecydowanie_zgadzam_suma_grupa = z_t + zdecydowanie_zgadzam_suma_grupa
        raczej_sie_niezgadzam_suma_grupa = r_n + raczej_sie_niezgadzam_suma_grupa
        raczej_zgadzam_suma_grupa = r_t + raczej_zgadzam_suma_grupa
        trudno_powiedziec_suma_grupa = t_p + trudno_powiedziec_suma_grupa

        # calculation "%"
        z_t_proc_grup_1 = ((zdecydowanie_zgadzam_suma_grupa * 100)/size_grup_nb)
        z_t_proc_grup_1 = '%-.2f' % z_t_proc_grup_1
        r_n_proc_grup_1 = ((raczej_sie_niezgadzam_suma_grupa * 100) / size_grup_nb)
        r_n_proc_grup_1 = '%-.2f' % r_n_proc_grup_1
        r_t_proc_grup_1 = ((raczej_zgadzam_suma_grupa * 100) / size_grup_nb)
        r_t_proc_grup_1 = '%-.2f' % r_t_proc_grup_1
        t_p_proc_grup_1 = ((trudno_powiedziec_suma_grupa * 100) / size_grup_nb)
        t_p_proc_grup_1 = '%-.2f' % t_p_proc_grup_1

    print(header)
    row_0 = (header)
    print('Grupa ', grupa_nb, ' = ', zdecydowanie_zgadzam_suma_grupa, ' - zdecydowanie zgadzam się', '-', z_t_proc_grup_1, '%')
    row_1 = ('Grupa ', grupa_nb, ' = ', zdecydowanie_zgadzam_suma_grupa, ' - zdecydowanie zgadzam się', '-', z_t_proc_grup_1, '%')
    print('Grupa ', grupa_nb, ' = ', raczej_sie_niezgadzam_suma_grupa, ' - raczej się nie zgadzam',  '-', r_n_proc_grup_1, '%')
    row_2 = ('Grupa ', grupa_nb, ' = ', raczej_sie_niezgadzam_suma_grupa, ' - raczej się nie zgadzam',  '-', r_n_proc_grup_1, '%')
    print('Grupa ', grupa_nb, ' = ', raczej_zgadzam_suma_grupa, ' - raczej zgadzam się',  '-', r_t_proc_grup_1, '%')
    row_3 = ('Grupa ', grupa_nb, ' = ', raczej_zgadzam_suma_grupa, ' - raczej zgadzam się',  '-', r_t_proc_grup_1, '%')
    print('Grupa ', grupa_nb, ' = ', trudno_powiedziec_suma_grupa, ' - trudno powiedzieć',  '-', t_p_proc_grup_1, '%')
    row_4 = ('Grupa ', grupa_nb, ' = ', trudno_powiedziec_suma_grupa, ' - trudno powiedzieć',  '-', t_p_proc_grup_1, '%')
    row_6 = ('Liczba respondentów = ', size_grup_nb,)
    file_out = []
    b = nb_qustion
    filename = str('number15_' + str(b) + ' _Grupa- ' + grupa_nb + '.csv')
    #file_out.append(row_0)
    file_out.append(row_1)
    file_out.append(row_2)
    file_out.append(row_3)
    file_out.append(row_4)
    file_out.append(row_6)
    f = open(filename, 'w')

    with f:
        fnames = [row_0]
        writer = csv.DictWriter(f, fieldnames = fnames)
        writer.writeheader()
        writer = csv.writer(f)
        writer.writerows(file_out)

    return file_out


get_dates_answer_grup_1('Pytanie_15_1.csv', header_ask, grupa_1)

question_grup(pyt_1_grupa_1, 1, grupa_1, header_ask[0])
question_grup(pyt_2_grupa_1, 2, grupa_1, header_ask[1])
question_grup(pyt_3_grupa_1, 3, grupa_1, header_ask[2])



# -------- Grupa 2
get_dates_answer_grup_2('Pytanie_15_1.csv', header_ask, grupa_2)

question_grup(pyt_1_grupa_2, 1, grupa_2, header_ask[0])
question_grup(pyt_2_grupa_2, 2, grupa_2, header_ask[1])
question_grup(pyt_3_grupa_2, 3, grupa_2, header_ask[2])


# -------- Grupa 3
get_dates_answer_grup_3('Pytanie_15_1.csv', header_ask, grupa_3)

question_grup(pyt_1_grupa_3, 1, grupa_3, header_ask[0])
question_grup(pyt_2_grupa_3, 2, grupa_3, header_ask[1])
question_grup(pyt_3_grupa_3, 3, grupa_3, header_ask[2])

















