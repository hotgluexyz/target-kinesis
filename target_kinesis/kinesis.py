import boto3
import json

def deliver(config, record):
  stream_name = config.get("stream_name")
  partition_key = config.get("partition_key", "id")
  aws_access_key_id = config.get("aws_access_key_id")
  aws_secret_access_key = config.get("aws_secret_access_key")
  region_name = config.get("region_name")

  client = boto3.client(
    'kinesis',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
  )

  response = client.put_record(
    StreamName=stream_name,
    Data=json.dumps(record).encode(),
    PartitionKey=record[partition_key]
  )
