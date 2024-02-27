+++
title = "Terraform Cloudformation Using Intrinsic & Other Functions"
description = ""
date = 2023-12-19T22:53:56
updated = 2023-12-19T22:55:00
draft = false
slug = "terraform-cloudformation-using-intrinsic-other-functions"
aliases = ['2023/12/19/terraform-cloudformation-using-intrinsic-other-functions/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = []
+++


resource "aws_cloudformation_stack_set" "backup_vault" {
  name                    = "AWS-Backup-Vault"
  description             = "Deploys the AWS Backup Vaults across accounts and regions."
  permission_model = "SERVICE_MANAGED"

  auto_deployment {
    enabled = true
    retain_stacks_on_account_removal = false
  }
  capabilities = ["CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]

  lifecycle {
    ignore_changes = [
      administration_role_arn
    ]
  }

  template_body = jsonencode({
    Resources = {
      BackupVault = {
        Type = "AWS::Backup::BackupVault"
        Properties = {
          BackupVaultName = local.backup_vault_name
          Notifications = {
            BackupVaultEvents = [
                "BACKUP_JOB_STARTED",
                "BACKUP_JOB_COMPLETED",
                "COPY_JOB_STARTED",
                "COPY_JOB_SUCCESSFUL",
                "COPY_JOB_FAILED",
                "RESTORE_JOB_STARTED",
                "RESTORE_JOB_COMPLETED",
                "RECOVERY_POINT_MODIFIED",
                "S3_BACKUP_OBJECT_FAILED",
                "S3_RESTORE_OBJECT_FAILED"
            ]
            SNSTopicArn = { "Fn::GetAtt" = ["EmailNotificationTopic","TopicArn"]}
          }
        }
      }
      EmailNotificationTopic = {
        Type = "AWS::SNS::Topic"
        Properties = {
            TopicName = "aws-backup-vault-notifier"
            DisplayName = "AWS Backup Notification Topic"
        }
      }
      EmailNotificationTopicPolicy = {
          Type = "AWS::SNS::TopicPolicy"
          Properties = {
              Topics = [
                  { Ref = "EmailNotificationTopic" }
              ]
              PolicyDocument = {
                  Statement = [{
                    Sid = "AWSBackupNotificationSNSPolicy"
                      Action = [
                          "sns:Publish"
                      ]
                      Effect = "Allow"
                      Resource = { Ref = "EmailNotificationTopic" }
                      Principal = {
                          Service = [
                              "backup.amazonaws.com"
                          ]
                      }
                  }]
              }
          }
      }
      EmailNotification = {
        Type = "AWS::SNS::Subscription"
        Properties = {
            Endpoint = "aaa@aaa.com"
            Protocol = "email"
            TopicArn = { "Fn::GetAtt" = ["EmailNotificationTopic","TopicArn"]}
        }
      }
    
  }
})
}