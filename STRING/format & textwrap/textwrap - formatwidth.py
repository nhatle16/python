# import textwrap library
import textwrap as tw

def format_text(str):
    # fit the text within the given width
    print()
    print(tw.fill(str, width = 50))

    # shorten the text within the given width
    print()
    print(tw.shorten(str, width = 70, placeholder='...'))

def main():
    sample_text = '''Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.'''

    format_text(sample_text)

main()
