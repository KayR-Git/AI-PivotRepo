def is_valid_email(email: str) -> bool:
 at = email.find("@")
 dot = email.find(".", at + 1)

 return at > 0 and dot > at + 1
 
 if "@" in email and "." in email:
  return True
 else:
  return False

email = input("Enter your email ID")
print(is_valid_email(email))          