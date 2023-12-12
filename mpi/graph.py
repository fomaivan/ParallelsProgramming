import re
import matplotlib.pyplot as plt

arr = {1000: dict(), 1000000: dict(), 100000000: dict()}

with open ('bin/data.txt') as file:
    while True:
        line = file.readline()
        if not line:
            break
        tmp = re.findall(r"[-+]?\d*\.\d+|\d+", line)
        arr[int(tmp[0])][int(tmp[1])] = (float(tmp[2]))

fig, ax = plt.subplots(nrows=1, ncols=3)
fig.set_size_inches(13, 6)
fig.suptitle('Зависимость время от кол-ва процессов N')
ax[0].plot(list(arr[1000].keys()), list(arr[1000].values()), label='10^3')
ax[0].title.set_text('N = 10^3')
ax[0].set_ylabel('time')
ax[0].set_xlabel('num_of_process')
ax[1].plot(list(arr[1000000].keys()), list(arr[1000000].values()), label='10^6')
ax[1].title.set_text('N = 10^6')
ax[1].set_ylabel('time')
ax[1].set_xlabel('num_of_process')
ax[2].plot(list(arr[100000000].keys()), list(arr[100000000].values()), label='10^8')
ax[2].title.set_text('N = 10^8')
ax[2].set_ylabel('time')
ax[2].set_xlabel('num_of_process')
fig.tight_layout()

plt.savefig('output.png')

