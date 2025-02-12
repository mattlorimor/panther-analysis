from panther import aws_cloudtrail_success

# API calls that are indicative of an EC2 SecurityGroup modification
EC2_SG_MODIFIED_EVENTS = {
    "AuthorizeSecurityGroupIngress",
    "AuthorizeSecurityGroupEgress",
    "RevokeSecurityGroupIngress",
    "RevokeSecurityGroupEgress",
    "CreateSecurityGroup",
    "DeleteSecurityGroup",
}


def rule(event):
    return aws_cloudtrail_success(event) and event.get("eventName") in EC2_SG_MODIFIED_EVENTS


def dedup(event):
    return event.get("recipientAccountId")
