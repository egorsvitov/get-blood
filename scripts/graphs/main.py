from scipy.signal import savgol_filter
from matplotlib import pyplot
import numpy as np

ca_x = []
ca_y = []

count = 0
with open('C:\\get-lab-1-main\\pasha\\report\\1.txt', 'r') as f:
    for line in f.readlines():
        count += 1
        if count > 4:
            ca_y.append(int(line))
            ca_x.append(40)
count = 0
with open('C:\\get-lab-1-main\\pasha\\report\\2.txt', 'r') as f:
    for line in f.readlines():
        count += 1
        if count > 4:
            ca_y.append(int(line))
            ca_x.append(80)
count = 0
with open('C:\\get-lab-1-main\\pasha\\report\\3.txt', 'r') as f:
    for line in f.readlines():
        count += 1
        if count > 4:
            ca_y.append(int(line))
            ca_x.append(120)
count = 0
with open('C:\\get-lab-1-main\\pasha\\report\\4.txt', 'r') as f:
    for line in f.readlines():
        count += 1
        if count > 4:
            ca_y.append(int(line))
            ca_x.append(160)
k, b = tuple(np.polyfit(ca_x, ca_y, 1))
fig, a = pyplot.subplots(figsize=(16, 9), dpi=400)
a.set_xlabel("Количество делений")
a.set_ylabel("Показания АЦП")
a.set_title("Калибровка")
a.scatter(ca_x, ca_y)
x = [1, 160]
y = [k+b, 160*k+b]
a.plot(x, y)
a.minorticks_on()
a.grid(which='major')
a.grid(which='minor', linestyle=':')
fig.savefig("calibrate.png")







eg_1_x = []
eg_1_y = []
count = 0
lenEg_1 = sum(1 for line in open('C:\\get-lab-1-main\\pasha\\report\\egor_1.txt', 'r'))
with open('C:\\get-lab-1-main\\pasha\\report\\egor_1.txt', 'r') as f:
    for line in f.readlines():
        count += 1
        if count > 4:
            eg_1_y.append((int(line)-b)/k)
            eg_1_x.append(count*60/lenEg_1)
rest_eg, pt = pyplot.subplots(figsize=(16, 9), dpi=400)
pt.axis(xmin=0, xmax=60, ymin=min(eg_1_y), ymax=max(eg_1_y))
pt.set_xlabel("Время с начала эксперимента")
pt.set_ylabel("Давление")
pt.set_title("Зависимость давления от времени")
number = 0
mark_x = []
mark_y = []
w = savgol_filter(eg_1_y, 101, 2)
i = 30000
lhs = max(w)
rhs = 0
cont = 1
while i < len(w)-2000:
    i += 1
    if w[i-3000] < w[i] > w[i+3000]:
        number += 1
        lhs = rhs
        rhs = w[i]
        i += 4000
    if number == 15 and cont == 1:
        mark_y.append(w[i])
        mark_x.append(eg_1_x[i])
        pt.text(eg_1_x[i]+1, w[i]+2, 'Систола')
        cont = 0
    if abs(rhs-lhs) < 0.6:
        mark_y.append(w[i])
        mark_x.append(eg_1_x[i])
        pt.text(eg_1_x[i] + 1, w[i] + 2, 'Диастола')
        break
pt.plot(eg_1_x, w, label='Давление')
pt.scatter(mark_x, mark_y, color='red', marker='o')
pt.minorticks_on()
pt.grid(which='major')
pt.grid(which='minor', linestyle=':')
rest_eg.savefig('rest-pressure-egor.png')
pulse_eg_1_x = []
pulse_eg_1_y = []
tmp_x = []
tmp_y = []
for i in range(int(len(w)*35/60), int(len(w)*50/60)):
    tmp_x.append(eg_1_x[i])
    tmp_y.append(w[i])
k_pulse_eg_1, b_pulse_eg_1 = tuple(np.polyfit(tmp_x, tmp_y, 1))
# k_pulse_eg_1 = ((w[int(len(w)*50/60)]-w[int(len(w)*30/60)])/(eg_2_x[int(len(w)*50/60)]-eg_2_x[int(len(w)*30/60)]))
for i in range(int(len(w)*35/60), int(len(w)*50/60)):
    pulse_eg_1_x.append(eg_1_x[i])
    # pulse_eg_1_y.append(w[i]-(k_pulse_eg_1*(eg_1_x[i]-eg_1_x[int(len(w)*50/60)])+w[int(len(w)*50/60)]))
    pulse_eg_1_y.append(w[i] - (k_pulse_eg_1 * (eg_1_x[i]) + b_pulse_eg_1))
