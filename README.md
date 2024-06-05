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
           
           
