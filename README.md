# Area_Under_Graphs
Short Python project for displaying area under mathematical graphs


# Guide
Running the file will create a number of graphs in a created folder called "Graphs". These graphs then can be imported/added into a Word document for use in notes, etc.
The main function is the plot_shaded_area function.
It takes three arguments: plot_shaded_area( function, start, stop, label)
* Function: this is the mathematical function you want to plot. Use lambda x: to define the function in terms of x e.g. to define a linear function you could write "lambda x: 2*x+1" for 2x+1. Note that python mathematical operators must be used for multiplication or division.
* Start: This is where you want the function to start shading in area from
* Stop: This is where the shading of area will end
* label: This is the label that will be written on the graph, it is not necessary and can be left blank with "".

There are a number of examples of linear, quadratic, etc. types of functions in the code already. 

# Solutions
The code will also print out the areas under the generated graphs, useful if you were making these for questions, etc. 

# Known issues
Plotting trig functions means that pi is not rendered as pi but rather 3.1415..., similarly for pi/2, etc. 
