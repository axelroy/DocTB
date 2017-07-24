#!/usr/bin/env bash

if [ "$1" = "train" ]; then
	echo "Running statefull docker container in training mode..."
	python main.py train
fi


if [ "$1" = "test" ]; then
	echo "Running statefull docker container in test mode..."
	python main.py test
fi
