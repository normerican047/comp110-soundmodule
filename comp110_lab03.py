"""
lab03_problem1
"""
import sound


love_sound = sound.load_sound("love.wav")
love_sound.play()
sound.wait_until_played()  # waits until love_sound is done playing

# change the volume of the love sound
for i in range(len(love_sound)):
    sample = love_sound.get_sample(i)
    new_left_val = sample.get_left() * 2
    new_right_val = sample.get_right() * 2
    sample.set_left(new_left_val)
    sample.set_right(new_right_val)

love_sound.play()
sound.wait_until_played()  # waits until love_sound is done playing
