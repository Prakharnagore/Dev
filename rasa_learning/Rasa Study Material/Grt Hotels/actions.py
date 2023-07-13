
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from Submit_details import dataupdate
from Confirmation_number_submit import datatoget
import mysql.connector
from rasa_sdk.events import UserUtteranceReverted
import smtplib


class Actiongreet(Action):

    def name(self) -> Text:
        return "action_greet_user"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_greet_user")

        return [UserUtteranceReverted()]


class ActionSend_mail_to_me(Action):

    def name(self) -> Text:
        return "action_send_mail"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        to = tracker.get_slot('el')
        ansk = f'"{to}"'

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # connect to smtp server
        server.login("sauravemail@gmail.com", "Apeksha%1991")
        # you can write your mail and or get it from the slots with tracker.get_slot
        # if you are using your email is better that you dont pass it through the code for security u can
        # set path variables with email and password and use them instead
        Subject = "list of customer at our hotel to look into"
        Body = "This is the mail and name of the client"
        fromdate = tracker.get_slot("fromdate")
        todate = tracker.get_slot("todate")
        rooms = tracker.get_slot("room")
        names = tracker.get_slot('names')
        emails = tracker.get_slot('email_customer')
        msg = "Subject: {} \n\n {} \n Name : {} \n Email: {} \n Booking date : {} \n checkoutdate : {} \n Rooms : {}".format(
            Subject, Body, names, emails, fromdate, todate, rooms)  # creating the message

        server.sendmail(  # send the email
            "These are your details",
            ansk,
            msg)
        server.quit()

        dispatcher.utter_message(" Email of all the information about the customer send  to the requested email")


class Actionubmit(Action):

    def name(self) -> Text:
        return "action_submits"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        #dispatcher.utter_message(text="Your name is {0}\n your fromdate is {1}\n your todate is {2}\n rooms is {3}\n".format(
        #    tracker.get_slot("name"),tracker.get_slot("a"),tracker.get_slot("kj"),tracker.get_slot("nf")))
        dataupdate(tracker.get_slot("names"),tracker.get_slot("fromdate"),tracker.get_slot("todate"),tracker.get_slot("room"),tracker.get_slot("email_customer"))
        #dispatcher.utter_message("thanks for the information")

        return []


class ActionSendmail23(Action):

    def name(self) -> Text:
        return "action_all_information"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        tos = "sauravemail@gmail.com"
        anskk = f'"{tos}"'


        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # connect to smtp server
        server.login("sauravemail@gmail.com", "Apeksha%1991")
        # you can write your mail and or get it from the slots with tracker.get_slot
        # if you are using your email is better that you dont pass it through the code for security u can
        # set path variables with email and password and use them instead
        Subject = "list of customer at our hotel to look into"
        Body = "This is the mail and name of the client"
        fromdate = tracker.get_slot("fromdate")
        todate = tracker.get_slot("todate")
        rooms = tracker.get_slot("room")
        names = tracker.get_slot('names')
        emails = tracker.get_slot('email_customer')
        feedback = tracker.get_slot('feedback')
        msg = "Subject: {} \n\n {} \n Name : {} \n Email: {} \n Booking date : {} \n checkoutdate : {} \n Rooms : {} \n feedback: {} \n".format(Subject, Body, names, emails, fromdate, todate, rooms, feedback)  # creating the message

        server.sendmail(  # send the email
            "Details about the customer for the hotel personal",
            anskk,
            msg)
        server.quit()

        #dispatcher.utter_message(" Email sended ! to the requested email")


class Actioneshubishs(Action):

    def name(self) -> Text:
        return "action_submit_value"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        #dispatcher.utter_message(text="Your name is {0}\n your fromdate is {1}\n your todate is {2}\n rooms is {3}\n".format(
        #    tracker.get_slot("name"),tracker.get_slot("a"),tracker.get_slot("kj"),tracker.get_slot("nf")))
        datatoget(tracker.get_slot("names"),tracker.get_slot("email_customer"),tracker.get_slot("confirm"))
        #dispatcher.utter_message("thanks for the information")

        return []


class Sendmail23s(Action):

    def name(self) -> Text:
        return "action_con_all"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        tos = "sauravemail@gmail.com"
        anskk = f'"{tos}"'


        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # connect to smtp server
        server.login("sauravemail@gmail.com", "Apeksha%1991")
        # you can write your mail and or get it from the slots with tracker.get_slot
        # if you are using your email is better that you dont pass it through the code for security u can
        # set path variables with email and password and use them instead
        Subject = "list of customer at our hotel to look into"
        Body = "This is the mail and name of the client"

        confirmroomnumber = tracker.get_slot("confirm")
        names = tracker.get_slot('names')
        emails = tracker.get_slot('email_customer')
        feedback = tracker.get_slot('feedback')
        msg = "Name : {} \n Email: {} \n confirmroomnumber: {} \n feedback: {} \n".format(names, emails, confirmroomnumber,feedback)  # creating the message

        server.sendmail(  # send the email
            "Details about the customer for the hotel personal",
            anskk,
            msg)
        server.quit()


class Actioncustomer(Action):

    def name(self) -> Text:
        return "action_confirmation_value"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mydb = mysql.connector.connect(host="localhost", port='3308', user="root", passwd="1234", database='hotelsbot')

        mycursor = mydb.cursor()

        sqls = 'select confirmnumber from hotelconfirm'

        mycursor.execute(sqls)

        eskls = tracker.get_slot("confirm")
        print(eskls)

        ns = list(mycursor)
        print(ns)

        out = [item for t in ns for item in t]
        print(out)
        print(type(out))
        if eskls in out:
            dispatcher.utter_message("value in this database \n you are staying for 2 nights with us.")
        else:
            dispatcher.utter_message("no value is there in the database")

        return []


class Actioncarousel(Action):

    def name(self) -> Text:
        return "action_carousel"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        data = [{"title":"hello", "name":"DELUXE SUITE", "image":"https://imgcy.trivago.com/c_limit,d_dummy.jpeg,f_auto,h_1300,q_auto,w_2000//uploadimages/15/92/15925650.jpeg", "descriptions": "The elegant designed rooms for people" , "toh":"https://stackoverflow.com/questions/27427073/how-to-fit-in-an-image-inside-span-tag"}, {"title":"helloss", "name":"GRAND CLUB", "image":"https://www.chardhamhotels.net/Sitapur/images/P_20161019_094127.jpg", "descriptions": "Spread across the 4th,5th levels of grand grt.", "toh":"https://www.chardhamhotels.net/Sitapur/Hotel-J-P-G-Palace.html"}, {"title":"hellssdsdo", "name":"THEME SUITE", "image":"https://imgcy.trivago.com/c_limit,d_dummy.jpeg,f_auto,h_1300,q_auto,w_2000//partnerimages/70/56/70562138.jpeg","descriptions": "The most luxurious and spacious suite", "toh":"https://www.radissonhotels.com/en-us/brand/radisson-blu"}]

        message = {"payload": "cardsCarousel", "data": data}

        dispatcher.utter_message(text="List of hotel", json_message=message)

        return[]



