import boto3
import botocore
import json
import config
import res.utils as utils
import res.glob  as glob

# =======================================================================================================================
#
#  Supported services   : RDS, DynamoDB
#  Unsupported services : ElastiCache, Neptune, Amazon Redshift
#
# =======================================================================================================================

#  ------------------------------------------------------------------------
#
#    RDS 
#
#  ------------------------------------------------------------------------

def get_rds_inventory(oId):
    """
        Returns RDS inventory

        :param ownerId: ownerId (AWS account)
        :type ownerId: string
        :param region_name: region name
        :type region_name: string

        :return: RDS inventory
        :rtype: json

        ..note:: http://boto3.readthedocs.io/en/latest/reference/services/rds.html
                 if the region is not supported, an exception is raised (EndpointConnectionError 
                 or AccessDeniedException)
    """
    return glob.get_inventory(
        ownerId = oId,
        aws_service = "rds", 
        aws_region = "all", 
        function_name = "describe_db_instances", 
        key_get = "DBInstances"
    )


#  ------------------------------------------------------------------------
#
#    DynamoDB 
#
#  ------------------------------------------------------------------------

def get_dynamodb_inventory(oId):
    """
        Returns dynamoDB inventory

        :param ownerId: ownerId (AWS account)
        :type ownerId: string
        :param region_name: region name
        :type region_name: string

        :return: dynamoDB inventory
        :rtype: json

        ..note:: http://boto3.readthedocs.io/en/latest/reference/services/dynamodb.html
                 if the region is not supported, an exception is raised (EndpointConnectionError 
                 or AccessDeniedException)
    """
    return glob.get_inventory(
        ownerId = oId,
        aws_service = "dynamodb", 
        aws_region = "all", 
        function_name = "list_tables", 
        key_get = "TableNames",
        detail_function = "describe_table", 
        join_key = "TableName", 
        detail_join_key = "TableName", 
        detail_get_key = "Table"
    )


#  ------------------------------------------------------------------------
#
#    Neptune 
#
#  ------------------------------------------------------------------------

def get_neptune_inventory(oId):
    """
        Returns neptune inventory

        :param ownerId: ownerId (AWS account)
        :type ownerId: string
        :param region_name: region name
        :type region_name: string

        :return: neptune inventory
        :rtype: json

        ..note:: http://boto3.readthedocs.io/en/latest/reference/services/neptune.html

    """
    return glob.get_inventory(
        ownerId = oId,
        aws_service = "neptune", 
        aws_region = "all", 
        function_name = "describe_db_instances", 
        key_get = "DBInstances"
    )

#
# Hey, doc: we're in a module!
#
if (__name__ == '__main__'):
    print('Module => Do not execute')