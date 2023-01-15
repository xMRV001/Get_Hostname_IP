print("----------------------------------")
print("    This Code Was Made By MRV     ")
print("----------------------------------")

# Library to get IP from URL.



import socket

# defenetion of our tool which is Get_IP.

def Get_IP():
    
    #  User input.
    
    hostname = input('Please input website address (URL): ')
    
    # try and except statement.
    
    try:
        
        # if the url is correct it will be printed.
        
        print(f'{hostname}')
        
        # print IP word then use the method from socket lib to get URL IP and print it.
        
        print(f'IP: {socket.gethostbyname(hostname)}')
    
    # Exception of any error.
        
    except socket.gaierror as e:
        
        # print invalid host and the error with it so user can know what he did wrong.
        
        print('Invalid hostname, Error is : {e}')

Get_IP()