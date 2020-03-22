#!/bin/bash

DATA_FILE="data.csv"

while :
do
    WEIGHT_RAW="$(./usb-scale-reader/usbscale /dev/scale)"
    TIME="$(date +%s)"
    WEIGHT_VALUE_REGEX="([0-9]+.[0-9]*) g"
    if [[ $WEIGHT_RAW =~ $WEIGHT_VALUE_REGEX ]]; then 
        WEIGHT_VALUE="${BASH_REMATCH[1]}"
        echo "$TIME, $WEIGHT_VALUE" >> $DATA_FILE
    else 
        echo "Could not get data from scale"; 
    fi
    sleep 2
done

