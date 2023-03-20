import os
power = 1
looper_control = 1

if power == 1:
    og_doc = str(input("Enter name: "))
    power += 1

while power >= 0:
    while True:
        try:
            if power == 2:
                menu = str(input("Calculator (1), File Mode (2), or Exit (3)?"))
                if menu == "1":
                    power = 3
                elif menu == "2":
                    power = 4
                elif menu == "3":
                    power = 0
                elif menu == "/0":
                    power = 0
                    break
                else:
                    raise ValueError("Invalid input. Please try")
            if power == 3:
                calc_doc = open(og_doc, "a")
                print("Welcome the The Calculator.")
                calc1 = str(input("Enter first number: "))
                if calc1 == "/0":
                    power -= 1
                    calc_doc.close()
                    break
                print(calc1," ", "operation"," ", "2nd", " ", "=", "result")
                the_op = str(input("Enter desired operation (+), (*), (/), (-) : "))
                if the_op == "/0":
                    power -= 1
                    calc_doc.close()
                    break
                print(calc1," ", the_op," ", "second number", " ", "=", "result")
                calc2 = str(input("Enter second number: "))
                if calc2 == "/0":
                    power -= 1
                    calc_doc.close()
                    break
                elif the_op == "+":
                    answer = float(calc1) + float(calc2)
                    num3 = str(answer)
                    equation = calc1 + " + " + calc2 + " = " + num3
                    equation_edit = str(equation)
                    print(equation_edit)
                    calc_doc.write(equation_edit)
                    calc_doc.write("\n")
                    looper_control += 1
                    #Rewrites instead of appends
                    break
                elif the_op == "-":
                    answer = float(calc1) - float(calc2)
                    num3 = str(answer)
                    equation = calc1 + " - " + calc2 + " = " + num3
                    equation_edit = str(equation)
                    print(equation_edit)
                    calc_doc.write(equation_edit)
                    calc_doc.write("\n")
                    looper_control += 1
                    #Rewrites instead of appends
                    break
                elif the_op == "*":
                    answer = float(calc1) * float(calc2)
                    num3 = str(answer)
                    equation = calc1 + " + " * calc2 + " = " + num3
                    equation_edit = str(equation)
                    print(equation_edit)
                    calc_doc.write(equation_edit)
                    calc_doc.write("\n")
                    looper_control += 1
                    #Rewrites instead of appends
                elif the_op == "/":
                    answer = float(calc1) + float(calc2)
                    num3 = str(answer)
                    equation = calc1 + " / " + calc2 + " = " + num3
                    equation_edit = str(equation)
                    print(equation_edit)
                    calc_doc.write(equation_edit)
                    calc_doc.write("\n")
                    looper_control += 1
                    #Rewrites instead of appends
                    break
                else:
                    continue
            if power == 4:
                print("File mode.")
                file_menu_user = str(input(print("(E)dit file name, or (r)ead content? ")))
                file_menu_code = file_menu_user.lower()
                if file_menu_code == "/0":
                    power -= 1
                    break
                elif file_menu_code == "e":
                    #Original name of doc
                    old_name = str(og_doc)
                    new_name = str(input("Enter new name: "))
                    #Changing the old filename for the new
                    os.rename(og_doc, new_name)
                    regen_doc = og_doc.replace(old_name, new_name)
                    og_doc = str(regen_doc)
                    #Making the newly created name into the old one
                    #To continue loop
                    power -= 2
                    continue
                elif file_menu_code == "r":
                    working_doc = open(og_doc, "r")
                    printed_output = working_doc.read()
                    print(printed_output)
                    power -= 2
                    working_doc.close()
                    break
            else:
                continue
        except ValueError:
            print("Incorrect input, please try again.")
            break
        finally:
            continue
    if  power == 0:
        print("Goodbye")
        exit()


