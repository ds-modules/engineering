# Engineering 7 in Python Notebooks

This project is a proof of concept to convert the assignments of the Berkeley Engineering 7 course, which is currently taught in MATLAB, into a series of Jupyter Notebooks. Engineering 7 is a freshman-level introduction to programming for scientists and engineering students.

Our goal is to revamp the course materials to be fully python based, so that new students will have a more interactive and intutive experience in an open-source language. With Jupyter notebooks, students do not need to worry about the scaffolding of creating seperate files for every function, and can read and solve problems directly in one place. Instead, they can focus on learning the fundamentals of programming and writing the actual code itself, all managed in one place. Python and Jupyter Notebooks are also open-source and free to use, and also more extendable to future computer science and coding projects compared to MATLAB. For data science purposes, Jupyter notebooks are incredibly convient, as they support rendering of visuals directly in the notebook, which can be updated along with code.


## Structure

The repo is split between the 2016 and 2017 ENGIN-7 assignments, and currently we are focused on finishing the 2016 version. The raw python code is created in PyCharm, so the folders is structued for that IDE. Each lab will contain the MATLAB problems in PDF, some MATLAB helper files, a .py file with raw python solutions, and a .ipynb file that will be the completed notebook.


## Current Progress
- [ ] 2016
	- [x] Converting the MATLAB assingments into raw python code
		- [x] Lab 1-5
		- [x] Lab 6-7
		- [x] Lab 8 (besides last question)
		- [x] Lab 9-12
	- [x] Translating the MATLAB PDF assignments into markdown and LaTeX in the Jupyter notebook
		- [x] Lab 1-12
	- [x] Finishing soluton notebooks with finished python code
		- [x] Lab 1-4
		- [x] Lab 5-12
	- [ ] Writing autograders for each notebook with Python `unittest`s
	- [ ] Polishing the notebooks and creating student notebooks
		- Replace markdown pictures with html, and make nice captions
		- replace vectors with \mathbf{} font
		- fix wording for lists/vectors/arrays
		- make sure MATLAB remnants are replaced with python
			- especially headers
		- add equation numbers where needed
		- update bigo to \mathcal{O}
		- space equation numbers using \qquad\qquad
		- how to deal with classes

- [ ] 2017
	- Development halted


### Contact
Daniel Ho: daniel.ho at berkeley.edu if you have any questions!