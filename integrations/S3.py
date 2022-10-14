import boto3 as b3
import uuid


class S3:

    def __init__(self):
        self.session = b3.session.Session()
        self.s3_client = b3.client('s3')
        self.s3_resource = b3.resource('s3')

    def create_bucket(self, bucket_prefix: str):
        return self.s3_client.create_bucket(
            Bucket=self.__create_unique_bucket_name(bucket_prefix),
            CreateBucketConfiguration={'LocationConstraint': self.session.region_name}
        )

    def upload_file_to_bucket(self, file_name: str, bucket_name: str, key: str):
        self.s3_client.upload_file(
            Filename=file_name,
            Bucket=bucket_name,
            Key=key,
            ExtraArgs={'ACL': 'public-read'}
        )

    def download_file_from_bucket(
            self,
            bucket_name: str,
            file_name: str,
            location: str = '.'
    ):
        self.s3_resource.Object(bucket_name, file_name).download_file(f'{file_name}')

    def delete_file_from_bucket(self, bucket_name: str, file_name: str):
        self.s3_resource.Object(bucket_name, file_name).delete()

    @staticmethod
    def __create_unique_bucket_name(bucket_prefix: str) -> str:
        return ''.join([bucket_prefix, str(uuid.uuid4())])
