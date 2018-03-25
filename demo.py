class abcd(object):
    def __init__(self):
        print('__init__(self)')

    def __init__(self,**kargs):
        print('__init__(self,**kargs):')
        for i in kargs:
            print(i)