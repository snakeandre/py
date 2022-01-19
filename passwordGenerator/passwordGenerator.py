from random import shuffle
n = int(input("Choose number of password: "))
l = int(input("Insert password length: "))
c = int(input("Choose password complexity (1 - only letters, 2 - letters and numbers, 3 - letters, numbers and special characters: "))
while True:
    if c>3 or c<0:
        c = int(input("Choose a number between 1-3: "))
    else:
        break
if c==1:
    ch = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
if c==2:
    ch = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9'.split()
if c==3:
    ch = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9 @ _ ! # % ^ & * ( ) < > ? / | } { ~ : ] ['.split()
for num in range(n):
    shuffle(ch)
    password = ch[:l]
    password = "".join(password)
    print(f"password {num}: {password}")
input("\nPress enter to close")