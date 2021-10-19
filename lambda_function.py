import boto3
from find_vanity_numbers import find_words
from validate_phone_number import validate_phone_number
from save_vanity_numbers import save_vanity_numbers

def lambda_handler(event, context):
  # Get the service resource.
  ddb = boto3.resource('dynamodb')
  # Instantiate vanity_numbers table resource
  table = ddb.Table('vanity_numbers')
  # Get customer phone_number from AWS Connect contact flow event
  phone_number = event["Details"]["ContactData"]["CustomerEndpoint"]["Address"]
  print(phone_number)

  number_validation = validate_phone_number(phone_number)

  if number_validation["valid"] is False:
    return "Error: Invalid Phone Number"

  validated_phone_number = number_validation["full_number"]
  # Check to see if the vanity numbers for the phone
  # number have already been saved.
  response = table.get_item(
      Key={
          "phone_number": validated_phone_number
      }
  )

  if "Item" in response:
    item = response["Item"]
    print(item)
    return item
  else:
    print("RESPONSE: ", response)
    vanity_numbers = find_words(validated_phone_number)
    print("VANITY NUMBERS: ", vanity_numbers)
    response = save_vanity_numbers(validated_phone_number, vanity_numbers)
    print(f"SAVE VANITY NUMBERS RESPONSE {response}")
    return response
