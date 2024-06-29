import csv  # Import the cvs in order to be able to read and write the file


def Ateneo_Comp(file_path, nome1, nome2):  # We defined the function which has 3 parameters: the first one takes the file path, the second the name of a university and the third the name of the other university that we want to be compared
    """
    Compares the number of male and female students enrolled in two universities

    Parameters:
        file_path (str): Path to the CSV file containing enrollment data.
        nome1 (str): Name of the first university.
        nome2 (str): Name of the second university.

    Returns:
        dict: A dictionary with the number of male (M) and female (F) students for each university.
              Returns 'invalid input' if the inputs are not valid strings.
    """

    risultato = {}  # The dictionary called risultato will show the result of the comparison

    if not isinstance(nome1, str) or not isinstance(nome2, str):  # We first need to check if the parameters nome are string
        return 'invalid input'  # If yest it will go to the next step, on the contrary it will return invalid input

    with open(file_path, newline='', encoding='ISO-8859-1') as file_csv:  # We open the file and name it file_csv
        lettore = csv.DictReader(file_csv, delimiter=';')  # It reads the file and interprets each row as a disctionary where the keys are the column headers and the values are the corresponding row values. The semicolon is used as the field delimiter in the CSV file

        for riga in lettore:  # Each row of the file
            ateneo_nome = riga['AteneoNOME']  # Each value in the column AteneoNOME will be assigned to the variable ateneo_nome
            numero_iscritti = int(riga['Isc'])
            sesso = riga['Sesso']

            if ateneo_nome in [nome1, nome2]:  # Check if ateneo_nome is either in nome1 or nome2
                if ateneo_nome not in risultato:  # If it is neither in risultato
                    risultato[ateneo_nome] = {'M': 0, 'F': 0}  # The value of male and female will be respectively 0

                risultato[ateneo_nome][sesso] += numero_iscritti  # We add the number of  enrolled students to the count of students of a particular gender for a specific university

    return risultato
