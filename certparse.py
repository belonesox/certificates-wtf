#pylint: disable-all
# Create your views here.

import os

import sys
from rhsm import certificate

def parse_cert():
        client_cert = '''
-----BEGIN CERTIFICATE-----
MIIEyjCCArKgAwIBAgIIISy0Q9KHEoMwDQYJKoZIhvcNAQEFBQAwMzELMAkGA1UE
BhMCVVMxEjAQBgNVBAoMCVZpcnR1b3p6bzEQMA4GA1UEAwwHUm9vdCBDQTAeFw0x
NjAxMjUwMDAwMDBaFw0xNzA5MDUwMDAwMDBaMCsxKTAnBgNVBAMTIGZmODA4MTgx
NTJlZjkxZGQwMTUyZWY5NWRlYWEwMDU2MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8A
MIIBCgKCAQEArhqai9AEoyIhX2wevUoEtFE2YPk/XIA+TDhUnd32N6u9hNe8LM3x
JqquLpFB1VQLbbPajogIUrmm4b62e+GpGYUEJP6kyeFf4QbXuUWbkwbgft2drvFA
wEzbv/Yi2i4SuDFjAIXez49ToK9PTfl6u3BhXqetPc5i+FGYtsc86txm53F+meO2
WXhEMAVCfXnw4/7QpCsXRfN5S4n+cu46teUFlaPAzGeflnFBrpdQwQw+IsFjsWds
kKTg07OVJ0PJ4sdH61fPtROAoQtdt668yTifk56vjEztrAjA/G+NkYEZngBj8zb+
InmN+3b7Fkw3EM3QuQQsanGA7Z7gtGdh6wIDAQABo4HpMIHmMBEGCWCGSAGG+EIB
AQQEAwIFoDALBgNVHQ8EBAMCBLAwXAYDVR0jBFUwU4AUJxLzb7nZOcojBlKHPKE4
d/zgUdChN6Q1MDMxCzAJBgNVBAYTAlVTMRIwEAYDVQQKDAlWaXJ0dW96em8xEDAO
BgNVBAMMB1Jvb3QgQ0GCAhABMB0GA1UdDgQWBBTJHgdTJ5WPg9c85XH3aQikHXPJ
4TATBgNVHSUEDDAKBggrBgEFBQcDAjASBgkrBgEEAZIICQYEBQwDMy4yMB4GCSsG
AQQBkggJBwQRBA942itJLS5hAAAGHgHBAmAwDQYJKoZIhvcNAQEFBQADggIBAHCz
PJgSvoaCkmuQGRFo2M5cF9IxfQ8wf9R0o9E2cbfH7hwDXUZoztlm6OhrdFJONfzO
i+i3VE2s2QkDyxV6RHFpJ4e3XoC9V5eiGI9X5xdY5d5jD+B5SjEd4WVpaRm+H6qK
eatUY1ldo9FVyMuMSWdj2J3Wzmrz16O4zpU/2gdwkYr//BsuCz6dTwsKoPK2+0FZ
EMixVZXT3osowu5huiJ42Of8arNFz85lTVXkY8X/3X/nABFU2+LfvGsXTrroy0yY
aWC7Katj5r/lnZCfy84nPT1wafyczJlZCZ37+rjlKga5Y06blLt4I36YDt42fi5w
A8CoiH/PI46bNJos2mvTd6+uzZnBh7ZR+kLI2+8eadDetsOfrqpfyUNcyCv2UFos
rJOt8K/oQuX4qidLaJscWaxcfP8rtmNEHj7tcRD4U/YhAk+oY43tyKDYh7V8ve9b
mfguLMq692DJGTgZ/v3Aq/UV1K26t+OMvpo1am+fyXLWSMeiBrTP9Sg+lT981057
NBnyV8bO1Js9FWs+yBLFh8dMVaGl4QdxMNBS+140gWkHJ349id9LMEjgwo+cVjYU
dDlq4c7RmzboDI3xccqDPJzBklp8bX1yQRx+dIcUV11ZCV6H1Nbcin6cZ+9Z+MFu
JdgBZ1ABr6Hq0KzACwFjsq6ybJOAstuqyL1SACri
-----END CERTIFICATE-----        
        '''.strip()
        
        path2check = '/test'
        cert = certificate.create_from_pem(client_cert)
        cert.check_path('/') # AttributeError: 'NoneType' object has no attribute 'value' 
        pass    
    

if __name__ == '__main__':
    parse_cert()
    
    