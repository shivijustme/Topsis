# import setuptools
 
# with open("README.md", "r") as fh:
#     long_description = fh.read()
 
# setuptools.setup(
#     #Here is the module name.
#     name="TOPSIS-Shivansh-101803103",
 
#     #version of the module
#     version="0.0.1",
 
#     #Name of Author
#     author="Shivansh Kumar",
 
#     #your Email address
#     author_email="skumar_be18@thapar.edu",
 
#     #Small Description about module
#     description="TOPSIS in Python",
 
#     long_description=long_description,
 
#     #Specifying that we are using markdown file for description
#     long_description_content_type="text/markdown",
 
#     packages=setuptools.find_packages(),
 
#     #classifiers like program is suitable for python3, just leave as it is.
#     classifiers=[
#         "Programming Language :: Python :: 3",
#         "License :: OSI Approved :: MIT License",
#         "Operating System :: OS Independent",
#     ],
# )


from setuptools import setup

with open("README.md","r") as fh:
    long_description = fh.read()

setup(
  name = 'TOPSIS-Shivansh-101803103',
  version = '0.0.1',
  description = 'Find the Topsis Score Easily as well as preciously - Multiple Criteria Decision Making!',
  py_modules = ["topsis"],
  package_dir = {'':'TOPSIS-Shivansh-101803103'},
  package_data={'':['LICENSE.txt']},
  include_package_data=True,
#   url="https://github.com/manmeet-kaur18/Topsis",
  author="Shivansh Kumar",
  author_email="shivansh.justme@gmail.com",
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
  long_description=long_description,
  long_description_content_type="text/markdown",
  extras_require={
    "dev":[
        "pytest>=3.7",
    ],
  },
)
