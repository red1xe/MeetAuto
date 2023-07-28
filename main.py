import webbrowser
import time
import schedule
import pickle


def open_link(link):
    webbrowser.open(link)

#Function to load meetings data from a file
def load_meetings_data():
    try:
        with open('meetings_data.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []


Meetings = load_meetings_data()

def monday(time, link):
    schedule.every().monday.at(time).do(open_link, link)
def tuesday(time, link):
    schedule.every().tuesday.at(time).do(open_link, link)
def wednesday(time, link):
    schedule.every().wednesday.at(time).do(open_link, link)
def thursday(time, link):
    schedule.every().thursday.at(time).do(open_link, link)
def friday(time, link):
    schedule.every().friday.at(time).do(open_link, link)


def main():
    for meet in Meetings:
        if meet["day"] == "Monday":
            monday(meet["time"], meet["link"])
        elif meet["day"] == "Tuesday":
            tuesday(meet["time"], meet["link"])
        elif meet["day"] == "Wednesday":
            wednesday(meet["time"], meet["link"])
        elif meet["day"] == "Thursday":
            thursday(meet["time"], meet["link"])
        elif meet["day"] == "Friday":
            friday(meet["time"], meet["link"])

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
