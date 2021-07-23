import datetime

SLOT_STATUS_CHOICES = (
    ('Available', 'Available'),
    ('UnAvailable', 'UnAvailable'),
)

MEETING_STATUS_CHOICES = (
    ('Requested', 'Requested'),
    ('Booked', 'Booked'),
    ('Cancelled', 'Cancelled'),
    ('Completed', 'Completed'),

)

ALGO_TRADING_PLATFORM = (
    ('Python', 'Python'),
    ('Tradingview', 'Tradingview'),
    ('MT4/MT5', 'MT4/MT5'),
    ('Ninjatrader', 'Ninjatrader'),
    ('AmiBroker', 'AmiBroker'),
    ('Others', 'Other? Specify in comments box'),
)

SEGMENT_CHOICES =(
    ('Equity', 'Equity'),
    ('Futures', 'Futures'),
    ('Options', 'Options'),
    ('Currency', 'Currency'),
    ('Commodity', 'Commodity'),
    ('Crypto', 'Cryptos'),
)

TIME_CHOICES = (
    (datetime.datetime.strptime('12:00 am', "%I:%M %p").time(), '12:00 am'),
    (datetime.datetime.strptime('12:30 am', "%I:%M %p").time(), '12:30 am'),
    (datetime.datetime.strptime('1:00 am', "%I:%M %p").time(), '1:00 am'),
    (datetime.datetime.strptime('1:30 am', "%I:%M %p").time(), '1:30 am'),
    (datetime.datetime.strptime('2:00 am', "%I:%M %p").time(), '2:00 am'),
    (datetime.datetime.strptime('2:30 am', "%I:%M %p").time(), '2:30 am'),
    (datetime.datetime.strptime('3:00 am', "%I:%M %p").time(), '3:00 am'),
    (datetime.datetime.strptime('3:30 am', "%I:%M %p").time(), '3:30 am'),
    (datetime.datetime.strptime('4:00 am', "%I:%M %p").time(), '4:00 am'),
    (datetime.datetime.strptime('4:30 am', "%I:%M %p").time(), '4:30 am'),
    (datetime.datetime.strptime('5:00 am', "%I:%M %p").time(), '5:00 am'),
    (datetime.datetime.strptime('5:30 am', "%I:%M %p").time(), '5:30 am'),
    (datetime.datetime.strptime('6:00 am', "%I:%M %p").time(), '6:00 am'),
    (datetime.datetime.strptime('6:30 am', "%I:%M %p").time(), '6:30 am'),
    (datetime.datetime.strptime('7:00 am', "%I:%M %p").time(), '7:00 am'),
    (datetime.datetime.strptime('7:30 am', "%I:%M %p").time(), '7:30 am'),
    (datetime.datetime.strptime('8:00 am', "%I:%M %p").time(), '8:00 am'),
    (datetime.datetime.strptime('8:30 am', "%I:%M %p").time(), '8:30 am'),
    (datetime.datetime.strptime('9:00 am', "%I:%M %p").time(), '9:00 am'),
    (datetime.datetime.strptime('9:30 am', "%I:%M %p").time(), '9:30 am'),
    (datetime.datetime.strptime('10:00 am', "%I:%M %p").time(), '10:00 am'),
    (datetime.datetime.strptime('10:30 am', "%I:%M %p").time(), '10:30 am'),
    (datetime.datetime.strptime('11:00 am', "%I:%M %p").time(), '11:00 am'),
    (datetime.datetime.strptime('11:30 am', "%I:%M %p").time(), '11:30 am'),
    (datetime.datetime.strptime('12:00 pm', "%I:%M %p").time(), '12:00 pm'),
    (datetime.datetime.strptime('12:30 pm', "%I:%M %p").time(), '12:30 pm'),
    (datetime.datetime.strptime('1:00 pm', "%I:%M %p").time(), '1:00 pm'),
    (datetime.datetime.strptime('1:30 pm', "%I:%M %p").time(), '1:30 pm'),
    (datetime.datetime.strptime('2:00 pm', "%I:%M %p").time(), '2:00 pm'),
    (datetime.datetime.strptime('2:30 pm', "%I:%M %p").time(), '2:30 pm'),
    (datetime.datetime.strptime('3:00 pm', "%I:%M %p").time(), '3:00 pm'),
    (datetime.datetime.strptime('3:30 pm', "%I:%M %p").time(), '3:30 pm'),
    (datetime.datetime.strptime('4:00 pm', "%I:%M %p").time(), '4:00 pm'),
    (datetime.datetime.strptime('4:30 pm', "%I:%M %p").time(), '4:30 pm'),
    (datetime.datetime.strptime('5:00 pm', "%I:%M %p").time(), '5:00 pm'),
    (datetime.datetime.strptime('5:30 pm', "%I:%M %p").time(), '5:30 pm'),
    (datetime.datetime.strptime('6:00 pm', "%I:%M %p").time(), '6:00 pm'),
    (datetime.datetime.strptime('6:30 pm', "%I:%M %p").time(), '6:30 pm'),
    (datetime.datetime.strptime('7:00 pm', "%I:%M %p").time(), '7:00 pm'),
    (datetime.datetime.strptime('7:30 pm', "%I:%M %p").time(), '7:30 pm'),
    (datetime.datetime.strptime('8:00 pm', "%I:%M %p").time(), '8:00 pm'),
    (datetime.datetime.strptime('8:30 pm', "%I:%M %p").time(), '8:30 pm'),
    (datetime.datetime.strptime('9:00 pm', "%I:%M %p").time(), '9:00 pm'),
    (datetime.datetime.strptime('9:30 pm', "%I:%M %p").time(), '9:30 pm'),
    (datetime.datetime.strptime('10:00 pm', "%I:%M %p").time(), '10:00 pm'),
    (datetime.datetime.strptime('10:30 pm', "%I:%M %p").time(), '10:30 pm'),
    (datetime.datetime.strptime('11:00 pm', "%I:%M %p").time(), '11:00 pm'),
    (datetime.datetime.strptime('11:30 pm', "%I:%M %p").time(), '11:30 pm'),
    )
