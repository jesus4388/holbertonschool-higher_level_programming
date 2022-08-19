#!/usr/bin/python3                                                                                                               
'# python script that takes in a URL and an email'                                                                               
from sys import argv                                                                                                             
import urllib.request                                                                                                            
import urllib.parse                                                                                                              
                                                                                                                                 
if __name__ == "__main__":                                                                                                       
        data = { "email":argv[2] }                                                                                               
        print(type(data))                                                                                                        
        print(data)                                                                                                              
        data = urllib.parse.urlencode(data)                                                                                      
        data = data.encode('utf-8')                                                                                              
        print(type(data))                                                                                                        
        with urllib.request.urlopen(argv[1], data) as resp:                                                                      
                response = resp.read() 
