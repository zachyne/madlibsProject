print("Welcome to Madlibs!")
print("\n")

male_name = input("Male name: ")
fave_teacher = input("Name of your favorite teacher: ")
exclamation = input("Exclamation: ")
number = input("Number: ")
plural_objects = input("Plural Objects: ")
store_name = input("Store Name: ")
body_part = input("Body Part: ")
silly_word = input("Silly Word: ")
holiday = input("Name of Holiday: ")
celebrity = input("Celebrity Name: ")
movie = input("Movie Title: ")
ing = input("Verb ending in -ing: ")
distance = input("Amount of Distance: ")
country = input("Country: ")
object_name = input("Object: ")
occupation = input("Occupation: ")
animal = input("Animal: ")
movie_quote = input("Famous Movie Quote: ")
body_part2 = input("Body Part: ")
song = input("Children's Song: ")
adj = input("Adjective: ")

print("Hello. I’m Detective {}. And, you are…".format(male_name))
print("{}".format(fave_teacher))
print(" You are here today under suspicion of second degree robbery.")
print(f"{exclamation}!")
print("DETECTIVE That’s right. {} {} were stolen from {} and the crime scene has your {} written ALL over "
      "it.".format(number, plural_objects, store_name, body_part))
print("SUSPECT: That is {}.".format(silly_word))
print("DETECTIVE: Where were you on the night of {}?".format(holiday))
print("SUSPECT: I was with {}. We were watching the movie {}.".format(celebrity, movie))
print("DETECTIVE: Then why does security camera footage show you {} just {} away from the crime scene?".format(ing, distance))
print("SUSPECT: That’s a coincidence.")
print("DETECTIVE: Alright, I’m through playing games. Where are you from?")
print(f"SUSPECT: {country}.")
print("DETECTIVE: What did your parents do for a living?")
print("SUSPECT: My father was a {} salesman and my mother was a {}.".format(object_name, occupation))
print("DETECTIVE: Did they teach you to steal?")
print("SUSPECT: No. I told you didn’t do it!")
print("DETECTIVE: That’s enough! One of the best parts about being a detective is that I get to lock up" 
      "criminals like you, and go home to my children and my pet {} and say, {}.".format(animal, movie_quote))
print("SUSPECT: Fine, I did it. I committed the robbery. But I only did it because I needed the money to buy myself {} implants.".format(body_part2))
print(f"DETECTIVE: I knew it all along. And every time I solve a crime, I sing my favorite song, {song}")
print("(sing song)")
print(f"SUSPECT: You have a [{adj} voice.")