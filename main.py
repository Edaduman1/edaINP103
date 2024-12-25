Alter =int(input ("Geben Sie Ihr Alter ein"))
note =float(input("Geben Sie Ihre Abschlussnote ein"))

if Alter<=20 or Alter>=50:
 print("Alter nicht geeignet")
else:
  if note>80:
   print("Kandidat geeignet")
  else:
    print("Kandidat nicht geeignet")
  