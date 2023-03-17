#  ------------------------------------------------------------
# Downloading data from a csv file (social survey file)
# Analysis of votes by age group. Saving the analysis
# results in a csv file. Result of votes cast and percentage share
# by Radosław Tecmer
# radek69tecmer@gmail.com
# 2023 -02-28 ( ok)
#  --------------------------------------------------------------
#


import pandas as pd
import numpy as np
import csv
from csv import reader
from csv import DictReader
import numpy
import os
from collections import defaultdict

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

# grupy wiekowe
grupa_1 = "18-23 lat"
grupa_2 = "24-39 lat"
grupa_3 = "40-55 lat"
grupa_4 = '56 lat i więcej'

# lista dostępnych odpowiedzi
bardzo_wazne = 'bardzo ważne'
raczej_niewazne = "raczej nieważne"
raczej_wazne = "raczej ważne"
trudno_powiedziec = "trudno powiedzieć"
zdecydowanie_nieważne = 'zdecydowanie nieważne'


respondent_grupa_1 = 0
respondent_grupa_2 = 0
respondent_grupa_3 = 0
respondent_grupa_4 = 0

# Header read


def get_dates_header(one_file, encoding='utf-8'):
    # variable initiation
    header = []
    header_1 = []

    with open(one_file, 'r', newline='', encoding='utf-8') as the_file:
        reader = csv.reader(the_file, delimiter=';')
        line_csv_dict = DictReader(the_file)
        header_title = line_csv_dict.fieldnames
        for line in header_title:
            header_1.append(line)
            header = header_1[1:]
    the_file.close()
    return header

# header from file


headers = (get_dates_header("Pytanie_5_1.csv"))


# Group 1
def get_dates_answer_grup_1(one_file, header_ask, encoding='utf-8'):
    # variable initiation
    size_grup_1 = 15
    size_grup_2 = 42
    size_grup_3 = 37
    size_grup_4 = 0

    grupa_1 = "18-23 lat"
    grupa_2 = "24-39 lat"
    grupa_3 = "40-55 lat"
    grupa_4 = '56 lat i więcej'

    with open(one_file, 'r', newline='', encoding='utf-8') as the_file:
        #reader = csv.reader(the_file, delimiter=';')
        #header_line = next(the_file)

        csv_line_dict = DictReader(the_file)
        for line1 in csv_line_dict:
            if line1['Twój wiek?'] == grupa_1:
                pyt_1_grupa_1.append(line1[headers[0]])
            if line1['Twój wiek?'] == grupa_1:
                pyt_2_grupa_1.append(line1[headers[1]])
            if line1['Twój wiek?'] == grupa_1:
                pyt_3_grupa_1.append(line1[headers[2]])
            if line1['Twój wiek?'] == grupa_1:
                pyt_4_grupa_1.append(line1[headers[3]])
            if line1['Twój wiek?'] == grupa_1:
                pyt_5_grupa_1.append(line1[headers[4]])
            if line1['Twój wiek?'] == grupa_1:
                pyt_6_grupa_1.append(line1[headers[5]])
            if line1['Twój wiek?'] == grupa_1:
                pyt_7_grupa_1.append(line1[headers[6]])
            if line1['Twój wiek?'] == grupa_1:
                pyt_8_grupa_1.append(line1[headers[7]])
            if line1['Twój wiek?'] == grupa_1:
                pyt_9_grupa_1.append(line1[headers[8]])
            if line1['Twój wiek?'] == grupa_1:
                pyt_10_grupa_1.append(line1[headers[9]])
            if line1['Twój wiek?'] == grupa_1:
                pyt_11_grupa_1.append(line1[headers[10]])
            if line1['Twój wiek?'] == grupa_1:
                pyt_12_grupa_1.append(line1[headers[11]])
            if line1['Twój wiek?'] == grupa_1:
                pyt_13_grupa_1.append(line1[headers[12]])
            if line1['Twój wiek?'] == grupa_1:
                pyt_14_grupa_1.append(line1[headers[13]])
            if line1['Twój wiek?'] == grupa_1:
                pyt_15_grupa_1.append(line1[headers[14]])
    the_file.close()
    return


