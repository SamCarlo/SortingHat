#Science, Tech, and Society Task 2
##By Sam Carlos
###Began: 1/21/22

##Journal 1/21:

I made the first version of table_drawer which draws as many tables onto a 1000x1000 space as you tell it to.
Next, I need to get it to draw table groups. This may require creating a Class.

Just to think aloud --
table groups will be the class,
and student cards will be the objects that fill the class.
I don't need it to be a perfect map of the classroom.
I don't even need it to show where individual students sit.
I just need each table to tell me which students are in each group.

sketching it out:
-create a randomly sorted list of student names
-for every 4 students, put them into one group
-print that group onto a card
-if the last group has 3 students, make it a group.
-if the last group has 2 students, make the last 2 groups 3 students each
-if the last group has 1 student, make the last group 5 students.
-Do this until all the students are in a group.

##journal 1/23:
I realize I can make this program use "get_groups" to pull groups of certain charactaristics.

I can create a ranking characteristic by sorting scores into "low", "med", or "high" depending on a specified range.
I can then create a "ranking" column that says their ranking.
Finally, I can use "get_groups" to create the groups that are low, med, or high.
That's a different way to do what I'm trying to do.

For now I am just slicing sorted lists into 3.

#journal 1/24
I actually ended up doing what I thought of yesterday:
I categorized scores based on an arbitrary grading bracket.
Now, I can operate on their "rank" of high, med, or low scoring.
The next function should be an alogrithm that
groups students into high-med, med-med, and med-low groups.

Additionally, I discovered a new form of coding:
I 'prove' one function or method at a time before moving on,
annotating each method as I prove them. What I end up with is a list of tools
that I know will work. Then I can put them together however I like.
I call this "narrative tinkering." It's a comprehensible input strategy.

Pandas "sample" and "groupby" are the methods I need to create random (or not random) groups!

#Journal 1/25
I did a pretty heavy-handed solution that will work for now.
Later I'll learn more about manipulating data tables Pandas.
It just turns out that a lot of table manipulation already exists as Pandas methods.

Another project I'd like to complete some day: sorting out students by scores.
The groupby() method allows you to change the probablity that certain features
will be selected, which seems pretty cool.

--

Ok I finished 2 programs: RandomHat creates random groups, ScoreHat creates score-based groups. I will not create a visualizer today - that will require forming objects out of the tables I create, and I'm not quite ready to do that. I'll need to play around with processing by itself for a while.

Overall takeaways from this project:
Pandas Methods are way deeper than I thought. Examples of each trick:
-`df2 = df.assign(math_rank = 1)` : create a new column for a DataFrame. This one makes a column called 'math_rank' that's just full of 1's.
-`df[df['Math Score'] > 70]` : select all cells in a specified column...or row?
-`arr = df.to_numpy()`: convert a DataFrame to a numpy array.
-`df_math = df.sort_values('Math Score')` .sort_values() sorts ascendingly relative to the stated column.
-A cheap method for labelling rows:
`scores = df_astro_rank['Astronomy score']
rank = []
for i in scores:
    if i > 60:
        rank.append('High')
    if 60 > i > 50:
        rank.append('Med')
    if 50 > i > 0:
        rank.append('Low')

ranked_astro = df_astro.assign(Rank = rank)`

This ranks student scores into 3 categories and then creates a series called "rank" that contains all the ranks of the students. The last line attaches this series onto the appropriate DataFrame.

-`high_astro = ranked_astro[ranked_astro['Rank'] == 'High']` return the rows of a DataFrame based on a given attribute. In this example, I returned a list of all students who had a score labelled "high."
-`df_shuffled0 = df['Name'].sample(frac=1, replace = False, random_state=1)` .sample() randomly samples rows from a DataFrame. It has more arguments than I used. You can change how random it is, for example.
-Slice up a DataFrame like a pie:
`group1 = df_shuffled0.iloc[0:5]
group2 = df_shuffled0.iloc[5:10]
group3 = df_shuffled0.iloc[10:15]
group4 = df_shuffled0.iloc[15:20]
group5 = df_shuffled0.iloc[20:23]
group6 = df_shuffled0.iloc[23:]`
The key is to use colons, not commas, to say x 'through' y.

-Stitching dataframes backtogether:
`grps_ = [group1["Name"], group2["Name"], [...] ]
grouped = pd.concat(grps_, axis = 1, ignore_index = True)`
Again, there are more arguments, but you get the point. Very useful, but I didn't find a use for it. 
