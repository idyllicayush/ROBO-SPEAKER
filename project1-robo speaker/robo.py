import pyttsx3 # Import the pyttsx3 library for text-to-speech conversion

def robo_speaker(text):  # Define a function named 'robo_speaker' that takes one parameter 'text'
    engine = pyttsx3.init()  # Initialize the TTS engine by creating an instance of pyttsx3.Engine
    engine.say(text)  # Storing the text for speech call
    engine.runAndWait()  # Process the text and perform the speech call

# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    print("created by Ayush")
    while True:  # Start an infinite loop
        # Prompt the user to enter text and store it in the variable 'text'
        text = input("Enter what you want the robo speaker to say (or 'exit' to quit): ")
        # Check if the user input (converted to lowercase) is 'exit'
        if text.lower() == 'exit':
            print("Thank You for using this app")
            break  # Break out of the loop if the input is 'exit'
        robo_speaker(text)  # Call the 'robo_speaker' function with the user input as the argument








# # # Change the speaking rate
#     rate = engine.getProperty('rate')
#     print(f"Current speaking rate: {rate}")
#     engine.setProperty('rate', 150)  # Set a new speaking rate (e.g., 150 words per minute)
    
#     # Change the volume
#     volume = engine.getProperty('volume')
#     print(f"Current volume level: {volume}")
#     engine.setProperty('volume', 0.9)  # Set a new volume level (e.g., 90%)
    
#     # Change the voice
#     voices = engine.getProperty('voices')
#     for voice in voices:
#         print(f"Voice: {voice.name}, ID: {voice.id}")
    
#     engine.setProperty('voice', voices[1].id)  # Change to the second voice in the list

#     engine.say(text)  # Queue the text for speech synthesis
#     engine.runAndWait()  # Process the queued text and perform the speech synthesis
