### Instructions for Uploading
![alt text](ConnectLambdaDynamoDBCloudFormation-designer.png)

#### Problems I ran into:

I was able to create a CloudFormation most services successfuly, except for the Connect service. It kept failing on deployment and I found documentation on Connect CloudFormation properties and attributes to be quite sparse. 

For this reason, I've included two CloudFormation templates. One fully working one, and one buggy one. You can find them in the root folder: 
```
ConnnectLambdaDynamoDBCloudFormation
```
and
```
LambdaDynamoDBCloudFormation
```
The second one will deploy everything you need to pipe information into the Connect Vanity Number Call Center: Lambada, DynamoDB, Roles, Permissions. You'll just have to set up the Call center itself independently. 

From the [CloudFormation service page](https://us-west-2.console.aws.amazon.com/cloudformation/home?region=us-west-2#/):
1. click Create Stack 
2. select Template is Ready and Upload Template File radios and click upload. Upload one of the above templates (found in the root folder)
3. click Next
4. Name the stack
5. Configure Options (don't really need to do anything)
6. Review, Acknowledge click Submit





