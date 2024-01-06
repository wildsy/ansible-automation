import timeit
import os
start = timeit.default_timer()
os.system("ansible-playbook main.yml")
stop = timeit.default_timer()
waktu = stop - start
print("waktu : %.2f detik" % waktu)