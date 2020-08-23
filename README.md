# s3-bucket-load
Random script to add the same file to an S3 bucket any number of times.

You'll need to change the following with the respective variables:

```python
AWS_ACCESS_KEY_ID = '####################'
SECRET_AWS_SECRET_ACCESS_KEY_KEY = '########################################'
BUCKET_NAME = '' # Bucket name as string
BUCKET_FOLDER = '' # Name of bucket 
NUM_OF_FILES = # Number of files
FILE_LOCATION = '' # Location of file on computer
FILE_TYPE = '' # File type (.json, .png, .txt, etc.)
```