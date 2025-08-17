import sys  # Efek typerwriter / mengetik
import time  # Menambahkan library waktu

lyrics = [
    "Ooh, that's so true, ooh",
    "...",
    "Made it out alive, but I think I lost it",
    "Said that I was fine, I said it from my coffin",
    "Remember how I died when you started walking?",
    "That's my life,",
    "that's my life",
    "I put up a fight,", "taking out my earrings",
    "Don't you know the vibe? Don't you know the feeling?",
    "You should spend the night catch me on your ceiling",
    "That's your prize, that's your price,",
    "well "
]

# print(len(lyrics[3]))
# print(0.85 + 1.31)
speed = [0.15, 0.5, 0.05, 0.04, 0.039, 0.04, 0.047, 0.037,
         0.05, 0.032, 0.032, 0.046, 0.1]


def typewriter(text, delay=speed):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed[i])
    print()


for i, line in enumerate(lyrics):
    typewriter(line, delay=speed[i])
    time.sleep(0.2)
