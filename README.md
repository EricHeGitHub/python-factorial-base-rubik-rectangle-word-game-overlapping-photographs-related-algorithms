# python-factorial-base-rubik-rectangle-word-game-overlapping-photographs-related-algorithms

1. Factorial base question

Write a program, stored in a file named factorial_base.py, that performs the following task.

• Prompts the user to input a nonnegative integer. If the input is not a nonnegative integer, then the program outputs an error message and exits.
• Outputs the conversion of that number in “factorial base”: a number written in factorial base is of the form dk ...d1 with di <= i for all 1 <= i <= k, and its decimal value is dk ⇥k!+···+d1 ⇥1!. For instance, the decimal value of 2301 read in factorial base is 2 * 4! + 3 * 3! + 0 * 2! + 1 * 1! = 67.

Here is a sample run of the program.
$ python3 factorial base .py <br/>Input a nonnegative integer : 12a Incorrect input, giving up...

$ python3 factorial base .py <br/>Input a nonnegative integer : Incorrect input, giving up...

$ python3 factorial base .py <br/>Input a nonnegative integer :  3 Incorrect input, giving up...

$ python3 factorial   base .py
  12 13 <br/>
 Input a nonnegative <br/>
Decimal 67 reads as

$ python3 factorial   base .py
integer : 67
2301 in factorial base. <br/>
Input a nonnegative <br/>
Decimal 2301 reads as 310311 in factorial base.

$ python3 factorial base .py <br/>
Input a nonnegative integer : 310311 <br/>
Decimal 310311 reads as 75354211 in factorial base.


2. Rubik’s rectangle

Write a program, stored in a file named rubiks_rectangle.py, that performs the following task.

• Prompts the user to input the digits 1 to 8 (with possibly whitespace inserted anywhere), in some order, say d1 d2 d3 d4 d5 d6 d7 d8, without repetition; if the input is incorrect, then the program outputs an error message and exits.
• Finds the minimal number of steps needed to go from the initial state

Here is a sample run of the program.
$ python3 rubiks rectangle .py <br/>
Input final configuration : 01234567 <br/>
Incorrect configuration , giving up...

$ python3 rubiks rectangle .py <br/>
Input final configuration : 12345678 <br/>
0 step is needed to reach the final configuration.

$ python3 rubiks rectangle .py <br/>
Input final configuration: 2 6 8 4 5 7 3 1 <br/>
7 steps are needed to reach the final configuration.

$ python3 rubiks rectangle .py <br/>
Input final configuration : 7215 4368 <br/>
16 steps are needed to reach the final configuration.

$ python3 rubiks rectangle .py <br/>
Input final configuration : 1 5 3 2 4 6 7 8 <br/>
18 steps are needed to reach the final configuration.

3. A word game

Write a program, stored in a file named highest_scoring_words.py, that performs the following task.

• Prompts the user to input between 3 and 10 lowercase letters (with possibly whitespace inserted any- where); if the input contains too few or too many lowercase letters or any character which is neither a lowercase letter nor whitespace, then the program outputs an error message and exits.
• Finds in the file wordsEn.txt, assumed to be stored in the working directory, the words built from the letters input by the user (with the exclusion of any other character) with highest score, if any; the score of a word is defined as the sum of the values of the letters that make up that word, the value of each letter being defined as follows:
a2	b5	c4	d4	e1	f6	
g5	h5  i1	j7	k6	l3
m5	n2	o3	p5	q7	r2
s1	t2	u4	v6	w6	x7
y5	z7

• Outputs a specific message if there is no such word; otherwise, outputs the highest score and all words with that score, one word per line, with a di↵erent introductory message depending on whether there is a unique such word (in which case the introductory message is on the same line as the word) or at least two such words (in which case the introductory message is on a line of its own and all words are preceded with 4 spaces).

Here is a sample run of the program.
$ python3 highest scoring words .py
Enter between 3 and 10 lowercase letters : abc2ef Incorrect input , giving up . . .

$ python3 highest scoring words .py
Enter between 3 and 10 lowercase letters: ab Incorrect input , giving up . . .

$ python3 highest scoring words .py
Enter between 3 and 10 lowercase letters : abcdefghijk Incorrect input , giving up . . .

$ python3 highest scoring words .py
Enter between 3 and 10 lowercase letters: zz zz zz
No word is built from some of those letters.

$ python3 highest scoring words .py
Enter between 3 and 10 lowercase letters: a a a The highest score is 2.

The highest scoring word is a

$ python3 highest scoring words .py
Enter between 3 and 10 lowercase letters: a e i o u The highest score is 8.

The highest scoring words are , in alphabetical order :
iou
oui

$ python3 highest scoring words .py
Enter between 3 and 10 lowercase letters: prmgroa The highest score is 24.

The highest scoring word is program

$ python3 highest scoring words .py
Enter between 3 and 10 lowercase letters: r a mm o x y The highest score is 17.

The highest scoring words are , in alphabetical
mayor moray moxa oryx

$ python3 highest scoring words .py
Enter between 3 and 10 lowercase letters: eaeo rtsmn The highest score is 17.

The highest scoring words are , in alphabetical order :
matrons transom

4. Overlapping photographs

Write a program, stored in a file named perimeter.py, that performs the following task.

• Prompts the user to input the name of text file assumed to be stored in the working directory. We assume that if the name is valid then the file consists of lines all containing 4 integers separated by whitespace, of the form x1 y1 x2 y2 where (x1,y1) and (x2,y2) are meant to represent the coordinates of two opposite corners of a rectangle. With the provided file frames_1.txt, the rectangles can be represented as follows, using from top bottom the colours green, yellow, red, blue, purple, olive, and magenta.

We assume that all rectangles are distinct and either properly overlap or are disjoint (they do not touch
each other by some of their sides or some of their corners).

• Computes and outputs the perimeter of the boundary, so with the sample file perimeter.py, the sum
of the lengths of the (external or internal) sides of the following picture.

Here is a sample run of the program with the two provided sample files.
$ python3 perimeter . py
Which data file do you want to use? frames 1.txt <br/>
The perimeter is: 228

$ python3 perimeter . py
Which data file do you want to use? frames 2.txt <br/>
The perimeter is: 9090





