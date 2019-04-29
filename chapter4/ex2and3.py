# Move the last line of this program to the top, so the function call appears before the definitions. Run the program and see what error message you get.
#In first case it produces a trace back to line one 'repeat_lyrics' is not defined'
# Move the function call back to the bottom and move the definition of print_lyrics after the definition of repeat_lyrics. What happens when you run this program?
#In second case the function runs.
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')


def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()
