route -n 
"""
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.2.1     0.0.0.0         UG    600    0        0 wlp3s0
169.254.0.0     0.0.0.0         255.255.0.0     U     1000   0        0 wlp3s0
192.168.2.0     0.0.0.0         255.255.255.0   U     600    0        0 wlp3s0
"""

arpspoof -i eth0 target_ip who_am_i_ip

ping facebook.com

#trace every route
traceroute facebook.com
#or
mtr facebook.com

mtr playthough.com
"""
Host                                                        Loss % Snt   Last   Avg  Best  Wrst StDev
1. _gateway                                                  0.0%    25    5.3   3.5   2.6   6.1   0.9
2. 93.155.1.196                                              0.0%    25    9.4  10.9   9.2  23.4   3.3
3. 81.212.78.29.static.turktelekom.com.tr                    0.0%    25   11.6  11.4   9.6  14.5   1.3
4. 212.156.251.216.static.turktelekom.com.tr                 0.0%    25   10.1  11.8   9.8  18.8   2.1
5. 00-ebgp-gayrettepe-k---00-gayrettepe-xrs-t2-2.statik.tur  0.0%    25   10.5  10.5   9.3  14.0   1.0
6. 306-mil-col-2---00-gayrettepe-xrs-t2-2.statik.turkteleko  0.0%    25   43.1  45.9  43.1  69.2   5.0
7. 81.25.202.209                                             0.0%    25   56.9  57.0  54.2  78.9   5.5
8. ae-2.r24.frnkge08.de.bb.gin.ntt.net                       0.0%    25   62.6  62.6  61.1  65.0   0.9
9. ae-5.r24.londen12.uk.bb.gin.ntt.net                       0.0%    25   70.7  71.7  69.3  80.3   2.5
10. ae-8.r02.londen03.uk.bb.gin.ntt.net                       0.0%    25   77.7  79.6  77.0 100.0   4.5
11. 212.119.4.66                                              0.0%    25   68.8  71.3  68.4  80.2   3.7
12. 54.239.100.212                                            0.0%    25   68.8  70.7  68.8  79.2   2.1
13. 52.94.35.17                                               0.0%    25   71.1  72.0  69.8  80.1   2.1
14. 52.94.35.56          
""" 
