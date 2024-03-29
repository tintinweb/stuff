BinaryPlotter
=====

Plot binary images based on a list of decimal values

    # define a colorscheme by passing colorscheme={'0':(R,G,B),'1':(R,G,B),None:(R,G,B)} 
    # None = default background color; default scheme = 0=black, 1=white, default=Grey
    b = BinaryPlotter()
    # print all primes from 1 to 2^16 (each prime is one row in the binary image, MSB left)
    # optionally save it as test1.png
    # primes method is defined in BinaryPlotter; primes( max_value, low=1)
    b.paint ( primes(2**8) ,filename="test1.png" )
    # get image ref (PIL)
    b.getImage().show()
    print "-- done --"
    

Dependencies
-------------

Python PIL - http://www.pythonware.com/products/pil/


Examples:
---------

primes up to 10 bits:
![BinaryPlot1](https://github.com/tintinweb/stuff/raw/master/BinaryPlotter/primes_upto1024.png "BinaryPlot of Primes up to 1024")   

primes up to 14 bits:
![BinaryPlot2](https://github.com/tintinweb/stuff/raw/master/BinaryPlotter/primes_14bit.png "14 Bit primes binary plot")  

 

