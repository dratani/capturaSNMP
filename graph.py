import rrdtool
variables = {'IfLastChange':'rate=100,initial=100000000',
             'IfInOctets':'rate=200,deviation=10,cumulative=1',
             'IfInUcastPkts':'rate=18,initial=1,cumulative=1',
             'ifInNUcastPkts':'numeric|rate=2,cumulative=1',
             'IfInDiscards':'scale=0.4,offset=1,deviation=1,function=sin,cumulative=1',
             'IfInErrors':'scale=0.6,offset=1,deviation=1,function=cos%3.1416/2,cumulative=1',
             'ifInUnknownProtos':'rate=0.1,deviation=2,cumulative=1',
             'ifOutOctets':'rate=100,deviation=5,cumulative=1',
             'ifOutUcastPkts':'rate=9,initial=1,cumulative=1',
             'ifOutNucastPkts':'rate=1,cumulative=1',
             'ifOutDiscards':'scale=0.6,offset=1,deviation=1,function=sin,cumulative=1',
             'ifOutErrors':'scale=0.4,offset=1,deviation=1,function=cos,cumulative=1',
            'ifOutQLen': 'function=pow%<time>%2,scale=100,offset=100,rate=150'}
title = 'ifInErrors'
end = rrdtool.last('netCounter.rrd')
start = end - 7400
for x,y in variables.items():
    ret = rrdtool.graph("IMG/"+x +"Counter2.png",
                    "--start", str(start),
                    "--end",str(end),
                    "--title", x+"Counter",
                    "--color", "ARROW#009900",
                    "DEF:input=netCounter.rrd:"+x+":AVERAGE",
                    "COMMENT:"+y,
                    "LINE1:input#00FF00:"+x)


