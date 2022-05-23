1. ### To add new food item
----------
```curl --location --request POST 'http://0.0.0.0:4331/rms/v1/food/?inStock=false&slot=DINNER' --header 'Content-Type: application/json' --header 'Accept: application/json, text/plain, */*' --data-raw '{"name": "Toast","timeslot": "BREAKFAST","price": 50,"category": "VEG","in_stock": true}'```
    
    Response Structure
    -------
    {
        "result": {
           "category": "VEG",
           "id": "628bafa5a0ade5dbdbcb3a8a",
           "inStock": false,
           "name": "Toast",
           "price": 50.0,
           "slot": "BREAKFAST"
       },
       "status": 200 
      }
-----------------------------------
2. ### To update food status
   ```curl --location --request PATCH 'http://0.0.0.0:4331/rms/v1/food/628bafa5a0ade5dbdbcb3a8a?status=true'```

       Response Structure
       ------
       {
        "result": {
           "category": "VEG",
           "id": "628bafa5a0ade5dbdbcb3a8a",
           "inStock": true,
           "name": "Toast",
           "price": 50.0,
           "slot": "BREAKFAST"
       },
       "status": 200}
-----------------------------------
3. ### To list all food items
   To list all food in given slot and given category
       1) slot value could be any one of these [BREAKFAST, LUNCH, DINNER, SNACKS]
       2) foodType value could by any one of these [VEG, NON_VEG]
   ```
   curl --location --request GET 'http://0.0.0.0:4331/rms/v1/food/?slot=DINNER&foodType=VEG'
   ```
   
       Response Structure
        ------
        {
         "results": [
            {
               "category": "VEG",
               "id": "628bafa5a0ade5dbdbcb3a8a",
               "inStock": false,
               "name": "Toast",
               "price": 50.0,
               "slot": "BREAKFAST"
           },
           {
               "category": "VEG",
               "id": "628bafc92e2ab3b2bdc828f3",
               "inStock": false,
               "name": "Toast",
               "price": 50.0,
               "slot": "BREAKFAST"
           },
       ],
       "status": 200}
-----------------------------------
