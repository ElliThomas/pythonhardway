name = 'Elli Thomas'
age = 25 # not a lie
height_inches = 64 # inches
height_cm = height_inches/1.5
weight = 132 # pounds
eyes = 'Hazel'
teeth = 'White'
hair = 'Brown'



print "Let's talk about %s." % name
print "She's %d inches tall." % height_inches
print "She's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (
	age, height_inches, weight, age + height_inches + weight)


