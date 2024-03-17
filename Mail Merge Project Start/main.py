#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

file_path_for_letters = 'Input/Letters/starting_letter.txt'
file_path_for_names = 'Input/Names/invited_names.txt'

#C:\VS_python_projects\python_prodjects\working_this_files\Mail Merge Project Start\Input\Letters\starting_letter.txt


with open (file_path_for_letters, mode="r") as letter, open (file_path_for_names, mode="r") as name:
    letter1=letter.read()
    name1 = name.read().splitlines()
    for names in name1:
        person_letter=letter1.replace('[name]',names)
        filename = f"ReadyToSend/person_letter_{names}.txt"
        with open(filename, mode='w') as p_l:
            p_l.write(person_letter)
    