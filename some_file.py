print("This is a file from GitHub")

print('these are new local chenge')

print('/\_/\\\n>^,^<\n / \\\n(|_|)_/')

def get_string(string: str, times: int, sep: str=',') -> str:
    return sep.join([string] * times)
    
print(get_string('t', 12))