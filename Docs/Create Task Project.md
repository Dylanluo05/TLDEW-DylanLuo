{% include Navbar.html %}

# Create Task Project #
## Project Description: ##
**Achievement Journey.** For this year's College Board Create Task Project, I am planning on progamming an application that helps students, particularly high school students, with planning out their school life and managing their time in order to have effective and useful learning, as well as to become successful students.

* #### Program Purpose: Create an application that helps students manage their time by assiting them in having adequete and sustainable productivity.
* #### Input: The user can create a to-do list, in which they can list out their activities within time frams as well as by levels of priority and importance. 
* #### Lists: The to-do list elements will be stored in organized, ordered, and displayed sequences, and will be available for view to the users.
* #### Procedure: When a user logs on to the Achievement Journey, they will be able start planning their goals for school as well as for their future(e.g. Universities and Colleges, Career, Etc.). They will also have the ability to create daily to-do lists, in which they can organize their tasks, jobs, and events into specific times, as well as be able to assign rankings to the elements of their to-do lists and sort them in order of priority.
* #### Parameters: The inputs of users will be displayed on the Achievement Journey website, and the presented items will be sorted by the preference of users.
* #### Iteration: Users are able to repeatedly add elements to their to-do lists and goals planner. Users can also choose to create daily tasks,which will continuously reappear on their designated to-do lists once a new day starts.
* #### Output: After creating their to-do list(s) and outlines for their goals and aspirations, users will be to view all of the elements that they had made with ease, since there will be labels that will help them navigate through the website to view their to-do lists and plans for their dreams.
* #### Sequencing: Sequencing will be primarily be shown in the Python code and CRUD programming system.

## Two Program Code Snippets: ##
Code Snippet #1:

```
<body>

<div class="topnav">
    <a input type="button" onClick="document.getElementById('AJBackground1').scrollIntoView();" style = "color: black;">Home</a>
    <a input type="button" onClick="document.getElementById('AJBackground2').scrollIntoView();" style = "color: black;">To-Do List</a>
    <a input type="button" onClick="document.getElementById('AJBackground3').scrollIntoView();" style = "color: black;">Dream Planner</a>
    <a input type="button" onClick="document.getElementById('').scrollIntoView();" style = "color: black;">Coming Soon...</a>
    <div class="search-container" style = "position:relative; left:7px;">
        <form autocomplete="off" action="/action_page.php">
            <div class="autocomplete" style="width:300px; color:black;">
                <input id="myInput" type="text" name="myAchievementSearch" placeholder="Search">
            </div>
            <button type="submit" onClick="document.getElementById('AJBackground2').scrollIntoView();"><i class="fa fa-search"></i></button>
        </form>
    </div>
</div>

<div id = "AJBackground1">
    <h1>Achievement Journey</h1>
    <h4>Create to-do lists for everyday tasks, as well as plan out all of your goals and dreams</h4>
</div>

<div id = "AJBackground2">
    <div id="myDIV" class="header" style = "position: relative; text-align: center; top: -100px;">
        <h2 style="margin:5px">To-Do List</h2>
        <input type="text" id="myInput2" placeholder="Title...">
        <span onclick="newElement()" class="addBtn">Add</span>
    </div>
    <ul id="myUL" style = "position: relative; text-align: center; top: -100px;">
    </ul>
</div>

<div id = "AJBackground3">
    <h1 style = "position: relative; text-align: center; color: white;">Record The Progression For Your Dreams</h1>
    <div class="timeline" style = "position: relative; text-align: center;">
        <div class="containertimeline left">
            <div class="content">
                <div class="container">
                    <form action="/action_page.php">
                        <div class="row">
                            <div class="col-25">
                                <label for="title1">Goal</label>
                            </div>
                            <div class="col-75">
                                <input type="text" id="title1" name="goaltitle" placeholder="Title">
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-25">
                                <label for="finishingdate1">Finishing Date</label>
                            </div>
                            <div class="col-75">
                                <input type="datetime-local" placeholder="Date and Time" id="finishingdate1" required name="date" value="2022-02-14T11:11"> <!-- AM -->
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-25">
                                <label for="description1">Description</label>
                            </div>
                            <div class="col-75">
                                <textarea id="description1" name="goaldescription" placeholder="Describe Your Aspiration" style="height:200px"></textarea>
                            </div>
                        </div>
                        <div class="row">
                            <button type="button" class="btn btn-two" id = "CreateGoal1" style = "position: relative; left: 100px; top: 24px; color: royalblue;">Integrate Goal</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
        <div class="containertimeline right">
            <div class="content">
                <div class="container">
                    <form action="/action_page.php">
                        <div class="row">
                            <div class="col-25">
                                <label for="title2">Goal</label>
                            </div>
                            <div class="col-75">
                                <input type="text" id="title2" name="goaltitle" placeholder="Title">
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-25">
                                <label for="finishingdate2">Finishing Date</label>
                            </div>
                            <div class="col-75">
                                <input type="datetime-local" placeholder="Date and Time" id="finishingdate2" required name="date" value="2022-02-14T11:11"> <!-- AM -->
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-25">
                                <label for="description2">Description</label>
                            </div>
                            <div class="col-75">
                                <textarea id="description2" name="goaldescription" placeholder="Describe Your Aspiration" style="height:200px"></textarea>
                            </div>
                        </div>
                        <div class="row">
                            <button type="button" class="btn btn-two" id = "CreateGoal2" style = "position: relative; left: 100px; top: 24px; color: royalblue;">Integrate Goal</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
```

