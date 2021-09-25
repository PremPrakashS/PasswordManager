import json
import getpass

user_dict = {
    'app_name' : '',
    'website_name' : '',
    'username' : '',
    'password' : '',
    'other_details' : '',
}

details = {

}

def getdetails():
    app_name = input('Enter the Application Name : ')
    user_dict['website_name'] = input('Enter the Website Name : ')
    user_dict['username'] = input('Enter the username : ')
    user_dict['password'] = input('Enter the password : ')
    user_dict['other_details'] = input('Enter other info : ')
    
    details = {
        app_name : {
            'WebsiteName' : user_dict['website_name'],
            'username' : user_dict['username'],
            'password' : user_dict['password'],
            'other_details' : user_dict['other_details']
        }
    }

def saveDetailsInFile():
    with open("file.json", 'a') as file:
        json.dump(details, file, indent=4)

# def readDetailsFromFile():
#     with open('file.json', 'r') as file_reader:
#         data = json.load(file_reader)

getdetails()

saveDetailsInFile()

# readDetailsFromFile()

#getdetails()

#y = json.dumps(user_dict)

#print(y)