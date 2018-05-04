students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},#students[0], you want to extract 
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def names(students):
    for i in range(len(students)):
        print "{first_name} {last_name}".format(**students[i])



users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def name2(users):
    for i in users.keys():
        print i
        for key in range(len(users[i])):
            print "{} - {} {} - ".format([key+1],)
  
       
 
name2(users)