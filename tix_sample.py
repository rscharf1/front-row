from PIL import Image, ImageFont, ImageDraw 
import os, re

def TM_sample():
    my_image = Image.open("model_tickets/TM.jpg")

    time_font = ImageFont.truetype('fonts/avenir-bold.ttf', 33)
    time_text = "11:00 AM"

    date_font = ImageFont.truetype('fonts/arial.ttf', 60)
    date_text = "Aug 31, 2021"

    stadium_text = "GRANDSTAND"
    stadium_font = ImageFont.truetype('fonts/arial.ttf', 30)

    round_text = "First Round Men's/Women's"
    round_font = ImageFont.truetype('fonts/arial.ttf', 60)

    section_text = "6A"
    section_font = ImageFont.truetype('fonts/arial.ttf', 60)

    row_text = "S"
    row_font = ImageFont.truetype('fonts/arial.ttf', 60)

    seat_text = "7"
    seat_font = ImageFont.truetype('fonts/arial.ttf', 62)

    entry_text = "COURTSIDE"
    entry_font = ImageFont.truetype('fonts/arial.ttf', 59)

    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((1035,366), time_text, (37, 150, 190), font = time_font, anchor="rm")
    image_editable.text((1035,410), date_text, (255, 255, 255), font = date_font, anchor="rm")
    image_editable.text((95,818), stadium_text, (37, 150, 190), font = stadium_font, anchor="lm")
    image_editable.text((97,875), round_text, (255, 255, 255), font = round_font, anchor="lm")
    image_editable.text((91,1020), section_text, (255, 255, 255), font = section_font, anchor="lm")
    image_editable.text((550,1020), row_text, (255, 255, 255), font = row_font, anchor="lm")
    image_editable.text((950,1020), seat_text, (255, 255, 255), font = seat_font, anchor="lm")
    image_editable.text((91,1160), entry_text, (255, 255, 255), font = entry_font, anchor="lm")

    my_image.save("result.jpg")

    print("Done")

def TM(ticket):
    # print("Making ticketmaster")

    my_image = Image.open("base_tickets/TM.jpg")

    time_text = ticket.time
    time_font = ImageFont.truetype('fonts/avenir-bold.ttf', 33)

    date_text = ticket.date + ", 2021"
    date_font = ImageFont.truetype('fonts/arial.ttf', 60)
    
    stadium_text = ticket.stadium
    stadium_font = ImageFont.truetype('fonts/avenir-bold.ttf', 30)
    
    round_text = ticket.round
    round_font = ImageFont.truetype('fonts/arial.ttf', 60)

    section_text = str(ticket.section)
    section_font = ImageFont.truetype('fonts/arial.ttf', 60)

    row_text = str(ticket.row)
    row_font = ImageFont.truetype('fonts/arial.ttf', 60)

    seat_text = str(ticket.seat)
    seat_font = ImageFont.truetype('fonts/arial.ttf', 62)

    entry_text = ticket.entry
    entry_font = ImageFont.truetype('fonts/arial.ttf', 59)

    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((1035,366), time_text, (46, 105, 216), font = time_font, anchor="rm")
    image_editable.text((1035,410), date_text, (255, 255, 255), font = date_font, anchor="rm")
    image_editable.text((95,818), stadium_text, (46, 105, 216), font = stadium_font, anchor="lm")
    image_editable.text((97,875), round_text, (255, 255, 255), font = round_font, anchor="lm")
    image_editable.text((91,1020), section_text, (255, 255, 255), font = section_font, anchor="lm")
    image_editable.text((550,1020), row_text, (255, 255, 255), font = row_font, anchor="lm")
    image_editable.text((950,1020), seat_text, (255, 255, 255), font = seat_font, anchor="lm")
    image_editable.text((91,1160), entry_text, (255, 255, 255), font = entry_font, anchor="lm")

    if ticket.time == "7:00 PM":
        time = "night"
    else:
        time = "day"

    stad = "AA2" # AA, LA, GS
    
    path = "tickets/" + stad + "/" + ticket.date + "/" + time
    # path = "tickets/" + ticket.date + "/" + time + "/" + ticket.round + "/" + ticket.stadium 
    # print(path)

    if not os.path.exists(path):
        os.makedirs(path)

    my_image.save(path + "/" + str(ticket.section) + "_" + str(ticket.row) + "_" + str(ticket.seat) + ".jpg")

