day = (input  ("What Day Is It Today?\n "))
while int(day) > 7 or int(day) < 1:
  day = str(    input   ("Day Must Be In A Number Between 1 And 7. Try Again.\n "))
match int(day):
    case 1:
        print   ("Monday")
    case 2:
        print   ("Tuesday")
    case 3:
        print   ("Wednesday")
    case 4:
        print   ("Thursday")
    case 5:
        print   ("Friday")
    case 6:
        print   ("Saturday")
    case 7:
        print   ("Sunday")
