import boto3
import time 

def upload_to_s3(csv_file_path):
    # Initialize the S3 client
    bucket_name = "Enter here bucket name"
    s3 = boto3.client('s3',
                    aws_access_key_id= "Enter AWS access key",
                    aws_secret_access_key="Enter AWS secret key"
                    )
    object_name = f"{str(time.time()).split('.')[0]}.csv"
    try:
        s3.upload_fileobj(csv_file_path, bucket_name, object_name)
        s3_url =  f"https://{bucket_name}.s3.ap-south-1.amazonaws.com/{object_name}"
        
        return s3_url
    except Exception as e:
        return str(e)
