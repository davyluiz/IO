#!/bin/bash

function breakLine(){
    local count=1
    while [ $count -le "$1" ]; do
        #echo "espaço nº $count"
        echo ""
        count=$((count+1))
    done
}

function checkRoot(){
    if [[ "$(id -u)" -ne 0 ]];then
        return 1
        #printf "A execução requer privilégios!"
        #exit 1
    fi
}





