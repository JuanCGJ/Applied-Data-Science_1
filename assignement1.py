# PARTE A
# import re
# def names():
#     simple_string = """Amy is 5 years old, and her sister Mary is 2 years old.
#     Ruth and Peter, their parents, have 3 kids."""
#
#     # YOUR CODE HERE
#     pattern="[A-Z][a-z]*"
#     names=re.findall(pattern,simple_string)
#     print(names)
#     return names
# names()

# PARTE B
# import re
# def grades():
#     with open ("grades.txt", "r") as file:
#         grades = file.read()
#         pattern="(\w+\s\w+): B"
#         grades=re.findall(pattern,grades)
#         print(grades)
#     return grades
# grades()

# PARTE C
# import re
# def logs():
#     with open("logdata.txt", "r") as file:
#         logdata = file.read()
#         pattern="""(?P<host>.*)                #hostname
#                    (\s-\s)                     #formato de lo que sigue
#                    (?P<user_name>.*.(?=\s\[))  #grupo username es:todos los caracteres que coincidan 0 o + veces (.*) seguido
#                                                #de todos los caracteres hasta que encuentre espacio y corchete .(?=\s\[)
#                    (\s\[)                      #formato de lo que sigue
#                    (?P<time>.*(?=\]))          #grupo time es: todos los caracteres hasta que encuentre [
#                    (\]\s\")                    #formato de lo que sigue
#                    (?P<request>.*(?=\"))       #grupo request es: todos los caracteres hasta que encuentre " que cierran
#
#                 """
#         logs=[]
#         for item in re.finditer(pattern,logdata,re.VERBOSE):
#             a=item.groupdict()
#             logs.append(a)
#             print(logs)
#
#         print(len(logs))
#     return logs
# logs()
