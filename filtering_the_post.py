


import json
import pandas as pd
import re
import random

#pd.read_csv('trump_pol_200.csv', error_bad_lines = False)

def get_post_titles(inp,out):

    file_in = open(inp,'r')
    file_out = open(out,'w')
    for line in file_in:
        try:
            data = json.loads(line)
            file_out.write(data['data']['title'] + '\n')
        except Exception as e:
            continue
    
#get_post_titles("../data/20201119_hottest_politics.json", "../data/20201119_hottest_pol_titles.json")

#file = open("../data/20201118_hottest_politics_titles.json",'r')
def write_file_trump(file_in,file_out):
    
    file  = open(file_in,'r')
    file_o = open(file_out,'w')
    
    for line in file:
        if re.search("[^0-9a-zA-Z]Trump[^0-9a-zA-Z]", line) or re.search("^Trump[^0-9a-zA-Z]", line):
            file_o.write(line)
    file.close()
    file_o.close()

#write_file_trump("../data/20201119_hottest_pol_titles.json",'../data/trump_politics_20201119.json')
#get_post_titles("../data/20201118_hottest_politics.json","../data/20201118_hottest_politics_titles.json")


#Now we need to look at the merge betweem all the files.
    
def chose_random_line(file_in, num_post):
    list_of_post = []
    lines = open(file_in).read().splitlines()
    while(len(list_of_post) < num_post):
        myline = lines.pop(random.randint(0,len(lines)-1))
        list_of_post.append(myline)
    return list_of_post

    
def choose_lines(in_file1,in_file2,in_file3):#, out_file):
    list_1= chose_random_line(in_file1,67)
    list_2= chose_random_line(in_file2,67)
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
    
    

    

choose_lines("../data/trump_files/trump_politics_20201118.json","../data/trump_files/trump_politics_20201119.json","../data/trump_files/trump_politics_20201120.json")#"../data/trump_pol_200.csv")
    
    
