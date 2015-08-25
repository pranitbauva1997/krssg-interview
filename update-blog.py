#!/usr/bin/python3
import os

def get_posts(page):
    """
        This method gets the posts already present
        in the webpage. It returns the id of the posts
        already present as array.
    """

    index = 0
    post_id = []
    while True:
        index = page.find('<div class="post"', index)
        if index < 0:
            break
        temp = page.find('id=', index) + 4
        post_id.append(int(page[temp:page.find('"', temp)]))
#        print(post_id)
        temp += 10
        index = temp + 50
#        print("post_id" + str(post_id))
    return post_id

def add_post(page, index, post_id, title, content):
    """
        This method will add the contents of the posts
        to the web page and then return the web page.
    """

    data = '<div class="post" id="' + str(post_id) + '">\n<div class="post-title">\n<div class="post-subject">\n<h2>' + title + '</h2>'
    data += '</div>\n</div>\n<div class="post-content">\n<p>' + content + '</p>\n</div></div>'
#    print(data)
    page = page[:index-1] + data + page[index-1:]
#   print("index pos : " + str(page.find("Intro")))
    page = page[:173] + '\n' + title + '<br>\n' + page[174:]
    return page

def get_post_details(id):
    """
        This method will get the details about the blog post
        by reading the file and return title, content, date, time
    """

    f = open('posts/' + str(id) + ".post", 'r')
    text = f.read().split('\n')
    f.close()
    print(text)
    title = text[0]
    content = text[1]
    date = text[2]
    time = text[3]
    return title[6:], content[8:], date[5:], time[5:]

def generate_web_page(page):
    """
        This will write the web page to the index.html file.
    """

    f = open('index.html', 'w')
    f.write(page)

# Reading the posts present.
posts_in_dir = os.listdir("posts/")
f = open("index.html", "r")
posts_in_dir.sort(reverse=True)
#print("posts_in_dir : " + str(posts_in_dir))
web_page = f.read()
f.close()
posts_in_blog = get_posts(web_page)
posts_in_blog.sort(reverse=True)
#print("posts_in_blog : " + str(posts_in_blog))

# Remove the ".post"
counter = 0
while counter < len(posts_in_dir):
	temp = posts_in_dir[counter]
#	print(temp)
	posts_in_dir[counter] = int(temp[:temp.find(".")])
	counter += 1
posts_to_be_added = []


# Getting new posts
for post in posts_in_dir:
    if post not in posts_in_blog:
        posts_to_be_added.append(post)


# Reading and generating content for new posts.
posts_to_be_added.sort()
for id in posts_to_be_added:
    title, content, date, time = get_post_details(id)
    web_page = add_post(web_page, web_page.find('<div id="section"') + 19, id, title, content)

generate_web_page(web_page)
print("Added the remaining posts. Check your file.")
