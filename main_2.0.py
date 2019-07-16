from collections import OrderedDict


# Enter HTML between the triple-quotes:
html = """

"""


class_data = OrderedDict({

    "p":"les-p",

    "h3":"les-h3",

    "hr":"les-hr",

    "a":"les-a",

    "att":"les-att",

    "iframe":"les-iframe",

    "img":"les-iframe",

    "body":"les-body",

    "ul":"les-p",

    "ol":"les-p",

    "vid-ti":"les-vid-ti",

    "pic-ti":"les-pic-ti"

})


html_list = list(html)
new_html_list = html_list
pos = 0


for char in html_list:
    if char == "<":
        # stops check if it finds it is a closing statement
        if html_list[pos+1] == "/":
            pass

        else:
            for element in class_data:
                # makes check word
                check_element_word_list = html_list[pos+1:pos+len(element)+1]
                check_element_word = ""
                for i in check_element_word_list:
                    check_element_word += i

                if check_element_word == element:

                    # makes sure it's not a false match by checking to make sure it's a 1 letter element if checking against 1 letter element
                    if len(element) == 1 and html_list[pos + 2] != ">":
                        continue

                    else:
                        for i in range(1, 400):
                            if html_list[pos + i] == ">":
                                insert_pos = pos + i
                                break

                            # this condition is met if there is no end bracket (within 400 char.s)
                            elif i >= 399:
                                insert_pos = pos
                                print("Could not complete conversion.  You are probably missing a closing '>'.")

                        html_list.insert(insert_pos, ' class="' + class_data[element] + '"')
                    break
    pos+=1


new_html_str = ""
new_html_str = new_html_str.join(new_html_list)
print(new_html_str)
