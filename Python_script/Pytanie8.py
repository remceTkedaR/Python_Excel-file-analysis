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

# Lista pytań
header_ask = [' narzędzi niezbędnych do wykonywania pracy i/lub właściwych warunków bhp',
              'odpowiednich do Twoich potrzeb warunków socjalnych',
              'możliwości awansu i/lub przejrzystych warunków jego uzyskania',
              'satysfakcjonującego wynagrodzenia i/lub przejrzystych zasad jego podwyżek',
              'szansy na rozwój osobisty wykraczający poza zajmowane stanowisko',
              'możliwości udziału w szkoleniach rozwijających kwalifikacje na zajmowanym stanowisku',
              'bezpieczeństwa zatrudnienia, tj. stałej umowy o pracę',
              'samodzielności w pracy adekwatnej do posiadanych kwalifikacji i doświadczenia',
              'dopasowanego do potrzeb systemu motywacyjnego',
              'równowagi pomiędzy pracą a życiem osobistym (work life balance)',
              'przejrzystego systemu oceny pracy',
             'równego traktowania pracowników (brak dyskryminacji i brak faworyzowania wybranych pracowników)',
             'regularnego otrzymywania informacji zwrotnych dotyczących oceny jakości pracy',
             'szacunku i poszanowania godności',
             'dbałości o klimat sprzyjający zadowoleniu z pracy']


# Grupy respondentów
grupa_1 = '18-23 lat'
grupa_2 = '24-39 lat'
grupa_3 = '40-55 lat'

grupa_1_pyt_1 = []
grupa_1_pyt_2 = []
grupa_1_pyt_3 = []
grupa_1_pyt_4 = []
grupa_1_pyt_5 = []
grupa_1_pyt_6 = []
grupa_1_pyt_7 = []
grupa_1_pyt_8 = []
grupa_1_pyt_9 = []
grupa_1_pyt_10 = []
grupa_1_pyt_11 = []
grupa_1_pyt_12 = []
grupa_1_pyt_13 = []
grupa_1_pyt_14 = []
grupa_1_pyt_15 = []


