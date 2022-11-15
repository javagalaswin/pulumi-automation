#Stack Validation Policies

from pulumi_policy import (
    EnforcementLevel,
    PolicyPack,
    ReportViolation,
    StackValidationArgs,
    StackValidationPolicy,
)

#variables
required_region = "us-east-2"
ami = "ami-09d3b3274b6c5d4a"
instanceType = "t2.micro"
associatePublicIpAddress = True

#functions

def s3_region_check_validator(stack: StackValidationArgs, report_violation: ReportViolation):
    for resource in stack.resources:
        if resource.resource_type == "aws:s3/bucket:Bucket": 
            if "region" in resource.props and resource.props["region"] != required_region:
                report_violation(f"Bucket, {resource.name}, must be in region {required_region}")

def ec2_ami_check_validator(stack: StackValidationArgs, report_violation: ReportViolation):
    for resource in stack.resources:
        if resource.resource_type == "aws:ec2/instance:Instance":
            if "ami" in resource.props and resource.props["ami"] != ami:
                report_violation(f"Instance, {resource.name}, must be with ami {ami}")
            
            
def ec2_instanceType_check_validator(stack: StackValidationArgs, report_violation: ReportViolation):
    for resource in stack.resources:
        if resource.resource_type == "aws:ec2/instance:Instance":
            if "instanceType" in resource.props and resource.props["instanceType"] != instanceType:
                report_violation(f"Instance, {resource.name}, must be with instanceType {instanceType}")


def ec2_associatePublicIpAddress_check_validator(stack: StackValidationArgs, report_violation: ReportViolation):
    for resource in stack.resources:
        if resource.resource_type == "aws:ec2/instance:Instance":
            if "associatePublicIpAddress" in resource.props and resource.props["associatePublicIpAddress"] != associatePublicIpAddress:
                report_violation(f"Instance, {resource.name}, must be with associatePublicIpAddress {True}")

#policies
                
s3_region_check = StackValidationPolicy(
    name="s3-region-check",
    description= "Checks the region the bucket was deployed in",
    validate=s3_region_check_validator
)

ec2_ami_check = StackValidationPolicy(
    name="ec2-ami-check-validator",
    description= "Checking EC2 Insatances ami",
    validate=ec2_ami_check_validator
)

ec2_instanceType_check = StackValidationPolicy(
    name="ec2-instanceType-check-validator",
    description= "Checking EC2 Insatances type",
    validate=ec2_instanceType_check_validator
)

ec2_associatePublicIpAddress_check = StackValidationPolicy(
    name="ec2-associatePublicIpAddress-check-validator",
    description= "Checking EC2 Insatances associatePublicIpAddress",
    validate=ec2_associatePublicIpAddress_check_validator
)

#poliy-pack

PolicyPack(
    name="Stack_Policy_Pack",
    enforcement_level=EnforcementLevel.ADVISORY,
    policies=[
        s3_region_check,
        ec2_ami_check,
        ec2_instanceType_check,
        ec2_associatePublicIpAddress_check
    ],
)
