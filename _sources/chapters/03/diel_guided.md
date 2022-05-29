(h1:03:diel_guided)=
# Guided practice with dielectric data

Here's one idea for a sequence of programming tasks that you can explore today. 💡
Once again, these are just _suggestions_ and you don't have to get through everything today.
We have plenty of time left to complete these tasks, which you surely will do.

1\) Create a new Python notebook in [the DataHub](https://datahub.berkeley.edu)! 
We recommend creating it in a sensible location (like `mi-book-2022/my-work`) so you can easily find it in the future.

2\) Start with creating a Markdown cell (like all of the tutorial notebooks) explaining what this notebook is about.
You may want to have a [Markdown cheat sheet](https://www.markdownguide.org/cheat-sheet) handy for stylizing your Markdown cells.

3\) Then, in a Code cell(s), see if you can write some Python code to make a simple query to the Materials Project.
This will involve importing some Python packages, loading your API key, and constructing the query syntax.
Feel free to reference previous notebooks or ask for help if you get stuck!

4\) Now make a query for _just_ the materials with the dielectric properties already computed.
There's some 7000 of these.
You already did this yesterday, so this is to practice recall.

5\) **Challenge**: Write some more code to extract all the relevant dielectric properties of these materials and store them into a DataFrame, kinda like this:
```{image} ../../assets/fig/03/diel_df_example.png
:alt: diel_df_example
:width: 50%
:align: center
```
Essentially, we're asking you to convert data from JSON to tabular format.

6\) Can you save this DataFrame as a CSV file so you can easily access it later?

7\) Next, consider what _other_ properties you'll also want to get out of the Materials Project.
Maybe the band gap? How about density?
Modify the query to include these properties as well, and add them to the DataFrame.
- Note: For this step, and to give you a mental **break from coding**, we invite you to explore the [Materials Project UI](https://materialsproject.org/).
Click around and see what cool things you find!

8\) **Challenge**: Can you get structural information about your materials?
How would you save such information?
Note that with this step you may run out of memory (oof) and you'll have to look up ways to save a DataFrame as a binary file.

9\) **Challenge**: What _other_ properties relevant to the design of dielectric materials are important to consider and that we might obtain from another data source?
This step is incredibly open-ended.
