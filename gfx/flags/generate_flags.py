# Generates a flag for every title... well, copies a template for one.
import os, re, shutil

landed_titles_filename = "../../common/landed_titles/autogenerated_landed_titles.txt"
#landed_titles_filename = "../../common/landed_titles/autogenerated_mercenary_titles.txt"
flag_template_filename = "c_template.tga"

# Given a line, split it into component "words"
def split_line(line):
    line_split_by_space = line.split()
    # Brackets and equals should have their own words
    all_words = []
    for word in line_split_by_space:
        # Assumptions:
        # In a word, if there's a =, it will come before {
        # If there's a {, it will come before }
        remaining_string = word
        equals_index = remaining_string.find("=")
        if equals_index >= 0:
            all_words.append(remaining_string[:equals_index])
            remaining_string = remaining_string[equals_index:]
        lbr_index = remaining_string.find("{")
        if lbr_index >= 0:
            all_words.append(remaining_string[:lbr_index])
            remaining_string = remaining_string[lbr_index:]
        rbr_index = remaining_string.find("}")
        if rbr_index >= 0:
            all_words.append(remaining_string[:rbr_index])
            remaining_string = remaining_string[rbr_index:]
        all_words.append(remaining_string)
    return all_words

# Given a string, determine if it's a title
def is_nonbarony_title(word):
    return re.match('[ekdc]_', word)

# First, read all titles from landed_titles
landed_titles_file = open(landed_titles_filename)
landed_titles_lines = landed_titles_file.readlines()
landed_titles_file.close()

all_titles = []
for line in landed_titles_lines:
    line_words = split_line(line)
    if len(line_words) > 0:
        potential_title = line_words[0]
        if is_nonbarony_title(potential_title):
            # print("Found title " + potential_title)
            new_filename = potential_title + ".tga"
            if new_filename not in os.listdir("."):
                shutil.copyfile(flag_template_filename, new_filename)
            