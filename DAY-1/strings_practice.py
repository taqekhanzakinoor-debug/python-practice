text = "Alauddin "
print(text[0]) # first character
print(text[7]) # last character
print(text[-3]) # third character from the end
print(text[0:6]) # substring from index 0 to 5
print(text[7:10]) # substring from index 7 to 9
print(text[:6]) # substring from the beginning to index 5
print(text[7:10]) # substring from index 7 to 9
print(text[::-1]) # reverse the string
print(len(text)) # length of the string
print(text.upper()) # convert to uppercase
print(text.lower()) # convert to lowercase
print(text.title()) # convert to title case
print(text.capitalize()) # capitalize the first character
print(text.replace("Alauddin", "khan")) # replace a substring
print(text.count("n")) # count occurrences of a substring
print(text.find("is")) # find the index of a substring
padded = "   gdg bootcamp   "
print(padded.strip())
print(padded.lstrip())
print(padded.rstrip()) #strip whitespace from the right
csv = "red,green,blue"
colors = csv.split(",")
print(colors)
print("-".join(colors))
print(text.split())
print("Alauddin" in text)
print(text.startswith("Alauddin"))
print(text.endswith("Alauddin"))
name = "meow"
age = 21
print(f"My name is {name} and I am {age} years old")
print("".strip( ))
print(text[0:100]) # substring from index 0 to 99