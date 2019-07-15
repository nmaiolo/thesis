# Nina Maiolo
# Master's Thesis
# Roosevelt University
# Merging Computer Science with Graphic Design

# Get file name from user and send to text file using Photo OCR ---------------------------------
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

fileName = input("Enter file name: ")
img = Image.open(fileName)
text = pytesseract.image_to_string(img)

text = text.encode('ascii', 'ignore').decode('ascii')

f_name = open("f_name.txt","w")
f_name.write(text)
f_name.close()

#with open("f_name.txt") as f:
    #print (f.read())

# Initialize variables ---------------------------------------------------------------------
overall_score = 10
num_words = 0
buzz_count = 0
bad_count = 0
buzzwords = ['act', 'agree', 'apply', 'arrive', 'ask', 'bake', 'bring', 'build', 'buy',
             'call', 'climb', 'close', 'come', 'cry', 'dance', 'dream', 'drink', 'eat', 'enter',
             'exit', 'fall', 'fix', 'go', 'grab', 'help', 'hit', 'hop', 'insult', 'joke', 'jump',
             'kick', 'laugh', 'leave', 'lift', 'listen', 'make', 'march', 'move', 'nod', 'open',
             'play', 'push', 'read', 'ride', 'run', 'send', 'shout', 'sing', 'sit', 'smile', 'spend'
                                                                                             'stand', 'talk', 'think',
             'throw', 'touch', 'turn', 'visit', 'vote', 'wait', 'walk',
             'write', 'yell', 'give', 'now', 'today', 'soon', 'fast', 'tomorrow']

badwords = ['damn', 'ugly', 'useless', 'fuck', 'shit', 'bad']

print("Analyzing...")


# Count words in billboard and see if it's in a safe range 6-24 ----------------------------
with open("f_name.txt", 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)

    # Check for buzzwords/calls to action ------------------------------------------------------
    for num, line in enumerate(f, start=1):
        for word in buzzwords:
            if word in line:
                buzz_count += 1

    # Check for alienating/inappropriate words -------------------------------------------------
    for num, line in enumerate(f, start=1):
        for word in badwords:
            if word in line:
                bad_count += 1

# Run Spellcheck ---------------------------------------------------------------------------




# Add billboard feedback to new file that opens and displays feedback ----------------------
feedback = open("feedback.txt","w")

feedback.write("----- BILLBOARD FEEDBACK -----\n")
feedback.write("\n")
with open("f_name.txt") as f:
    feedback.write(f.read())
feedback.write("\n")
feedback.write("\n")


if num_words > 20:
    number = "- Your billboard has %s words, which is lengthy. Drivers may miss your message. Consider revising." %(num_words)
    overall_score -= 1
elif num_words < 6:
    number = "- Your billboard has $s words. Your message is short. You may want to add additional info." %(num_words)
    overall_score -= 1
else:
    number = "- Your billboard has %s words. Safe range for word count. Nice job." %(num_words)

feedback.write(number)
feedback.write("\n")


if buzz_count >= 1:
    feedback.write("- Billboard contains a call to action.")
else:
    feedback.write("- No call to action is present. Try adding one to engage the reader.")
    overall_score -= 1

feedback.write("\n")


if bad_count >= 1:
    feedback.write("- Some of your copy may be alienating to drivers. Consider using more friendly language.")
    overall_score -= 1
else:
    feedback.write("- Your language appears to be neutral. Good work.")

feedback.write("\n")
feedback.write("\n")
overall = ("Overall Score: %s / 10") %(overall_score)
feedback.write(overall)

feedback.close()
print("Done.")