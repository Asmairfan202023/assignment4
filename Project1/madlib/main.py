from sample_madlibs import hp, coding, zombie, hungergames
import random

if __name__ == "__main__":
    stories = [hp, coding, zombie, hungergames]  # Change "code" to "coding"
    selected_story = random.choice(stories)
    selected_story.play()

