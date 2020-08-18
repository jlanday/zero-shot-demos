from transformers import pipeline

classifier = pipeline("zero-shot-classification")

labels = ["Equip Item", "Attack" , "Run Away" , "Cry"]

def action(text):
  return classifier(text, labels)['labels'][0]

def loop(text, result_to_end):
	result = None
	while result != result_to_end:
	  response = input("\n{}. What do you do?\n    ".format(text))
	  result = action(response)
	  if result != result_to_end:
	    print("\nTry something else. '{}'. Does not work".format(response))
	  else:
	  	print('\nYay you did it.\nAction : {}'.format(response))

print('\n\n\n\n\n~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~')
print("\nNarrarator: In this game you can do 4 things. cquip Items, Attack, Run, and Cry.")
loop("Narrarator: You enter a room with nothing but a lousy broom", "Equip Item")
loop("Narrarator: Suddenly Mordekaiser appears! He is pissed AF. Apparently, you touched his favorite broom and he is not happy. He charges towards you", "Attack")
loop("Narrarator: He's looking a little weak... Now what?", "Attack")
loop("Narrarator: Haha JK, he is Mordekiser and you are a data nerd. You are no match for him. He pulls out his giant hammer and goes to smack you", "Run Away")
loop("Narrarator: You finally made it out but youre starting to feel bad for breaking his broom", "Cry")
print("Narrarator: Okay Game over this is no Skyrim")