from psychopy import visual, core, event
import random
import pandas as pd
import os

print("Current Working Directory:", os.getcwd())

def display_instructions():
    instruction_text = ("In this game, you will see color words (RED, BLUE, GREEN) appear one at a time. "
                        "Your task is to press the button corresponding to the font color of the word, not the word itself.\n\n"
                        "Respond as quickly and accurately as possible.\n\n"
                        "The response keys are as follows:\n\n"
                        "r = red\n"
                        "b = blue\n"
                        "g = green\n\n"
                        "Remember, choose the color of the letters, ignore the word itself.\n\n"
                        "Press 'Enter' to start once you understand the rules.")

    instructions = visual.TextStim(win, text=instruction_text, height=20, color='black')
    instructions.draw()
    win.flip()
    start_time = core.getTime()
    
    # Wait for 5 seconds or until 'Enter' key is pressed
    while core.getTime() - start_time < 5.0 and not event.getKeys(keyList=['return']):
        pass

# Create a window
win = visual.Window(size=(800, 600), color='white', units='pix')

# Create text stimulus
text_stim = visual.TextStim(win, height=40, color='black')

# Display instructions
display_instructions()

# Define colors and words
colors = ['red', 'green', 'blue']
words = ['RED', 'GREEN', 'BLUE']

# Create a list to store the pairings
pairings = []

# Iterate through each color and color option to create pairings
for color in colors:
    for option in colors:
        # Repeat each pairing 4 times
        pairings.extend([(color, option)] * 4)

# Shuffle the pairings to randomize the order
random.shuffle(pairings)

# Create an empty list to store the trial data
trial_data = []

# Run 36 trials of the Stroop task
for pairing in pairings:
    color, option = pairing

    # Fixation cross (0.5 seconds)
    fixation_cross = visual.TextStim(win, text='+', height=40, color='black')
    fixation_cross.draw()
    win.flip()
    core.wait(0.5)

    # Stimulus presentation (1.5 seconds)
    text_stim.color = color.lower()  # Set color based on the chosen color
    text_stim.text = option.capitalize()  # Set the text based on the chosen color option
    text_stim.draw()
    win.flip()
    core.wait(1.5)

    # Clear the screen (0.5 seconds)
    win.flip()
    core.wait(0.5)

    # Feedback presentation (0.5 seconds)
    response = event.getKeys(keyList=['r', 'g', 'b'])
    if response and response[0] in ['r', 'g', 'b']:
        if response[0] == color[0].lower():
            feedback_text = "Correct!"
        else:
            feedback_text = "Incorrect!"
    else:
        feedback_text = "Respond faster."

    # Store trial data
    trial_data.append({'ParticipantID': len(trial_data) + 1, 'Color': color, 'Option': option, 'Response': response[0] if response else 'No response', 'Feedback': feedback_text})

    feedback = visual.TextStim(win, text=feedback_text, height=30, color='black')
    feedback.draw()
    win.flip()
    core.wait(0.5)

    # Clear the screen for the next trial
    win.flip()

# Close the window
win.close()
core.quit()

# Convert the trial data to a DataFrame
df = pd.DataFrame(trial_data)

try:
    # Save the DataFrame to an Excel file with an absolute path
    df.to_excel(r'C:\Users\ghung\Desktop\stroop experiment\stroop pthon attempt\data\experiment_data.xlsx', index=False)
except Exception as e:
    print("Error:", e)

