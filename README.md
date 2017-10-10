# ElonDeepAI

This is my attempt to create a coherent sounding Elon Musk bot by training a recurrent neural network on his tweets from 2010-2017. 

Although improvement is observable, it is still in the early stages.

He can be found at https://twitter.com/ElonDeepAI.

Check the [license file](https://github.com/skiman6010/ElonDeepAI/blob/master/license.txt) for the license.


## TODO
- Upload pre-trained data
- Explain setup
- Make it a clean dataset

## Explanation
This bot is built on top of Hunkim's Word RNN Tensorflow [repo](https://github.com/hunkim/word-rnn-tensorflow). It's very versatile in how you can use it to train models. 

Install Tweepy with this [tutorial](https://www.digitalocean.com/community/tutorials/how-to-create-a-twitterbot-with-python-3-and-the-tweepy-library).

Replace the sample.py from Hunkim's repo with mine and add twitterbot_ai.py to the folder. 

Run twitterbot_ai.py and it will generate and send a tweet to your account.

I will add my pre-trained data as soon as I clean it up.
