import csv


def Public_Private(file_path):
    """
    Compares the number of male and female students between public and private universities

    Parameters:
        file_path (str): Path to the CSV file containing enrollment data.

    Returns:
        dict: A dictionary with university names as keys and a nested dictionary wirh the count of male (M) and female (F) students as values.
    """

    risultato = {}
# Open the csv file
    with open(file_path, newline='', encoding='ISO-8859-1') as file_csv:
        lettore = csv.DictReader(file_csv, delimiter=';')
# Iteratation and get university, enrolled students and gender
        for riga in lettore:
            ateneo_nome = riga['AteneoNOME']
            numero_iscritti = int(riga['Isc'])
            sesso = riga['Sesso']
# If the university it's not present: add it to the dictionary
            if ateneo_nome not in risultato:
                risultato[ateneo_nome] = {'M': 0, 'F': 0}
# Update the count of enrolled students for the corresponding gender
            risultato[ateneo_nome][sesso] += numero_iscritti
# Return the final result
    return risultato
