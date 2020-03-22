#!/bin/bash

make usb-scale-reader
sudo cp usb-scale-reader/80-persistent-scale.rules /etc/udev/rules.d
sudo adduser $USER plugdev

