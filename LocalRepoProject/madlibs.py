print("Enter a noun, verb and adjective")
noun = str(input("noun" ))
verb = str(input("verb" ))
adjective= str(input("adjective" ))
story_template = "On a beautiful", adjective, "day, I went to the zoo. I saw a funny", adjective, "monkey swinging from the trees. Then I spotted a majestic", adjective, "lion lounging in the sun. What a wild and", adjective, "experience!" 
if adjective == "lazy":
    story_template = f"On a beautiful {adjective} day, I went to the zoo. I saw a funny {adjective} monkey swinging from the trees. Then, I spotted a majestic {adjective} lion lounging in the sun.  What a wild and {adjective} experience! I won't forget it"
else:
    story_template = "Fakkuyu!" 
print(story_template)
print("My first mad libs story is done")