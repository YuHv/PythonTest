import selectKey as sk
import numpy
import keyDeom as kd
import testApp as ta

if __name__ == '__main__':

    sum = 200;

    # ta.app_And_key(sum)

    for i in range(100):
        radAppId = numpy.random.randint(1, sum)
        appkey = sk.seleceKeyById(radAppId)
        if appkey != 1:
            kd.Token(appkey)