Code Snippet #2:

```
<script>
    /* To-Do List */
    var myNodelist = document.getElementsByTagName("LI");
    var i;
    for (i = 0; i < myNodelist.length; i++) {
        var span = document.createElement("SPAN");
        var txt = document.createTextNode("\u00D7");
        span.className = "close";
        span.appendChild(txt);
        myNodelist[i].appendChild(span);
    }

    // Click on a close button to hide the current list item
    var close = document.getElementsByClassName("close");
    var i;
    for (i = 0; i < close.length; i++) {
        close[i].onclick = function() {
            var div = this.parentElement;
            div.style.display = "none";
        }
    }

    // Add a "checked" symbol when clicking on a list item
    var list = document.querySelector('ul');
    list.addEventListener('click', function(ev) {
        if (ev.target.tagName === 'LI') {
            ev.target.classList.toggle('checked');
        }
    }, false);


    function newElement() {
        var li = document.createElement("li");
        var inputValue = document.getElementById("myInput2").value;
        var t = document.createTextNode(inputValue);
        li.appendChild(t);
        if (inputValue === '') {
            alert("You must write something!");
        } else {
            document.getElementById("myUL").appendChild(li);
        }
        document.getElementById("myInput2").value = "";

        var span = document.createElement("SPAN");
        var txt = document.createTextNode("\u00D7");
        span.className = "close";
        span.appendChild(txt);
        li.appendChild(span);

        for (i = 0; i < close.length; i++) {
            close[i].onclick = function() {
                var div = this.parentElement;
                div.style.display = "none";
            }
        }
    }

    /* Dream Progression 1 */
    const CreateGoal1 = document.getElementById('CreateGoal1');

    CreateGoal1.addEventListener('click', () => {
        CreateGoal1.style.display = 'none';
    })

    /* Dream Progression 2 */
    const CreateGoal2 = document.getElementById('CreateGoal2');

    CreateGoal2.addEventListener('click', () => {
        CreateGoal2.style.display = 'none';
    })

    /* Dream Progression 3 */
    const CreateGoal3 = document.getElementById('CreateGoal3');

    CreateGoal3.addEventListener('click', () => {
        CreateGoal3.style.display = 'none';
    })

    /* Dream Progression 4 */
    const CreateGoal4 = document.getElementById('CreateGoal4');

    CreateGoal4.addEventListener('click', () => {
        CreateGoal4.style.display = 'none';
    })

    /* Dream Progression 5 */
    const CreateGoal5 = document.getElementById('CreateGoal5');

    CreateGoal5.addEventListener('click', () => {
        CreateGoal5.style.display = 'none';
    })

    /* Dream Progression 6 */
    const CreateGoal6 = document.getElementById('CreateGoal6');

    CreateGoal6.addEventListener('click', () => {
        CreateGoal6.style.display = 'none';
    })

    /* Dream Progression 7 */
    const CreateGoal7 = document.getElementById('CreateGoal7');

    CreateGoal7.addEventListener('click', () => {
        CreateGoal7.style.display = 'none';
    })

</script>
```

## The Create Task Project Written Responses: ##
