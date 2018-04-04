
# UI Testing Lists Lab 

### Introduction

Ok, so now that we have a sense of how to read from a list and alter a list in Python, let's put this knowledge to use. 

### Objectives

* Practice reading one and multiple elements from lists
* Practice altering data in lists
* Practice adding elements and removing elements from lists

### Our initial data structure 

In the previous lesson, we had a list of top travel cities.


```python
top_travel_cities = ['Solta', 'Greenville', 'Buenos Aires', 'Los Cabos', 'Walla Walla Valley', 'Marakesh', 'Albuquerque', 'Archipelago Sea', 'Iguazu Falls', 'Salina Island', 'Toronto', 'Pyeongchang']
```

> Remember to press shift+enter to run each gray block of code (including the one above).  Otherwise, the variables will not be defined.


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

> Run the code in the cell above by pressing shift + enter.

Ok, so the list of countries associated with each city has been assigned to the variable `countries`.  Now we will work with reading and manipulating this list.

### Accessing elements from lists

For the tests in this lab to work, please run the following two cells.


```python
!pip install ipython_unittest
```

    Collecting ipython_unittest
      Downloading ipython_unittest-0.3.1-py2.py3-none-any.whl
    Installing collected packages: ipython-unittest
    Successfully installed ipython-unittest-0.3.1



```python
%load_ext ipython_unittest
```

First, set the variable `italy` to be equal to the third to last element from `countries`.  
>**Note:** If you see an **error** stating that `countries` is undefined, it means you must press shift+enter in the second gray box where `countries` variable is assigned.


```python
italy = None # 'Italy'
italy
```

> We assign the varible `italy` equal to `None`, but you should change the word `None` to code that uses the `countries` list to assign `italy` to `'Italy'`.  We wrote the variable `italy` a second time, so that you can see what it equals when you run the code block.  Currently, nothing is displayed below as it equals `None`, but when it's correct it will match the string which is commented out, `'Italy'`.


```python
italy # 'Italy'
```


```python
%%unittest_testcase

def test_italy(self):
    self.assertEqual(italy, 'Italy')
```

Now access the fourth element and set it equal to the variable `mexico`.


```python
mexico = None
mexico
```


```python
%%unittest_testcase

def test_mexico(self):
    self.assertEqual(mexico, 'Mexico')
```

Notice that the second through fifth elements are all in a row and all in the Western Hemisphere.  Assign that subset of elements to a variable called `kindof_neighbors`.


```python
kindof_neighbors = None
kindof_neighbors
```


```python
%%unittest_testcase

def test_kindof_neighbors(self):
    self.assertEqual(kindof_neighbors, ['USA', 'Argentina', 'Mexico', 'USA'])
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


```python
%%unittest_testcase

def test_countries(self):
    self.assertItemsEqual(countries, ['Croatia', 'USA', 'Argentina', 'Mexico', 'USA', 'Morocco', 'New Mexico', 'Finland', 'Argentina', 'Italy',  'Canada', 'South Korea',  'Malta',  'Thailand'])
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


```python
%%unittest_testcase

def test_countries_with_usa(self):
    self.assertNotIn('New Mexico', countries)
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




    ['Croatia',
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
     'Malta']




```python
%%unittest_testcase

def test_countries_with_usa(self):
    self.assertNotIn('Thailand', countries)
```

### Exploring Lists with Methods

Ok, now we notice that some countries are mentioned more than once.  Let's see how many repeat countries are on this list.  

First, use the `set` and `list` functions to return a unique list of countries.  Set this list equal to the variable `unique_countries`.


```python
unique_countries = None
```


```python
unique_countries # ['Canada', 'Italy', 'USA', 'Mexico', 'Finland', 
#'Malta', 'Morocco', 'Croatia', 'Argentina', 'South Korea']
```


```python
%%unittest_testcase

def test_unique_countries(self):
    self.assertItemsEqual(unique_countries, ['USA',  'South Korea',  'Morocco',  'Finland',  'Italy', 'Mexico',  'Argentina', 'Malta', 'Croatia', 'Canada'])
```

Now the number of repeat countries should be the number of countries minus the number of unique countries.  So use the `len` function on both `unique_countries` and `countries` to calculate this and assign the result to the variable `num_of_repeats`.


```python
num_of_repeats = None
num_of_repeats # 3
```


```python
%%unittest_testcase

def test_num_of_repeats(self):
    self.assertEqual(num_of_repeats, 3)
```

### Summary

In this lesson, we had some practice with working with lists in Python.  We saw how to add and remove elements from a list, as well as select specific elements.  Finally, we saw how to use a different data structure to calculate the number unique elements in the list.
