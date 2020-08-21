def minmp(filename, compound_formula):
    """(str, str) -> (str, int)
    When passed a filename with a listing of elements and properties and a compound_formula. Returns a tuple where the first element is the lowest melting point element in the compound and the second element is it's corresponding melting point.
    >>>minmp("elements.txt", "K1Fe4")
    'K', 336
    >>>minmp("elements.txt", "Fe6Cr1")
    'Fe', 1811
    """
    saved_list=[]
    lowest_mp = 3687.15
    lowest_element=''
    with open("elements.txt","r") as elements_text: 
        database= molform(compound_formula)
        #stores elements in a list so we can search for them in the text
        elements= list(database.keys())
        #loops through text line by line and searches for each element in the elements list. if found, saves the list. 
        for line in elements_text:
            new_line = line.split("\t")
            for element in elements:
                if element in new_line:
                    saved_list.append(new_line)
        #loops through saved list to find the element with the lowest melting point
        for sublist in saved_list:
            comparison_mp= int(sublist[1])
            if comparison_mp<lowest_mp:
                lowest_mp=comparison_mp
        lowest_mp=str(lowest_mp)
        #loops through saved list to find element corresponding to lowest melting point
        for final_sublist in saved_list:
            if lowest_mp in final_sublist:
                lowest_element = final_sublist[0]
                lowest_mp= final_sublist[1]
        return (lowest_element,int(lowest_mp))                
    
def molform(compound_formula):
    #"""(str) -> dictionary
    #When passed a string of the compound formula, returns a dictionary with a string of the element symbol as the key and the number of atoms of that element as the value.
    #>>>molform("C2H6O1")
    #{'C':2, 'H':6, 'O':1}
    #>>>molfor("C1H4")
    #{'C':1, 'H':4}
    #"""
    isolated_elements=[]
    corresponding_numbers=[]
    dictionary={}
    for i in range(len(compound_formula)):
        if compound_formula[i].isupper():
            char= compound_formula[i]
            if compound_formula[i+1].islower():
                char+=compound_formula[i+1]
            isolated_elements.append(char)
        if compound_formula[i].isnumeric():
            corresponding_numbers.append(compound_formula[i])
    dictionary = dict(zip(isolated_elements, corresponding_numbers))
    return dictionary
values = minmp("elements.txt", "Fe2O3")
print(values)