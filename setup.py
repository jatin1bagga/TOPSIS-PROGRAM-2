from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name="JATIN_BAGGA_102203713",
    version="1.0.3",
    author="JATIN_BAGGA",
    author_email="jbagga_be22@thapar.edu",
    description="A Python package implementing TOPSIS method for MCDM",
    long_description=readme(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas'
    ],
    entry_points={
        'console_scripts': [
            'topsis=topsis_jatin.topsis:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)