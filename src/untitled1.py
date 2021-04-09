# -*- coding: utf-8 -*-


import memcache

if __name__ == '__main__':
    shared = memcache.Client(['127.0.0.1:11211'], debug=0)    
    print (shared.get('Value'))

