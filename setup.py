from setuptools import setup

with open('README.md','r',encoding='utf-8') as fh:
    long_description = fh.read()
AUTHOR_NAME = 'BABBY AHMED'
SRC_REPO = 'src'
LIST_OF_REQUIRMENTS = ['streamlit']

setup(
    name = SRC_REPO,
    version = '0.0.1',
    author = AUTHOR_NAME,
    author_email = 'entbappy73@gmail.com',
    description = 'A small example package for movies recommender',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    package = [SRC_REPO],
    python_requires = '>=3.7',
    install_requires = LIST_OF_REQUIRMENTS,
)