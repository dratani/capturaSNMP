import rrdtool

variables = ['IfLastChange','IfInOctets','IfInUcastPkts','ifInNUcastPkts','IfInDiscards','IfInErrors','ifInUnknownProtos','ifOutOctets','ifOutUcastPkts', 'ifOutNucastPkts','ifOutDiscards',
             'ifOutErrors','ifOutQLen']

ret = rrdtool.create("netCounter.rrd",
                     "--start",'N',
                     "--step",'60',
                     (["DS:"+x+":COUNTER:600:U:U" for x in variables]),
                     "RRA:AVERAGE:0.5:1:30",
                     "RRA:AVERAGE:0.5:6:100")

if ret:
    print (rrdtool.error())
