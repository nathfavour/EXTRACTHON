import imaplib
import sys
import email
import os
import re


# Open the file for reading
with open("smtps.txt", "r") as f:
    # Iterate over the lines in the file
    for line in f:
        # Remove extra white space from the line
        line = line.strip()
        # Split the line into parts
        parts = line.split("|")
        # Store each part as a variable
        username = parts[0]
        password = parts[1]
        # Check if there is a third part
        if len(parts) > 2:
            imap_server = parts[2]
        else:
            # Open the file for reading
            with open("switch.txt", "r") as f:
                # Read the first line of the file
                first_line = f.readline()
                # Strip off spaces on either side of the string
                first_line = first_line.strip()
                # Check if the string starts with the character "1"
                if first_line.startswith("1"):
                    # Perform an action if the string starts with the character "1"
                    print("The default imap_server will be outlook's...")
                else:
                    print(f"Error with {username}'s imap_server...")
                    print("Please either change the value of switch.txt to 1")
                    print("or specify a specific imap_server in smtps.txt")
                    sys.exit()
                                    
                                            
        # Perform an action for each line
        print(f"username: {username}, password: {password}, imap_server: {imap_server}")
        # Set up the IMAP connection
        mail = imaplib.IMAP4_SSL(imap_server)

        # Try to login
        try:
            mail.login(username, password)
        except imaplib.IMAP4.error:
            print("Error logging in", file=sys.stderr)
            sys.exit(1)

        # Print message if login was successful
        print("Logged in successfully")
        mail.select("INBOX")

        # Get all the messages in the INBOX folder
        # Search for all messages
        status, messages = mail.search(None, "ALL")
        message_numbers = messages[0].split()

        # Get the email address of the recipient or owner of the IMAP account
    

        # Create a directory named "Emails" if it doesn't exist
        if not os.path.exists("Emails"):
            os.makedirs("Emails")

        # Open a file to save the emails
        with open(f"Emails/{username}.html", "w") as f:
            # Iterate over the message numbers
            for num in message_numbers:
                # Fetch the email message by RFC822 without marking it as read (use BODY.PEEK instead of BODY)
                status, data = mail.fetch(num, "(BODY.PEEK[HEADER])")
                # Get the email message object
                msg = email.message_from_bytes(data[0][1])
                # Get the subject of the email
                subject = msg["subject"]
                # Write the subject to the file
                f.write(f"<h1>{subject}</h1>\n")
                # Fetch the body of the email message without marking it as read (use BODY.PEEK instead of BODY)
                status, data = mail.fetch(num, "(BODY.PEEK[TEXT])")
                # Write the body to the file
                f.write(data[0][1].decode())
                f.write("\n")
                f.write("\n")
                f.write("\n")
                f.write("\n")
                f.write("MOVING TO THE NEXT MESSAGE...")
                f.write("\n")
                f.write("\n")
                f.write("\n")
                f.write("\n")
                f.write("\n")


        # Close the IMAP connection
        mail.close()
        mail.logout()


        # Open the file
        with open(f"Emails/{username}.html", 'r') as f:            # Read the file contents
            contents = f.read()

        # Extract all the links from the file
        links = re.findall(r"https?://\S+", contents)

        # Remove duplicates from the list of links
        links = set(links)

        # Create a directory named "Links" if it doesn't exist
        if not os.path.exists("Links"):
            os.makedirs("Links")

        # Write the links to a new file
        with open(f"Links/{username}.txt", "w") as f:
            for link in links:
                f.write(link + "\n")