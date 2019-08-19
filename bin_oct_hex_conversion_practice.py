import random

def create_chunks(string, width):
    words = string.split(" ")
    temp = []
    chunks = []
    for word in words:
        temp += [word]
        if len(" ".join(temp)) < width:
            candidate = " ".join(temp)
        else:
            chunks += [candidate]
            temp = []
            temp += [word]
    
    chunks += [" ".join(temp)]

    return chunks

        
def boarder_message(message, width):
    """ Places a boarder around a message. 
    """        

    print('+-' + '-' * width + '-+')

    for line in create_chunks(message, width):
        print('| {0:^{1}} |'.format(line, width))

    print('+-' + '-'*(width) + '-+')

def greeting():
    greeting_message = ("Welcome! This program will help you practice converting "
                        "between binary, octal, and hexadecimal numbers.")
    boarder_message(greeting_message, 32)      

def ask_question(question_number, number, num_system_1, num_system_2):
    print("Q{}: Convert {}({}) --> {}(?)".format(question_number, 
        num_system_1['str'], num_system_1["op"].format(number), num_system_2["str"]))

def process_answer(question_number, number, num_system_2):
    response = input("A{}: ".format(question_number))
    answer = num_system_2['op'].format(number)
    if response == 'q': exit()
    if response == answer:
        print("Correct!")
    else:
        print("Incorrect, the answer is {}".format(answer))
   
def main():
    """ A simple command line program that can help students practice 
        number conversions between binary, octal, and hexadecimal. 
    """
    greeting()

    print("")
    print("Enter 'q' as your answer to quit.")
    print("")
    print("Enter 8 digits for bin answers.")
    print("Enter 3 digits for oct answers.")
    print("Enter 2 digits for hex answers.")
    print("")

    binary = {"str": "binary", "op": '{:08b}'}
    octal = {"str": "octal", "op": '{:03o}'}
    hexadecimal = {"str": "hexadecimal", "op": '{:02X}'}

    ls_num_systems = [binary, octal, hexadecimal]

    for i in range(1, 11):
        number = random.randint(1, 255)
        num_system_1, num_system_2 = random.sample(ls_num_systems, 2)
        ask_question(i, number, num_system_1, num_system_2)
        process_answer(i, number, num_system_2)
        print("")


if __name__ == "__main__":
    main()