pulse_rest_eg, pt = pyplot.subplots(figsize=(16, 9), dpi=400)
# pt.axis(xmin=0, xmax=60, ymin=min(eg_2_y), ymax=max(eg_2_y))
pt.set_xlabel("Время с начала эксперимента")
pt.set_ylabel("Изменение давления")
pt.set_title("Зависимость изменения давления от времени")
pt.plot(pulse_eg_1_x, pulse_eg_1_y, label='Давление')
pt.minorticks_on()
pt.grid(which='major')
pt.grid(which='minor', linestyle=':')
i = 0
number = 0
cont = 1
aaa = []
bbb = []
while i < int(len(pulse_eg_1_x))-7000:
    i += 1
    if pulse_eg_1_y[i-4000] < pulse_eg_1_y[i] > pulse_eg_1_y[i+4000]:
        number += 1
        #aaa.append(pulse_eg_1_x[i])
        #bbb.append(pulse_eg_1_y[i])
        i += 7000
# print(number)
pt.text(48, 1.5, f'Пульс: {int(number/(50-35)*60)} уд/мин')
#pt.scatter(aaa, bbb, color='red', marker='o')
pulse_rest_eg.savefig('rest-pulse-egor.png')










eg_2_x = []
eg_2_y = []
count = 0
lenEg_2 = sum(1 for line in open('C:\\get-lab-1-main\\pasha\\report\\egor_2.txt', 'r'))
with open('C:\\get-lab-1-main\\pasha\\report\\egor_2.txt', 'r') as f:
    for line in f.readlines():
        count += 1
        if count > 4:
            eg_2_y.append((int(line)-b)/k)
            eg_2_x.append(count*60/lenEg_2)
fitness_eg, pt = pyplot.subplots(figsize=(16, 9), dpi=400)
pt.axis(xmin=0, xmax=60, ymin=min(eg_2_y), ymax=max(eg_2_y))
pt.set_xlabel("Время с начала эксперимента")
pt.set_ylabel("Давление")
pt.set_title("Зависимость давления от времени")
number = 0
mark_x = []
mark_y = []
w = savgol_filter(eg_2_y, 101, 2)
i = 30000
lhs = max(w)
rhs = 0
cont = 1
while i < len(w)-2000:
    i += 1
    if w[i-3000] < w[i] > w[i+3000]:
        number += 1
        lhs = rhs
        rhs = w[i]
        i += 4000
    if number == 15 and cont == 1:
        mark_y.append(w[i])
        mark_x.append(eg_2_x[i])
        pt.text(eg_1_x[i]+1, w[i]+2, 'Систола')
        cont = 0
    if abs(rhs-lhs) < 0.6:
        mark_y.append(w[i])
        mark_x.append(eg_2_x[i])
        pt.text(eg_2_x[i] + 1, w[i] + 2, 'Диастола')
        break
pt.plot(eg_2_x, w, label='Давление')
pt.scatter(mark_x, mark_y, color='red', marker='o')
pt.minorticks_on()
pt.grid(which='major')
pt.grid(which='minor', linestyle=':')
fitness_eg.savefig('fitness-pressure-egor.png')
pulse_eg_2_x = []
pulse_eg_2_y = []
tmp_x = []
tmp_y = []
for i in range(int(len(w)*35/60), int(len(w)*50/60)):
    tmp_x.append(eg_2_x[i])
    tmp_y.append(w[i])
k_pulse_eg_2, b_pulse_eg_2 = tuple(np.polyfit(tmp_x, tmp_y, 1))
# k_pulse_eg_1 = ((w[int(len(w)*50/60)]-w[int(len(w)*30/60)])/(eg_2_x[int(len(w)*50/60)]-eg_2_x[int(len(w)*30/60)]))
for i in range(int(len(w)*35/60), int(len(w)*50/60)):
    pulse_eg_2_x.append(eg_2_x[i])
    # pulse_eg_1_y.append(w[i]-(k_pulse_eg_1*(eg_1_x[i]-eg_1_x[int(len(w)*50/60)])+w[int(len(w)*50/60)]))
    pulse_eg_2_y.append(w[i] - (k_pulse_eg_2 * (eg_2_x[i]) + b_pulse_eg_2))
