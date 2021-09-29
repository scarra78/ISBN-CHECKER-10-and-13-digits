# ISBN-CHECKER-10-and-13-digits
A demonstration of classes with a 10 and 13 digit isbn checker 
Create a class 'Book'. Each book object should have the following attributes: title, author,
year of first publication, number of pages and ISBN. Define an init method which will
 assign these attributes for a new instance of
Book, a repr method which will provide details about a book, and a valid_isbn method
which will return True if a book's ISBN is valid and False otherwise.
The logic behind ISBNs is
described here: https://gitlab.com/qacdevops/python-exercises/-/blob/master/easy/isbn.md
Stretch goal: Create two new classes, FantasyNovel and ScifiNovel,
which inherit from Book, and override Book's repr method to give a
more genre-specific description
The first 12 digits are taken
Starting at index 0,
if the index is even - add it,
and if the index is odd
multiply the digit by three then add it.
From the sum find the remainder after dividing by 10.
10 minus the remainder give us the check digit
In other words the following algebra would give us the check digit:
digit_12 = 10 – (( digit_0 + (3 x digit_1) + digit_2 + (3 x digit_3) + digit_4 + (3 x digit_5) + digit_6 + (3 x digit_7) + digit_8 + (3 x digit_9) + digit_10 + (3 x digit_11) ) % 10)
