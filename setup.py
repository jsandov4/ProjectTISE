from distutils.core import setup

with open('README.md') as f:
    long_description = ''.join(f.readlines())

# get the dependencies and installs
with open('requirements.txt') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]


setup(name='ProjTISE',
      version='1.0',
      description='Solving TISE program',
      long_description=long_description,
      author='Juan S Sandoval',
      author_email='jsandov4@ur.rochester.edu',
      url='https://github.com/jsandov4/ProjectTISE',
      packages=['TISE'],
      install_requires=install_requires,
      entry_points = {
	'console_scripts' : ['TISE = TISE.Methods:main'],
      }
     )





