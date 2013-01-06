'''
Created on 06.01.2013

@author: martin
'''
from PIL import Image

class BinaryPlotter(object):
    COLOR_WHITE = (255, 255, 255)
    COLOR_BLACK = (0, 0, 0)
    COLOR_BLUE = (0, 0, 255)
    COLOR_RED = (255, 0, 0)
    COLOR_WHITE = (255,255,255)
    COLOR_YELLOW = (255,255,00)
    COLOR_GREY = (128,128,128)
    
    DEFAULT_COLORSCHEME = {"0":COLOR_BLACK, "1":COLOR_WHITE, None:COLOR_GREY}
    
    def __init__(self,colorscheme=None):
        self.colorscheme = colorscheme or self.DEFAULT_COLORSCHEME
        self.img = None
    
    def getImage(self):
        return self.img

    def dec2bin(self,dec):
        data = bin(dec)
        return data[data.find("b")+1:]
    
    def convert_data(self,data):
        # convert data and track longest bytechain
        ret = []
        len_x = 0
        len_y = len(data)
        for e in data: 
            binval = self.dec2bin(e)
            if len(binval)>len_x: len_x = len(binval)
            ret.append(binval)
        return ret,(len_x,len_y)
    
    def paint(self,data,filename=None):
        # data must be a 2D-List [ #rows   col#1(),col#2(),col#3() ]
        assert isinstance(data,list)
    
        data, (width,height) = self.convert_data(data)
        
        img = Image.new("RGB", (width, height), self.colorscheme[None])
        #draw = ImageDraw.Draw(img)
        x=0
        y=0
        for cols in data: 
            for col in cols:
                img.putpixel((x,y), self.colorscheme[col])
                x+=1
            x=0
            y+=1
        # left to right flip for so that MSB is left
        img =img.transpose(Image.FLIP_LEFT_RIGHT)
        if filename: img.save(filename)
        self.img = img
        

def primes(n,low=1):
    '''return a list of prime numbers between LOW and N'''
    '''
    taken from: http://code.activestate.com/recipes/366178-a-fast-prime-number-list-generator/  || comment
    '''
    low = low / 2 * 2 + 1   # convert LOW to odd number
    lNum = range(low,n+1,2) # create a list of all the odd numbers between LOW and N
    iRoot= n ** 0.5
    iMid = len(lNum)        # number of numbers in the list
    i = 0
    m = 3                   # 2 is removed from the list because we didn't include the even numbers, so we start with removing
                            # the 3 multiples (9,15,21 ....)
    while m < iRoot:
        if lNum[i] != 0:            # if we haven't removed the number and its multiplies already
                                    # I don't like this line, I think it might work in the original algorithm, but might make this one skip
                                    # some numbers. If it does skip numbers, remove this 'if' statement
            j = (m*m - low) / 2     # j is the _index_ of the first multiple of m to remove
            while (j<iMid):
                if (j >= 0):        # ignore indexes below zero (for obvious reasons)
                    lNum[j] = 0
                j+=m
        i += 1
        m += 2
    
    return [x for x in lNum if x != 0]


if __name__=="__main__":
    b = BinaryPlotter()
    b.paint ( primes(2**14) ,filename="primes_14bit.png" )
    b.getImage().show()
    print "-- done --"