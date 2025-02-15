#!/usr/bin/env python
import igrf
import os
from math import acos,sqrt

earth_radius=6371.2

class IGRF:
    
    def __init__(self):
       igrf.initize()
       self.BNorth=0
       self.BEast=0
       self.BDown=0
       self.BAbs=0
       self.BB0=0
       self.McIlwainL=0
       self.RigidityCutoff=0
       self.InvariantLatitude=0
       self.InvariantLambda=0
       self.InvariantRadius=0
       self.DipoleMoment=0
       self.BEquator=0

       
    def compute(self,lat,lon,alt,year):
        if year < 1990:
            raise ValueError, 'This model is valid only after 1990.'
        elif year >= 2030:
            if 'IGNORE_IGRF_BOUNDARY' in os.environ.keys():
                year = 2029.999
            else:
                raise ValueError, 'This model is valid only until 2030.'
	    #igrf.initize()
        self.DipoleMoment=igrf.feldcof(year)
        rigidity_const= 0.25 * self.DipoleMoment * earth_radius *  3e-2
        self.BNorth, self.BEast, self.BDown, self.BAbs = igrf.feldg(lat,lon,alt)
        self.McIlwainL, icode, bab1 = igrf.shellg(lat,lon,alt,self.DipoleMoment)
        val, self.BEquator, rr0 = igrf.findb0(0.05,0.001)
        if not (val and icode) : beq = self.DipoleMoment/(xl*xl*xl)
        self.BB0 = self.BAbs/self.BEquator	
        self.RigidityCutoff=rigidity_const/(self.McIlwainL*self.McIlwainL)

        if self.McIlwainL>=1:
            self.InvariantLatitude = acos(sqrt(1./self.McIlwainL))
        else: 
	        self.InvariantLatitude =  0
        if self.BB0>10:
            self.InvariantRadius = -1
            self.InvariantLambda =  0
        else:       
            rl = pow(self.BB0,-0.215108)*(1. - 0.020551*(self.BB0-1.)+ 0.0008148*((self.BB0-1.)**2))
            self.InvariantRadius= rl*self.McIlwainL
            if rl<=1: self.InvariantLambda = acos(sqrt(rl))
            else: self.InvariantLambda = 0

    def __str__(self):
        """ String formatting.
        """
        return '%s' % vars(self)




if __name__ == '__main__':
    model = IGRF()
    year = 2027.0
    model.compute(0, 315, 530, year)
    print "Babs=", model.BAbs*1e5
    print "Bx=", model.BNorth*1e5
    print "By=", model.BEast*1e5
    print "Bz=", model.BDown*1e5

    


    
    #model.compute(0, 0, 565, 2015.7)
    #print model
