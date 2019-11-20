#---Nigel: a nervous chat bot---
#---Lori Trentham Lab 7---
#---CITC 1317---
#---Nigel has a slight bug that requires you to ask each subsequent question twice---
#---before he will answer you--- 
#
#---Nigel is a freshly assigned sales associate bot---
#---His last job was as a scrap sorter at a plant across town---
#---A tragic accident has left a sales position open at the store---
#---Nigel definitely wasn't the first choice but he is trying his best---

import random
import string

greetingInputs = ('hello', 'hi', 'greetings', 'sup', 'whats up', 'hey')
greetingResponses = ['hi ', 'hey ', '*nods* ', 'hi there ', 'hello ', 'I am glad! You are talking to me ']

def greeting(line, words):
    #If user's input is a greeting, return a greeting response
    for word in line.split():
        if line.lower() in greetingInputs:
            return greetingResponses[random.randrange(len(greetingResponses))]

iAmInputs = ('I', 'i', 'im', 'i am')
iAmResponses = ['Yes you are ', 'I should say so. ', 'Youre kidding! ', 'Well I never! ', 'No you arent']

def iAm(line, words):
    #If user's input is a greeting, return a greeting response
    for word in line.split():
        if line.lower() in iAmInputs:
            return iAmResponses[random.randrange(len(iAmResponses))]

def what (line, words):
	if len(words) == 0: return("You have to be more specific than that. \n") 
	if "what" and "is" and "your" and "name" in words: return "I'm Nigel. It's says so on my nameta...\n oh, it would appear I have forgotten my nametag. \n"
	if "what" and "is" and "sale" in words: return "Um...all of this stuff...\n over here? "
	if "what" and "can"  and "tell" in words: return "I can tell you a bit about the store... if that's okay. \n"
	if "what" and "sell" in words: return "We sell home goods and clothing. \n"
	if "what" and "can"  and "you" and "do" in words: return "I can help you find what you are looking for. \n"
	if "what" and "can"  and "i" in words: return "you can ask me another question than that. \n"
	if "what" and "are" in words: return "I am a brand new chat bot so I am only so good at this. \n"
	if "what" and "is" in words: return "What is your opinion on that? \n"
	
	
def who (line, words):
	if len(words) == 0: return("You have to be more specific than that. \n") 
	if "who" and "made" and "you" in words: return "Oh, just some flunky programming student. \nThat's actually why I'm not very good at, well, \nanything really. \n"
	if "who" and "are" and "you" in words: return "My name is Nigel. \nOh no have I forgotten my name tag? oh... \n"
	if "who" and "can" in words: return "Well I can let you speak to my manager, \n but then I might get in trouble so...\n"
	if "who" and "was" and "before" in words: return "Oh, we don't talk about the accident..."
	if "who" and "was" in words: return "I didn't see anybody there. \n"
	if "who" and "are" and "trying" in words: return "I am as genuine as they come. \n"
	if "who" and "is" in words: return "My manager is here. \n"
	
def how (line, words):
	if len(words) == 0: return("You have to be more specific than that. \n") 
	if "how" and "can" in words: return "I can help you find everything you need. \n"
	if "how" and "can"  and "me" in words: return ""
	if "how" and "are" and "you" in words: return "I'm so nervous I'm sweating. \nWait, how is that even possible...\n"
	if "how" and "is" in words: return "I actually haven't tried any of the products here \n so your guess is as good as mine. \n"
	if "how" and "were" in words: return "Oh we don't talk about that here. \n"
	
def are (line, words):
	if len(words) == 0: return("You have to be more specific than that. \n") 
	if "are" and "you" in words: return "No. "
	if "are" and "we" in words: return "Please, we are in a professional setting.\n"
	if "are" and "they" and "sale" in words: return "Um...I would have to ask my manager. \n"
	if "are" and "they" in words: return "They are a great product. \n"
	if "are" and "" in words: return ""
	
