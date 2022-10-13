import re

s = "I am feeling very dizzy tonight. But I am sure I did not fire that missile when I was drunk. Being a very professional contract killer I do not fire or plant bombs until particularly needed. Also, I do not have the courage to shoot the President let alone burst a bomb or fire a missle. Stop blaming me or my wrath will burn you into ashes. Ashes is not a brand here, my wrath is like fire, you might die kiddo. So stop pulling my legs and focus on your job. Shoot through the exit now!"

danger = ['die', 'fire', 'kill', 'killer', 'missile', 'bomb', 'burst', 'shoot', 'president', 'burn']

re_s = re.split(r'[," "!.]', s)

for word in re_s:
    # print(word)
    if word in danger:
        print(word)
    

""" 
We can simplify this even further by passing in a regular expressions collection. Let’s see how we can do this:

import re
sample_string = 'hi! my name is nik, welcome; to datagy'
split_string = re.split(r'[,;!]', sample_string)
print(split_string)
# Returns: ['hi', ' my name is nik', ' welcome', ' to datagy']
This returns the same thing as before, but it’s a bit cleaner to write and to read.
 """