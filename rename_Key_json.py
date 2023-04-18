
# initialising dictionary
ini_dict = {'a': 1, 'b': 5,
            'c': 10, 'd': 15}
 
# initialising list
ini_list = ['nikhil', 'vashu', 'vashu', 'akshat']
 
# printing initial json
print("initial 1st dictionary", ini_dict)
 
# changing keys of dictionary
final_dict = dict(zip(ini_list, list(ini_dict.values())))
 
# printing final result
print("final dictionary", str(final_dict))