import requests as r

die = open('Die.txt','w')
work = open('Work.txt','w')

tokens = open("list.txt", 'r').read()
url = "https://discordapp.com/api/v6/users/@me/library"

tokens = tokens.split('\n')

for token in tokens:
    header = {
        "Content-Type": "application/json",
        "authorization": token
    }
    code = r.get(url, headers=header).status_code
    if (code == 200):
        print(f"WORK - {token}\n")
        work.write(token + "\n")
    else:
        print(f'DIE - {token}\n')
        die.write(token+ "\n")