def get_question_group_1(one_file, grupa_nb, nb_file, header_in):
    # Liość respondentów
    size_grup_1 = 15
    size_grup_2 = 42
    size_grup_3 = 37

    my_grupa_1 = "18-23 lat"
    my_grupa_2 = "24-39 lat"
    my_grupa_3 = "40-55 lat"

    if grupa_nb == my_grupa_1:
        size_grup_nb = size_grup_1
    if grupa_nb == my_grupa_2:
        size_grup_nb = size_grup_2
    if grupa_nb == my_grupa_3:
        size_grup_nb = size_grup_3

    with open('../Pytanie_8_1.csv', newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_NONE)
        csv_line_dict = DictReader(csv_reader)
        for row in csv_reader:
            if row[0] == grupa_nb:
                grupa_1_pyt_1.append(row[1])

            counter_grup_1_pyt_1 = grupa_1_pyt_1.count(header_in[0])

            if row[0] == grupa_nb:
                grupa_1_pyt_2.append(row[2])

            counter_grup_1_pyt_2 = grupa_1_pyt_2.count(header_in[1])

            if row[0] == grupa_nb:
                grupa_1_pyt_3.append(row[3])

            counter_grup_1_pyt_3 = grupa_1_pyt_3.count(header_in[2])

            if row[0] == grupa_nb:
                grupa_1_pyt_4.append(row[4])

            counter_grup_1_pyt_4 = grupa_1_pyt_4.count(header_in[3])

            if row[0] == grupa_nb:
                grupa_1_pyt_5.append(row[5])

            counter_grup_1_pyt_5 = grupa_1_pyt_5.count(header_in[4])

            if row[0] == grupa_nb:
                grupa_1_pyt_6.append(row[6])

            counter_grup_1_pyt_6 = grupa_1_pyt_6.count(header_in[5])

            if row[0] == grupa_nb:
                grupa_1_pyt_7.append(row[7])

            counter_grup_1_pyt_7 = grupa_1_pyt_7.count(header_in[6])

            if row[0] == grupa_nb:
                grupa_1_pyt_8.append(row[8])

            counter_grup_1_pyt_8 = grupa_1_pyt_8.count(header_in[7])

            if row[0] == grupa_nb:
                grupa_1_pyt_9.append(row[9])

            counter_grup_1_pyt_9 = grupa_1_pyt_9.count(header_in[8])

            if row[0] == grupa_nb:
                grupa_1_pyt_10.append(row[10])

            counter_grup_1_pyt_10 = grupa_1_pyt_10.count(header_in[9])

            if row[0] == grupa_nb:
                grupa_1_pyt_11.append(row[11])

            counter_grup_1_pyt_11 = grupa_1_pyt_11.count(header_in[10])

            if row[0] == grupa_nb:
                grupa_1_pyt_12.append(row[12])

            counter_grup_1_pyt_12 = grupa_1_pyt_12.count(header_in[11])

            if row[0] == grupa_nb:
                grupa_1_pyt_13.append(row[13])

            counter_grup_1_pyt_13 = grupa_1_pyt_13.count(header_in[12])

            if row[0] == grupa_nb:
                grupa_1_pyt_14.append(row[14])

            counter_grup_1_pyt_14 = grupa_1_pyt_14.count(header_in[13])

            if row[0] == grupa_nb:
                grupa_1_pyt_15.append(row[15])

            counter_grup_1_pyt_15 = grupa_1_pyt_15.count(header_in[14])






    # calculation "%"
    pyt1_proc_grup_1 = ((counter_grup_1_pyt_1 * 100) / size_grup_nb)
    pyt1_proc_grup_1 = '%-.2f' % pyt1_proc_grup_1

    pyt2_proc_grup_1 = ((counter_grup_1_pyt_2 * 100) / size_grup_nb)
    pyt2_proc_grup_1 = '%-.2f' % pyt2_proc_grup_1

    pyt3_proc_grup_1 = ((counter_grup_1_pyt_3 * 100) / size_grup_nb)
    pyt3_proc_grup_1 = '%-.2f' % pyt3_proc_grup_1

    pyt4_proc_grup_1 = ((counter_grup_1_pyt_4 * 100) / size_grup_nb)
    pyt4_proc_grup_1 = '%-.2f' % pyt4_proc_grup_1

    pyt5_proc_grup_1 = ((counter_grup_1_pyt_5 * 100) / size_grup_nb)
    pyt5_proc_grup_1 = '%-.2f' % pyt5_proc_grup_1

    pyt6_proc_grup_1 = ((counter_grup_1_pyt_6 * 100) / size_grup_nb)
    pyt6_proc_grup_1 = '%-.2f' % pyt6_proc_grup_1

    pyt7_proc_grup_1 = ((counter_grup_1_pyt_7 * 100) / size_grup_nb)
    pyt7_proc_grup_1 = '%-.2f' % pyt7_proc_grup_1

    pyt8_proc_grup_1 = ((counter_grup_1_pyt_8 * 100) / size_grup_nb)
    pyt8_proc_grup_1 = '%-.2f' % pyt8_proc_grup_1

    pyt9_proc_grup_1 = ((counter_grup_1_pyt_9 * 100) / size_grup_nb)
    pyt9_proc_grup_1 = '%-.2f' % pyt9_proc_grup_1

    pyt10_proc_grup_1 = ((counter_grup_1_pyt_10 * 100) / size_grup_nb)
    pyt10_proc_grup_1 = '%-.2f' % pyt10_proc_grup_1

    pyt11_proc_grup_1 = ((counter_grup_1_pyt_11 * 100) / size_grup_nb)
    pyt11_proc_grup_1 = '%-.2f' % pyt11_proc_grup_1

    pyt12_proc_grup_1 = ((counter_grup_1_pyt_12 * 100) / size_grup_nb)
    pyt12_proc_grup_1 = '%-.2f' % pyt12_proc_grup_1

    pyt13_proc_grup_1 = ((counter_grup_1_pyt_13 * 100) / size_grup_nb)
    pyt13_proc_grup_1 = '%-.2f' % pyt13_proc_grup_1

    pyt14_proc_grup_1 = ((counter_grup_1_pyt_14 * 100) / size_grup_nb)
    pyt14_proc_grup_1 = '%-.2f' % pyt14_proc_grup_1

    pyt15_proc_grup_1 = ((counter_grup_1_pyt_15 * 100) / size_grup_nb)
    pyt15_proc_grup_1 = '%-.2f' % pyt15_proc_grup_1


    print('8. Których Twoich oczekiwań pracodawca nie spełnia najczęściej? Nie zapewnia:')
    row_0 = ('8. Których Twoich oczekiwań pracodawca nie spełnia najczęściej? Nie zapewnia:')

    print('Grupa ', grupa_nb, ' Pytanie 8/1  -', header_in[0], '-', 'Odpowiedzi -', counter_grup_1_pyt_1, '-',
          pyt1_proc_grup_1, '%')
    row_1 = ('Grupa ', grupa_nb, ' Pytanie 8/1  -', header_in[0], '-', 'Odpowiedzi -', counter_grup_1_pyt_1, '-',
             pyt1_proc_grup_1, '%')
    print('Grupa ', grupa_nb, ' Pytanie 8/2  -', header_in[1], '-', 'Odpowiedzi -', counter_grup_1_pyt_2, '-',
          pyt2_proc_grup_1, '%')
    row_2 = ('Grupa ', grupa_nb, ' Pytanie 8/2  -', header_in[1], '-', 'Odpowiedzi -', counter_grup_1_pyt_2, '-',
             pyt2_proc_grup_1, '%')
    print('Grupa ', grupa_nb, ' Pytanie 8/3  -', header_in[2], '-', 'Odpowiedzi -', counter_grup_1_pyt_3, '-',
          pyt3_proc_grup_1, '%')
    row_3 = ('Grupa ', grupa_nb, ' Pytanie 8/3  -', header_in[2], '-', 'Odpowiedzi -', counter_grup_1_pyt_3, '-',
             pyt3_proc_grup_1, '%')
    print('Grupa ', grupa_nb, ' Pytanie 8/4  -', header_in[3], '-', 'Odpowiedzi -', counter_grup_1_pyt_4, '-',
          pyt4_proc_grup_1, '%')
    row_4 = ('Grupa ', grupa_nb, ' Pytanie 8/4  -', header_in[3], '-', 'Odpowiedzi -', counter_grup_1_pyt_4, '-',
             pyt4_proc_grup_1, '%')
    print('Grupa ', grupa_nb, ' Pytanie 8/5  -', header_in[4], '-', 'Odpowiedzi -', counter_grup_1_pyt_5, '-',
          pyt5_proc_grup_1, '%')
    row_5 = ('Grupa ', grupa_nb, ' Pytanie 8/5  -', header_in[4], '-', 'Odpowiedzi -', counter_grup_1_pyt_5, '-',
             pyt5_proc_grup_1, '%')
    print('Grupa ', grupa_nb, ' Pytanie 8/6  -', header_in[5], '-', 'Odpowiedzi -', counter_grup_1_pyt_6, '-',
          pyt6_proc_grup_1, '%')
    row_6 = ('Grupa ', grupa_nb, ' Pytanie 8/6  -', header_in[5], '-', 'Odpowiedzi -', counter_grup_1_pyt_6, '-',
             pyt6_proc_grup_1, '%')
    print('Grupa ', grupa_nb, ' Pytanie 8/7  -', header_in[6], '-', 'Odpowiedzi -', counter_grup_1_pyt_7, '-',
          pyt7_proc_grup_1, '%')
    row_7 = ('Grupa ', grupa_nb, ' Pytanie 8/7  -', header_in[6], '-', 'Odpowiedzi -', counter_grup_1_pyt_7, '-',
             pyt7_proc_grup_1, '%')
    print('Grupa ', grupa_nb, ' Pytanie 8/8  -', header_in[7], '-', 'Odpowiedzi -', counter_grup_1_pyt_8, '-',
          pyt8_proc_grup_1, '%')
    row_8 = ('Grupa ', grupa_nb, ' Pytanie 8/8  -', header_in[7], '-', 'Odpowiedzi -', counter_grup_1_pyt_8, '-',
             pyt8_proc_grup_1, '%')
    print('Grupa ', grupa_nb, ' Pytanie 8/9  -', header_in[8], '-', 'Odpowiedzi -', counter_grup_1_pyt_9, '-',
          pyt9_proc_grup_1, '%')
    row_9 = ('Grupa ', grupa_nb, ' Pytanie 8/9  -', header_in[8], '-', 'Odpowiedzi -', counter_grup_1_pyt_9, '-',
             pyt9_proc_grup_1, '%')
    print('Grupa ', grupa_nb, ' Pytanie 8/10  -', header_in[9], '-', 'Odpowiedzi -', counter_grup_1_pyt_10, '-',
          pyt10_proc_grup_1, '%')
    row_10 = ('Grupa ', grupa_nb, ' Pytanie 8/10  -', header_in[9], '-', 'Odpowiedzi -', counter_grup_1_pyt_10, '-',
             pyt10_proc_grup_1, '%')
    print('Grupa ', grupa_nb, ' Pytanie 8/11  -', header_in[10], '-', 'Odpowiedzi -', counter_grup_1_pyt_11, '-',
          pyt11_proc_grup_1, '%')
    row_11 = ('Grupa ', grupa_nb, ' Pytanie 8/11  -', header_in[10], '-', 'Odpowiedzi -', counter_grup_1_pyt_11, '-',
             pyt11_proc_grup_1, '%')
    print('Grupa ', grupa_nb, ' Pytanie 8/12  -', header_in[11], '-', 'Odpowiedzi -', counter_grup_1_pyt_12, '-',
          pyt12_proc_grup_1, '%')
    row_12 = ('Grupa ', grupa_nb, ' Pytanie 8/12  -', header_in[11], '-', 'Odpowiedzi -', counter_grup_1_pyt_12, '-',
             pyt12_proc_grup_1, '%')
    print('Grupa ', grupa_nb, ' Pytanie 8/13  -', header_in[12], '-', 'Odpowiedzi -', counter_grup_1_pyt_13, '-',
          pyt13_proc_grup_1, '%')
    row_13 = ('Grupa ', grupa_nb, ' Pytanie 8/13  -', header_in[12], '-', 'Odpowiedzi -', counter_grup_1_pyt_13, '-',
             pyt13_proc_grup_1, '%')
    print('Grupa ', grupa_nb, ' Pytanie 8/14  -', header_in[13], '-', 'Odpowiedzi -', counter_grup_1_pyt_14, '-',
          pyt14_proc_grup_1, '%')
    row_14 = ('Grupa ', grupa_nb, ' Pytanie 8/14  -', header_in[13], '-', 'Odpowiedzi -', counter_grup_1_pyt_14, '-',
             pyt14_proc_grup_1, '%')
    print('Grupa ', grupa_nb, ' Pytanie 8/15  -', header_in[14], '-', 'Odpowiedzi -', counter_grup_1_pyt_15, '-',
          pyt15_proc_grup_1, '%')
    row_15 = ('Grupa ', grupa_nb, ' Pytanie 8/15  -', header_in[14], '-', 'Odpowiedzi -', counter_grup_1_pyt_15, '-',
             pyt15_proc_grup_1, '%')

    print('Liczba respondentów = ', size_grup_nb)
    row_16 = ('Liczba respondentów = ', size_grup_nb)


    file_out = []
    b = nb_file
    filename = str('number8_' + str(b) + ' _Grupa- ' + grupa_nb + '.csv')
    # file_out.append(row_0)
    file_out.append(row_1)
    file_out.append(row_2)
    file_out.append(row_3)
    file_out.append(row_4)
    file_out.append(row_5)
    file_out.append(row_6)
    file_out.append(row_7)
    file_out.append(row_8)
    file_out.append(row_9)
    file_out.append(row_10)
    file_out.append(row_11)
    file_out.append(row_12)
    file_out.append(row_13)
    file_out.append(row_14)
    file_out.append(row_15)
    file_out.append(row_16)
    f = open(filename, 'w')

    with f:
        fnames = [row_0]
        writer = csv.DictWriter(f, fieldnames=fnames)
        writer.writeheader()
        writer = csv.writer(f)
        writer.writerows(file_out)

    return


print(get_question_group_1('../Pytanie_8_1.csv', grupa_3, 3, header_ask))




