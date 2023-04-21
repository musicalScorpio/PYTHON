import pylab
import random

pylab.figure(1)
                                         
pylab.plot([1,2,3,4],[1,2,3,4])
pylab.plot ([1,2],[6,8])
pylab.plot([5,10])
                                                 
#pylab.savefig('FirstFigure')
                                                 
#pylab.show()


#Plot compound interest for 20 years 
def calculateCompoundInterest():
      principal =10000
      interest =0.05
      values=[]
      for n in range(20+1):
          values.append(principal)
          principal +=(interest * principal)

      return values

values = calculateCompoundInterest()
print("Now plotting compound interest ...."+ str(values))
pylab.plot(values)
pylab.title('Compound interest growth of 10K at 5 percent')
pylab.xlabel ('Years in compounding')
pylab.ylabel ('values of principal')
pylab.show()







