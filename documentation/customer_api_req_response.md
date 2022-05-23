1. ### To add new customer 
```
curl --location --request POST 'http://0.0.0.0:4331/rms/v1/customer/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "test1",
    "phoneNumber": "343543541"
}'
```

        Response Structure
        -------
        {
            "result": {
                   "createdAt": "2022-05-23T21:59:42 PM",
                   "customerId": "628bb676163d0e755eb46c66",
                   "firstName": "test1",
                   "phoneNumer": "343543541"
            },
            "status": 200
       }
2. ### To update phone number or name of a customer
```commandline
curl --location --request PATCH 'http://0.0.0.0:4331/rms/v1/customer/628bb676163d0e755eb46c66?name=Final&phoneNumber=2322356' \
--header 'Content-Type: application/json' \
```
        Response Structure
        -------
        {
            "result": {
                   "createdAt": "2022-05-23T21:59:42 PM",
                   "customerId": "628bb676163d0e755eb46c66",
                   "firstName": "Final",
                   "phoneNumer": "2322356"
            },
            "status": 200
       }




