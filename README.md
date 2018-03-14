
# Lists Lab

### Introduction

Ok, so now that we have gotten a sense of how to read from a list and alter a list in Python, let's put this knowledge to practice. 

### Objectives

* Practice reading one and multiple elements from lists
* Practice altering data in lists
* Practice add elements and removing elements from lists

### Our initial data structure 

In the previous lesson, we had a list of top travel cities.


```python
top_travel_cities = ['Solta', 'Greenville', 'Buenos Aires', 'Los Cabos', 'Walla Walla Valley', 'Marakesh', 'Albuquerque', 'Archipelago Sea', 'Iguazu Falls', 'Salina Island', 'Toronto', 'Pyeongchang']
```

> Remember to press shift enter to run each gray block of code.

In this lesson we can work with a list of each associated countries for each of those travel cities.


```python
countries = ['Croatia',
 'USA',
 'Argentina',
 'Mexico',
 'USA',
 'Morocco',
 'New Mexico',
 'Finland',
 'Argentina',
 'Italy',
 'Canada',
 'South Korea']
```

Ok, so the list of countries associated with each city has been assigned to the variable `countries`.  Now we will work with reading and manipulating this list.

### Accessing elements from lists

First, access the third to last element from `countries` and set it equal to the variable `italy`.


```python
italy = None # 'Italy'
italy
```

> We assign the varible `italy` equal to `None`, but you should change the word `None` to code that uses the `countries` list to assign `italy` to `'Italy'`.


```python
italy # 'Italy'
```

Now access the fourth element and set it equal to the variable `mexico`.


```python
mexico = None
mexico
```

Notice that the second through fifth elements are all in a row and all in the Western Hemisphere.  Assign that subset of elements to a variable called `kindof_neighbors`.


```python
kindof_neighbors = None
kindof_neighbors
```

### Changing Elements

Ok, now let's add a couple of countries onto this list.  At the end of the list, add the country 'Malta'.


```python
None # add code here
```

Then add the country 'Thailand'.


```python
None # add code here
```

Now your list of countries should look like the following.


```python
countries 
# ['Croatia', 'USA', 'Argentina', 'Mexico', 'USA', 'Morocco', 'New Mexico', 'Finland', 
# 'Argentina', 'Italy',  'Canada', 'South Korea',  'Malta',  'Thailand']
```

You may have noticed that "New Mexico" is included in our list of countries.  That doesn't seem right.  Let's change 'New Mexico' to 'USA'.


```python
None # add code here
```


```python
countries 
# ['Croatia', 'USA', 'Argentina', 'Mexico', 'USA', 'Morocco', 'USA', 'Finland', 
# 'Argentina', 'Italy',  'Canada', 'South Korea',  'Malta',  'Thailand']
```

Finally, let's remove Thailand from the list.  No good reason, we're acting on whimsy.


```python
countries = ['Croatia',
 'USA',
 'Argentina',
 'Mexico',
 'USA',
 'Morocco',
 'USA',
 'Finland',
 'Argentina',
 'Italy',
 'Canada',
 'South Korea', 
 'Malta', 
 'Thailand']
countries.pop() # 'Thailand'
countries
# ['Croatia', 'USA', 'Argentina', 'Mexico', 'USA', 'Morocco', 'USA', 'Finland',  'Argentina', 'Italy', 'Canada', 'South Korea',  'Malta']
```

### Exploring Lists with Methods

Ok, now we notice that some countries are mentioned more than once.  Let's see how many repeat countries are on this list.  

First, use the `set` and `list` functions to return a unique list of countries.  Set this list equal to the variable `unique_countries`.


```python
unique_countries = None
```


```python
unique_countries # ['USA',  'South Korea',  'Morocco',  'Finland',  'Italy', 
# 'Mexico',  'Argentina', 'Malta', 'Croatia', 'New Mexico', 'Canada']
```

Now the number of repeat countries should be the number of countries minus the number of unique countries.  So use the `len` function on both `unique_countries` and `countries` to calculate this and assign the result to the variable `num_of_repeats`.


```python
num_of_repeats = None
num_of_repeats # 3
```

### Summary

In this section we saw how to get our data from the outside world and into Python.  The purpose isn't to understand all of this code right now, but rather to see how easily we can start working with outside data.  As we become better at Python, the usefulness of taking data and operating on it in code rather than a spreadsheet will become more apparent.  But that doesn't mean we can't get step outside of Python sandbox now.  It's not too difficult to take some data we may already have, and begin to use it with Python.  In the next section, we'll use a lab to get data from excel and work with lists.
