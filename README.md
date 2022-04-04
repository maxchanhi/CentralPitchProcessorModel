# CentralPitchProcessorModel
This program find the possible fundamental frequency between two notes.
The main deals with two simple sine tones and mainv2 deals with tone with harmonics (up to 4).
Copy the code to a online python compiler to run the code.
Enter 2 frequencies and seperate with space-bar.

When two tones are played in the high range, our brain will make a low frequency as a fundamental frequency.
Two playing frequencies are fa and fb. fb>fa
The fundamental frequency is f1.
n is number of partials.

The fa and fb frequencies are considered two successive harmonics of fa = n*f1 and fb = (n+1)*f1.  
For example, the SineTone, 1000Hz and 800Hz are playing at the same time, in the previous article, the result is 200Hz, 
and the program returns a perfect fit message. 
If the pair with no harmonic relationship, the program tries all possible partials from 1 to 24, to find the closest result of the fundamental.

The Complex can work with complex harmonic partials and inharmonic partials, up the 4 partials, both found down in harmonic series patterns. 
All individual partials are treated as a pair of sine tones, performing the same process above and finding downward for the possible fundamentals.
For inharmonic pairs, the program may suggest possible results, sorting from high to low. 
Higher frequency is preferred since the loudness is higher according to the equal-loudness contour.

The boundary of the results is ranged within +/-5% of the input lower frequency.
