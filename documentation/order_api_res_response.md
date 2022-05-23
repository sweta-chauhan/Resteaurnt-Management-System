1. ### In order to update order status
   ```commandline
   curl --location --request PATCH 'http://0.0.0.0:4331/rms/v1/order/628bc3f0fc6c31812dc94ad0?status=DELIVERED' \
   --header 'Content-Type: application/json' \
   --data-raw '{
    "action": "CHECKOUT",
    "body":{
            "mode": "DIGITAL"
        }
    
   }'
```

           Response Structure
           -----------
            {
                  "result": {
                  "billAmount": 100.0,
                  "createdAt": "2022-05-23T22:57:12 PM",
                  "customerId": "628bb676163d0e755eb46c66",
                  "mode": "DIGITAL",
                  "modifiedAt": "2022-05-23T23:13:12 PM",
                  "orderId": "628bc3f0fc6c31812dc94ad0",
                  "paymentStatus": "PAID",
                  "status": "DELIVERED"
                },
           "status": 200
           }