get_dates_answer_grup_1('Pytanie_5_1.csv', headers)


# Group 2

def get_dates_group_2(one_file, encoding='utf-8'):
    # ivariable initiation
    list_grupa_2 = []
    grupa_2 = "24-39 lat"

    with open(one_file, 'r', newline='', encoding='utf-8') as the_file:
        reader = csv.reader(the_file, delimiter=';')
        #header = next(reader)
        for line2 in reader:
            a = line2[0]
            if a == grupa_2:
                line2.pop(0)
                list_grupa_2.append(line2)

    the_file.close()
    return list_grupa_2

# Group 3

def get_dates_group_3(one_file, encoding='utf-8'):
    # ivariable initiation
    list_grupa_3 = []
    grupa_3 = "40-55 lat"

    with open(one_file, 'r', newline='', encoding='utf-8') as the_file:
        reader = csv.reader(the_file, delimiter=';')
        #header = next(reader)
        for line1 in reader:
            a = line1[0]
            if a == grupa_3:
                line1.pop(0)
                list_grupa_3.append(line1)

    the_file.close()
    return list_grupa_3

# Group 4

def get_dates_group_4(one_file, encoding='utf-8'):
    # ivariable initiation
    list_grupa_4 = []
    grupa_4 = "56 lat i więcej"

    with open(one_file, 'r', newline='', encoding='utf-8') as the_file:
        reader = csv.reader(the_file, delimiter=';')
        #header = next(reader)
        for line4 in reader:
            a = line4[0]
            if a == grupa_4:
                line4.pop(0)
                list_grupa_4.append(line4)

    the_file.close()
    return list_grupa_4


# Sum respondent


def get_dates_respondent(one_file, encoding='utf-8'):
    # ivariable initiation
    list_grupa_respon = []
    respond_grup_1 = 0
    respond_grup_2 = 0
    respond_grup_3 = 0
    respond_grup_4 = 0
    # grupy wiekowe
    grupa_1 = "18-23 lat"
    grupa_2 = "24-39 lat"
    grupa_3 = "40-55 lat"
    grupa_4 = '56 lat i więcej'

    with open(one_file, 'r', newline='', encoding='utf-8') as the_file:
        reader = csv.reader(the_file, delimiter=';')
        #header = next(reader)
        for line1 in reader:
            a = line1[0]
            list_grupa_respon.append(a)
        respond_grup_1 = list_grupa_respon.count(grupa_1)
        respond_grup_2 = list_grupa_respon.count(grupa_2)
        respond_grup_3 = list_grupa_respon.count(grupa_3)
        respond_grup_4 = list_grupa_respon.count(grupa_4)
        #respond_range = len(list_grupa_respon)
        #respond_grup_3 = (list_grupa_3[x].count(grupa_3))

    the_file.close()
    print("18-23 lat = ", respond_grup_1)
    print("24-39 lat = ", respond_grup_2)
    print("40-55 lat = ", respond_grup_3)
    print("56 < lat = ", respond_grup_4)
    return

# Print Sum Respondent


get_dates_respondent('Pytanie_5.csv')


L = get_dates_group_1("Pytanie_5.csv")
M = get_dates_group_2("Pytanie_5.csv")
P = get_dates_group_3("Pytanie_5.csv")
R = get_dates_group_4("Pytanie_5.csv")
sum_answers = 0


#bardzo_wazne_suma_grup_1 = 0
#raczej_niewazne_suma_grupa_1 = 0
#raczej_wazne_suma_grupa_1 = 0
#trudno_powiedziec_suma_grupa_1 = 0
#zdecydowanie_nieważne_suma_grupa_1 = 0

