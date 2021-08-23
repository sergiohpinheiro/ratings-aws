import boto3
import pandas as pd

#cria cliente para interagir com o S3

s3_client= boto3.client('s3')
s3_client.download_file("bucket-digao-mydog",
                        "data/data.csv",
                        "/home/alunoigti/Loterias/IGTI/Data/data.csv")

df = pd.read_csv('/home/alunoigti/Loterias/IGTI/Data/data.csv',sep=",")
print(df

s3_client.upload_file("Data/banco_de_podcast.csv",
                    "bucket-digao-mydog",
                    "data/banco_de_podcast.csv")