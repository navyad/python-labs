"""
This script checking out various command line options
https://docs.python.org/3/using/cmdline.html
"""


from poi import Language
print("Hello World")
assert True == True


"""
python -i cmd.py

a). after running a script, python shell is opened
"""


"""
python -B cmd.py

a). Will not create .pyc file for imported module (poi.Language)
b). set PYTHONDONTWRITEBYTECODE is set non-empty string, will also skip creaing .pyc file
"""


"""
python -O cmd.py

a).assert statements are not evaluted
b). .pyc files will have the opt-1 appended
"""
