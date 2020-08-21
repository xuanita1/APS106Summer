# lab3
#Write a function that is passed the length (l) and width (w) of a rectangle and the
#coordinates (x, y) of a point (in that order)
def rectangle_point(l,w,x,y):
    """
    (float,float,float,float) -> NoneType
    Input:  l, the x direction length of the rectangle, w, the y direction length of the rectangle, x, the x-coordinate of a point, and y, the y-coordinate of a point. 
    
    Output: A string representing the quadrant of the point as a Roman numeral between I and IV, and a string indicating if the point lies 'inside the rectangle' or 'outside the rectangle' of length l and width w centered at the origin.
    
    If the calculations determine that the length or width are less than or equal to zero, return 'invalid length' or 'invalid width' as the second string in the list.
    
    >>>rectangle_point (5,4,3,1)
    ['I', 'outside the rectangle']

    >>>rectangle_point (-5,4,3,1)
    ['I', 'invalid length']

    """
    #Determine quadrant point is located in
    
    if(x > 0 and  y > 0):
        first_element = "I"
    elif( x < 0 and y > 0):
        first_element = "II"
    elif( x < 0 and y < 0):
        first_element = "III"
    elif ( x > 0 and y < 0): 
        first_element = "IV"
        
    
    #Is the point inside or outside the rectangle
    
    if l <= 0:
        second_element = "invalid length"
    elif w <= 0:
        second_element = "invalid width" 
    elif abs(x) > (l/2) or abs(y) > (w/2):
        second_element = "outside the rectangle"
    else: 
        second_element = "inside the rectangle" 
    
    #organize results into a list
    
    print(first_element)
    print(second_element)
    
    

rectangle_point(5,4,-3,1)
    
    