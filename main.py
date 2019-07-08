# Enter HTML between the triple-quotes:

html = """

"""

# maybe add ability to check full element rather than first letter for more thorough use

def p_check(text, pos):
    if text[pos+1] == "p":
        return True

def h3_check(text, pos):
    if text[pos+1] == "h":
        if text[pos+2] == "3":
            return True

def hr_check(text, pos):
    if text[pos+1] == "h":
        return True

def a_check(text, pos):
    if text[pos + 1] == "a":
        # checks a against att:
        if text[pos+2] != "t":
            return True

# assumes text has been checked for a
def att_check(text, pos):
    if text[pos + 1] == "a":
            return True

def iframe_check(text, pos):
    if text[pos + 1] == "i":
        return True

def body_check(text, pos):
    if text[pos+1] == "b":
        return True



def vid_ti_check(text, pos):
    if text[pos+1] == "v":
        return True

def pic_ti_check(text, pos):
    if text[pos+1] == "p":
        if text[pos + 2] == "i":
            return True





def insert_class(element,list,pos):
    list.insert(pos+len(element)+1,' class="les-'+element+'"')


html_list = list(html)
new_html_list = html_list
counter = 0
for char in html_list:
    if char == "<":
        if p_check(html_list, counter):
            insert_class("p",new_html_list,counter)
        elif h3_check(html_list, counter):
            insert_class("h3",new_html_list,counter)
        # hr check only works if html has already been checked for h3
        elif hr_check(html_list, counter):
            insert_class("hr",new_html_list,counter)
        elif a_check(html_list, counter):
            insert_class("a",new_html_list,counter)
        # att check only works if html has already been checked for a
        elif att_check(html_list, counter):
            insert_class("att",new_html_list,counter)
        elif iframe_check(html_list, counter):
            insert_class("iframe",new_html_list,counter)
        elif body_check(html_list, counter):
            insert_class("body",new_html_list,counter)
        elif vid_ti_check_check(html_list, counter):
            insert_class("vid-ti",new_html_list,counter)
        elif pic_ti_check_check(html_list, counter):
            insert_class("pic-ti",new_html_list,counter)

    counter +=1


new_html_str = ""
new_html_str = new_html_str.join(new_html_list)
print(new_html_str)
