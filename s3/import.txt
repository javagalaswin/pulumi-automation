import pulumi
import pulumi_aws as aws

instance_vpc = aws.ec2.Vpc("instance-vpc",
    cidr_block="172.31.0.0/16",
    enable_dns_hostnames=True,
    enable_dns_support=True,
    instance_tenancy="default",
    opts=pulumi.ResourceOptions(protect=True))
public_1 = aws.ec2.Subnet("public-1",
    assign_ipv6_address_on_creation=False,
    cidr_block="172.31.16.0/20",
    enable_dns64=False,
    enable_resource_name_dns_a_record_on_launch=False,
    enable_resource_name_dns_aaaa_record_on_launch=False,
    ipv6_native=False,
    map_public_ip_on_launch=True,
    private_dns_hostname_type_on_launch="ip-name",
    vpc_id="vpc-0b8f3176",
    opts=pulumi.ResourceOptions(protect=True))
instance_sg = aws.ec2.SecurityGroup("instance-sg",
    description="default VPC security group",
    egress=[aws.ec2.SecurityGroupEgressArgs(
        cidr_blocks=["0.0.0.0/0"],
        from_port=0,
        protocol="-1",
        self=False,
        to_port=0,
    )],
    ingress=[aws.ec2.SecurityGroupIngressArgs(
        from_port=0,
        protocol="-1",
        self=True,
        to_port=0,
    )],
    name="default",
    revoke_rules_on_delete=False,
    vpc_id="vpc-0b8f3176",
    opts=pulumi.ResourceOptions(protect=True))
instance_volume = aws.ebs.Volume("instance-volume",
    availability_zone="us-east-1a",
    iops=100,
    size=8,
    snapshot_id="snap-0c0b30d420db08ab8",
    type="gp2",
    opts=pulumi.ResourceOptions(protect=True))
