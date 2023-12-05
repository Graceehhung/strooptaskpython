from psychopy import visual, core, event

def display_instructions():
    instruction_text = ("In this game, you will see color words (RED, BLUE, GREEN, BROWN) appear one at a time. "
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
    while core.getTime() - start_time < 10.0 or not event.getKeys(keyList=['return']):
        pass

# Create a window
win = visual.Window(size=(800, 600), color='white', units='pix')

# Create text stimulus
text_stim = visual.TextStim(win, height=40, color='black')

# Display instructions
display_instructions()

# Define colors and words
colors = ['red', 'green', 'blue']
words = ['RED', 'GREEN', 'BLUE', 'BROWN']

# Run the Stroop task
for word in words:
    # Fixation cross (0.5 seconds)
    fixation_cross = visual.TextStim(win, text='+', height=40, color='black')
    fixation_cross.draw()
    win.flip()
    core.wait(0.5)

    # Stimulus presentation (1.5 seconds)
    text_stim.color = word.lower()  # Set color based on the word itself
    text_stim.text = word
    text_stim.draw()
    win.flip()
    core.wait(1.5)

    # Clear the screen (0.5 seconds)
    win.flip()
    core.wait(0.5)

    # Feedback presentation (0.5 seconds)
    response = event.getKeys(keyList=['r', 'g', 'b'])
    if response and response[0] in ['r', 'g', 'b']:
        if response[0] == word[0].lower():
            feedback_text = "Correct!"
        else:
            feedback_text = "Incorrect!"
    else:
        feedback_text = "No response or invalid response."

    feedback = visual.TextStim(win, text=feedback_text, height=30, color='black')
    feedback.draw()
    win.flip()
    core.wait(0.5)

    # Clear the screen for the next trial
    win.flip()

# Close the window
win.close()
core.quit()
