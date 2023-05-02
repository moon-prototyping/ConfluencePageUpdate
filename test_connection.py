from atlassian import Confluence

confluence = Confluence(
    url=url,
    username=username,
    password=password)

space='~shmoon2'
title=''
page_id=244735450

#confluence.page_exists(space, title, type=None)

print(confluence.get_page_space(page_id))

print(confluence.get_all_pages_from_space(space, start=0, limit=1, status=None, expand=None, content_type='page'))