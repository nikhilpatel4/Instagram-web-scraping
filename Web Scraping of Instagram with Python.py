#!/usr/bin/env python
# coding: utf-8

# In[15]:


import instaloader

#create an instance of Instaloader class
bot = instaloader.Instaloader()

# Load a profile from an Instagram handles
#you can write any valid username of instagram

profile = instaloader.Profile.from_username(bot.context,'instagram')

#instagram account information
print("Username: ", profile.username)
print("User ID: ", profile.userid)
print("Number of Posts: ", profile.mediacount)
print("Followers: ", profile.followers)
print("Followees: ", profile.followees)
print("Bio: ", profile.biography,profile.external_url)

