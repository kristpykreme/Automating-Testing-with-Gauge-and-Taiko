# Test process to register user profile in ProfilePrint Hub
* Open ProfilePrint website

## Successfully register profile
* Key in name as "Test name 1"
* Key in display name as "Test display name 1"
* Key in email as "test_email1@gmail.com"
* Key in password as "550^QkTXnHK3"
* Key in confirm password as "550^QkTXnHK3"
* Key in country as "singapore"
* Key in country code as "+65" and number as "85554794"
* Agree to terms and conditions
* Register profile (success)

## Failure to register profile (invalid phone number)
* Key in name as "Test name"
* Key in display name as "Test display name"
* Key in email as "test_email@gmail.com"
* Key in password as "password1"
* Key in confirm password as "password2"
* Key in country as "singapore"
* Key in country code as "+65" and number as "12345678"
* Agree to terms and conditions
* Register profile (pop up)

## Failure to register profile (passwords do not match)
* Key in name as "Test name"
* Key in display name as "Test display name"
* Key in email as "test_email@gmail.com"
* Key in password as "password1"
* Key in confirm password as "password2"
* Key in country as "singapore"
* Key in country code as "+65" and number as "85554793"
* Agree to terms and conditions
* Register profile (pop up)

## Failure to register profile (password does not meet requirements)
* Key in name as "Test name"
* Key in display name as "Test display name"
* Key in email as "test_email@gmail.com"
* Key in password as "password"
* Key in confirm password as "password"
* Key in country as "singapore"
* Key in country code as "+65" and number as "85554793"
* Agree to terms and conditions
* Register profile (pop up)

## Failure to register profile (invalid email)
* Key in name as "Test name"
* Key in display name as "Test display name"
* Key in email as "test_email@.com"
* Key in password as "550^QkTXnHK3"
* Key in confirm password as "550^QkTXnHK3"
* Key in country as "singapore"
* Key in country code as "+65" and number as "85554793"
* Agree to terms and conditions
* Register profile (pop up)

## Failure to register profile (missing fields)
* Key in name as "Test name"
* Key in email as "test_email@gmail.com"
* Key in password as "550^QkTXnHK3"
* Key in confirm password as "550^QkTXnHK3"
* Key in country as "singapore"
* Key in country code as "+65" and number as "85554793"
* Agree to terms and conditions
* Register profile (pop up)


