#lets set a unique password
password = "123@2023"

#initial number of trials = 5
trials = 5

#lets loop it
while True:

  # lets take input from the user for password
  user_password = input('please Enter your password: ')

  # lets Compare both the password
  if password != user_password:

    # Reduce the by value by 1
    trials = trials - 1

    # if this the last traial
    if trials == 0:
      print("you have exceed the number of trials. LOCKED!")
      break

    print('Wrong pasword', trials, "trials left")

  else:
    print('Welcome prince')
    break
