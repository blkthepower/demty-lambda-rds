import sys
import logging
import pymysql
import json
import os
import boto3
from botocore.exceptions import ClientError

DB_NAME = os.environ["DB_NAME"]
DB_HOST = os.environ["DB_HOST"]
DB_USER = os.environ["DB_USER"]
DB_PASS = os.environ["DB_PASS"]
DB_TABLE = os.environ["DB_TABLE"]

try:
    conn = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        passwd=DB_PASS,
        db=DB_NAME,
        connect_timeout=10
    )
except pymysql.MySQLError as e:
    raise e

def lambda_handler(event, context):
    """AWS Lambda handler function."""
    try:
        with conn.cursor() as cursor:
            query = f"SELECT * FROM {DB_TABLE}"
            cursor.execute(query)
            result = cursor.fetchall()

        result_json = [dict(zip([column[0] for column in cursor.description], row)) for row in result]

        return {"statusCode": 200, "body": json.dumps(result_json)}
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
