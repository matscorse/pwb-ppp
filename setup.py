import setuptools

def get_content(filename):
  with open(filename, "r") as fh:
    return fh.read()

setuptools.setup(
  include_package_data=True,
  name='pwb-ppp',
  version='0.0.1',
  description='penguin weighbridge python processing package',
  author='matscorse',
  author_email='matsco@bas.ac.uk',
  package_dir={"": "src"},
  packages=setuptools.find_packages(where='src'),
  install_requires=['numpy==1.26.4', ],
  entry_points={
    'console_scripts': ['pwb-ppp=pwb-ppp.pwb-ppp:main']},
  long_description=get_content("README.md"),
  long_description_content_type="text/markdown",
  url="https://www.github.com/antarctica",
  classifiers=[el.lstrip() for el in """Development Status :: Beta
    Intended Audience :: Science/Research
    Intended Audience :: System Administrators
    License :: OSI Approved :: MIT License
    Natural Language :: English
    Operating System :: OS Independent
    Programming Language :: Python
    Programming Language :: Python :: 3
    Topic :: Scientific/Engineering""".split('\n')],
)