pulse_fitness_eg, pt = pyplot.subplots(figsize=(16, 9), dpi=400)
# pt.axis(xmin=0, xmax=60, ymin=min(eg_2_y), ymax=max(eg_2_y))
pt.set_xlabel("Время с начала эксперимента")
pt.set_ylabel("Изменение давления")
pt.set_title("Зависимость изменения давления от времени")
pt.plot(pulse_eg_2_x, pulse_eg_2_y, label='Давление')
pt.minorticks_on()
pt.grid(which='major')
pt.grid(which='minor', linestyle=':')
i = 0
number = 0
cont = 1
aaa = []
bbb = []
while i < int(len(pulse_eg_2_x))-7000:
    i += 1
    if pulse_eg_2_y[i-4000] < pulse_eg_2_y[i] > pulse_eg_2_y[i+4000]:
        number += 1
        #aaa.append(pulse_eg_2_x[i])
        #bbb.append(pulse_eg_2_y[i])
        i += 7000
# print(number)
pt.text(48, 3, f'Пульс: {int(number/(50-35)*60)} уд/мин')
#pt.scatter(aaa, bbb, color='red', marker='o')
pulse_fitness_eg.savefig('fitness-pulse-egor.png')







pa_1_x = []
pa_1_y = []
count = 0
lenPa_1 = sum(1 for line in open('C:\\get-lab-1-main\\pasha\\report\\pasha_1.txt', 'r'))
with open('C:\\get-lab-1-main\\pasha\\report\\pasha_1.txt', 'r') as f:
    for line in f.readlines():
        count += 1
        if count > 4:
            pa_1_y.append((int(line)-b)/k)
            pa_1_x.append(count*60/lenPa_1)
rest_pa, pt = pyplot.subplots(figsize=(16, 9), dpi=400)
pt.axis(xmin=0, xmax=60, ymin=min(pa_1_y), ymax=max(pa_1_y))
pt.set_xlabel("Время с начала эксперимента")
pt.set_ylabel("Давление")
pt.set_title("Зависимость давления от времени")
number = 0
mark_x = []
mark_y = []
w = savgol_filter(pa_1_y, 101, 2)
i = 30000
lhs = max(w)
rhs = 0
cont = 1
while i < len(w)-2000:
    i += 1
    if w[i-3000] < w[i] > w[i+3000]:
        number += 1
        lhs = rhs
        rhs = w[i]
        i += 4000
    if number == 15 and cont == 1:
        mark_y.append(w[i])
        mark_x.append(pa_1_x[i])
        pt.text(pa_1_x[i]+1, w[i]+2, 'Систола')
        cont = 0
    if abs(rhs-lhs) < 0.6:
        mark_y.append(w[i])
        mark_x.append(pa_1_x[i])
        pt.text(pa_1_x[i] + 1, w[i] + 2, 'Диастола')
        break
pt.plot(pa_1_x, w, label='Давление')
pt.scatter(mark_x, mark_y, color='red', marker='o')
pt.minorticks_on()
pt.grid(which='major')
pt.grid(which='minor', linestyle=':')
rest_pa.savefig('rest-pressure-pasha.png')
pulse_pa_1_x = []
pulse_pa_1_y = []
tmp_x = []
tmp_y = []
for i in range(int(len(w)*35/60), int(len(w)*50/60)):
    tmp_x.append(pa_1_x[i])
    tmp_y.append(w[i])
k_pulse_pa_1, b_pulse_pa_1 = tuple(np.polyfit(tmp_x, tmp_y, 1))
# k_pulse_eg_1 = ((w[int(len(w)*50/60)]-w[int(len(w)*30/60)])/(eg_2_x[int(len(w)*50/60)]-eg_2_x[int(len(w)*30/60)]))
for i in range(int(len(w)*35/60), int(len(w)*50/60)):
    pulse_pa_1_x.append(pa_1_x[i])
    # pulse_eg_1_y.append(w[i]-(k_pulse_eg_1*(eg_1_x[i]-eg_1_x[int(len(w)*50/60)])+w[int(len(w)*50/60)]))
    pulse_pa_1_y.append(w[i] - (k_pulse_pa_1 * (pa_1_x[i]) + b_pulse_pa_1))
