# fifa19-players

Data from https://www.kaggle.com/karangadiya/fifa19

The players attributes were processed in order to create a content-based recommendation system. The created function will help people identify players that are similar to an other player. It is based on a KNN algorithm developed with the codification of every variable as a number between 0 and 1. 

I am currently working on improving the recommendation algorithm by adding weights to different variables, in order to determine the most important ones. Also, a flask web app is being developed in order to create an interface that improves the interaction with the algorithm.

The goal of this project is to eventually develope a recommendation system that is useful to FIFA 21 gammers (will require obtaining data from the current game and keeping it up to date) when they are making purchasing decisions.
