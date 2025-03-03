from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'  # String used in requirements files for local installation

def get_requirements(file_path:str)->List[str]:
    """Reads a requirements file and returns a list of dependencies."""
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()  # Read and clean up lines
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:  # Remove '-e .' requirements list
            requirements.remove(HYPEN_E_DOT)

        return requirements

# Setup function to configure the package
setup(
    name='DiamondPricePrediction', # Package name
    version='0.0.1',
    author='Awinash',
    author_email='awinashkr31@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages() # Automatically detect and include packages

)