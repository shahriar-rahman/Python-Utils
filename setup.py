from setuptools import setup, find_packages

setup(
    name='python_utils',
    version='1.0.1',
    author='Shahriar Rahman',
    author_email='shahriarrahman1101@gmail.com',
    description='A Python package that includes several common Python util functions.',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)