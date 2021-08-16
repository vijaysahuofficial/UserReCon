#!/usr/bin/python
import pyfiglet
import socialLinks
from colorama import init, Fore
import requests
import os
init()
print(Fore.RED + pyfiglet.figlet_format("User ReCon"))
created_by = '''Vijay Sahu''' 
banner = pyfiglet.figlet_format(created_by, font='small')
print (Fore.GREEN + "Created By:\n", created_by + '\nhttps://www.github.com/vijaysahuofficial')
failed = Fore.RED +' [-] Not Found : '
found = Fore.GREEN + '[+] Found : '

outputFolder = 'output'
print('\n')

username = str(input('Enter username >>> '))

print(Fore.GREEN + "Finding Accounts")
class ReCon:
    def __init__(self,site_name, social_url, username, credits, output):
        self.site_name = site_name
        self.social_url = social_url
        self.name = username
        self.credits = credits
        self.output = output
    def find_account(self):
        try:
            response = requests.get(self.social_url.format(self.name), timeout=5) 
            if response.status_code == 200:
                print(found + self.site_name, self.social_url.format(self.name))
                
                ifexist = os.path.exists(self.output)
                if ifexist == False:
                    os.mkdir(self.output)
                    file = open(f'{self.output}/{self.name}.txt','a')
                    file.write(f'{self.social_url.format(self.name)}\n')
                elif ifexist == True:
                    file = open(f'{self.output}/{self.name}.txt','a')
                    file.write(f'{self.social_url.format(self.name)}\n')
                    
                else:
                    print(Fore.Red + "Something Went Wrong")

            else:
                print(failed + self.site_name)
        except requests.exceptions.ReadTimeout:
                print(failed + self.site_name + ' : Request timed out')
for i in socialLinks.links:
    ReCon(i, socialLinks.links[i], username, credits, outputFolder).find_account()

print('\n\n\nThanks for using UserReCon')