bardzo_wazne_suma_grup_2 = 0
raczej_niewazne_suma_grupa_2 = 0
raczej_wazne_suma_grupa_2 = 0
trudno_powiedziec_suma_grupa_2 = 0
zdecydowanie_nieważne_suma_grupa_2 = 0

bardzo_wazne_suma_grup_3 = 0
raczej_niewazne_suma_grupa_3 = 0
raczej_wazne_suma_grupa_3 = 0
trudno_powiedziec_suma_grupa_3 = 0
zdecydowanie_nieważne_suma_grupa_3 = 0

bardzo_wazne_suma_grup_4 = 0
raczej_niewazne_suma_grupa_4 = 0
raczej_wazne_suma_grupa_4 = 0
trudno_powiedziec_suma_grupa_4 = 0
zdecydowanie_nieważne_suma_grupa_4 = 0


# Group 1

l_range = len(pyt_2_grupa_1)

for x in range(l_range):
    b_w = (pyt_2_grupa_1[x].count(bardzo_wazne))
    r_n = (L[x].count(raczej_niewazne))
    r_w = (L[x].count(raczej_wazne))
    t_p = (L[x].count(trudno_powiedziec))
    z_n = (L[x].count(zdecydowanie_nieważne))
    bardzo_wazne_suma_grup_1 = b_w + bardzo_wazne_suma_grup_1
    raczej_niewazne_suma_grupa_1 = r_n + raczej_niewazne_suma_grupa_1
    raczej_wazne_suma_grupa_1 = r_w + raczej_wazne_suma_grupa_1
    trudno_powiedziec_suma_grupa_1 = t_p + trudno_powiedziec_suma_grupa_1
    zdecydowanie_nieważne_suma_grupa_1 = z_n + zdecydowanie_nieważne_suma_grupa_1


print('--------------------------')
print('Grupa 18-23 lata = ', bardzo_wazne_suma_grup_1, ' - bardzo ważne')
print('Grupa 18-23 lata = ', raczej_niewazne_suma_grupa_1, ' - raczej nieważne')
print('Grupa 18-23 lata = ', raczej_wazne_suma_grupa_1, ' - raczej ważne')
print('Grupa 18-23 lata = ', trudno_powiedziec_suma_grupa_1, ' - trudno powiedzieć')
print('Grupa 18-23 lata = ', zdecydowanie_nieważne_suma_grupa_1, ' - zdecydowanie nieważne')

# Group 2

m_range = len(M)

for x in range(m_range):
    b_w = (M[x].count(bardzo_wazne))
    r_n = (M[x].count(raczej_niewazne))
    r_w = (M[x].count(raczej_wazne))
    t_p = (M[x].count(trudno_powiedziec))
    z_n = (M[x].count(zdecydowanie_nieważne))
    bardzo_wazne_suma_grup_2 = b_w + bardzo_wazne_suma_grup_2
    raczej_niewazne_suma_grupa_2 = r_n + raczej_niewazne_suma_grupa_2
    raczej_wazne_suma_grupa_2 = r_w + raczej_wazne_suma_grupa_2
    trudno_powiedziec_suma_grupa_2 = t_p + trudno_powiedziec_suma_grupa_2
    zdecydowanie_nieważne_suma_grupa_2 = z_n + zdecydowanie_nieważne_suma_grupa_2

print('--------------------------')
print('Grupa 24-39 lata = ', bardzo_wazne_suma_grup_2, ' - bardzo ważne')
print('Grupa 24-39 lata = ', raczej_niewazne_suma_grupa_2, ' - raczej nieważne')
print('Grupa 24-39 lata = ', raczej_wazne_suma_grupa_2, ' - raczej ważne')
print('Grupa 24-39 lata = ', trudno_powiedziec_suma_grupa_2, ' - trudno powiedzieć')
print('Grupa 24-39 lata = ', zdecydowanie_nieważne_suma_grupa_2, ' - zdecydowanie nieważne')

# Group 3

p_range = len(P)

