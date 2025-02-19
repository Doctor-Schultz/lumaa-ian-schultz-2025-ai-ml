Setup
============
**pandas** and **scikit-learn** are necessary for this program, as well as **Python 3**.10.12 or later. If you don't have the libraries already, run:
> pip install scikit-learn

> pip install pandas

Running:
============
This is a console based program. The command to run this program must follow the format *python3 movieRecommender.py numRows numRecommendations*, where *numRows* is the number of rows to use from the dataset, and *numRecommendations* is the number of movies you want recommended to you. 
The higher the value numRows is set to the better the results, because there are more movies to search, so I recommend starting with a value of at least *2000*. 

An example to get you started would be:
> python3 movieRecommender.py 2000 5

After entering said command, you will be asked to provide a short description of what type of movie you like in to the console. A few examples to try out are:
    * Horror or slasher movies where the main protagonists are chased by an evil killer.
    * World war two movie following soldiers as they liberate German occupied Europe.
    * A mystery where the protagonist must find the killer behind the string of murders before it is too late.

Results:
============
A list of movie titles, cosine similarity scores, and movie descriptions will be printed to the console. 

An example of running 
> python3 movieRecommender.py 2000 5 

and entering
> Horror or slasher movies where the main protagonists are chased by an evil killer.

will print the following to your console:
~~~
Your recommended movies, in descending order:

Title: Scary Movie 2
Cos Similarity: 0.1407188798679068
Description: While the original parodied slasher flicks like Scream Keenen Ivory Wayans's sequel to Scary Movie takes
comedic aim at haunted house movies. A group of students visit a mansion called "Hell House" and murderous high jinks
ensue.


Title: Bring It On: Cheer Or Die
Cos Similarity: 0.11725679311269392
Description: When a cheer squad practices their routines on Halloween weekend in an abandoned school they are picked offone by one by an unknown killer.


Title: Scary Movie
Cos Similarity: 0.10508147348956917
Description: A familiar-looking group of teenagers find themselves being stalked by a more-than-vaguely recognizable
masked killer! As the victims begin to pile up and the laughs pile on none of your favorite scary movies escape the
razor-sharp satire of this outrageously funny parody!


Title: Senior Year
Cos Similarity: 0.09777313843010346
Description: A thirty-seven-year-old woman wakes up from a twenty-year coma and returns to the high school where she wasonce a popular cheerleader to finish her senior year and become prom queen. The main plot is the empowerment of LGBTQ
rights and progress through the years.


Title: The Gangster, the Cop, the Devil
Cos Similarity: 0.09701549432067275
Description: After barely surviving a violent attack by an elusive serial killer crime boss Jang Dong-su finds himself
forming an unlikely partnership with local detective Jung Tae-seok to catch the sadistic killer simply known as K.
~~~

Dataset
============
This program uses the **wykonos/movies** dataset from Hugging Face. For convenience, the dataset is included as the movies_dataset.csv file in this repo- as long as this .csv is in the same directory as the python file, no extra steps are necessary.

For more information on the dataset [click here](https://huggingface.co/datasets/wykonos/movies?row=5)

Miscellaneous:
============
My contact info is ischultz@asu.edu and 602-377-6290

As per instruction, my expected monthly salary is $1600, however this is flexible. 