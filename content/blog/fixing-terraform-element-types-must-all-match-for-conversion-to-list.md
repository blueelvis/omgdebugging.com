+++
title = "Fixing Terraform - element types must all match for conversion to list."
description = ""
date = 2023-12-16T18:31:11
updated = 2023-12-16T18:39:49
draft = false
slug = "fixing-terraform-element-types-must-all-match-for-conversion-to-list"
aliases = ['2023/12/16/fixing-terraform-element-types-must-all-match-for-conversion-to-list/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = []
+++


This was a really weird error coming from Terraform while doing a terraform plan
. Good thing is this allows me to write a blog post because pretty sure I am
going to forget about this...

The Terraform code which was causing this issue -

module "access_log_bucket" {
  source  = "cloudposse/lb-s3-bucket/aws"
  version = "~> 0.16.4"

  context = module.access_log_bucket_label.context
  tags    = module.access_log_bucket_label.tags

  versioning_enabled = true
  lifecycle_configuration_rules = [
    {
      id                                     = "abort-incomplete-multipart-upload-after-7days"
      enabled                                = true
      abort_incomplete_multipart_upload_days = 7
      filter_and = null
      expiration = null
      transition = []
      noncurrent_version_transition = []
      noncurrent_version_expiration = null
    },
    {
      id                                     = "delete-non-current-versions-after-30-days"
      enabled                                = true
      abort_incomplete_multipart_upload_days = null
      filter_and = null
      expiration = null
      transition = []
      noncurrent_version_transition = []
      noncurrent_version_expiration = {
        days = 30
      }
    }
  ]
}


The error I was seeing is as below -

Error: Invalid value for input variable

  on dev-network\access-log.tf line 17, in module "access_log_bucket":
  17:   lifecycle_configuration_rules = [
  18:     {
  19:       id                                     = "abort-incomplete-multipart-upload-after-7days"
  20:       enabled                                = true
  21:       abort_incomplete_multipart_upload_days = 7
  22:       filter_and = null
  23:       expiration = null
  24:       transition = []
  25:       noncurrent_version_transition = []
  26:       noncurrent_version_expiration = null
  27:     },
  28:     {
  29:       id                                     = "delete-non-current-versions-after-30-days"
  30:       enabled                                = true
  31:       abort_incomplete_multipart_upload_days = null
  32:       filter_and = null
  33:       expiration = null
  34:       transition = []
  35:       noncurrent_version_transition = []
  36:       noncurrent_version_expiration = {
  37:         days = 30
  38:       }
  39:     }
  40:   ]

The given value is not suitable for
module.dev-network.module.access_log_bucket.var.lifecycle_configuration_rules
declared at
.terraform\modules\dev-network.access_log_bucket\variables.tf:47,1-41:
element types must all match for conversion to list.


If we see the variable declaration for this module
[https://github.com/cloudposse/terraform-aws-lb-s3-bucket/blob/502f2f75fb91730cbf986c55e9560ad4163e5c12/variables.tf#L47C1-L69C2]
, it has the following type -

variable "lifecycle_configuration_rules" {
  type = list(object({
    enabled = bool
    id      = string

    abort_incomplete_multipart_upload_days = number

    # `filter_and` is the `and` configuration block inside the `filter` configuration.
    # This is the only place you should specify a prefix.
    filter_and = any
    expiration = any
    transition = list(any)

    noncurrent_version_expiration = any
    noncurrent_version_transition = list(any)
  }))
  default     = []
  description = <<-EOT
    A list of S3 bucket v2 lifecycle rules, as specified in [terraform-aws-s3-bucket](https://github.com/cloudposse/terraform-aws-s3-bucket)"
    These rules are not affected by the deprecated `lifecycle_rule_enabled` flag.
    **NOTE:** Unless you also set `lifecycle_rule_enabled = false` you will also get the default deprecated rules set on your bucket.
    EOT
}


Turns out that the problem is with the noncurrent_version_expiration property.
As you can see, I have 2 rules and in rule, I have set this property but in the
other, I have kept it as null.

This is exactly what Terraform is complaining about (really weird error!). As
soon as I changed the noncurrent_version_expiration to {} instead of null, 
terraform plan worked.

Working piece -

module "access_log_bucket" {
  source  = "cloudposse/lb-s3-bucket/aws"
  version = "~> 0.16.4"

  context = module.access_log_bucket_label.context
  tags    = module.access_log_bucket_label.tags

  versioning_enabled = true
  lifecycle_configuration_rules = [
    {
      id                                     = "abort-incomplete-multipart-upload-after-7days"
      enabled                                = true
      abort_incomplete_multipart_upload_days = 7
      filter_and = null
      expiration = null
      transition = []
      noncurrent_version_transition = []
      noncurrent_version_expiration = {}
    },
    {
      id                                     = "delete-non-current-versions-after-30-days"
      enabled                                = true
      abort_incomplete_multipart_upload_days = null
      filter_and = null
      expiration = null
      transition = []
      noncurrent_version_transition = []
      noncurrent_version_expiration = {
        days = 30
      }
    }
  ]
}