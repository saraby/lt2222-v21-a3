# LT2222 V21 Assignment 3

Your name: Sarab Youssef

## Part 1
Figuring out train.py:

### Function 'a()':
tokenizes the text in the opened file (f) and returns a list of characters (mm) in addition to a list of non-repeated (unique) characters, where two start tokens are added at the beginning of the (mm) list and two end tokens at the end of it.

### Function 'g()':
returns an array that contains lists of zeros and ones where 1 determin the position (index) of character (x). these list are originally generated of the same list that contains all the unique characters in the tokenized text.

### Function 'b()':
builds big matrix that includes instances of vowels and their features and context. To do this we call the function a() and then return two lists:
    - gt: contains list of indexes where the vowels are placed.
    - gr: list of features/context.
We iterate over the tokenized text without the start and end tokens. If the token is not a vowel in the current iteration skip to the next iteration. Perform this check for each iteration and then create list of features (gr) of the checked vowel by calling function g().

### Command Line Arguments:
   - k is the hidden size of the features. This is optional and the default value is set to 200.
   - r is the number of epochs to train the model. This is also optional and the default value is set to 100.
   - m is the path to the input file where we can find the text to train the model.
   - h is the path and name of the file where we save the output model


## Part 2

We need to process the test data just like we did with the train data before building the model and testing. For that we used the structure in train.py with a bit of changes, we used the same set of vowels and function a() as they are by importing them and made a little changes to both b and g with changing their names to make it easier to read the function. We needed these changes because the test data is different from the train data which might indicate they would not have the same characters (observed because of the errors we got while trying to process the test data). due to these challenges we decided to skip the characters that did not exist in the unique characters (models.vocab).
After that we create evaluation instances. Then predict instances using the model and use it to write the predicted text then calculate the accuracy of our model.


## Part 3

|     epochs(r)  |  hidden layers(k)|  Accuracy |
|    :-----:     |      :-----:     |   :---:   |
|      15        |                  |    21%    |
|      50        |                  |    30%    |
|      200       |        200       |    21%    |
|      500       |                  |    15%    |
|     1000       |                  |     3%    |
| default = 100  |   default = 200  |    46%    |
|                |        50        |    20%    |
|                |        100       |    39%    |
|      100       |        150       |    42%    |
|                |        250       |    26%    |
|                |        500       |    38%    |
______________________________________________

What we can notice here is that extremely high numbers of epochs will be as bad as extremely low ones and could be worse! That will result in overfitting which means our model does not learn the data anymore, but memorize it instead. That's why we can notice that the best result we got was when we kept the default values of both the hidden layers and epochs which gave us an accuracy of 46%. The second best result which is 42% used only 150 layers whereas the default number of hidden layers was 200 and both gave two almost similar accuracy. We can see that the number of hidden layers did not generate a pattern as we can see after the accuracy dropped when using 250 hidden layers it increased again when using 500 layers. Which means the increasing of hidden layers might and it does not guarantee the increase in accuracy in general but it will reduse performance (and increase the waiting time) but this depends on the model itself, if we don't have a large training data increasing the hidden layers will be useless and will only result in bad performance.

We notice in the output texts that the usually used words (which are the words most definitely were in the training data) were the most successful to be correctly guessed by the best models, the words (och, den, för, det, till, på, under, han, som, här, mycket, gå, honom, jag, sin, pris, från, i, om, etc..) but it also failed to guess (men ≠ mån, att ≠ ått, har ≠ här, ofta ≠ eftå med ≠ måd, stad ≠ ståd, efter ≠ eftår, också ≠ ickså, arbeta ≠ årbåtå, etc...)we notice the model tend to predict the vowels as 'å' in most cases for some reason. for the worst model we can notice that when used 1000 epochs the model guessed almost if not all the vowels to be 'é' which I couldn't explain the reason behind using this particular vowel above all else.


## Bonuses

## Other notes
This assignment is a joint effort by: Sigrid Jonsson, Judit Casademont Moner and Sarab Youssef.
