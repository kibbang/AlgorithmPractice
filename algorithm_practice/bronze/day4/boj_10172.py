import textwrap

def dog():
    art = r'''
    |\_/|
    |q p|   /}
    ( 0 )"""\
    |"^"`    |
    ||_/=\\__|
    '''
    print(textwrap.dedent(art).strip("\n"))

if __name__ == "__main__":
    dog()