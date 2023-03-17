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
header_ask = ['nie wierzysz, że to coś zmieni',
              'boisz się, że zostaniesz uznany(a) za roszczeniowego',
              'uważasz, że Twoje oczekiwania nie są ważne',
              'boisz się, że zostaniesz zwolniony(a)',
              'w firmie, w której pracujesz, nikt nie komunikuje potrzeb',
              'uważasz, że pracodawca powinien się domyśleć',
              'uważasz, że pracodawcy nie interesują Twoje oczekiwania',
              'bo już próbowałeś(aś) i zostałeś(aś) za to ukarany(a)',
              'inne',
              ]


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

    with open('../Pytanie_10_1.csv', newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';', quoting=csv.QUOTE_NONE)
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



    print('10. Dlaczego nie komunikujesz pracodawcy  że nie spełnia on Twoich oczekiwań? ')
    row_0 = ('10. Dlaczego nie komunikujesz pracodawcy  że nie spełnia on Twoich oczekiwań?')

    print('Grupa ', grupa_nb, ' Pytanie 6101  -', header_in[0], '-', 'Odpowiedzi -', counter_grup_1_pyt_1, '-',
          pyt1_proc_grup_1, '%')
    row_1 = ('Grupa ', grupa_nb, ' Pytanie 10/1  -', header_in[0], '-', 'Odpowiedzi -', counter_grup_1_pyt_1, '-',
             pyt1_proc_grup_1, '%')
    print('Grupa ', grupa_nb, ' Pytanie 10/2  -', header_in[1], '-', 'Odpowiedzi -', counter_grup_1_pyt_2, '-',
          pyt2_proc_grup_1, '%')
    row_2 = ('Grupa ', grupa_nb, ' Pytanie 10/2  -', header_in[1], '-', 'Odpowiedzi -', counter_grup_1_pyt_2, '-',
             pyt2_proc_grup_1, '%')
    print('Grupa ', grupa_nb, ' Pytanie 10/3  -', header_in[2], '-', 'Odpowiedzi -', counter_grup_1_pyt_3, '-',
          pyt3_proc_grup_1, '%')
    row_3 = ('Grupa ', grupa_nb, ' Pytanie 10/3  -', header_in[2], '-', 'Odpowiedzi -', counter_grup_1_pyt_3, '-',
             pyt3_proc_grup_1, '%')
    print('Grupa ', grupa_nb, ' Pytanie 10/4  -', header_in[3], '-', 'Odpowiedzi -', counter_grup_1_pyt_4, '-',
          pyt4_proc_grup_1, '%')
    row_4 = ('Grupa ', grupa_nb, ' Pytanie 10/4  -', header_in[3], '-', 'Odpowiedzi -', counter_grup_1_pyt_4, '-',
             pyt4_proc_grup_1, '%')
    print('Grupa ', grupa_nb, ' Pytanie 10/5  -', header_in[4], '-', 'Odpowiedzi -', counter_grup_1_pyt_5, '-',
          pyt5_proc_grup_1, '%')
    row_5 = ('Grupa ', grupa_nb, ' Pytanie 10/5  -', header_in[4], '-', 'Odpowiedzi -', counter_grup_1_pyt_5, '-',
             pyt5_proc_grup_1, '%')
    print('Grupa ', grupa_nb, ' Pytanie 10/6  -', header_in[5], '-', 'Odpowiedzi -', counter_grup_1_pyt_6, '-',
          pyt6_proc_grup_1, '%')
    row_6 = ('Grupa ', grupa_nb, ' Pytanie 10/6  -', header_in[5], '-', 'Odpowiedzi -', counter_grup_1_pyt_6, '-',
             pyt6_proc_grup_1, '%')
    print('Grupa ', grupa_nb, ' Pytanie 10/7  -', header_in[6], '-', 'Odpowiedzi -', counter_grup_1_pyt_7, '-',
          pyt7_proc_grup_1, '%')
    row_7 = ('Grupa ', grupa_nb, ' Pytanie 10/7  -', header_in[6], '-', 'Odpowiedzi -', counter_grup_1_pyt_7, '-',
             pyt7_proc_grup_1, '%')
    print('Grupa ', grupa_nb, ' Pytanie 6108  -', header_in[7], '-', 'Odpowiedzi -', counter_grup_1_pyt_8, '-',
          pyt8_proc_grup_1, '%')
    row_8 = ('Grupa ', grupa_nb, ' Pytanie 10/8  -', header_in[7], '-', 'Odpowiedzi -', counter_grup_1_pyt_8, '-',
             pyt8_proc_grup_1, '%')
    print('Grupa ', grupa_nb, ' Pytanie 10/9  -', header_in[8], '-', 'Odpowiedzi -', counter_grup_1_pyt_9, '-',
          pyt9_proc_grup_1, '%')
    row_9 = ('Grupa ', grupa_nb, ' Pytanie 6109  -', header_in[8], '-', 'Odpowiedzi -', counter_grup_1_pyt_9, '-',
             pyt9_proc_grup_1, '%')


    print('Liczba respondentów = ', size_grup_nb)
    row_16 = ('Liczba respondentów = ', size_grup_nb)


    file_out = []
    b = nb_file
    filename = str('number10_' + str(b) + ' _Grupa- ' + grupa_nb + '.csv')
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
    file_out.append(row_16)
    f = open(filename, 'w')

    with f:
        fnames = [row_0]
        writer = csv.DictWriter(f, fieldnames=fnames)
        writer.writeheader()
        writer = csv.writer(f)
        writer.writerows(file_out)

    return


print(get_question_group_1('../Pytanie_10_1.csv', grupa_3, 3, header_ask))




