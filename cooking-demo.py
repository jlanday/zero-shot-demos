def craft_action(text, classifier, action_labels,):
	action = classifier(text, action_labels)
	result = action['labels'][0]
	print("You should bake...")
	print('~ ~ ~ {} ~ ~ ~'.format(result))
	return result

import glob
from simshow import simshow
from transformers import pipeline

images = glob.glob('food/*')
recipe_to_image = {image.split('.')[0].replace('_', ' ').replace('food/', '') : image for image in images}
classifier = pipeline("zero-shot-classification")

print('\n\n\n\n\n~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~')
print("\n⭑･ﾟﾟ･*:༅｡.｡༅:*ﾟ:*:✼✿ Welcome to the kitchen ! ✿✼:*ﾟ:༅｡.｡༅:*･ﾟﾟ･⭑")

while True:
	text = input("\nList your ingredients:\n    ")
	result = craft_action(text, classifier, list(recipe_to_image.keys()))
	image = recipe_to_image[result]
	simshow(image)