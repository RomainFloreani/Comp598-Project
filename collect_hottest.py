import argparse
import json
import requests
import time
import datetime
import argparse
import pandas as pd

def scrape_reddit(num_posts,subreddit,before = 'null', after = 'null'):
    
    data = requests.get(f'http://api.reddit.com{subreddit}/hot?limit={num_posts}&before={before}&after={after}', 
                        headers={'User-Agent':'windows: requests (by /u/rflore)'})
    return data.json()['data']
    

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-o','--output_file', help = "output file", required = True)
    parser.add_argument('subreddit')
    args = parser.parse_args()
    
    out_file = open(f'../data/{args.output_file}', 'w')
    content = scrape_reddit(100, "/r/politics")
    list_of_posts = []
    while (len(list_of_posts) < 1000):
        post = content['children']
        for i in range(0,100):
            try:
                list_of_posts.append(json.dumps(post[i]))
            except Exception as e:
                continue
        after = content['after']
        content  = scrape_reddit(100,"/r/politics" ,after = after)
        
        
    for i in list_of_posts:
        out_file.write(str(i)+ '\n')
        
    out_file.close()

    
    
if __name__ == '__main__':
    main()
    
