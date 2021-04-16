# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 14:47:22 2021

@author: ULVI PC """

import json
from urllib.request import urlopen
from math import hypot

class Wariant2():

    
    # Download and convert data from url to list of dictionaries
    
    link_posts = "https://jsonplaceholder.typicode.com/posts"
    post_url = urlopen(link_posts)
    posts = post_url.read().decode()
    posts_data = json.loads(posts)
    
    # Download and convert users data from url to list of dictionaries
    
    link_users = "https://jsonplaceholder.typicode.com/users"
    users_url = urlopen(link_users)
    users = users_url.read().decode()
    users_data = json.loads(users)
    
    
    def user_posts_info(users_data, posts_data):
        '''Return dictionary with posts information'''
        
        list_post_per_user = []
        total_post_count = 0
        post_statistic = {}
        
        for user in users_data:
            user_id = user["id"]
            user_name = user["username"]
            user_posts_count = 0
            for post in posts_data:
                if post["userId"] == user_id:
                    user_posts_count += 1
           
            total_post_count += user_posts_count 
            list_post_per_user.append({"userId": user_id, "userName": user_name, "postCount": user_posts_count})
        
        post_statistic ["userPosts"] = list_post_per_user   
        post_statistic ["totalPostsCount"] = total_post_count
    
    
        return post_statistic
    
    # Total post count
    user_posts = user_posts_info(users_data, posts_data)

        
    def total_number_post(user_posts):
        '''Return total number of posts'''
        
        return(("Total number of posts: {}".format(user_posts["totalPostsCount"])))
    
    total_number = total_number_post(user_posts)
    
    
    def posts_per_users(user_posts):
        ''' Return post per user - list'''
        
        users_post_info = []
        
        for i in user_posts["userPosts"]:
            user_info = ("{} napisał(a) {} postów".format(i["userName"], i["postCount"]))
            users_post_info.append(user_info)
            
        return(users_post_info)
    

    
    def non_unique_posts(posts_data):
        '''Function wich find non unique post titles'''
        
        only_title_list = []
        non_unique_posts = set()
        
        for post in posts_data:
            only_title_list.append(post["title"])
                
        for title in only_title_list:
            title_repetitions = only_title_list.count(title)
            if title_repetitions > 1:
              non_unique_posts.add(title) 
        
        non_unique_posts_list = list(non_unique_posts)
        
        if non_unique_posts_list:
            return(non_unique_posts_list)
        else: 
            return("All titles are unique.")
    
    non_unique_posts(posts_data)
    
    
    
    def closest_person(users_data):
        '''Function return dict of the closest living people'''
        
        closest_persons = {}
        
        for user_1 in users_data:
            all_distances = {}
            user_1_id = user_1["id"]
            user_1_name = user_1["name"]
            user_1_geo = user_1["address"]["geo"]
            lat_1 = float(user_1_geo["lat"])
            lng_1 = float(user_1_geo["lng"])
            
            for user_2 in users_data:
                user_2_id = user_2["id"]
                user_2_name = user_2["name"]
                user_2_geo = user_2["address"]["geo"]
                lat_2 = float(user_2_geo["lat"])
                lng_2 = float(user_2_geo["lng"])
                
                if user_1_id == user_2_id:
                    continue
                else:
                    distance = hypot((lat_2 - lat_1),(lng_2 - lng_1))  
                    all_distances[user_2_name] = distance
                    
            min_distance = min(all_distances, key= lambda k: all_distances[k])
            closest_persons[user_1_name] = min_distance
            
            
        return(closest_persons)
    
                    
                