
import json
import pandas as pd
import re
import random



def get_post_titles(inp,out):
    """
    (this takes as input a file with reddit posts), and returns a 
    """
    file_in = open(inp,'r')
    file_out = open(out,'w')
    for line in file_in:
        try:
            data = json.loads(line)
            file_out.write(data['data']['title'] + '\n')
        except Exception as e:
            continue
       
def write_file_trump(file_in,file_out):
    """
    (file in) --> file out This takes a file of reddit post titles.
    this will return a normal title file.
    """
    file_i  = open(file_in,'r')
    file_o = open(file_out,'w')
    
    for line in file_i:
        if re.search("[^0-9a-zA-Z]Trump[^0-9a-zA-Z]", line) or re.search("^Trump[^0-9a-zA-Z]", line):
            file_o.write(line)
            #append to a list//
    file_i.close()
    file_o.close()

    
def chose_random_line(file_in, num_post):
    """
    Takes a file as input a file and a number of posts and returns a list of posts.
    
    """
    list_of_post = []
    lines = open(file_in).read().splitlines()
    while(len(list_of_post) < num_post):
        myline = lines.pop(random.randint(0,len(lines)-1))
        list_of_post.append(myline)
    return list_of_post


 def main():
    
    list_1= chose_random_line(in_file1,67)
    list_2= chose_random_line(in_file2,66)
    list_3 = chose_random_line(in_file3,66)
    big_list = [list_1, list_2,list_3]
    flat_list = []
    for sublist in big_list:
        for item in sublist:
            flat_list.append(item)
    
    list_of_titles = flat_list
     posts = {'titles': list_of_titles}
    
    df = pd.DataFrame(posts,columns = ['titles'])
    
    df.to_csv('sample_donald.csv', index = False, encoding = 'utf-8')
    
    

if __name__ == "__main__":
    main()
