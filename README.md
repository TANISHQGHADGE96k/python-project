Team 1

Creating String Data Structure Using all Methods

String Data Structure 

A string is a sequence of characters stored in contiguous memory locations. In custom implementations, the goal is to provide functionality similar to those in standard libraries, such as string creation, modification, concatenation, comparison, and more.

Structure of the Custom String Class

1. Attributes:

Data: A dynamic array or fixed-size array to store the string characters.
Size: The current length of the string.
Capacity (Optional): Total allocated memory, useful for dynamic resizing.

Methods

1. Basic Operations
   
Constructor: Initializes the string object with an empty or predefined value.
Destructor: Frees allocated memory to prevent leaks.
Length: Returns the length of the string.

2. Access Methods
   
Get Character (Indexing):Access a character at a specific index.
char charAt(int index) const;
Set Character:Modify the character at a specific index.

3. Manipulation

Concatenation:Combine two strings and return a new string.
Insert:Add a substring at a specific position.
Erase/Delete:Remove characters from a specific range.
Replace:Replace a substring with another.
Substring:Extract a part of the string.

4. Utility Functions

Comparison:Compare two strings lexicographically.
Search:Find a character or substring within the string.
Reverse:Reverse the string in place.

5. Advanced Features

Dynamic Resizing:Handle memory allocation and resizing for large strings.
Case Conversion:Convert the string to uppercase or lowercase.
Trim:Remove whitespace from the beginning or end of the string.
Split:Divide the string into tokens based on a delimiter.