for x in range(p_range):
    b_w = (P[x].count(bardzo_wazne))
    r_n = (P[x].count(raczej_niewazne))
    r_w = (P[x].count(raczej_wazne))
    t_p = (P[x].count(trudno_powiedziec))
    z_n = (P[x].count(zdecydowanie_nieważne))
    bardzo_wazne_suma_grup_3 = b_w + bardzo_wazne_suma_grup_3
    raczej_niewazne_suma_grupa_3 = r_n + raczej_niewazne_suma_grupa_3
    raczej_wazne_suma_grupa_3 = r_w + raczej_wazne_suma_grupa_3
    trudno_powiedziec_suma_grupa_3 = t_p + trudno_powiedziec_suma_grupa_3
    zdecydowanie_nieważne_suma_grupa_3 = z_n + zdecydowanie_nieważne_suma_grupa_3

print('--------------------------')
print('Grupa 40-55 lata = ', bardzo_wazne_suma_grup_3, ' - bardzo ważne')
print('Grupa 40-55 lata = ', raczej_niewazne_suma_grupa_3, ' - raczej nieważne')
print('Grupa 40-55 lata = ', raczej_wazne_suma_grupa_3, ' - raczej ważne')
print('Grupa 40-55 lata = ', trudno_powiedziec_suma_grupa_3, ' - trudno powiedzieć')
print('Grupa 40-55 lata = ', zdecydowanie_nieważne_suma_grupa_3, ' - zdecydowanie nieważne')
print('******************')
print('Respondentów - ', respondent_grupa_3)


# Group 3

r_range = len(R)

for x in range(r_range):
    b_w = (R[x].count(bardzo_wazne))
    r_n = (R[x].count(raczej_niewazne))
    r_w = (R[x].count(raczej_wazne))
    t_p = (R[x].count(trudno_powiedziec))
    z_n = (R[x].count(zdecydowanie_nieważne))
    bardzo_wazne_suma_grup_4 = b_w + bardzo_wazne_suma_grup_4
    raczej_niewazne_suma_grupa_4 = r_n + raczej_niewazne_suma_grupa_4
    raczej_wazne_suma_grupa_4 = r_w + raczej_wazne_suma_grupa_4
    trudno_powiedziec_suma_grupa_4 = t_p + trudno_powiedziec_suma_grupa_4
    zdecydowanie_nieważne_suma_grupa_4 = z_n + zdecydowanie_nieważne_suma_grupa_4

print('--------------------------')
print('Grupa 56 < lata = ', bardzo_wazne_suma_grup_4, ' - bardzo ważne')
print('Grupa 56 < lata = ', raczej_niewazne_suma_grupa_4, ' - raczej nieważne')
print('Grupa 56 < lata = ', raczej_wazne_suma_grupa_4, ' - raczej ważne')
print('Grupa 56 < lata = ', trudno_powiedziec_suma_grupa_4, ' - trudno powiedzieć')
print('Grupa 56 < lata = ', zdecydowanie_nieważne_suma_grupa_4, ' - zdecydowanie nieważne')
print('******************')
print('Respondentów - ', respondent_grupa_4)

# Sum answers

sum_answers = (trudno_powiedziec_suma_grupa_3 + trudno_powiedziec_suma_grupa_2 + trudno_powiedziec_suma_grupa_1 +
               raczej_wazne_suma_grupa_3 + raczej_wazne_suma_grupa_2 + raczej_wazne_suma_grupa_1 +
               raczej_niewazne_suma_grupa_3 + raczej_niewazne_suma_grupa_2 + raczej_niewazne_suma_grupa_1 +
               bardzo_wazne_suma_grup_3 + bardzo_wazne_suma_grup_2 + bardzo_wazne_suma_grup_1 +
               zdecydowanie_nieważne_suma_grupa_3 + zdecydowanie_nieważne_suma_grupa_2 + zdecydowanie_nieważne_suma_grupa_1
               )
print('Total ---------------------' )
print('Suma odpowiedzi =  ', sum_answers)

# -- end ---












