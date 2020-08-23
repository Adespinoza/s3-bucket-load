import boto3
from botocore.exceptions import NoCredentialsError

AWS_ACCESS_KEY_ID = '####################'
SECRET_AWS_SECRET_ACCESS_KEY_KEY = '########################################'
BUCKET_NAME = '' # Bucket name as string
BUCKET_FOLDER = '' # Name of bucket 
NUM_OF_FILES = # Number of files
FILE_LOCATION = '' # Location of file on computer
FILE_TYPE = '' # File type (.json, .png, .txt, etc.)

def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=SECRET_AWS_SECRET_ACCESS_KEY_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print('Successfully uploaded to Amazon S3 bucket - %s' % (s3_file))
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

for x in range(1, NUM_OF_FILES):
	uploaded = upload_to_aws(FILE_LOCATION, BUCKET_NAME, '%s/%s.%s' % (BUCKET_FOLDER, x, FILE_TYPE))