BinaryPlotter
=====

Plot binary images based on a list of decimal values

    b = BinaryPlotter()
    # print all primes from 1 to 2^16 (each prime is one row in the binary image, MSB left)
    # optionally save it as test1.png
    # primes method is defined in BinaryPlotter; primes( max_value, low=1)
    b.paint ( primes(2**8) ,filename="test1.png" )
    # get image ref (PIL)
    b.getImage().show()
    print "-- done --"
    

Prints this neat picture:

![BinaryPlot1](https://github.com/tintinweb/stuff/raw/master/BinaryPlotter/primes_upto1024.png "BinaryPlot of Primes up to 256")   

![BinaryPlot2](https://github.com/tintinweb/stuff/raw/master/BinaryPlotter/primes_14bit.png "14 Bit primes binary plot")  

 
Dependencies
-------------

Python PIL - http://www.pythonware.com/products/pil/
