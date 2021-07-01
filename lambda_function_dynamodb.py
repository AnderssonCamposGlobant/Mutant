import boto3
import json

def lambda_handler(event, context):
  client = boto3.resource('dynamodb')
  table=client.Table('mutants')

  print(event)
  jsonStr = json.dumps(event)

  input={'guid':jsonStr, 'dna': jsonStr}
  
  dataresult = table.put_item(Item=input)
  
  app_response = {}
  app_response['message'] = 'Dato Ingresado Correctamente en DynamoDB' 
    
  response_object={}
  response_object['headers'] = {}
  response_object['headers']['Content-Type'] = 'application/json'
  response_object['statusCode']=200

  response_object['body']=json.dumps(app_response)
  
  return response_object