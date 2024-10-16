import random

characters = ["a brave knight", "a clever scientist", "a curious child", "an old wizard", "a young adventurer"]
settings = ["in a mystical forest", "in a bustling city", "on a distant planet", "in a small village", "in an ancient castle"]
conflicts = ["must find a hidden treasure", "is trapped in a mysterious maze", "needs to solve a complicated puzzle", "is challenged by a fierce dragon", "has to save a magical kingdom"]
resolutions = ["and finally discovers the secret", "and cleverly outwits the antagonist", "and learns a valuable lesson", "and finds unexpected allies", "and triumphs through sheer determination"]

def generate_story():
    character = random.choice(characters)
    setting = random.choice(settings)
    conflict = random.choice(conflicts)
    resolution = random.choice(resolutions)
    
    story = (f"Once upon a time, {character} {setting}. "
             f"One day, {character} {conflict}. "
             f"In the end, {character} {resolution}.")
    
    return story

print(generate_story())