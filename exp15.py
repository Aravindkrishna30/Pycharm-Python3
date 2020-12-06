#import arra as ar
from array import *
vals= array('f', [2,3,4,5,-1,3.4,6,7,8])
newArr=array(vals.typecode,(a*a for a in vals ))
for n in newArr:
     print(n)