from UI.Login import login
import threading
from Web_Automation.web_automate import open_website


while True:
    website_name = input("Enter website name: ")
    open_website(website_name)
