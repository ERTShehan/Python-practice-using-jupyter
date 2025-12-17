# print(my_variable)
# Traceback - stack trace:
#   File "error.py", line 1, in <module>
# NameError: name 'my_variable' is not defined

def function_a():
    print("function_a called")
    function_b()

def function_b():
    print("function_b called")
    function_c()

def function_c():
    print("function_c called")

function_a()

# stack trace error kiyawanna ona yata idala udata
# trackback eke yata sita udata kiyawanna ona