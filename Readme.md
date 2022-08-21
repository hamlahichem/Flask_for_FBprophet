The test is creating a Flask web application that exposes an interface of Facebook’s prophet
 <https://facebook.github.io/prophet/> for non technical users to make predictions.

The usage scenario is that a user visiting the site can upload his data from a CSV file 
then choose some of the model training parameters and provide a forecast period then ask 
for a prediction, once that is done they get to explore the results graphs and data which 
they could also export back into a csv file.

The application should return meaningful feedback about expected errors or bad user inputs
and should also be able to handle multiple concurrent users. The code must be versioned and 
pushed to a GitLab repository along with a deployment method and instructions.

Extra features like authentication or REST API or any enhancements thought of by the 
developer are appreciated.

You can find some useful resources at:

 *

   Facebook prophet’s Quick Start
   <https://facebook.github.io/prophet/docs/quick_start.html> and Data
   examples <https://github.com/facebook/prophet/tree/main/examples>

 *

   Flask Quickstart 
    <https://flask.palletsprojects.com/en/2.0.x/quickstart/>
