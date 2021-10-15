#!/usr/bin/env python3
# importing the libraries
from bs4 import BeautifulSoup
import requests
import os
import webbrowser
import dmenu
import sys
import wget
import datetime
import time
import subprocess

#start at page
site_url=str(input("url? "))
novel_name = str(input("Novel Name? "))
novel_name = novel_name.replace(" ", "_").lower()
url_ext=""
final_text= ""
url=site_url+url_ext
pages_amouth = int(input("How meny pages? "))
print("Enter the href text for the (Next) button")
next_btn = input("(Next) button text? ")
print("End of chaper text line? ")
txt_end = str(input("text? "))
current_page=0

for x in range(pages_amouth):
	page = requests.get(url)
	time.sleep(0.5)
	soup = BeautifulSoup(page.content, 'html.parser')
	time.sleep(0.5)
	for link in soup.find_all('a'):
	    if str(link.get_text()) == next_btn:
	    	next_url = link.get('href')
	    	break
	button=0
	for link in soup.find_all('p'):
		if txt_end in str(link.get_text()):
			button+=1
		else:
			final_text+=str(link.get_text())+"\n"
		if button>1:
			final_text+="\n\n"
			break
	print("page:"+str(current_page)+" loaded")
	final_text+=str(next_url)+"\n\n"
	final_text+="<///////////////////////////// page:"+str(current_page)+"\n\n"
	url = next_url
	current_page+=1
print("next_url: "+str(next_url))
print("loading complete")
print("creating the file...")
with open(novel_name+'.txt', 'w') as f:
    f.write(final_text)
print("file was created")
#print("convert txt to epub")
bashCommand = "ebook-convert "+novel_name+".txt "+novel_name+".epub"
print(bashCommand)
print("convertion complete")