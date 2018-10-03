#!/usr/bin/env python
# -*- coding: utf-8 -*-

x = 23
guess = int(raw_input("Guess a number between 5 and 78: "))

if guess == x:
    print "Congradulations, You Win"
else:
    print "Sorry, try again. The number is not " + str(guess)