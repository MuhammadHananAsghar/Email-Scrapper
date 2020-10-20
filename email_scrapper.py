# Email Scrapper By Muhammad Hanan Asghar
# !pip install requests
# !pip install bs4
import requests
from bs4 import BeautifulSoup as Soup
import re
print("[*] Email Scrapper By Muhammad Hanan Asghar [*]")
pattern = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"
URL = input("Enter Url : ")
r = requests.get(URL).content
emails = re.findall(pattern,str(r))
if emails == []:
  print("No Emails Found")
else:
  number = 0
  print("{} Emails Found...".format(len(emails)))
  with open("emails.txt","w") as file:
    for em in emails:
      number += 1
      print(number,"-",em)
      file.write(str(number)+" "+"-"+" "+em+"\n")
  file.close()
