The current script I am using to run the bqskit optimization is the bqskitTesting.py file.
When using the default compiler, I get no errors. However, when trying to specify a custom workflow to follow the advice Dr. Iancu gave, I am getting the error shown in error.txt
I found that this only occurs when I add in the LEAPSynthisesPass() to the workflow.

The bqskitTesting.py script has been run in a clean conda envrionment with the latest version of python installed by: conda install python
Bqskit and all of its dependinces are installed in the recomended way through pip: pip install bqskit

I have also added an example of the qasm files (sigma_x_0.1_circ.qasm) I read into the program which contain the Qiskit circuits I am hoping to optimize.

Below are all of the packages that I currently have installed in this envrionment.

# packages in environment at /opt/homebrew/Caskroom/miniconda/base/envs/Bqskit:
#
# Name                    Version                   Build  Channel
annotated-types           0.7.0                    pypi_0    pypi
bqskit                    1.2.0                    pypi_0    pypi
bqskitrs                  0.4.1                    pypi_0    pypi
bzip2                     1.0.8                h80987f9_6  
ca-certificates           2025.2.25            hca03da5_0  
certifi                   2025.1.31                pypi_0    pypi
cffi                      1.17.1                   pypi_0    pypi
charset-normalizer        3.4.1                    pypi_0    pypi
cryptography              44.0.2                   pypi_0    pypi
dill                      0.3.9                    pypi_0    pypi
expat                     2.6.4                h313beb8_0  
ibm-cloud-sdk-core        3.23.0                   pypi_0    pypi
ibm-platform-services     0.63.0                   pypi_0    pypi
idna                      3.10                     pypi_0    pypi
lark                      1.2.2                    pypi_0    pypi
libcxx                    14.0.6               h848a8c0_0  
libffi                    3.4.4                hca03da5_1  
libmpdec                  4.0.0                h80987f9_0  
mpmath                    1.3.0                    pypi_0    pypi
ncurses                   6.4                  h313beb8_0  
numpy                     2.2.4                    pypi_0    pypi
openssl                   3.0.16               h02f6b3c_0  
packaging                 24.2                     pypi_0    pypi
pbr                       6.1.1                    pypi_0    pypi
pip                       25.0            py313hca03da5_0  
pycparser                 2.22                     pypi_0    pypi
pydantic                  2.9.2                    pypi_0    pypi
pydantic-core             2.23.4                   pypi_0    pypi
pyjwt                     2.10.1                   pypi_0    pypi
pyspnego                  0.11.2                   pypi_0    pypi
python                    3.13.2          h4862095_100_cp313  
python-dateutil           2.9.0.post0              pypi_0    pypi
python_abi                3.13                    0_cp313  
qiskit                    2.0.0                    pypi_0    pypi
qiskit-ibm-runtime        0.37.0                   pypi_0    pypi
readline                  8.2                  h1a28f6b_0  
requests                  2.32.3                   pypi_0    pypi
requests-ntlm             1.3.0                    pypi_0    pypi
rustworkx                 0.16.0                   pypi_0    pypi
scipy                     1.15.2                   pypi_0    pypi
setuptools                75.8.0          py313hca03da5_0  
six                       1.17.0                   pypi_0    pypi
sqlite                    3.45.3               h80987f9_0  
stevedore                 5.4.1                    pypi_0    pypi
symengine                 0.13.0                   pypi_0    pypi
sympy                     1.13.3                   pypi_0    pypi
tk                        8.6.14               h6ba3021_0  
typing-extensions         4.13.0                   pypi_0    pypi
tzdata                    2025a                h04d1e81_0  
urllib3                   2.3.0                    pypi_0    pypi
websocket-client          1.8.0                    pypi_0    pypi
wheel                     0.45.1          py313hca03da5_0  
xz                        5.6.4                h80987f9_1  
zlib                      1.2.13               h18a0788_1
