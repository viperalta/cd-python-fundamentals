# 1. Update Values in Dictionaries and Lists

from distutils.ccompiler import show_compilers

x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1.1 Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0]=15
print(x)
# 1.2 Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]["last_name"]="Bryant"
print(students)
# 1.3 In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0]="Andres"
print(sports_directory)
# 1.4 Change the value 20 in z to 30
z[0]['y']=30
print(z)

# 2.Iterate Through a List of Dictionaries

def iterateDictionary(students):
    for student in students:
        print ("first_name - "+student['first_name']+", last_name - " + student['last_name'])

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 

# 3. Get Values From a List of Dictionaries

def iterateDictionary2(key_name,list):
    for element in list:
        print(element[key_name])

iterateDictionary2('last_name', students)

# 4. Iterate Through a Dictionary with List Values

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key in some_dict.keys():
        print (str(len(some_dict[key]))+" "+key.upper())
        for value in some_dict[key]:
            print(value)

printInfo(dojo)
   

