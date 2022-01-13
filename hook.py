import sys
import json

def checkerr(errcode):
	if errcode == 204:
		return False
	else:
		return True


def main():
	print("\n\nWebhook sender by Someone1611")
	print("Send any message any discord webhook")
	print("No colorama, no beauti design for easy to use and compatibility, performance")
	print("Project's GitHub: https://github.com/Someone8859/discordwebhook-sender")
	print("If you want to contribute, report error, it's free to email the author and create pull requests.")
	print("This program is licensed with the AbsOpenLicense, mean it is always open-source even free or commercial.")
	print("At least the core is open-source. \n\n\n")

	url = input("Enter your webhook URL: ")
	name = input("Enter your webhook name: ")
	print("Please enter which mode do you want to send. 0 for input text, 1 to read all content in a file and send it to the webhook")
	mode = int(input("Enter mode to send: "))

	if mode == 0:
		print("")
		txt = input("Enter what to send: ")
		data = {
			"username": name, 
			"content": txt
		}

		r = requests.post(url, data)

		if checkerr(r.status_code) == False:
			print(f"Hook {name}, mode {mode} sent [SUCCESS]")
		else:
			print(f"Hook {name}, mode {mode} sent [FAILURE]")
			print("\nDebugging information:")
			print(f"Error code: {r.status_code}")
			print(f"Response text: {r.text}")


	elif mode == 1:
		print("First fill the file with your content. ")
		file = input("Enter path to file: ")

		try:
			ftxt = open(file, "r")
		except FileNotFoundError:
			print("File not found.")
			sys.exit(1)
		filecontent = ftxt.read()

		data = {
			"username": name, 
			"content": filecontent
		}

		r = requests.post(url, data)

		if checkerr(r.status_code) == False:
			print(f"Hook {name}, mode {mode} sent [SUCCESS]")
		else:
			print(f"Hook {name}, mode {mode} sent [FAILURE]")
			print("\nDebugging information:")
			print(f"Error code: {r.status_code}")
			print(f"Response text: {r.text}")

	else:
		print("Error: Choose mode 0 or 1 only.")
		sys.exit(-1)


if __name__ == "__main__":
	print("Testing the imports...")
	try:
		import requests
		print("Requests was found. Going ahead...")
	except ModuleNotFoundError:
		print("The requests module was not found on your machine. Please install it by pip: pip install requests")
		sys.exit(-1)
	try:
		main()
	except KeyboardInterrupt:
		print("\n\n\nKeyboardInterrupt >>> Exiting")
		sys.exit(0)
