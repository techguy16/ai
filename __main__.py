import speech_recognition as sr
import pyttsx3

def item_split_by(item, string, splitby):
  item2 = item - 1
  return string.split(splitby)[item2]

def get_characters_in_range(string, start_index, end_index):
    return string[start_index:end_index]
  
# Initialize the recognizer
r = sr.Recognizer()
 
# Function to convert text to
# speech
def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
     
     
# Loop infinitely for user to
# speak
 
while(1):   
     
    # Exception handling to handle
    # exceptions at the runtime
    try:
         
        # use the microphone as source for input.
        with sr.Microphone() as source2:
             
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)
             
            #listens for the user's input
            audio2 = r.listen(source2)
             
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            if "plus" in MyText:
              print(f"plus in {MyText}")
              text = MyText.replace(" plus ", ",")
              addition = int(item_split_by(1, text, ",")) + int(item_split_by(1, text, ","))
              say = MyText + ' equals ' + addition
              SpeakText(say)
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")