pulse_rest_pa, pt = pyplot.subplots(figsize=(16, 9), dpi=400)
# pt.axis(xmin=0, xmax=60, ymin=min(eg_2_y), ymax=max(eg_2_y))
pt.set_xlabel("Время с начала эксперимента")
pt.set_ylabel("Изменение давления")
pt.set_title("Зависимость изменения давления от времени")
pt.plot(pulse_pa_1_x, pulse_pa_1_y, label='Давление')
pt.minorticks_on()
pt.grid(which='major')
pt.grid(which='minor', linestyle=':')
i = 7000
number = 0
cont = 1
#aaa = []
#bbb = []
while i < int(len(pulse_pa_1_x))-8000:
    i += 1
    if pulse_pa_1_y[i-3000] < pulse_pa_1_y[i] > pulse_pa_1_y[i+3000]:
        number += 1
        #aaa.append(pulse_pa_1_x[i])
        #bbb.append(pulse_pa_1_y[i])
        i += 8000
# print(number)
pt.text(48, 1.5, f'Пульс: {int(number/(50-35)*60)} уд/мин')
#pt.scatter(aaa, bbb, color='red', marker='o')
pulse_rest_pa.savefig('rest-pulse-pasha.png')





pa_2_x = []
pa_2_y = []
count = 0
lenPa_2 = sum(1 for line in open('C:\\get-lab-1-main\\pasha\\report\\pasha_2.txt', 'r'))
with open('C:\\get-lab-1-main\\pasha\\report\\pasha_2.txt', 'r') as f:
    for line in f.readlines():
        count += 1
        if count > 4:
            pa_2_y.append((int(line)-b)/k)
            pa_2_x.append(count*60/lenPa_2)
fitness_pa, pt = pyplot.subplots(figsize=(16, 9), dpi=400)
pt.axis(xmin=0, xmax=60, ymin=min(pa_2_y), ymax=max(pa_2_y))
pt.set_xlabel("Время с начала эксперимента")
pt.set_ylabel("Давление")
pt.set_title("Зависимость давления от времени")
number = 0
mark_x = []
mark_y = []
w = savgol_filter(pa_2_y, 101, 2)
i = 30000
lhs = max(w)
rhs = 0
cont = 1
while i < len(w)-2000:
    i += 1
    if w[i-3000] < w[i] > w[i+3000]:
        number += 1
        lhs = rhs
        rhs = w[i]
        i += 4000
    if number == 15 and cont == 1:
        mark_y.append(w[i])
        mark_x.append(pa_2_x[i])
        pt.text(pa_2_x[i]+1, w[i]+2, 'Систола')
        cont = 0
    if abs(rhs-lhs) < 0.6:
        mark_y.append(w[i])
        mark_x.append(pa_2_x[i])
        pt.text(pa_2_x[i] + 1, w[i] + 2, 'Диастола')
        break
pt.plot(pa_2_x, w, label='Давление')
pt.scatter(mark_x, mark_y, color='red', marker='o')
pt.minorticks_on()
pt.grid(which='major')
pt.grid(which='minor', linestyle=':')
fitness_pa.savefig('fitness-pressure-pasha.png')
pulse_pa_2_x = []
pulse_pa_2_y = []
tmp_x = []
tmp_y = []
for i in range(int(len(w)*35/60), int(len(w)*50/60)):
    tmp_x.append(pa_2_x[i])
    tmp_y.append(w[i])
k_pulse_pa_2, b_pulse_pa_2 = tuple(np.polyfit(tmp_x, tmp_y, 1))
# k_pulse_eg_1 = ((w[int(len(w)*50/60)]-w[int(len(w)*30/60)])/(eg_2_x[int(len(w)*50/60)]-eg_2_x[int(len(w)*30/60)]))
for i in range(int(len(w)*35/60), int(len(w)*50/60)):
    pulse_pa_2_x.append(pa_2_x[i])
    # pulse_eg_1_y.append(w[i]-(k_pulse_eg_1*(eg_1_x[i]-eg_1_x[int(len(w)*50/60)])+w[int(len(w)*50/60)]))
    pulse_pa_2_y.append(w[i] - (k_pulse_pa_2 * (pa_2_x[i]) + b_pulse_pa_2))
pulse_fitness_pa, pt = pyplot.subplots(figsize=(16, 9), dpi=400)
# pt.axis(xmin=0, xmax=60, ymin=min(eg_2_y), ymax=max(eg_2_y))
pt.set_xlabel("Время с начала эксперимента")
pt.set_ylabel("Изменение давления")
pt.set_title("Зависимость изменения давления от времени")
pt.plot(pulse_pa_2_x, pulse_pa_2_y, label='Давление')
pt.minorticks_on()
pt.grid(which='major')
pt.grid(which='minor', linestyle=':')
i = 7000
number = 0
cont = 1
#aaa = []
#bbb = []
while i < int(len(pulse_pa_2_x))-8000:
    i += 1
    if pulse_pa_2_y[i-3000] < pulse_pa_2_y[i] > pulse_pa_2_y[i+3000]:
        number += 1
        #aaa.append(pulse_pa_1_x[i])
        #bbb.append(pulse_pa_1_y[i])
        i += 8000
