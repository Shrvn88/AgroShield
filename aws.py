import boto3

def send_aws(image_file_path):
    file_name = image_file_path[-23:]
    
# Set your AWS credentials and region
    

# Initialize an S3 client
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)

# Set the bucket name and image file path
    bucket_name = 'agroshield-aws'
    content_type = 'image/jpeg'

# Upload the image to S3
    try:
        s3.upload_file(image_file_path, bucket_name, file_name, ExtraArgs={'ContentType': content_type,'ContentDisposition': 'inline'})
        print(f"Image uploaded to {bucket_name}/{file_name}")
    except Exception as e:
        print(f"Error uploading image: {e}")

