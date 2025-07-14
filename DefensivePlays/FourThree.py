import numpy as np
import DPlays as dp

##Location Grid for Zones
##Deep -- 0, 1, 2, 3, 4, 5
##Middle -- 6, 7, 8, 9, 10, 11
##Short -- 12, 13, 14, 15, 16, 17
##Screens -- 18_____19______20

##Locations for Man are specific responsibilities
##ReceiverXXX pulls the equivalent receiver on the opposing depth chart, mostly used for the top two CBs in the play to shadow the top two on the other side
##SlotLeft/SlotRight will work from the outside in, taking up a Slot WR (3/4/5), then a TE on that side, then a RB
##Backfield works inside out, focusing on the backfield, then a TE, then moving out to a WR if absolutely necessary


a = dp.DefensivePlay(0)
a.FullName = "Cover 2 Man"
a.RoleFS1 = "ZoneCoverage"
a.RoleSS1 = "ZoneCoverage"
a.RoleCB1 = "ManCoverage"
a.RoleCB2 = "ManCoverage"
a.RoleLOLB = "ManCoverage"
a.RoleMLB = "ManCoverage"
a.RoleROLB = "ManCoverage"
a.LocationFS1 = 1
a.LocationSS1 = 4
a.LocationCB1 = "ReceiverOne"
a.LocationCB2 = "ReceiverTwo"
a.LocationLOLB = "SlotRight"
a.LocationMLB = "Backfield"
a.LocationROLB = "SlotLeft"

b = dp.DefensivePlay(0)
b.FullName = "Cover 2 Zone"
b.RoleFS1 = "ZoneCoverage"
b.RoleSS1 = "ZoneCoverage"
b.RoleCB1 = "ZoneCoverage"
b.RoleCB2 = "ZoneCoverage"
b.RoleLOLB = "ZoneCoverage"
b.RoleMLB = "ZoneCoverage"
b.RoleROLB = "ZoneCoverage"
b.LocationFS1 = 1
b.LocationSS1 = 4
b.LocationCB1 = 17
b.LocationCB2 = 12
b.LocationLOLB = 10
b.LocationMLB = 9
b.LocationROLB = 7

c = dp.DefensivePlay(0)
c.FullName = "Cover 3"
c.RoleFS1 = "ZoneCoverage"
c.RoleSS1 = "ZoneCoverage"
c.RoleCB1 = "ZoneCoverage"
c.RoleCB2 = "ZoneCoverage"
c.RoleLOLB = "ZoneCoverage"
c.RoleMLB = "ZoneCoverage"
c.RoleROLB = "ZoneCoverage"
c.LocationFS1 = 3
c.LocationSS1 = 10
c.LocationCB1 = 5
c.LocationCB2 = 0
c.LocationLOLB = 16
c.LocationMLB = 8
c.LocationROLB = 13