from setuptools import setup,find_packages
from typing import List

hypen="-e ."

def get_requirements(file_obj:str)->List[str]:
    requirements=[]
    with open (file_obj)as f:
        requirements=f.readlines()
        requirements=[i.replace("\n","") for i in requirements]
        
        if hypen in requirements:
            requirements.remove(hypen)
    return requirements
    


setup(name="my ml proj",
      author="hema datascientist",
      author_email="hemasrinivasulu.ds@gmail.com",
      version="0.0.2",
      packages=find_packages(),
      install_requires=get_requirements("requirements.txt")
      )