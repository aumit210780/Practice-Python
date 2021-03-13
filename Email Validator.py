"""
For valid email:
     1. there should be at least 2 characters before the @
     2. there should be one @
     3. there should be .  after @
     4. there should be at least two characters between . and @
     5. there should be at least two characters after the dot
"""
email = input("Enter an email address to check whether it is valid or not: ")
haveattherate = email.find("@")>-1
havefirstchar = len(email[:email.index("@")])>2
havedot = email.find(".")>-1
btnatanddot = len(email[email.index("@")+1:email.rindex(".")])>2
afterlastdot = len(email[email.rindex(".")+1:])>2

if haveattherate and havefirstchar and havedot and btnatanddot and afterlastdot:
     print("EMAIL is valid")
else:
     print("Invalid Email")

