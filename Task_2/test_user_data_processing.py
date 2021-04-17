# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 11:11:41 2021

@author: ULVI PC
"""

import unittest
from user_data_processing import Wariant2

# Simple test
test_1 = [[{'id': 1, 'name': 'Aaaa Bbbb', 'username': 'Ab', 'address': {'geo': {'lat': '1', 'lng': '1'}}}, 
                   {'id': 2, 'name': 'Cccc Dddd', 'username': 'Cd', 'address': {'geo': {'lat': '2', 'lng': '2'}}}, 
                   {'id': 3, 'name': 'Eeee Ffff', 'username': 'Ef', 'address': {'geo': {'lat': '5', 'lng': '5'}}}, 
                   {'id': 4, 'name': 'Gggg Hhhh', 'username': 'Gh', 'address': {'geo': {'lat': '-7', 'lng': '-7'}}}, 
                   {'id': 5, 'name': 'Iiii Jjjj', 'username': 'Ij', 'address': {'geo': {'lat': '-1', 'lng': '1'}}}], 
                 [{'userId': 1, 'id': 1, 'title': 'unique-1'}, 
                  {'userId': 1, 'id': 2, 'title': 'non unique-1'}, 
                  {'userId': 1, 'id': 3, 'title': 'unique-2'}, 
                  {'userId': 2, 'id': 4, 'title': 'unique-3'}, 
                  {'userId': 2, 'id': 5, 'title': 'unique-4'}, 
                  {'userId': 2, 'id': 6, 'title': 'non unique-2'}, 
                  {'userId': 3, 'id': 7, 'title': 'unique-5'}, 
                  {'userId': 3, 'id': 8, 'title': 'unique-6'}, 
                  {'userId': 3, 'id': 9, 'title': 'unique-7'}, 
                  {'userId': 4, 'id': 10, 'title': 'non unique-1'}, 
                  {'userId': 4, 'id': 11, 'title': 'unique-8'}, 
                  {'userId': 5, 'id': 12, 'title': 'unique-9'}, 
                  {'userId': 5, 'id': 13, 'title': 'non unique-2'}]] 

answer_1 = [{'userPosts': [{'userId': 1, 'userName': 'Ab', 'postCount': 3}, 
                           {'userId': 2, 'userName': 'Cd', 'postCount': 3}, 
                           {'userId': 3, 'userName': 'Ef', 'postCount': 3}, 
                           {'userId': 4, 'userName': 'Gh', 'postCount': 2}, 
                           {'userId': 5, 'userName': 'Ij', 'postCount': 2}], 
                 'totalPostsCount': 13,},
                "Total number of posts: 13",
                ['Ab napisał(a) 3 postów', 'Cd napisał(a) 3 postów', 'Ef napisał(a) 3 postów', 'Gh napisał(a) 2 postów', 'Ij napisał(a) 2 postów'],
                ['non unique-1','non unique-2'],
                {'Aaaa Bbbb':['Cccc Dddd'], 'Cccc Dddd':['Aaaa Bbbb'], 'Eeee Ffff':['Cccc Dddd'], 'Gggg Hhhh':['Iiii Jjjj'], 'Iiii Jjjj': ['Aaaa Bbbb']}]
    

# Test users with the same distance (2 of them) and for repetative titles
test_2 = [[{'id': 1, 'name': 'Aaaa Bbbb', 'username': 'Ab', 'address': {'geo': {'lat': '1', 'lng': '1'}}}, 
                   {'id': 2, 'name': 'Cccc Dddd', 'username': 'Cd', 'address': {'geo': {'lat': '2', 'lng': '2'}}}, 
                   {'id': 3, 'name': 'Eeee Ffff', 'username': 'Ef', 'address': {'geo': {'lat': '2', 'lng': '2'}}}, 
                   {'id': 4, 'name': 'Gggg Hhhh', 'username': 'Gh', 'address': {'geo': {'lat': '-7', 'lng': '-7'}}}, 
                   {'id': 5, 'name': 'Iiii Jjjj', 'username': 'Ij', 'address': {'geo': {'lat': '-1', 'lng': '1'}}}], 
                 [{'userId': 1, 'id': 1, 'title': 'unique-1'}, 
                  {'userId': 1, 'id': 2, 'title': 'non unique-1'}, 
                  {'userId': 1, 'id': 3, 'title': 'unique-2'}, 
                  {'userId': 1, 'id': 4, 'title': 'unique-3'}, 
                  {'userId': 1, 'id': 5, 'title': 'unique-4'}, 
                  {'userId': 2, 'id': 6, 'title': 'non unique-2'}, 
                  {'userId': 3, 'id': 7, 'title': 'unique-5'}, 
                  {'userId': 3, 'id': 8, 'title': 'unique-6'}, 
                  {'userId': 3, 'id': 9, 'title': 'unique-7'}, 
                  {'userId': 4, 'id': 10, 'title': 'non unique-1'}, 
                  {'userId': 4, 'id': 11, 'title': 'unique-8'}, 
                  {'userId': 5, 'id': 12, 'title': 'non unique-2'}, 
                  {'userId': 5, 'id': 13, 'title': 'non unique-2'}]] 

answer_2 = [{'userPosts': [{'userId': 1, 'userName': 'Ab', 'postCount': 5}, 
                           {'userId': 2, 'userName': 'Cd', 'postCount': 1}, 
                           {'userId': 3, 'userName': 'Ef', 'postCount': 3}, 
                           {'userId': 4, 'userName': 'Gh', 'postCount': 2}, 
                           {'userId': 5, 'userName': 'Ij', 'postCount': 2}], 
            'totalPostsCount': 13,},
            "Total number of posts: 13",
            ['Ab napisał(a) 5 postów', 'Cd napisał(a) 1 postów', 'Ef napisał(a) 3 postów', 'Gh napisał(a) 2 postów', 'Ij napisał(a) 2 postów'],
            ['non unique-1','non unique-2'],
            {'Aaaa Bbbb':['Cccc Dddd','Eeee Ffff'], 'Cccc Dddd':['Eeee Ffff'], 'Eeee Ffff':['Cccc Dddd'], 'Gggg Hhhh':['Iiii Jjjj'], 'Iiii Jjjj': ['Aaaa Bbbb']}]


# Test with one user without coments titles  
test_3 = [[{'id': 1, 'name': 'Aaaa Bbbb', 'username': 'Ab', 'address': {'geo': {'lat': '1', 'lng': '1'}}}, 
           {'id': 2, 'name': 'Cccc Dddd', 'username': 'Cd', 'address': {'geo': {'lat': '1', 'lng': '1'}}}], 
          [{'userId': 1, 'id': 1, 'title': 'unique-1'}, 
           {'userId': 1, 'id': 2, 'title': 'unique-2'}]] 
        
answer_3 = [{'userPosts': [{'userId': 1, 'userName': 'Ab', 'postCount': 2}, 
                           {'userId': 2, 'userName': 'Cd', 'postCount': 0}], 
                    'totalPostsCount': 2},
                    "Total number of posts: 2",
                    ['Ab napisał(a) 2 postów', 'Cd napisał(a) 0 postów'],
                    "All titles are unique.",
                    {'Aaaa Bbbb':['Cccc Dddd'], 'Cccc Dddd':['Aaaa Bbbb']}]

    
# Test only with one user
test_4 = [[{'id': 1, 'name': 'Aaaa Bbbb', 'username': 'Ab', 'address': {'geo': {'lat': '1', 'lng': '1'}}}], 
          [{'userId': 1, 'id': 1, 'title': 'unique-1'}, 
           {'userId': 1, 'id': 2, 'title': 'unique-2'}]] 
        
answer_4 = [{'userPosts': [{'userId': 1, 'userName': 'Ab', 'postCount': 2}], 
             'totalPostsCount': 2},
            "Total number of posts: 2",
            ['Ab napisał(a) 2 postów'],
            "All titles are unique.",
            {}]


    
parametrs = [[test_1, answer_1],[test_2, answer_2],[test_3, answer_3], [test_4, answer_4]]
    
for parametr in parametrs:
    
    class UserPostsTestCase(unittest.TestCase):
        '''Test for user_postst function'''
              
        def setUp(self):
            '''Create test variants and answers'''
            self.test = parametr[0]
            self.answer = parametr[1] 
            

        def test_user_posts(self):
                user_posts = Wariant2.user_posts_info(self.test[0], self.test[1])
                self.assertEqual(user_posts, self.answer[0])
                return(user_posts)
        
        def test_total_post_number(self):
                total = Wariant2.total_number_post(Wariant2.user_posts_info(self.test[0], self.test[1]))
                self.assertEqual(total, self.answer[1])
                
        def test_printed_list(self):
                list_of_post_per_person = Wariant2.posts_per_users(Wariant2.user_posts_info(self.test[0], self.test[1]))
                self.assertEqual(list_of_post_per_person, self.answer[2])
            
        def test_non_unique_post(self):
                list_of_nonique_posts = Wariant2.non_unique_posts(self.test[1])
                for non_unique_post in list_of_nonique_posts:
                    self.assertIn(non_unique_post,self.answer[3])
            
        def test_closest_person(self):
                dict_of_closest = Wariant2.closest_person(self.test[0])
                self.assertEqual(dict_of_closest, self.answer[4])
            
    unittest.main()       
        




