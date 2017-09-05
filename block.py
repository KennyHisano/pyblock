#!/usr/bin/python

import hashlib



class blockHead():
	

    def __init__(self,ver,prev_hash,merkRoot,timestamp,diffic=0,nonce=0):
        self.ver = ver
        self.prev_hash = prev_hash
        self.merkRoot = merkRoot
        self.timestamp =  timestamp
        self.diffic = diffic
        self.nonce = nonce 


    def __len__(self):
    	return 'Nonce {}'.format(self.nonce)
#    def hash(self):




class block(blockHead):


	def __init__(self,size,txcount,tx):
		self.size = size
		self.txcount = txcount
		self.tx = tx