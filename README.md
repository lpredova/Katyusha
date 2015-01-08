Katyusha is straightforward REST and SOAP fuzzer

## Synopsis

Wiki page of the project (croatian) http://security.foi.hr/wiki/index.php/Fuzzing_web_servisa_(REST_i_SOAP)

Kayyusha is simple REST and SOAP API fuzzer. It's straightforward,lightweight and written in Python and Angular JS.


## Code Example

Before runnig the code please check that you have installed dependancies listed below.
In bash run:

```python
python main.py
```

After that it's really simple (example for REST)

```python
  _   __      _                   _
 | | / /     | |                 | |
 | |/ /  __ _| |_ _   _ _   _ ___| |__   __ _
 |    \ / _` | __| | | | | | / __|  _ \ / _` |
 | |\  \ (_| | |_| |_| | |_| \__ \ | | | (_| |
 \_| \_/\__,_|\__|\__, |\__,_|___/_| |_|\__,_|
                   __/ |
                  |___/
REST and SOAP fuzzer

################################################

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
running localhost server...
I'm listening....on 8088
```

## Motivation

This web API fuzzer is made as project asignment for SIS (Security of information systems at FOI http://security.foi.hr/wiki/index.php/Glavna_stranica).
We tried to make it as straightforwad as it can be. Just follow the instructions and you'll get where you want to be.

## Installation

Dependencies:
 Pysimpesoap - https://code.google.com/p/pysimplesoap/
 Requests - http://docs.python-requests.org/en/latest/
 
Also thanks to :
 Fuzz db - https://code.google.com/p/fuzzdb/

## Tests

Describe and show how to run the tests with code examples.

## Contributors

Made by Milan Pavlović and Lovro Predovan 2015.

Please report bugs and sugestions to:
https://twitter.com/lovro_p

## License

This software is under a DBAD license