# print(number)
pt.text(48, 2.5, f'Пульс: {int(number/(50-35)*60)} уд/мин')
#pt.scatter(aaa, bbb, color='red', marker='o')
pulse_fitness_pa.savefig('rest-pulse-pasha.png')




na_1_x = []
na_1_y = []
count = 0
lenNa_1 = sum(1 for line in open('C:\\get-lab-1-main\\pasha\\report\\nazar_1.txt', 'r'))
with open('C:\\get-lab-1-main\\pasha\\report\\nazar_1.txt', 'r') as f:
    for line in f.readlines():
        count += 1
        if count > 4:
            na_1_y.append((int(line)-b)/k)
            na_1_x.append(count*60/lenNa_1)
rest_na, pt = pyplot.subplots(figsize=(16, 9), dpi=400)
pt.axis(xmin=0, xmax=60, ymin=min(na_1_y), ymax=max(na_1_y))
pt.set_xlabel("Время с начала эксперимента")
pt.set_ylabel("Давление")
pt.set_title("Зависимость давления от времени")
number = 0
mark_x = []
mark_y = []
w = savgol_filter(na_1_y, 101, 2)
i = 30000
lhs = max(w)
rhs = 0
cont = 1
while i < len(w)-2000:
    i += 1
    if w[i-3000] < w[i] > w[i+3000]:
        number += 1
        lhs = rhs
        rhs = w[i]
        i += 4000
    if number == 10 and cont == 1:
        mark_y.append(w[i])
        mark_x.append(na_1_x[i])
        pt.text(na_1_x[i]+1, w[i]+2, 'Систола')
        cont = 0
    if abs(rhs-lhs) < 0.6:
        mark_y.append(w[i])
        mark_x.append(na_1_x[i])
        pt.text(na_1_x[i] + 1, w[i] + 2, 'Диастола')
        break
pt.plot(na_1_x, w, label='Давление')
pt.scatter(mark_x, mark_y, color='red', marker='o')
pt.minorticks_on()
pt.grid(which='major')
pt.grid(which='minor', linestyle=':')
rest_na.savefig('rest-pressure-nazar.png')
pulse_na_1_x = []
pulse_na_1_y = []
tmp_x = []
tmp_y = []
for i in range(int(len(w)*35/60), int(len(w)*50/60)):
    tmp_x.append(na_1_x[i])
    tmp_y.append(w[i])
k_pulse_na_1, b_pulse_na_1 = tuple(np.polyfit(tmp_x, tmp_y, 1))
# k_pulse_eg_1 = ((w[int(len(w)*50/60)]-w[int(len(w)*30/60)])/(eg_2_x[int(len(w)*50/60)]-eg_2_x[int(len(w)*30/60)]))
for i in range(int(len(w)*35/60), int(len(w)*50/60)):
    pulse_na_1_x.append(na_1_x[i])
    # pulse_eg_1_y.append(w[i]-(k_pulse_eg_1*(eg_1_x[i]-eg_1_x[int(len(w)*50/60)])+w[int(len(w)*50/60)]))
    pulse_na_1_y.append(w[i] - (k_pulse_na_1 * (na_1_x[i]) + b_pulse_na_1))
pulse_rest_na, pt = pyplot.subplots(figsize=(16, 9), dpi=400)
# pt.axis(xmin=0, xmax=60, ymin=min(eg_2_y), ymax=max(eg_2_y))
pt.set_xlabel("Время с начала эксперимента")
pt.set_ylabel("Изменение давления")
pt.set_title("Зависимость изменения давления от времени")
pt.plot(pulse_na_1_x, pulse_na_1_y, label='Давление')
pt.minorticks_on()
pt.grid(which='major')
pt.grid(which='minor', linestyle=':')
i = 7000
number = 0
cont = 1
#aaa = []
#bbb = []
while i < int(len(pulse_na_1_x))-8000:
    i += 1
    if pulse_na_1_y[i-3000] < pulse_na_1_y[i] > pulse_na_1_y[i+3000]:
        number += 1
        #aaa.append(pulse_pa_1_x[i])
        #bbb.append(pulse_pa_1_y[i])
        i += 8000
