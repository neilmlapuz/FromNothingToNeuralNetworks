## 1\. Introduction

**1.1 Overview**  
The tool is an interactive Neural Network learning resource that will introduce the user to the subject of Neural Networks and guide them through a series of learning challenges accompanied by hands-on coding walkthroughs.
The tool will consist of a webapp which will provide the necessary learning material, visual aids, video tutorials, optional quizzes, and milestone programming exercises. The learning material will include a general introduction to Neural Networks, covering key concepts and terminology, a breakdown of the different types of Neural Networks with a particular focus on Deep Neural Networks. The material will be cumulative and work towards a set of learning goals. The learning material  will be supplemented with concrete examples and real world illustrations. There will be succinct run throughs of the mathematics where required.
We will then guide the user through some practical exercises in order to solidify understanding and give them an introduction into creating their own neural networks. 
We will create our own diagrams and visual aids in order to concretise abstract concepts and  further facilitate the user’s learning. We hope to add in optional quizzes at the end of certain topics in order to help the user retain the knowledge they have just learned.

The tool will provide a user that is already comfortable with programming and has a grasp of basic python with a comprehensive overview and introduction to Neural Networks, and experience creating Deep Neural Networks. The tool will also enable those that already have an understanding of Neural Networks and wish to gain some practical experience implementing their knowledge.
 

**1.2 Business Context**  
The project is not intended to return a profit, however, if monitisation was required, advertisment could be easily implemented into the site in a none intrusive manner.

**1.3 Glossary**  
* **Neural Network:** A series of algorithms that attempts to identify underlying relationships in a set of data by using a process that mimics the way the human brain operates.

* **Deep Neural Network:** Network composed of several layers of Neural Networks.

* **Keras:** An open source Neural Network library written in python.

* **AngularJS:** A JavaScript-based open source front-end web application framework.

* **Flask:** A micro web framework written in Python.

* **TenserFlow:** An open source software library for dataflow programming across a range of tasks.

* **GPU:** Graphical Processing Unit. This enables to render images more quickly.

## 2\. General Description

**2.1 Product/System Functions**
The general functionality of the Web application is to act as a learning resource for individuals seeking a better understanding of Neural Networks and a selfcontained introduction on the topic. The user will be provided with a comprehensive walkthrough on the knowledge and tools surrounding creation and implementation of Neural Network based programs. Additionally, diagrams and visual aids will be included in order to reinforce and supplement material where appropriate. After each core section of the learning material, there will be an optional quiz that the user can take in order to solidify the knowledge they just learned. The quiz contents will directly relate to the material covered in the completed section. This will help the user actively engage with the material and help reinforce their understanding. Upon completing all of the learning exercises and covering the material provided, the user should have a good grasp of Neural Networks and perhaps be motivated to go on to build a program of their own related to the material covered.

**2.2 User Characteristics and Objectives**
It is expected that the core user base of the Web App will be those that have a background in, or knowledge on, Computer Science and Linear Algebra. These individuals should have a desire to learn about Neural Networks and will consequently be our target user audience as we believe that we can cater best to their needs, and for whom our Web App is mainly structured. Given the hypothetical scenario, a computer science student is interested in building a program related to Neural Networks for a project but they don’t have the necessary knowledge or understanding of the concepts and tools required to build such a program. The Web App’s objective is to make such information easily accessible with a user-friendly interface and well presented, coherent content, providing the student a comprehensive view on Neural Networks. This content will help user to understand the logic behind Neural Networks and how to get started with building them. Additionally, the web app aims to help the user retain key concepts through the use of optional quizzes.

**2.3 Operational Scenarios**

