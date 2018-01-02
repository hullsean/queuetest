
# pip install boto3 first (as root)
import boto3

# create your queue object
sqs = boto3.resource('sqs')

# open the queuetest.fifo queue
myq = sqs.get_queue_by_name(QueueName='queuetest.fifo')

# read contents of payload.txt file
with open('payload.txt', 'r') as myfile:
    data=myfile.read()

# send message to queuetest with payload.txt contents as payload
rsp = myq.send_message(
    MessageBody=data,
    MessageGroupId='messageGroup1'
)

# The response is NOT a resource, but gives you a message ID and MD5
print(rsp.get('MessageId'))
print(rsp.get('MD5OfMessageBody'))



