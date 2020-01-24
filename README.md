# VIT-RM-Organizer
A python script to organize a directory having Reference material of teachers.
.
# Features
<ol>
  <li>
   The tool sorts DA's and syllabus and other non-reference material into seperate folder. Outside the root SEMESTER directory
  </li>
  <li>
    The tool doesn't rename the files, so they can be re-sorted if they are ever misplaced.
  </li>
</ol>  



# Future Features
<ul>
  <li>Course code being automatically being replaced by the name of the course.</li>
  <li>The class number being replaced by the name of the teacher.</li>
  <li>The materials being sorted by the date of lecture, followed by the reference number and the lesson.</li>
</ul>


# Constraints
<ul>
<li>If the file names are chaged from the once used by the VTOP Resource manager,the tool will not recognize the file as a reference material.</li>
 </ul>

# How to make it work on linux?
step 1. mkdir ~/bin <br>
step 2. place vtool.py in ~/bin<br>
step 3. mv vtool.py vtool<br>
step 4. chmod 777 vtool<br>
step 5. echo "export PATH=\\$PATH:\\$HOME/bin" >> ~/.bashrc<br>
step 6. source .bashrc <br>
step 7. use the following command on any directory:  vtool "path-to-directory" <br>

# How to make it work on windows?
STEP 1. place vtool.py in the folder to organize and run it in python terminal ( the default open with option).<br>

# How to install on linux?
![](https://github.com/mayankkumar2/readmeFiles/raw/master/myimage.gif)

# How to use the tool on linux?
![](https://github.com/mayankkumar2/readmeFiles/raw/master/myimage2.gif)
