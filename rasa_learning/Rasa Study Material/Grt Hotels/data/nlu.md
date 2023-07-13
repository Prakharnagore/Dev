## intent:greet
- hey
- hello
- hi
- hey there

## intent:goodbye
- bye
- goodbye
- see you around

## intent:affirm
- yes
- indeed
- of course
- correct

## intent:deny
- no
- never
- I don't think so

## intent:mood_great
- perfect
- very good
- great

## intent:general

## intent:existing

## intent:New_booking

## intent:confirm

## intent:submits

## intent:feedback

## intent:feedback_given

## intent:explore

## intent:web_information

## intent:get_email_details

## intent:Basic

## intent:Delux

## intent:Elite

## intent:no

## intent:name_of_customer
- [saurav](names)
- [eshaan](names)
- [dames](names)
- [james](names)
- [ayush](names)
- [kunal](names)
- [arave](names)
- [dhruv](names)
- [rajesh](names)
- [anant](names)
- [himanshu](names)
- [gaurav](names)
- [lakhan](names)
- [prashant](names)
- [ganesh](names)
- [ishaan](names)
- [muchi](names)

## regex:names
- ^[a-zA-Z]{3,9}$

## intent:phone_number
- [9847328809](phone)
- [8541328069](phone)
- [7842932809](phone)
- [8473267809](phone)
- [9117323809](phone)

## regex:phone
- ^[6-9]{1}[0-9]{9}$

## intent:ask_phone

## intent:confirmvalue
- [1e2f](confirm)
- [aa-123](confirm)
- [bb-321](confirm)

## regex:confirm
- \b[a-z]{2}-\d{3}\b

## intent:from_date
- [24-01](fromdate)
- [15-02](fromdate)
- [02-03](fromdate)
- [05-04](fromdate)
- [12-05](fromdate)
- [16-06](fromdate)
- [28-07](fromdate)
- [09-08](fromdate)
- [07-09](fromdate)
- [03-10](fromdate)
- [10-11](fromdate)
- [14-12](fromdate)

## regex:fromdate
- ^\d{2}-\d{2}$

## intent:to_date
- [2019-01-15](todate)
- [2020-02-14](todate)
- [2019-03-23](todate)
- [2020-04-02](todate)
- [2019-05-19](todate)
- [2020-06-12](todate)
- [2019-07-05](todate)
- [2020-08-14](todate)
- [2019-09-16](todate)
- [2020-10-09](todate)
- [2019-11-07](todate)
- [2020-12-25](todate)

## regex:todate
- ^\d{4}-\d{2}-\d{2}$

## intent:rooms
- [2](room)
- [1](room)
- [3](room)
- [4](room)
- [5](room)
- [6](room)
- [7](room)

## regex:room
- ^[0-9]{1}$

## intent:email_of_customer
- [eshaan233@gmail.com](email_customer)
- [coole123@gmail.com](email_customer)
- [eshaan201@gmail.com](email_customer)
- [coolesh957@gmail.com](email_customer)
- [happusln2391@gmail.com](email_customer)
- [kspwlqxz21@gmail.com](email_customer)

## regex:email_customer
- \b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,30}\b

## intent:feed
- [it is a great hotel](feedback)
- [beautiful and a great hotel that i think will do wonders](feedback)
- [nice and beautiful hotel](feedback)
- [I don't like this hotel a lot](feedback)
- [bad experience regarding the customers and people here](feedback)

## regex:feedback
- ^[a-zA-Z''-'\s]{15,60}$

## intent:type
- asType
- like its well

## intent:Y
- Y
- Y_payload

## intent:N
- N
- N_payload
