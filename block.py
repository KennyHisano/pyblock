#!/usr/bin/python

import hashlib



class blockHead():
	

    def __init__(self,ver,prev_hash,merkRoot,timestamp,diffic,nonce):
        self.ver = ver
        self.prev_hash = prev_hash
        self.merkRoot = merkRoot
        self.timestamp =  timestamp
        self.diffic = diffic
        self.nonce = nonce 

#    def hash(self):