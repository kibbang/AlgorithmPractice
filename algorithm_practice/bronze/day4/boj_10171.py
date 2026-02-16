import textwrap

def cat():
    art = """
        \\    /\\
         )  ( ')
        (  /  )
         \\(__)|
    """
    print(textwrap.dedent(art).strip("\n"))

if __name__ == "__main__":
    cat()