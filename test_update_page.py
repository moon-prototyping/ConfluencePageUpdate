from atlassian import Confluence

confluence = Confluence(
    url=url,
    username=username,
    password=password)



space='~shmoon2'
title='apitest5'
page_id=253388961
parent_id=253388724

body='''
|| name || validAfterTime || validBeforeTime || keyAlgorithm || keyOrigin || keyType ||
| projects/prj-cc-sandbox-devops-0010/serviceAccounts/sa-mkt-sandbox-moon@prj-cc-sandbox-devops-0010.iam.gserviceaccount.com/keys/4fc55fcde44668afe3f5daa2967f8242ca356133 | 2023-03-23T11:26:37Z | 2023-04-09T11:26:37Z | KEY_ALG_RSA_2048 | GOOGLE_PROVIDED | SYSTEM_MANAGED |
'''

body='''
| Column 1 | Column 2 | Column 3 |
| --- | --- | --- |
| Merged cell | | |
| Content 1 | Content 2 | Content 3 |
'''

body='''
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Row 1, cell 1 | Row 1, cell 2 | Row 1, cell 3 |
| Row 2, cell 1 | Row 2, cell 2 | Row 2, cell 3 |
| Row 3, cell 1 | Row 3, cell 2 | Row 3, cell 3 |
'''

body='''
| Forwarding Rule Name | IP Address:Port | Cert Name | Creation Time | Expiration Time | DNS HostNames(SSL) |
|
| push-recv-dev-lb-forwarding-rule | 35.201.93.129:443-443 | wemake-2023 | 2023-01-02T01:47:02.929-08:00 | 2023-01-02T01:47:02.929-08:00 | ['*.wemakeprice.com', 'wemakeprice.com'] |
| push-recv-prd-lb-forwarding-rule | 34.96.126.248:443-443 | wemake-2023 | 2023-01-02T01:47:02.929-08:00 | 2023-01-02T01:47:02.929-08:00 | ['*.wemakeprice.com', 'wemakeprice.com'] |
| push-recv-stg-lb-forwarding-rule | 35.241.41.120:443-443 | wemake-2023 | 2023-01-02T01:47:02.929-08:00 | 2023-01-02T01:47:02.929-08:00 | ['*.wemakeprice.com', 'wemakeprice.com'] |
'''

body='''
new_body
'''

status = confluence.update_page(
    parent_id=parent_id,
    page_id=page_id,
    title=title,
    body=body,
    representation='wiki'
)

#print(status)

