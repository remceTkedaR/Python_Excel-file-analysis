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
pyt_17_grupa_1 = []


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
pyt_17_grupa_2 = []


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
pyt_17_grupa_3 = []



grupa_1 = "18-23 lat"
grupa_2 = "24-39 lat"
grupa_3 = "40-55 lat"


# lista dostępnych odpowiedzi
zdecydowanie_tak = 'zdecydowanie tak'
raczej_tak = 'raczej tak'
raczej_nie = 'raczej nie'
trudno_powiedzieć = 'trudno powiedzieć'
zdecydowanie_nie = 'zdecydowanie nie'


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


header_ask = (get_dates_header("Pytanie_12_1.csv"))

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
            if line1['Twój wiek?'] == grup_nb:
                pyt_16_grupa_1.append(line1[header_ask[15]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_17_grupa_1.append(line1[header_ask[16]])
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
            if line1['Twój wiek?'] == grup_nb:
                pyt_4_grupa_2.append(line1[header_ask[3]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_5_grupa_2.append(line1[header_ask[4]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_6_grupa_2.append(line1[header_ask[5]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_7_grupa_2.append(line1[header_ask[6]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_8_grupa_2.append(line1[header_ask[7]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_9_grupa_2.append(line1[header_ask[8]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_10_grupa_2.append(line1[header_ask[9]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_11_grupa_2.append(line1[header_ask[10]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_12_grupa_2.append(line1[header_ask[11]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_13_grupa_2.append(line1[header_ask[12]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_14_grupa_2.append(line1[header_ask[13]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_15_grupa_2.append(line1[header_ask[14]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_16_grupa_2.append(line1[header_ask[15]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_17_grupa_2.append(line1[header_ask[16]])
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
            if line1['Twój wiek?'] == grup_nb:
                pyt_4_grupa_3.append(line1[header_ask[3]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_5_grupa_3.append(line1[header_ask[4]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_6_grupa_3.append(line1[header_ask[5]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_7_grupa_3.append(line1[header_ask[6]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_8_grupa_3.append(line1[header_ask[7]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_9_grupa_3.append(line1[header_ask[8]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_10_grupa_3.append(line1[header_ask[9]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_11_grupa_3.append(line1[header_ask[10]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_12_grupa_3.append(line1[header_ask[11]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_13_grupa_3.append(line1[header_ask[12]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_14_grupa_3.append(line1[header_ask[13]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_15_grupa_3.append(line1[header_ask[14]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_16_grupa_3.append(line1[header_ask[15]])
            if line1['Twój wiek?'] == grup_nb:
                pyt_17_grupa_3.append(line1[header_ask[16]])
    the_file.close()
    return

# Przetwarzanie danych dla wszystkich grup


def question_grup(question_number, nb_qustion, grupa_nb, header=[]):
    #---
    zdecydowanie_tak_suma_grupa = 0
    raczej_tak_suma_grupa = 0
    raczej_nie_suma_grupa = 0
    trudno_powiedziec_suma_grupa = 0
    zdecydowanie_nie_suma_grupa = 0

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
        z_t = (question_number[x].count(zdecydowanie_tak))
        r_t = (question_number[x].count(raczej_tak))
        r_n = (question_number[x].count(raczej_nie))
        t_p = (question_number[x].count(trudno_powiedzieć))
        z_n = (question_number[x].count(zdecydowanie_nie))

        zdecydowanie_tak_suma_grupa = z_t + zdecydowanie_tak_suma_grupa
        raczej_nie_suma_grupa = r_n + raczej_nie_suma_grupa
        raczej_tak_suma_grupa = r_t + raczej_tak_suma_grupa
        trudno_powiedziec_suma_grupa = t_p + trudno_powiedziec_suma_grupa
        zdecydowanie_nie_suma_grupa = z_n + zdecydowanie_nie_suma_grupa

        # calculation "%"
        z_t_proc_grup_1 = ((zdecydowanie_tak_suma_grupa * 100)/size_grup_nb)
        z_t_proc_grup_1 = '%-.2f' % z_t_proc_grup_1
        r_n_proc_grup_1 = ((raczej_nie_suma_grupa * 100) / size_grup_nb)
        r_n_proc_grup_1 = '%-.2f' % r_n_proc_grup_1
        r_t_proc_grup_1 = ((raczej_tak_suma_grupa * 100) / size_grup_nb)
        r_t_proc_grup_1 = '%-.2f' % r_t_proc_grup_1
        t_p_proc_grup_1 = ((trudno_powiedziec_suma_grupa * 100) / size_grup_nb)
        t_p_proc_grup_1 = '%-.2f' % t_p_proc_grup_1
        z_n_proc_grup_1 = ((zdecydowanie_nie_suma_grupa * 100) / size_grup_nb)
        z_n_proc_grup_1 = '%-.2f' % z_n_proc_grup_1


    print(header)
    row_0 = (header)
    print('Grupa ', grupa_nb, ' = ', zdecydowanie_tak_suma_grupa, ' - zdecydowanie tak', '-', z_t_proc_grup_1, '%')
    row_1 = ('Grupa ', grupa_nb, ' = ', zdecydowanie_tak_suma_grupa, ' - zdecydowanie tak', '-', z_t_proc_grup_1, '%')
    print('Grupa ', grupa_nb, ' = ', raczej_nie_suma_grupa, ' - raczej nie',  '-', r_n_proc_grup_1, '%')
    row_2 = ('Grupa ', grupa_nb, ' = ', raczej_nie_suma_grupa, ' - raczej nie',  '-', r_n_proc_grup_1, '%')
    print('Grupa ', grupa_nb, ' = ', raczej_tak_suma_grupa, ' - raczej tak',  '-', r_t_proc_grup_1, '%')
    row_3 = ('Grupa ', grupa_nb, ' = ', raczej_tak_suma_grupa, ' - raczej tak',  '-', r_t_proc_grup_1, '%')
    print('Grupa ', grupa_nb, ' = ', trudno_powiedziec_suma_grupa, ' - trudno powiedzieć',  '-', t_p_proc_grup_1, '%')
    row_4 = ('Grupa ', grupa_nb, ' = ', trudno_powiedziec_suma_grupa, ' - trudno powiedzieć',  '-', t_p_proc_grup_1, '%')
    print('Grupa ', grupa_nb, ' = ', zdecydowanie_nie_suma_grupa, ' - zdecydowanie nie',  '-', z_n_proc_grup_1, '%')
    row_5 = ('Grupa ', grupa_nb, ' = ', zdecydowanie_nie_suma_grupa, ' - zdecydowanie nie',  '-', z_n_proc_grup_1, '%')
    row_6 = ('Liczba respondentów = ', size_grup_nb,)
    file_out = []
    b = nb_qustion
    filename = str('number12_' + str(b) + ' _Grupa- ' + grupa_nb + '.csv')
    #file_out.append(row_0)
    file_out.append(row_1)
    file_out.append(row_2)
    file_out.append(row_3)
    file_out.append(row_4)
    file_out.append(row_5)
    file_out.append(row_6)
    f = open(filename, 'w')

    with f:
        fnames = [row_0]
        writer = csv.DictWriter(f, fieldnames = fnames)
        writer.writeheader()
        writer = csv.writer(f)
        writer.writerows(file_out)

    return file_out


get_dates_answer_grup_1('Pytanie_12_1.csv', header_ask, grupa_1)

question_grup(pyt_1_grupa_1, 1, grupa_1, header_ask[0])
question_grup(pyt_2_grupa_1, 2, grupa_1, header_ask[1])
question_grup(pyt_3_grupa_1, 3, grupa_1, header_ask[2])
question_grup(pyt_4_grupa_1, 4, grupa_1, header_ask[3])
question_grup(pyt_5_grupa_1, 5, grupa_1, header_ask[4])
question_grup(pyt_6_grupa_1, 6, grupa_1, header_ask[5])
question_grup(pyt_7_grupa_1, 7, grupa_1, header_ask[6])
question_grup(pyt_8_grupa_1, 8, grupa_1, header_ask[7])
question_grup(pyt_9_grupa_1, 9, grupa_1, header_ask[8])
question_grup(pyt_10_grupa_1, 10, grupa_1, header_ask[9])
question_grup(pyt_11_grupa_1, 11, grupa_1, header_ask[10])
question_grup(pyt_12_grupa_1, 12, grupa_1, header_ask[11])
question_grup(pyt_13_grupa_1, 13, grupa_1, header_ask[12])
question_grup(pyt_14_grupa_1, 14, grupa_1, header_ask[13])
question_grup(pyt_15_grupa_1, 15, grupa_1, header_ask[14])
question_grup(pyt_16_grupa_1, 16, grupa_1, header_ask[15])
question_grup(pyt_17_grupa_1, 17, grupa_1, header_ask[16])


# -------- Grupa 2
get_dates_answer_grup_2('Pytanie_12_1.csv', header_ask, grupa_2)

question_grup(pyt_1_grupa_2, 1, grupa_2, header_ask[0])
question_grup(pyt_2_grupa_2, 2, grupa_2, header_ask[1])
question_grup(pyt_3_grupa_2, 3, grupa_2, header_ask[2])
question_grup(pyt_4_grupa_2, 4, grupa_2, header_ask[3])
question_grup(pyt_5_grupa_2, 5, grupa_2, header_ask[4])
question_grup(pyt_6_grupa_2, 6, grupa_2, header_ask[5])
question_grup(pyt_7_grupa_2, 7, grupa_2, header_ask[6])
question_grup(pyt_8_grupa_2, 8, grupa_2, header_ask[7])
question_grup(pyt_9_grupa_2, 9, grupa_2, header_ask[8])
question_grup(pyt_10_grupa_2, 10, grupa_2, header_ask[9])
question_grup(pyt_11_grupa_2, 11, grupa_2, header_ask[10])
question_grup(pyt_12_grupa_2, 12, grupa_2, header_ask[11])
question_grup(pyt_13_grupa_2, 13, grupa_2, header_ask[12])
question_grup(pyt_14_grupa_2, 14, grupa_2, header_ask[13])
question_grup(pyt_15_grupa_2, 15, grupa_2, header_ask[14])
question_grup(pyt_16_grupa_2, 16, grupa_2, header_ask[15])
question_grup(pyt_17_grupa_2, 17, grupa_2, header_ask[16])

# -------- Grupa 3
get_dates_answer_grup_3('Pytanie_12_1.csv', header_ask, grupa_3)

question_grup(pyt_1_grupa_3, 1, grupa_3, header_ask[0])
question_grup(pyt_2_grupa_3, 2, grupa_3, header_ask[1])
question_grup(pyt_3_grupa_3, 3, grupa_3, header_ask[2])
question_grup(pyt_4_grupa_3, 4, grupa_3, header_ask[3])
question_grup(pyt_5_grupa_3, 5, grupa_3, header_ask[4])
question_grup(pyt_6_grupa_3, 6, grupa_3, header_ask[5])
question_grup(pyt_7_grupa_3, 7, grupa_3, header_ask[6])
question_grup(pyt_8_grupa_3, 8, grupa_3, header_ask[7])
question_grup(pyt_9_grupa_3, 9, grupa_3, header_ask[8])
question_grup(pyt_10_grupa_3, 10, grupa_3, header_ask[9])
question_grup(pyt_11_grupa_3, 11, grupa_3, header_ask[10])
question_grup(pyt_12_grupa_3, 12, grupa_3, header_ask[11])
question_grup(pyt_13_grupa_3, 13, grupa_3, header_ask[12])
question_grup(pyt_14_grupa_3, 14, grupa_3, header_ask[13])
question_grup(pyt_15_grupa_3, 15, grupa_3, header_ask[14])
question_grup(pyt_16_grupa_3, 16, grupa_3, header_ask[15])
question_grup(pyt_17_grupa_3, 17, grupa_3, header_ask[16])















