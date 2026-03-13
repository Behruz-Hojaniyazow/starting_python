#login or create a new account
login = {
        "behruz" : 260708,
        "adyl" : 241008,
        "mahmut" : 031010,
        "jawahyr" : 110508,
        "sardar" : 240808
}
#asking from the user
user =input("enter the name").lower()
user2 = input("enter the code")
for name, code in login.items():
  if user == name and user2 == code:
    print("Welcome to our community")
  elif user == name or user2 == code:
    print("incorrect password")
  else:
   print("create a new account")