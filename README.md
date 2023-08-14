# Programming-1-Introduction-to-Programming-Energy-statistics
Tampere University, Projects made in the course Programming 1: Introduction to Programming

Instructions

In this assignment you will implement a little program capable of printing energy cunsumption histograms based on the data the user entered. The energy consumption values will be divided into classes based on a logarithmic scale. In practise this means that the limits of the classes (or categories) of the values will differ from each other by multiples of 10.

As an example, here are the first five classes:

Class

number	Values belonging

to the class

1.

2.

3.

4.

5.
  
0–9

10–99

100–999

1000–9999

10000–99999

It is not neccessary to understand the meaning of logarithmic scale as long as you can see from the example how the values belonging to the class relate to the ordinal number of the class.

If needed, you can calculate the smallest and the largest values belonging to a particular class using the formulae:

smallest_value = 10 ** class_number // 100 * 10

largest_value  = 10 ** class_number - 1

In case you decide to use the formulae above, make sure to copy them correctly to avoid typing errors. They are tested and work correctly.

On the other hand, if you need to know which class does a value belongs to, one possibility is to use the following algorithm:

class_number = 1

while True:

    if smallest_value_of_the_class <= value <= largest_value_of_the_class:

         here we know for sure that value belongs to class class_number

    class_number += 1

Note that the algorithm above is not ready code, at minimum you have to figure out what goes to the placeholders expressed as italic text.

Another thing worth realizing is that all the inputs for this program are integers (int). This simplifies things and also avoids rounding errors, which would complicate the program unneccesarily.

Your purpuse in this project is to design and implement a program able to print histograms from the energy consumption values when those values can differ from each other by multiple ordes of magnitude.

Program Behavior

In some of the examples we have used special character ␣ to express a whitespace so that misunderstandings can be avoided.

When the program starts it will first print:

Enter energy consumption data.

End by entering an empty line.

After this, it will start asking user inout by printing a prompt like this:

Enter energy consumption (kWh):␣

At which point the user is expected to enter energy consumption values. The entered values can't be negative. Whenever the user tries to enter a negative value, the program prints an error message and waits for the user to enter next value:

You entered: X. Enter non-negative numbers only!

Enter energy consumption (kWh):␣

Where X is the entered negative value. The errorneous input is ignored otherwise.

When the user inputs an empty line, the program finishes asking for inout and printes a histogram based on the values the user entered. The histogram looks generally like this:

            0-9:␣*********

          10-99:␣*

        100-999:␣********

      1000-9999:␣**

    10000-99999:␣*******

  100000-999999:␣***

1000000-9999999:␣*****

    ⋮       ⋮      ⋮

As you can see, the scale is logarithmic since the lower and upper limits of the consecutive classes differ from each other by one order of magnitude.

Each line has as many "*" characters printed as there was user input values belonging to that category.

The program has to be able to follow the shown output format even when the smallest and the largest value entered by the user are wildly different in scale.

Examples of the Program's Behavior

Here are some examples of how the program shoudl work. The automatic tests expect the output format to be followed strictly.

Small Set of Input Values

Only three categories/classes of input values:

Enter energy consumption data.

End by entering an empty line.

Enter energy consumption (kWh): 91

Enter energy consumption (kWh): 10

Enter energy consumption (kWh): 101

Enter energy consumption (kWh): 912

Enter energy consumption (kWh): 22

Enter energy consumption (kWh): 6

Enter energy consumption (kWh):

    0-9: *

  10-99: ***

100-999: **

The first category is always 0–9 and the last one depends on the largest value the user entered.

Greater Difference in Magnitudes

When the smalles and largest input value differ from each other multiple orders of magnitude:

Enter energy consumption data.

End by entering an empty line.

Enter energy consumption (kWh): 1

Enter energy consumption (kWh): 10
Enter energy consumption (kWh): 100

Enter energy consumption (kWh): 1000

Enter energy consumption (kWh): 10000

Enter energy consumption (kWh): 100000

Enter energy consumption (kWh): 1000000

Enter energy consumption (kWh): 10000000

Enter energy consumption (kWh): 100000000

Enter energy consumption (kWh): 1000000000

Enter energy consumption (kWh): 10000000000

Enter energy consumption (kWh): 100000000000

Enter energy consumption (kWh):

                      0-9: *

                    10-99: *

                  100-999: *

                1000-9999: *

              10000-99999: *

            100000-999999: *

          1000000-9999999: *

        10000000-99999999: *

      100000000-999999999: *

    1000000000-9999999999: *

  10000000000-99999999999: *

100000000000-999999999999: *

The most important point in this example is how the lower categories must be indented to make the colon ":" charachter align horizontally on the histogram printout.

Empty categories

It is possible to have categories which have now values:

Enter energy consumption data.

End by entering an empty line.

Enter energy consumption (kWh): 7

Enter energy consumption (kWh): 1

Enter energy consumption (kWh): 1010

Enter energy consumption (kWh): 9120

Enter energy consumption (kWh): 0

Enter energy consumption (kWh): 1

Enter energy consumption (kWh):

      0-9: ****

    10-99:

  100-999:

1000-9999: **

The empty categories have to be present in the output.

Another little more pathological example of this is:

Enter energy consumption data.

End by entering an empty line.

Enter energy consumption (kWh): 1010

Enter energy consumption (kWh): 9120

Enter energy consumption (kWh): 5678

Enter energy consumption (kWh):

      0-9:

    10-99:

  100-999:

1000-9999: ***

User Does Not Enter Any Values

If th euser enters no values, the program won't get upset:

Enter energy consumption data.

End by entering an empty line.

Enter energy consumption (kWh):

Nothing to print. Done.

Errorneous Inputs

Example of how errorneous inputs are handled:


Enter energy consumption data.

End by entering an empty line.

Enter energy consumption (kWh): 42

Enter energy consumption (kWh): -42

You entered: -42. Enter non-negative numbers only!

Enter energy consumption (kWh): -240

You entered: -240. Enter non-negative numbers only!

Enter energy consumption (kWh): 240

Enter energy consumption (kWh): 391

Enter energy consumption (kWh): -1

You entered: -1. Enter non-negative numbers only!

Enter energy consumption (kWh): 1

Enter energy consumption (kWh): 123

Enter energy consumption (kWh): 1

Enter energy consumption (kWh): -1

You entered: -1. Enter non-negative numbers only!

Enter energy consumption (kWh):

    0-9: **

  10-99: *

100-999: ***
