import time
import rrdtool
from getSNMP import consultaSNMP

input = []
oid = []

for x in range (9,22):
    oid.append("1.3.6.1.2.1.2.2.1."+str(x)+".1")

while 1:
    input.clear()
    for x in oid:
        input.append(consultaSNMP('variation/virtualtable','8.12.0.201', x,'1024'))
    valor ="N:"
    valor += ":".join(input)
    print (valor)
    rrdtool.update('netCounter.rrd', valor)
    rrdtool.dump('netCounter.rrd','netCounter.xml')
#     time.sleep(1)
