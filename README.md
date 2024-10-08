# Python Utils 
![python](https://img.shields.io/badge/python-3.11-blue)
[![License: MIT License](https://img.shields.io/badge/License-MIT-red.svg)](LICENSE)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python Cookiecutter](https://img.shields.io/badge/-•Python_Cookiecutter-orange?style=flat&logo=surprise&link=https://github.com/shahriar-rahman)](https://github.com/shahriar-rahman/Python-Cookiecutter)

<br/>

## Description
A Python package that includes several common Python util functions. 

<br/>

## Installation
• Install the package using pip:
```pip
$ pip install git+https://github.com/shahriar-rahman/Python-Utils       
```
• Next, import and initialize it like the example below:
```py3
from python_utils import common_utils        

df = common_utils.create_df({'some_values': [5, 3, 2, 4, 9]})      
print(df.head(5))      
```

<br/>

## Usecases
• Create Dataframe
```py3
obj.create_df(key_dict={'col': 'values'})         
```
• Save Dataframe
```py3
obj.save_df(df, ext_type='csv', path)         
```
• Display Dataframe
```py3
obj.display_df(df, contents=5)         
```
• Load Dataframe
```py3
obj.load_df(ext_type='csv', library='pd', path='path_to_csv, d_type=False)           
```
