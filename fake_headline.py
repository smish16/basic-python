#import the random module
import random
#creating lists
subjects=[
   "Virat Kohli",
   "Shahrukh Khan",
   "Nirmala Sitharaman",
   "A Mumbai Cat",
   "Auto Rickshaw driver from Delhi",
   "Salman Khan"
]
actions=[

    "dances",
    "launches",
    "declares war",
    "orders",
    "celebrates"
]
places_or_things=[
     "in Mumbai local train",   
     "at Red fort",
     "inside parliament",
     "at ganga ghat",
     "during IPL match",
     "at india Gate"
]
#Start headline generation loop 
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    places_or_thing = random.choice(places_or_things)
    headline = f"BREAKING NEWS!!:{subject} {action} {places_or_thing}"
    print("\n"+ headline)

    user_input=input("\n Do you want another headline? (yes/no)").strip().lower()
    if user_input=="no":
      break
print("\n Thanks for using the Fake News headline Generator.have a good day")
