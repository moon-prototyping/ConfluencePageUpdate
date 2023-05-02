from atlassian import Confluence

confluence = Confluence(
    url=url,
    username=username,
    password=password)
space='~shmoon2'
title='apitest5'
page_id=244735450
parent_id=253388724
body='''
||Key||Name||Updated||
|halo|koniziwa|hi|
'''

status = confluence.create_page(space=space, parent_id=parent_id, title=title, body=body, representation='wiki')

#print(status)