# print(number)
pt.text(48, 1.5, f'Пульс: {int(number/(50-35)*60)} уд/мин')
#pt.scatter(aaa, bbb, color='red', marker='o')
pulse_rest_na.savefig('fitness-pulse-nazar.png')






na_2_x = []
na_2_y = []
count = 0
lenNa_2 = sum(1 for line in open('C:\\get-lab-1-main\\pasha\\report\\nazar_2.txt', 'r'))
with open('C:\\get-lab-1-main\\pasha\\report\\nazar_2.txt', 'r') as f:
    for line in f.readlines():
        count += 1
        if count > 4:
            na_2_y.append((int(line)-b)/k)
            na_2_x.append(count*60/lenNa_2)
fitness_na, pt = pyplot.subplots(figsize=(16, 9), dpi=400)
pt.axis(xmin=0, xmax=60, ymin=min(na_2_y), ymax=max(na_2_y))
pt.set_xlabel("Время с начала эксперимента")
pt.set_ylabel("Давление")
pt.set_title("Зависимость давления от времени")
number = 0
mark_x = []
mark_y = []
w = savgol_filter(na_2_y, 101, 2)
i = 30000
lhs = max(w)
rhs = 0
cont = 1
while i < len(w)-2000:
    i += 1
    if w[i-3000] < w[i] > w[i+3000]:
        number += 1
        lhs = rhs
        rhs = w[i]
        i += 4000
    if number == 5 and cont == 1:
        mark_y.append(w[i])
        mark_x.append(na_1_x[i])
        pt.text(na_2_x[i]+1, w[i]+2, 'Систола')
        cont = 0
    if abs(rhs-lhs) < 0.6:
        mark_y.append(w[i])
        mark_x.append(na_2_x[i])
        pt.text(na_2_x[i] + 1, w[i] + 2, 'Диастола')
        break
pt.plot(na_2_x, w, label='Давление')
pt.scatter(mark_x, mark_y, color='red', marker='o')
pt.minorticks_on()
pt.grid(which='major')
pt.grid(which='minor', linestyle=':')
fitness_na.savefig('fitness-pressure-nazar.png')
pulse_na_2_x = []
pulse_na_2_y = []
tmp_x = []
tmp_y = []
for i in range(int(len(w)*6/60), int(len(w)*12/60)):
    tmp_x.append(na_2_x[i])
    tmp_y.append(w[i])
k_pulse_na_2, b_pulse_na_2 = tuple(np.polyfit(tmp_x, tmp_y, 1))
# k_pulse_eg_1 = ((w[int(len(w)*50/60)]-w[int(len(w)*30/60)])/(eg_2_x[int(len(w)*50/60)]-eg_2_x[int(len(w)*30/60)]))
for i in range(int(len(w)*6/60), int(len(w)*12/60)):
    pulse_na_2_x.append(na_2_x[i])
    # pulse_eg_1_y.append(w[i]-(k_pulse_eg_1*(eg_1_x[i]-eg_1_x[int(len(w)*50/60)])+w[int(len(w)*50/60)]))
    pulse_na_2_y.append(w[i] - (k_pulse_na_2 * (na_2_x[i]) + b_pulse_na_2))
pulse_fitness_na, pt = pyplot.subplots(figsize=(16, 9), dpi=400)
# pt.axis(xmin=0, xmax=60, ymin=min(eg_2_y), ymax=max(eg_2_y))
pt.set_xlabel("Время с начала эксперимента")
pt.set_ylabel("Изменение давления")
pt.set_title("Зависимость изменения давления от времени")
pt.plot(pulse_na_2_x, pulse_na_2_y, label='Давление')
pt.minorticks_on()
pt.grid(which='major')
pt.grid(which='minor', linestyle=':')
i = 7000
number = 0
cont = 1
#aaa = []
#bbb = []
while i < int(len(pulse_na_2_x))-8000:
    i += 1
    if pulse_na_2_y[i-3000] < pulse_na_2_y[i] > pulse_na_2_y[i+3000]:
        number += 1
        #aaa.append(pulse_pa_1_x[i])
        #bbb.append(pulse_pa_1_y[i])
        i += 8000
# print(number)
pt.text(11, 2.5, f'Пульс: {int(number/(12-6)*60)} уд/мин')
#pt.scatter(aaa, bbb, color='red', marker='o')
pulse_fitness_na.savefig('fitness-pulse-nazar.png')