![](https://i.imgur.com/oSm61Ho.png)

Since the Web App is a learning resource for those who are interested in acquiring an understanding on Neural Networks, we can see from the diagram above that there will be similar situations or scenarios in which the product will operate for most of the users that will be using the Web App. However, we have also identified that certain situations relating to how the user interacts with the web app could vary depending on the knowledge and background of the user. 

**User with background (Neural Networks, Comp sci, Linear Algebra):** 

This user is an individual who wants to refresh their knowledge on Neural Networks and is looking for a resource that can provide an encapsulated overview of the topic while providing relevant examples. This user has prior experience with Neural Networks and so depending on what they are looking for, they are quite likely to skip or glance through certain topics or exercises offered by the Web App and go straight to what they are need. 

* **Tour**
All users are able to tour the site to get a general feel for what material the web app has to offer. 

* **_Taking the quizzes_**
This aspect of the web app will help the more experienced users gauge how much they remember and can also give them a little refresher on the material they should know. 

**User with background (Comp Sci, Linear Algebra):** 

This user will most likely be an individual that is currently studying Computer Science, will have covered the basics of Linear Algebra, and is interested in learning about Neural Networks. Considering that they have little to no prior experience with Neural Networks, they are the ideal user for this learning tool as they will benefit most from its use. The learning resource will enable the user to build a solid foundation of understanding on which they will be able to expand in the future.

* **_The Lessons_** 
They will be structured in progressive manner, meaning that each lesson will logically follow on from the last one, allowing the user to slowly construct a more wholesome understanding on Neural Networks. If the lessons were not structured correctly, the user could easily become confused and subject to misconceptions. 

* **_Taking the quizzes_** 
Optional quizzes are recommended for this user as they will allow the user to ensure that they fully understand the core concepts and retain the knowledge from the section that precedes the quiz. 

**User with background (Comp Sci):** 

This user is an individual with a background in Computer Science and is keen to learn about Neural Networks but has no knowledge concerning Linear Algebra. The user is encouraged to try all aspects of the learning tool, however, there will be points at which Linear Algebra related terms and/or concepts will be referred to and used to explain certain aspects of Neural Networks. The user may have difficulties understanding these aspects as the tool does not provide an overview of Linear Algebra. As a result, the user may have to visit external sources to procure the required knowledge on Linear Algebra in order to get the most out of the learning tool and what it has to offer.

**User with no background:**  

This user is an individual who is browsing the web and happens to stumble upon across the Web App. Although the user has no background in Computer Science, this user could browse around the site and have a little read on the introduction to Neural Networks and play around with the in- browser hand written recognition program. The user could then either be motivated to do a course on Computer Science or casually leave the site, fascinated.

**2.4 Constraints**
Below is a list of possible constraints that we might face; 

* **Knowledge concerning libraries**  
Since the libraries that we will be using are very substantial, we won’t be able to cover all of the functionalities that they have to offer. In the end, we won’t be experts on the libraries, however, we will have gained invaluable experience learning how to leverage certain functionalities they have to offer. 

* **Web App Cross Platform Usability**  
Bearing in mind that this project is the kind where there is a great deal of research involved, particularly when starting from a reference point of no prior knowledge, time could be a problem. This means that we might not have the time to enable our web app to function smoothly on a range of platforms. 

* **Access to adequate computing power**  
Many of the more advanced program examples that we will be covering are much more computationally demanding, and as a result, will require a high-end GPU in order to train the program in a reasonable time frame. 

* **Training**  
In order to properly train a Neural Network, quite a lot of time is required as it is a very computationally intensive task. If we do not leave enough time to train our Neural Networks, they might not perform very well. 


## 3\. Functional Requirements

**3.1 Navigation**
* **Description**
    This section of the functionality relates to a user navigating the Web App. The user will be greeted with the homepage, on which there will be a short summary of the Web App's intended purpose. The user can then begin the lessons in their sequential order or visit whichever section they wish by using the navigation bar. The user should be able to navigate to any parts of the Web App at all times.
    
* **Criticality**
    Navgation is a critical function as without it the Web App would be rendered unusable and useless. The navigation should be both functional and intuitive at all times. If the user is hindered by the navigation in any way, it could take away from their learning experience and may even lead them to not want to use Web App.
    
* **Technical Issues**
    Considering that there will be many aspects and technologies going into the Web App, HTML, CSS, AngularJS, Flask, in browser python terminal, we think that there is a possibility that we might have trouble intgrating all of the elements into one seamless product. There will be many things to take into account and we will have to plan very carefully.
    
    
    
**3.2 Lessons**
* **Description**
    This is for a user that has decided that they will use the Web App to learn about Neural Networks. This function will be come in the form of topics or sections. They will provide the user with the learning material and guide them through example program implementations from start to finish. At the end of each lesson there will be a button to proceed to the next section. Alternatively, for a user that has already started on a topic in a previous session, when they come back to resume the topic, they will be able to start off where they left off.
    
* **Criticality**
    Again this is another critical function as without it, the Web App becomes equally useless. This function should help the user to understand and build Neural Networks in a logical manner. If the lessons are not structured in an easily accessible and comprehendsible manner, the user will not get much use out of the Web App and possible leave having learned very little. If the user finds they did not learn much from the Web App, then they will be unlikely to tell others about it and increase it's exposure. We want the contents of our lessons to be logical, easy to follow and engaging.

* **Technical Issue**
    It will be important to ensure that all elements of the lessons are correctly implemented and working fully.


**3.3 Optional Quizzes**
* **Description**
    At the end of most sections, the user will be given a choice to take an optional quiz. This quiz will be related to the section that the user has covered.

* **Criticality**
    This function is not necessarily critial to the Web App as its omission will not prevent the tool from working. However, the quizzes add to the user experience by making the too more interactive and giving the user the option to review that they know. We believe that for a user to effectively learn, they should be encouraged to review their understanding of a topic.
    
* **Technical Issue**
    It is important to ensure that the questions are unambiguous and do not confuse the user.
    
* **Dependencies with other requirements**
    This function is dependent on the lessons of our Web App as the questions asked in the quizzes will directly relate to the materal covered in the lessons.

**3.4 Hand Written Number Recognition Program**
* **Description**
    This function will serve as an example of what the user can build after learning about Neural Networks. It  will consist of an in browser window on which the user will be able to draw a number, the number will be sent to a trained Neural Network as an input and it will output the correct number onto the browser in plain text. The user will have options submit a number to the program and the option to clear the window. 
    
* **Criticality**
    This functionn is not critial to the operation of the Web App. However, without it, the contents of the Web App could appear to be quite bland and boring. We hope that it will impress the user and motivate them to want to learn about Neural Networks and explore the similar programs applied to different problems.
    
* **A Technical Issue**
    A key issue relating to this function is the scenario in which the user draws something that does not resemble any number into the window and the program will not be able to determine what it is forcing it to output the number it "thinks" resembles it closest. The program will trained to recognise positive integers but not trained to determine whether the input is an integer or not.


## 4\. System Architecture

**4.1 Web Application System Architechture Diagram**

![](https://i.imgur.com/2rjfwCq.jpg)


Above **Fig 4.1** shows a Web Application system architecture diagram. This illustrates how a Web Browser client makes requests to a Web App on the internet and how the server responds accordingly. 


**4.2 System Architechture Diagram**

![](https://i.imgur.com/VAYlrPf.jpg)




In **Fig 4.2** above, it illustrates the architechtural system of the Web App. Here we can see how the whole system operates, showing the distribution of functions across the system, and the modules that we will be using. 

**4.2.1 Web App**
The Web App will be made using AngularJS and this will support the front end of the system architechture of the product. This is what the user will predominantly interact with as this is where the contents of the learning material will be presented. 


**4.2.2 In-Browser Progams**
The programs that will work in-browser and allow the user to interact with them, they will be written in python and supported by Flask. The hand written number recognition program for example, will take a hand written integer drawn in the browser window of the Web App, pass it as an input to the pre-trained Neural Network and output the number in plain text to the browers. Additionally, Flask will be used for the quizzes that the user will have the option of taking.

**4.2.3 Flask Web Framework**
The programs will be wrapped with the Flask Web Framework so that they can interact with the Web App as intended.



**4.2.4 Trained Network**
The Trained Neural Network will be the module of the system that processes the input data from the In Browser Program (Hand Written Number Recognition) and outputs the desired result that was drawn in.
 

## 5\. High-Level Design

For our high-level design of the system, we provided a system model using SSADM principles to present the overall system and how it interacts with external entities. 

**Fig 5.1 System Context flow Diagram**

![](https://i.imgur.com/a3ZTUfx.jpg)

**Fig 5.1** above shows a context flow diagram of the system. This shows how the Web App interacts and passes information between its external entities such a user, flask application and administator.


## 6\. Preliminary Schedule

**6.1 Overview**
The following task list and chart was designed using Microsoft Project. It provides an initial approach of the project plan. The schedule that we have planned for ourselves for this project is what we hope we actually get done on the specified dates. We are hoping to finish our product in around 2-3 weeks before the submission date to do some testing and write out the user/tech manual for the project.

![](https://i.imgur.com/VjOyeaW.jpg)
<center><small>Fig 6.2 Preliminary Schedule</small></center>


In **Fig 6.2**, the tasks list shows the list of tasks that we plan for our project, the duration it will take and the start and finish time. 

![](https://i.imgur.com/8enPKk7.jpg)
<center><small>Fig 6.3 Gannt Chart</small></center>


In the other window in **Fig 6.3**, it shows us a visual representation of our task list as a Gantt Chart. This clearly illustrates how some of the task in the project will require a lot of time to be completed and therefore, they have to be broken down to several sub-task. 



## 7\. Appendices

**7.1 Appendix 1 - Resources**
* **Research Tools**
    * https://www.youtube.com/
    * https://www.tensorflow.org/
    * https://keras.io/
    * https://www.w3schools.com/
    * https://www.tutorialspoint.com/flask/
    * http://searchnetworking.techtarget.com/definition/neural-network
    * https://sebastianraschka.com/faq/docs/logisticregr-neuralnet.html
    * https://machinelearningmastery.com/gradient-descent-for-machine-learning/


**7.2 Appendix 2 - References**
* www.google.com
* https://www.webopedia.com/