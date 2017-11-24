import time
import serial
import numpy as np
from sklearn import svm
import s_7_v3 as gm

def normalization (input):
    s = input.shape[0]
    for i in range (s):
        input[i,:] = input[i,:]/np.max(input[i,:])
    return input

test = serial.Serial(port="COM3",baudrate=921600)
DS1 = np.loadtxt('data/1122.txt', unpack=True, dtype='float32').reshape([64,35])
DS2 = np.loadtxt('data/1124.txt', unpack=True, dtype='float32').reshape([64,35])
DS3 = np.loadtxt('data/11242.txt', unpack=True, dtype='float32').reshape([64,35])
DS4 = np.loadtxt('data/11243.txt', unpack=True, dtype='float32').reshape([64,35])
DS = np.concatenate([DS1,DS3,DS4],1)
DS = DS.transpose()
DS = normalization(DS)

Label = np.repeat(np.array([1,2,3,4,5,6,7]), 5)
Label = np.resize(Label, 35*3)

CLF = svm.SVC()
CLF.fit(DS,Label)

input = 1


while True:
    input = raw_input(">> ")

    test.write(input + '\r\n')
    out = ' '
    time.sleep(1)
    #OUT = []
    while True:
        OUT = []
        out = ''
        while test.inWaiting() > 0:
            out += test.read()

        if out !='':
            OUT.append(out)

        if len(OUT)>0:
            sOut = OUT[0].split('\n')
            print ('length of sOut : ', len(sOut))

            inSample=np.zeros([1,len(sOut)-1])
            if len(sOut)==65:
                for j in range(len(sOut)-1):

                    inSample[0,j] = int(sOut[j])
                print inSample
                inSample = normalization(inSample)
                finalOut = CLF.predict([inSample[0,:]])
                print finalOut[0]

    #while test.inWaiting() > 0:
    #    out += test.read()
    #    OUT.append(test.read())

    #if out != ' ':
    #    print ">>" + out
    #    print len(OUT)

