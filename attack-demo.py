def attack_action(text, classifier, action_labels, intensity_labels):
	action = classifier(text, action_labels)
	intensity = classifier(text, intensity_labels)

	result = '{}-{}'.format(intensity['labels'][0], action['labels'][0])
	return result

from transformers import pipeline


action_labels = [
 "Slash",
 "Shoot Arrow",
 "Fire Gun",
 "Bash",
 "Poke",
 "Frozen",
 "Melt",
 "Poison",
 "Shocked and electrocuted",
 "Stunned and Paralyzed",
 "Conjure the Dead",
 "Spells and Magic",
]

intensity_labels = ["Weak" , "Strong"]

classifier = pipeline("zero-shot-classification")

print('\n\n\n\n\n~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~')
print("\nNarrarator: In this game, all you can do is attack the target.")

while True:
	text = input("\nDescribe an attack\n    ")
	result = attack_action(text, classifier, action_labels, intensity_labels)
	print(result)