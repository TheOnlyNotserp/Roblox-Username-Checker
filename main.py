import sys, fade, requests, time, json

import colorama

banner = """
                                                                                      
 █▀█ █▀█ █▄▄ █░░ █▀█ ▀▄▀ █░█ █▀ █▀▀ █▀█ █▄░█ ▄▀█ █▀▄▀█ █▀▀ █▀▀ █░█ █▀▀ █▀▀ █▄▀ █▀▀ █▀█
 █▀▄ █▄█ █▄█ █▄▄ █▄█ █░█ █▄█ ▄█ ██▄ █▀▄ █░▀█ █▀█ █░▀░█ ██▄ █▄▄ █▀█ ██▄ █▄▄ █░█ ██▄ █▀▄
"""
banner = fade.greenblue(banner)
print(banner)
time.sleep(2)
print(colorama.Fore.CYAN + "github.com/TheOnlyNotserp")
time.sleep(2)


with open("usernames.txt") as f:
	lines = f.readlines()
	for line in lines:
		user = line.rstrip()
		r = requests.get("https://auth.roblox.com/v1/usernames/validate?birthday=2000-01-01T00:00:00.000Z&context=Signup&username=" + user)
		resp = json.loads(r.text)
		msg = resp['message']
		print(user + ":", msg)
		if msg == "Username is already in use":
			with open("checked\\used.txt", "a") as f:
				f.write(user + "\n")
		elif msg == "Username not appropriate for Roblox":
			with open("checked\\inappropriate.txt", "a") as f:
				f.write(user + "\n")
		elif msg == "Username is valid":
			with open("checked\\valid.txt", "a") as f:
				f.write(user + "\n")
		elif msg == "Only a-z, A-Z, 0-9, and _ are allowed" or "Usernames can be 3 to 20 characters long":
			with open("checked\\invalid.txt", "a") as f:
				f.write(user + "\n")
		else:
			with open("checked\\invalid.txt", "a") as f:
				f.write(user + "\n")
	input("Finished checking usernames, press 'ENTER' to exit")
	sys.exit()