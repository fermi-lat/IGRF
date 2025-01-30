G77 = /usr/bin/g77
#F2PY = f2py2.6
#F2PY = /opt/TWWfsw/bin/f2py
F2PY = /sdf/group/fermi/a/isoc/flightOps/volumes/vol4/rhel6_gcc44/install_20150313_64bit/bin/f2py2.6

LDFLAGS = -shared 

igrf.so: igrf_sub.f
	$(F2PY) -c -m igrf igrf_sub.f
	
clean:
	rm -f igrf.so IGRF.pyo IGRF.pyc
