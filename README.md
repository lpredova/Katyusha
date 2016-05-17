#Katyusha REST and SOAP fuzzer

## Synopsis


Katyusha is simple **REST and SOAP API fuzzer**.

It's straightforward,lightweight and written in Python and Angular JS.  
Wiki page of the project (cro): http://security.foi.hr/wiki/index.php/Fuzzing_web_servisa_(REST_i_SOAP) .

We tried to make it as straightforwad as it can be. Just follow the instructions and you'll get where you want to be.

This web API fuzzer is made as project asignment for SIS - Security of information systems at FOI http://security.foi.hr/wiki/index.php/Glavna_stranica .


## Installation

Dependencies:

*   Pysimpesoap - https://code.google.com/p/pysimplesoap/
*   Requests - http://docs.python-requests.org/en/latest/
*   Fuzz db - https://github.com/fuzzdb-project/fuzzdb

## Example

Before runing the code please check that you have installed dependancies listed below.  In bash run:

```python
python main.py
```

After that it's really simple (example for REST):

```python
Please choose your action:
1) Fuzz API service
2) View results
3) Quit
Select:1
```
After that simply select methods and params you want to fuzz

```python
Please choose your protocole:
1) REST
2) SOAP
3) Quit
Select:1
################################################
REST FUZZER
################################################
Please insert URL to API :http://192.168.56.101/mutillidae/webservices/rest/ws-user-account.php

Method:
1) GET
2) POST
3) Quit
Select:1
################################################
Name of the parametar you want to fuzz :username
Fuzz this parameter (Y/N):y
Add more parameters (Y/N) ? n
Fuzzing started...
```

After the fuzzing is done you can see the results in your webbrowser

```python
Fuzzing done...
Results saved at: 'results/'rest_result_2015_01_08_02_23_04.json

View results:
1) YES
2) NO
3) Quit
Select:1
Find results at:
http://localhost:8088/#/rest_result_2015_01_08_02_23_04.json
running local server...
Listening on 8088
```

## Contributors

Made by **Milan Pavlović** and **Lovro Predovan** 2015.

Please report bugs and sugestions to:  
https://twitter.com/lovro_p

## License

This software is under a **DBAD** license
