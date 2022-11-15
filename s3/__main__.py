"""An AWS Python Pulumi program"""

import pulumi
import pulumi_aws as aws
from pulumi import ResourceOptions
import import_resource

# Importing existing resource
instance_1 = aws.ec2.Instance("Instance-1",
                              ami="ami-09d3b3274b6c5d4aa",
                              instance_type="t2.micro",
                              tags={
                                  "Name": "Instance-1",
                              },
                              opts=ResourceOptions(import_='i-0a8a23d36b28d221d')
                              )

# Creating new resource
bucket = aws.s3.Bucket("bucket-1",
                       acl="private",
                       tags={
                           "Environment": "Dev",
                           "Name": "Pulumi-poc-bucket",
                       })


# Exporting resource outputs
pulumi.export('bucket_name', bucket.id)
pulumi.export('instance_id', instance_1.id)
pulumi.export('instance_type', instance_1.instance_type)
