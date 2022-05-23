1. ### To add item in cart
   ```commandline
    curl --location --request POST 'http://0.0.0.0:4331/rms/v1/cart/' \
   --header 'Content-Type: application/json' \
   --data-raw '{
   "customerId": "628bb676163d0e755eb46c66"
   }'   
   ```
   
       Response Structure
       -----------
       {
          "result": {
                      "cartId": "628bb9e9026f82b269ab3889",
                       "createdAt": "2022-05-23T22:14:25 PM",
                       "customerId": "628bb676163d0e755eb46c66",
                       "foodList": [],
                       "lastUpdatedAt": ""
                    },
                 "status": 200
          }

2. ### To add item in a cart
   ```commandline
   curl --location --request PATCH 'http://0.0.0.0:4331/rms/v1/cart/628bb9e9026f82b269ab3889' \
   --header 'Content-Type: application/json' \
   --data-raw '{
    "action": "ADD_ITEM",
    "body": [
        {
            "id": "628bafa5a0ade5dbdbcb3a8a",
            "quantity": 2
        }
    ]
   }'
    ```
    
        Response Structure
         ------
         {
           "result": {
                          "cartId": "628bb9e9026f82b269ab3889",
                          "createdAt": "2022-05-23T22:14:25 PM",
                          "customerId": "628bb676163d0e755eb46c66",
                          "foodList": [
                                        {
                                           "628bafa5a0ade5dbdbcb3a8a": 2
                                        }
                          ],
                         "lastUpdatedAt": "2022-05-23T22:26:39 PM"
                      },
          "status": 200
         }

   1. ### To create order using checkout
       ```
      curl --location --request PATCH 'http://0.0.0.0:4331/rms/v1/cart/628bc05cd2a0597eb7d0fdfc' \
      --header 'Content-Type: application/json' \ 
      --data-raw '{
       "action": "CHECKOUT",
       "body":{
               "mode": "DIGITAL"
           }
    
      }'
       ```
   
          Response Structure
          ---------
          {
                "result": {
                             "cartId": "628bc05cd2a0597eb7d0fdfc",
                              "createdAt": "2022-05-23T22:41:56 PM",
                              "customerId": "628bb676163d0e755eb46c66",
                              "foodList": [],
                              "lastUpdatedAt": "2022-05-23T22:53:24 PM"
                   },
               "status": 200
          }