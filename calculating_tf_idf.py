import pandas as pd
import re
import json
from collections import Counter
import math


#This code is used to calculate the tf idf scores for the words in each category.

# I upload my conservative and politics sample annotate files.
conservative = pd.read_csv('con_trump_200.csv')

politics = pd.read_csv('sample_donald_politics.csv')


conservative = conservative.drop(['Unnamed: 0'], axis = 1)


# I also wanted to test to merge for the two files

frames = [conservative, politics]
merged = pd.concat(frames)
#print(merged)

# Over two mentions is good for getting more than words!

def clean_ponctuation(string):
    remove = '()[],-.?!:;#&'
    trans = str.maketrans(remove, ' '*len(remove))
    return string.translate(trans)


# Now we have the numbers with merged, politics and conservative
def word_count(df):
    topics = ['lawsuit','vote count', 'pandemic related','pol opi', 'trump a', 'trump c']
    
    df['title'] =df['title'].apply(clean_ponctuation)
    
    word_by_topics = {}
    dict1  ={}
    for topic in topics:
        dict1[topic] = df[df[topic]=='y']
        words = []
        titles = dict1[topic]['title'].tolist()
        total = []
        for i in range(len(titles)):
            words = titles[i].split()
            for word in words:
                to_add = word.lower()
                total.append(to_add)
    
        is_word = []
        for word in total:
            if word.isalpha():
                is_word.append(word)
        
        topics_dict = dict(Counter(is_word))
        final = {}
        for key,value in topics_dict.items():
            if value >=2:
                final[key] = value
                
        word_by_topics[topic] = final
            
    json_out = json.dumps(word_by_topics,indent = 4)
    #print(json_out)
    return json_out

word_count(politics)


def add_words(file1,file2,file3,file4,file5,file6):
    list_of_lists = []
    in_file1 = open(file1,'r') 
    in_file2  = open(file2,'r') 
    in_file3  = open(file3,'r') 
    in_file4  = open(file4,'r') 
    in_file5  = open(file5,'r') 
    in_file6  = open(file6,'r') 
    list1= []
    list2= []
    list3= []
    list4= [] 
    list5= []
    list6= []
    for line in in_file1:
        words = line.split()
        for word in words:
            list1.append(word)
    list_of_lists.append(list1)
    for line in in_file2:
        words = line.split()
        for word in words:
            list2.append(word)
    list_of_lists.append(list2)
    for line in in_file3:
        words = line.split()
        for word in words:
            list3.append(word)
    list_of_lists.append(list3)
    for line in in_file4:
        words = line.split()
        for word in words:
            list4.append(word)
    list_of_lists.append(list4)
    for line in in_file5:
        words = line.split()
        for word in words:
            list5.append(word)
    list_of_lists.append(list5)
    for line in in_file6:
        words = line.split()
        for word in words:
            list2.append(word)
    list_of_lists.append(list6)
    
    return list_of_lists

massive_list = add_words('hot_con_trump18.json','hot_con_trump19.json','hot_con_trump20.json',
                         'hot_pol_trump18.json','hot_pol_trump19.json','hot_pol_trump20.json')    

def ComputeTF_IDF(data,term,d,list_of_lists):
    sum_d = 0
    for w in data[d]:
        sum_d += data[d][w]
    DF = data[d][term]/sum_d

    sum_occurences = 0
    total = 0
    for lists in list_of_lists:
        if term in lists:
            sum_occurences += 1
            
    IDF = (6/(sum_occurences+1))
    return DF * math.log(IDF)

def main():
    
    words_count_dict = json.loads(word_count(conservative))
    words_dic = {}
    tf_idf_dict = {}
    num_words = 10
    #int(words_count_dict)
    
    
    for topic in words_count_dict:
        
        tf_idf = {}
        for word in words_count_dict[topic]:
            tf_idf[word] = ComputeTF_IDF(words_count_dict,word, topic,massive_list)
        tf_idf_df = pd.DataFrame.from_dict(tf_idf, orient='index', columns=['TF-IDF'])
        tf_idf_df.sort_values(by=['TF-IDF'],ascending=False, inplace=True)
        tf_idf_list = []
        for i in range(num_words):
            tf_idf_list.append(tf_idf_df.iloc[i].name)
        
        words_dic[topic] = tf_idf_list
    out = json.dumps(words_dic)
    out = out.replace('{','{\n')
    out = out.replace('],','],\n')
    out = out.replace('}','\n}')
    
    print("conservative")       
    print(out)

if __name__ == '__main__':
    main()