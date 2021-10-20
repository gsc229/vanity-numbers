import boto3
from vanitynumbers import (
  validate_phone_number,
  save_vanity_numbers,
  get_response_message,
  find_words
)
from vanitynumbers.data import lambda_test_events

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
    return { "ResponseMessage": "Sorry, we can process your request at this time." }

  validated_phone_number = number_validation["full_number"]
  # Check to see if the vanity numbers for the phone
  # number have already been saved.
  response = table.get_item(
      Key={
          "phone_number": validated_phone_number
      }
  )
  print("GET RESPONSE: ", response)

  if "Item" in response:
    item = response["Item"]
    print(item)
    return { "ResponseMessage": get_response_message(item["vanity_numbers"]) }

  vanity_numbers = find_words(validated_phone_number)
  print("VANITY NUMBERS: ", vanity_numbers)

  response = save_vanity_numbers(validated_phone_number, vanity_numbers)
  print(f"SAVE RESPONSE {response}")

  if response["HTTPStatusCode"] < 200 or response["HTTPStatusCode"] > 299:
    return { "ResponseMessage": "Sorry, we can process your request at this time." }

  return { "ResponseMessage": get_response_message(vanity_numbers) }

lambda_handler(lambda_test_events.test_1, None)
