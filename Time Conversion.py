# Time Conversion: 12hour AM/PM format to military (24-hour) time

# define function
def timeConversion(s):
    
    # split string based on (:), convert into list
    s = s.split(':')
    
    # if AM
    if s[-1].endswith('PM'):
        
        # if hr less than 12
        if int(s[0])<12:
            
            # calculate new hr for 24hr format
            s[0] = ('%02d'%(int(s[0])+12))
            
            # remove PM string
            s[-1] =  s[-1].rstrip('PM')
        
        # if hr is 12 or greater
        else:
            # remove PM string
            s[-1] =  s[-1].rstrip('PM')
    
    # if PM
    else:
        # if hr is 12 or greater
        if int(s[0])==12:
            
            # calculate new hr for 24hr format
            s[0] = ('%02d'%(int(s[0])-12))
            # remove AM string
            s[-1] =  s[-1].rstrip('AM')
            
        else:
            # remove AM string
            s[-1] =  s[-1].rstrip('AM')
    
    # join elements with (:), convert list to string 
    s = ':'.join(s)
    print(s)

# user input
s = input()

# calling function
result = timeConversion(s)
