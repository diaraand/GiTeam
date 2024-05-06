import cvs #import the cvs in order to be able to reade and the write the file

def Ateneo_Comp(file_path, nome1, nome2): #we define the function which has 3 parameters: the first one takes the file path, the second the name of a university and the thirde the name of the other university that we want to be compared

    risultato = {} #the dictionary called risultato will show the result of the comparison

    if not isinstance(nome1, str) or not isinstance(nome2, str): #we first need to check if the parameters nome are string
        return 'invalid input' #if yest it will go to the next step, on the contrary it will return invalid input
    
    with open(file_path, newline='', encoding='ISO-8859-1') as file_csv: #we open the file and name it file_csv
        lettore = csv.DictReader(file_cvs, delimiter=';') #it reads the file and interprets each row as a disctionary where the keys are the column headers and the values are the corresponding row values. The semicolon is used as the field delimiter in the CSV file

        for riga in lettore: #each row of the file
            ateneo_nome = riga['AteneoNOME'] #each value in the column AteneoNOME will be assigned to the variable ateneo_nome
            numero_iscritti = int(riga['Isc'])
            sesso = riga['Sesso']

            if ateneo_nome in [nome1, nome2]: #check if ateneo_nome is either in nome1 or nome2
                if ateneo_nome not in risultato: #if it is not neither in risultato
                    risultato[ateneo_nome] = {'M': 0, 'F': 0} #the value of male and female will be respectively 0

                risultato[ateneo_nome][sesso] += numero_iscritti #we add the number of  enrolled students to the count of students of a particular gender for a specific university

    return risultato