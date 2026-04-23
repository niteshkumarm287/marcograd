So, this implements some kind of backprorogation - like going back and checking things and figuring out what inputs made the existing outcome possible.

and based on that you can iteratively tune the parameters to improve the outcomes of the loss function and improve the accuracy

g.backward() -> In code, this is gonna trigger a backward prorogation

derivative-formula.png - This formula is the formal limit definition of a derivative. It is the mathematical way of finding the instantaneous rate of change (or the slope) of a function at a specific point a.

To be super precise:

h - is the horizontal change: It is the tiny horizontal distance ("run") you are shrinking toward zero.
f(a+h)-f(a) - is the vertical change: It is the difference in height ("rise") between those two points.