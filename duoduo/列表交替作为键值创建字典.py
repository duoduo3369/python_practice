'''
Created on 2012-12-29

@author: duoduo
'''
def dictFromList(keysAndValues):
    return dict(zip(keysAndValues[::2],keysAndValues[1::2]))