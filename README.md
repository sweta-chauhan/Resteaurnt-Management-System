# Resteaurnt-Management-System
Simple Project

## Tech Used
1. flask_restful
2. mongoDB

## Functionality
1. APIs to 
   1. create or add food items
   2. update food items stock status
   3. add new customer
   4. create cart
   5. patch cart 
      1. to add item 
      2. checkout which will create order
   6. patch order delivery status

## Source Code Structure
![](../../Pictures/Screenshot from 2022-05-21 14-16-55.png)

Config
----------
1. This will hold external dependencies


rms
---------
1. dao
2. views
3. handler
4. controller
5. utils

rms_app.py
--------
Main app file or can say driver program