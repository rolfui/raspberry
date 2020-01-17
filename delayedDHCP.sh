#!/bin/bash

sleepTime=1
while true; do
    ifconfig eth0 | grep "192.168.1.1"
    if [ $? -ne 0 ]; then
        sleepTime=1
        echo "eth0 not connected"
    else
        echo "eth0 connected"
	isActive=$(systemctl is-active isc-dhcp-server.service)
        echo $isActive
        if [ $isActive != "active" ]; then
           echo "Starting dhcp ..."
           sudo service isc-dhcp-server start
           sleepTime=20
        fi
    fi
    sleep $sleepTime
done
