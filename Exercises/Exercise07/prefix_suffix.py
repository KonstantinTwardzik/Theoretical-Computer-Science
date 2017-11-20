'''
Created on 20.11.2017

@author: Konstantin
'''
def prefix_set(word):
    prefixList = []
    length = len(word) + 1
    for i in range(length):
        prefixList.append(word[0:i])
    return prefixList
        
def suffix_set(word):
    suffixList = []
    length = len(word) + 1
    for i in range(length):
        suffixList.append(word[i:length])
    return suffixList
    
    