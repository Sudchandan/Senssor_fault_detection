from setuptools import find_packages,setup
# def get_requirements()->List[str]:
    
#     """
#     This Function Will List of Requirements
#     """

setup(

   name = "sensor",
   version = "0.0.1",
   author = "Sudesh",
   author_email = "sudesh9eng@gmil.com",
   packages = find_packages(),
   #nstall_requires =get_requirements() #["pymongo==4.2.0"],
   install_requires =["pymongo==4.2.0"],

)