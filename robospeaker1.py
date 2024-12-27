import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)

print("Welcome to Robo Speaker 1.2, created by Tharun")

print("Enter multiple lines of text. Type 'bye' to exit.")

while True:
    print("\nEnter your text (type 'bye' to exit):")
    lines = []
    while True:
        line = input()
        if line.lower() == "bye":
            engine.say("Bye bye friend")
            engine.runAndWait()
            break
        if line == "":
            break
        lines.append(line)

    full_text = "\n".join(lines)

    engine.say(full_text)
    engine.runAndWait()

    if line.lower() == "bye":
        break
