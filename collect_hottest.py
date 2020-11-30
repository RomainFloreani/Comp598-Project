import argparse
import json
import requests
import argparse
import os.path as osp

#We can't collect more than 1000. So we need to find a way to eliminate. There are only 750 on pages.

def scrape_reddit(num_posts,subreddit,before = 'null', after = 'null'):
    # This is the request, this uses the reddit api to collect the hottest posts.
    data = requests.get(f'http://api.reddit.com{subreddit}/hot?limit={num_posts}&before={before}&after={after}', 
                        headers={'User-Agent':'windows: requests (by /u/rflore)'})
    return data.json()['data']
    # Here we return the data of all the posts.

def main():
    
    #In the command line when we execute our post we will with 3 args, the name of our output file, the subreddit name "in the form /r/"subreddit"
    # and the number of posts needed to be collected.
    parser = argparse.ArgumentParser()
    parser.add_argument('-o','--output_file', help = "output file", required = True)
    parser.add_argument('subreddit', help = "This is the subreddit which will be used to collect the posts")
    parser.add_argument('number_of_posts', help ="This is the number of posts which will be collect")
    args = parser.parse_args()
    
    num_posts = int(args.number_of_posts)
    
    #out_file = open(f'../data/{args.output_file}', 'w')
    out_path = os.join("..",'data',args.output_file')
    out_file = open(out_path,'w')
    content = scrape_reddit(100, args.subreddit)
    list_of_posts = []
    while (len(list_of_posts) < num_posts):
        post = content['children']
        for i in range(0,100):
            try:
                list_of_posts.append(json.dumps(post[i]))
            except Exception as e:
                continue
        after = content['after']
        content  = scrape_reddit(100, args.subreddit,after = after)
        
        
    for i in list_of_posts:
        out_file.write(str(i)+ '\n')
        
    out_file.close()

    
    
if __name__ == '__main__':
    main()
    
