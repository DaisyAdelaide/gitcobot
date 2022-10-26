from datetime import datetime
then = datetime(2022,7,5)        # Random date in the past
now  = datetime.now()                         # Now
duration = now - then 
print (duration)