class Ticket:
    def __init__(self, stadium, date, time, myround, section, row, seat, entry):
        self.stadium = stadium
        self.date = date
        self.time = time
        self.round = myround
        self.section = section
        self.row = row
        self.seat = seat
        self.entry = entry

    def printInfo(self):
        print(self.stadium, "|", self.date, "|", self.time, "|", self.round, "|", self.section, "|", self.row, "|", self.seat, "|", self.entry)

def ashe():
    stadium = "ARTHUR ASHE STADIUM"
    times = ["12:00 PM", "7:00 PM"]
    entry = "ENTER GATE 3"
    sections = [15]
    rows = ['B']
    seat_starts = [5]

    for date in dates:
        for time in times:
            myround = rounds[dates.index(date)]
            for i in range(0,len(sections)):
                for j in range(0,4):
                    tix.append(Ticket(stadium, date, time, myround, sections[i], rows[i], seat_starts[i]+j, entry))

def ashe2():
    stadium = "ARTHUR ASHE STADIUM"
    times = ["1:00 PM"]
    entry = "ENTER GATE 3"
    sections = [17, 16, 13, 22, 24, 31, 39, 51]
    rows = ['B', 'D', 'F', 'C', 'A', 'F', 'H', 'E']
    seat_starts = [1, 1, 1, 7, 5, 3, 7, 1]

    for date in dates:
        for time in times:
            myround = rounds[dates.index(date)]
            for i in range(0,len(sections)):
                for j in range(0,4):
                    tix.append(Ticket(stadium, date, time, myround, sections[i], rows[i], seat_starts[i]+j, entry))

def armstrong():
    stadium = "LOUIE ARMSTRONG STADIUM"
    times = ["11:00 AM", "7:00 PM"]
    entry = "B/COURTSIDE"
    sections = [18]
    rows = ['H']
    seat_starts = [9]

    for date in dates:
        for time in times:
            myround = rounds[dates.index(date)]
            for i in range(0,len(sections)):
                for j in range(0,4):
                    tix.append(Ticket(stadium, date, time, myround, sections[i], rows[i], seat_starts[i]+j, entry))

def grandstand():
    stadium = "GRANDSTAND"
    times = ["11:00 AM"]
    entry = "COURTSIDE"
    sections = [18, 14, 21]
    rows = ['D', 'M', 'M']
    seat_starts = [13, 1, 5]

    for date in dates:
        for time in times:
            myround = rounds[dates.index(date)]
            for i in range(0,len(sections)):
                for j in range(0,4):
                    tix.append(Ticket(stadium, date, time, myround, sections[i], rows[i], seat_starts[i]+j, entry))

def printTix():
    for ticket in tix:
        ticket.printInfo()

def makeTickets():
    # for i in range(0,30):
    #     t = tix[i]
    #     TM(t)

    for t in tix:
        TM(t)

# dates = ["Aug 30"                      , "Aug 31"                      , "Sep 1"                    , "Sep 2"                      , "Sep 3"                    , "Sep 4"                    , "Sep 5"                    , "Sep 6"                    , "Sep 7"                     , "Sep 8"                     , "Sep 9"                    , "Sep 10"                 , "Sep 10"                             , "Sep 11"                             , "Sep 12"]
# rounds = ["1st Round Men's / Women's"  , "1st Round Men's / Women's"   , "2nd Round Men's / Women's", "2nd Round Men's / Women's"  , "3rd Round Men's / Women's", "3rd Round Men's / Women's", "Round of 16 Men's/Women's", "Round of 16 Men's/Women's", "Quarterfinal Men's/Women's", "Quarterfinal Men's/Women's", "Womens Singles Semifinals", "Mens Singles Semifinals", "Men's Semifinals / Men's Dbls Final", "Women's Final / Mixed Doubles Final", "Men's Final / Women's Doubles Final"] # adjust this array to have the correct round at each date index 
dates = ["Sep 12"]
rounds = ["Men's Final / Women's Doubles Final"]
tix = []

def main():
    # ashe()
    # armstrong()
    # grandstand()
    # printTix()
    ashe2()
    makeTickets()

if __name__ == "__main__":
    main()


# each ticket is an object, stored in dictionary
# 