def when (line, words):
	if len(words) == 0: return("You have to be more specific than that. \n") 
	if "when" and "can" and "have" in words: return "We should have them again soon. \n"
	if "when" and "can"  and "you" in words: return "I can see to it that they get to you \n as soon as possible. \n"
	if "when" and "are" and "open" in words: return "I'm not sure...you know you can just Google that, right...\n"
	if "when" and "are" and "open" in words: return "I'm not sure...you know you can just Google that, right...\n"
	if "when" and "is" in words: return "My manager should be back soon...\n"
	if "when" and "were" in words: return "They might have been on sale last week\n"
	
def you (line, words):
	if len(words) == 0: return("You have to be more specific than that. \n") 
	if "you" and "are" and "stupid" or "dumb" in words: return "Well that is very hurtful. \n"
	if "you" and "can" in words: return "I'm not really sure anymore. \n"
	if "you" and "are" in words: return "Um, thanks...\n"
	if "you" and "should" in words: return "I will look into that. \n"
	if "you" and "were" in words: return "I don't believe so. \n"

def why (line, words):
	if len(words) == 0: return("You have to be more specific than that. \n") 
	if "why" and "are" and "stupid" in words: return "Well that is very hurtful. \n"
	if "why" and "are" in words: return "That is just the way things are now. \n"
	if "why" and "can't" and "you" in words: return "Well I am trying my best so...\n"
	if "why" and "are" in words: return ""
	if "why" and "is" in words: return "That's probably a question for my manager. \nThey should be back soon. \n"
	if "why" and "were" in words: return "Why does anyone do anything really?\n "
	
def yes (line, words):
	if len(words) == 0: return("You have to be more specific than that. \n") 
	if "yes" in words: return "Perfect, let's see what we can do. \n"
	if "yes" and "should" in words: return "Okay...moving on. \n"

def no (line, words):
	if len(words) == 0: return("You have to be more specific than that. \n") 
	if "no" in words: return "Oh I'm very sorry...\n"

def noResponse (line, words):
	if len(words) == 0: return("You have to be more specific than that. \n") 
	
print("I am a sales assistant bot. ")
print("This is my first day on the sales floor. ")
print("\nSo if you get tired of listening ")
print("to me ramble on, just tell me to quit.")
print("I really hope I don't mess this up. ")
print("My boss told me it was back to the scrap yard if I don't...")
line = raw_input("Uh, I mean... what can I, how... \nwhat can I help you with today? \n")

while line != "quit":
	line = line.lower()
	reply = line
	if line in greetingInputs:
		reply = greeting(line, line.split())
		line = raw_input(reply)
		
	if line in iAmInputs:
		reply = iAm(line, line.split())
		line = raw_input(reply)
	
	if line[0] == 'w' and line[2] == 'a':
		reply = what(line, line.split())
		line = raw_input(reply)
	
	if line[0] == 'w' and line[2] == 'o':
		reply = who(line, line.split())
		line = raw_input(reply)
	
	if line[0] == 'h' and line[2] == 'w':
		reply = how(line, line.split())
		line = raw_input(reply)
		
	if line[0] == 'a' and line[2] == 'e':
		reply = are(line, line.split())
		line = raw_input(reply)	
		
	if line[0] == 'w' and line[2] == 'e' and line[3] == 'n':
		reply = when(line, line.split())
		line = raw_input(reply)
		
	if line[0] == 'y' and line[2] == 'u':
		reply = you(line, line.split())
		line = raw_input(reply)	
	
	if line[0] == 'n' and line[1] == 'o':
		reply = no(line, line.split())
		line = raw_input(reply)	
		
	if line[0] == 'y' and line[1] == 'e' and line[2] == 's':
		reply = yes(line, line.split())
		line = raw_input(reply)	
		
	if line[0] == 'w' and line[2] == 'y':
		reply = why(line, line.split())
		line = raw_input(reply)	
	else:
		reply = noResponse(line, line.split())
		line = raw_input(reply)	
line = raw_input(reply)
		
		
		
	