# GiTeam

## Table of Contents 

1. [Team composition](#1-team-composition)
2. [Dataset](#2-dataset)
3. [Description of the project](#3-description-of-the-project)
4. [Backend functions](#4-backend-functions)
5. [Frontend HTML templates](#5-frontend-html-templates)
6. [Usage](#6-usage)
7. [Testing](#7-testing)


## 1. Group Composition

- Ceapa Jennifer 889006
- Fornasa Chiara 889007
- Li Ambra 888688
- Ndiaye Sokhna Diara 890575
- Riso Anna 891038


## 2. Dataset

- File Name: ds752_iscritti_anno_accademico_2017-18.csv
- Format: CSV
- Columns:
     -  Year
     -  University
     -  Course (number)
     -  Gender
     -  Number of enrolled students per class 


## 3. Description of the project 

This project aims to analyze university enrollment data to gain insights into gender distribution and overall student enrollment across various universities. The analysis focuses on comparing enrollment figures between different universities and categorizing them based on their public or private status.

### **Universities of Milan** 

The first page presents a detailed overview of the totoal number of enrolled students, specificallt fot each university located in Milan. The results are displayed in adn easy-to-read format, listing each university's name alongside its total enrollment count. This section provides comprehensive snapshot of student distribution across different universities in Milan. Below, the interface offers two interactive options for further analysis: "Compare University" and "public VS private"

### **Compare University**

In this section, you can use a dropdown menu to select different universities for comparison. Once you have chosen the universities, the system will generate a graph displying the differences in the number of male and female students between the selected univerisities. This visual representation helps in understanding the gender distribution and highlights any significant disparties in enrollment figures.

### **publicVSprivate**

Int this section, this option enables users to compare the number of male (M) and female (F) students between public and private universities. Selecting this option provides a graph comparison of gender distribution within the two categories of universities, offering a broader perspective on student demographics across different types of institutions 


## 4. Backend functions 

In particular, in order to display these options, we developed three functions:
1. Ateneo_Comp

           - Description: This function compares the number of male (M) and female (F) students enrolled in two specified universities (Ateneo) based on provided CSV file. It sums up the gender-wise enrollment for each university and returns a dictionary with the comparison results 

           -Parameters:
           file_path: Path to the CSV file containing enrollment data. 
           nome1 and nome2: Names of the two universities to be compared.
           
           - Returns: A dictionary with the comparison results, where each university name is a key, and the corresponding value is another dictionary with the counts of male and female stundents 


2. Ateneo_Counter 

           - Description: This function counts the total number of enrolled students for each university (Ateneo) based on  the provided CSV file. It calculates the overall enrollment count for each university and returns dictionary with the results.

           -Parameters:
           file_path: Path to the CSV file containing enrollment data.

           - Returns: A dictionary with the total enrollment count for each university, where each name is a key, and the corrresponding value is the total number of enrolled students. 
           


3. Public_Private 
           
           - Description: This function compares the number of male (M) and female (F) students between public and private universities based on the provided CSV file. It categorizes universities into public and private and then sums up the gender-wisr enrollment fot each category. The results are returned in a dictionary.

           - Parameters:
           file_pathe: Path to the CSV file cointaining enrollment data 

           - Returns: A dictionary with the comparison results between public and private universities, where each university category (public or private) is a key, and the corresponding value is another dictionary with the counts of male and female students. 
           
## 5. Frontend HTML templates

The frontend represents the user interface. In particular:

1. base.html: The base.html file serves as the foundational template for other HTML files. It includes essential meta tags, links to JavaScript libraries and sets up the basic structure for the web pages.

2. compare.html: The compare.html file represents the comparison page of the application. Users can select two universities from a dropdown menu and click a "Compare" button to visualize a comparison. The page includes a form, a canvas for displaying a bar chart and a back button to return to the homepage.

3. index.html: The inde.html file serves as the homepage of the appllication, displaying a table with information about the Universities and their respective student populations.

4. publicVSprivate.html: The publicVSprivate.htnl file dispalys a pie chart comparing the number of male and female students between public and private universities. It uses the Chart.js library to create the visualization. The page also includes a back button for navigation. 

## 6. Usage 

1. Clone the repository and navigate to the directory:

    ```bash
    git clone https://github.com/diaraand/GiTeam.git
    ```

2. Open the terminal from the menu and type the following command:

    ```bash
    docker compose build backend
    ```

    ```bash
    docker compose build frontend
    ```

    ```bash
    docker compose up backend
    ```

    ```bash
    docker compose up frontend
    ```
3. Launch the Docker extension in VS Code and navigate to the Containers tab.\
You should see two containers that are currently running (indicated by green arrows).\
Right-click on each of them and select "Attach Visual Studio".\
This will open two new VS Code windows: one for the backend and one for the frontend.

4. Repeat this step for both the frontend and backend.

5. Navigate to the Run and Debug section, and start the backend first, followed by the frontend.

6. Open your web browser and navigate to http://localhost:8080 to access the frontend and http://localhost:8081 to access the backend.

## 7. Testing

We've created some tests to ensure our backend works correctly. To execute these tests, open the backend VS Code window, launch the terminal, and enter the following command:

```bash
    pytest --cov=app --cov-report=html tests/
```

The test we implemented are: 
- test_Ateneo_Comp: This script sets up unit tests using Python's `unittest` framework to verify the correct functionality of the `Ateneo_Comp` function with various inputs, ensuring it handles invalid inputs properly and produces the expected output for valid inputs. It includes tests for invalid numerical input, `None` values, and valid string inputs, and runs these tests when the script is executed as the main program.
- test_Public_Private: This script sets up a unit test for the `Public_Private` function, ensuring it processes the CSV file correctly and returns the expected enrollment data for various universities, categorized by gender. It runs the test when the script is executed as the main program, comparing the function's output to a predefined dictionary of expected results.
- test_Ateneo_Counter: This script conducts unit testing for the `Ateneo_Counter` class, verifying its functionality by instantiating the class with a provided CSV file and asserting the expected enrollment counts for various universities against the actual results. It runs the test when executed as the main program, ensuring accurate counts of student enrollments are returned by the `Ateneo_Counter` class.
