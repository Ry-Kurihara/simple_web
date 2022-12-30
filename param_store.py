import boto3
# debug用に.envファイルを使用する場合。.envファイルをcommitしないように注意
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass 

REGION = 'ap-northeast-1'

def get_parameters(param_name, is_secure=False):
    ssm = boto3.client('ssm', region_name=REGION)
    response = ssm.get_parameters(
        Names=[
            param_name
        ],
        WithDecryption=is_secure     
    )
    return response['Parameters'][0]['Value']