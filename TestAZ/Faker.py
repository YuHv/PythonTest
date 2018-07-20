import string
import random

import numpy
from faker import Factory

fake = Factory().create('zh_CN')

if __name__ == '__main__':

    # salt = ''.join(random.sample(string.ascii_letters + string.digits, numpy.random.randint(8, 16)))
    # salt = ''.join(random.sample(string.digits, 10))
    salt = numpy.random.randint(8, 16, 10)
    print(salt)