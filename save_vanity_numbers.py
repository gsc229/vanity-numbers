import boto3

def save_vanity_numbers(phone_number, vanity_numbers_list, dynamodb=None):
  if not dynamodb:
    dynamodb = boto3.resource('dynamodb')

  table = dynamodb.Table('vanity_numbers')

  response = table.put_item(
    Item={
      'phone_number': phone_number,
      'vanity_numbers': vanity_numbers_list
    },
  )
  return response
