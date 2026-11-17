import greeting

greeting.greet("Alice")
greeting.goodbye("Alice")

name = input("Enter your name: ")
greeting.greet(name)

from greeting import greet
greet("Bob")