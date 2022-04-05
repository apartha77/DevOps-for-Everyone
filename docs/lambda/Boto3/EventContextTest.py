# Check the contents of Events and Context - json.dumps
import json
# Pre handler
print('Loading function')

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    print("Printing the context details:")
    print(context)
    print("/n Now will print event details")
    print(event)
    print("Will explore json.dumps")
    print(json.dumps(event, indent=2))
    print("Now print the event items one by one ")
    print("value1 = " + event['key1'])
    print("value2 = " + event['key2'])
    print("value3 = " + event['key3'])
    print("value4 = " + event['key4'])
    return event['key1']  # Echo back the first key value
    #raise Exception('Something went wrong')

    
# Test the function events to send
#{
#  "key1": "Hello World",
#  "key2": "value2",
#  "key3": "value3",
#  "key4": "The Final Value-4"
#}
