#!/bin/bash

cd usb-scale-reader
make 
cd ..
sudo cp usb-scale-reader/80-persistent-scale.rules /etc/udev/rules.d
sudo adduser $USER plugdev
