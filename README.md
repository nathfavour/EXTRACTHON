# EXTRACTHON
Extract links from your email with python...

I came upon a problem where I couldn't find a crucial registration link in my emails, and I badly needed it...

I didn't want to download a third party app like "thunderbird" to review my emails

Since i knew a little of python, I thought it'd be nice if I solved the problem with code...

That was how EXTRACTHON was born.

You can clone the repository with github CLI using "git clone xxxx" where xxxx is the link of this very repository.

Otherwise, I also included a zip in the same repository, which you can download instead if you don't (and don't want to) have git CLI.



DIRECTIONS OF USE


All you need do, is run the code with "python imap.py"

then the code will extract all the links from your email, and store them in a file. 

You can then search through the links with Visual studio code's search-file feature, or even modify my code to also do that for you - or course, if you are geeky enough

Bear these in mind:

1. You need to generate an app password in your gmail account before you can do this. search google to know how, or ChatGPT, or Bard, etc.

2. You need to insert your email username, app-password and the imap-server of the email service you use ( in the order username|password|imap-server) in the file smtps.txt. In the case of gmail, the imap-server is imap.gmail.com. 

3. If you don't specify the imap server, outlook 365 imap server will be automatically used.

4. run the code😁
