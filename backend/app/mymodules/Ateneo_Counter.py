import csv


def Ateneo_Counter(file_path):
    """
    Counts the total number of students enrolled in each university.

    Parameters:
        file_path (str): Path to the CSV file containing enrollment data.

    Returns:
        dict: A dictionary with university names as keys and the total number of enrolled students as values.
    """

    risultato = {}  # Dictionary to store the result

    # Open the CSV file
    with open(file_path, newline='', encoding='ISO-8859-1') as file_csv:
        lettore = csv.DictReader(file_csv, delimiter=';')

        # Iterate through each row in the CSV
        for riga in lettore:
            # Get the university name and number of enrolled students from the row
            ateneo_nome = riga['AteneoNOME']
            numero_iscritti = int(riga['Isc'])

            # Check if the university name already exists in the result dictionary
            if ateneo_nome not in risultato.keys():
                # If not, add it to the dictionary with the number of enrolled students
                risultato[ateneo_nome] = numero_iscritti
            else:
                # If it exists, add the number of enrolled students to the existing total
                risultato[ateneo_nome] += numero_iscritti

    return risultato  # Return the dictionary containg university names and total enrolled students
