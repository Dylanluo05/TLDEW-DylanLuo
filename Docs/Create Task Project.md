{% include Navbar.html %}

# Create Task Project #
>  The Travel Recommendation Feature is essentially a type of Personality Quiz. Users will take a quiz that asks them questions about their personalities and ideal vacations. At the end, the quiz result will recommend users travel/vacation ideas that suit their personalities.
> >  Ex: Choose your preferred weather, types of foods, hobby → Recommended place shows up with details(image).
* #### Program Purpose: Create a page to give travel/vacation recommendations based on user selections and inputs.
* #### Input: The user can select quiz responses. 
* #### Lists: The quiz choices will be stored in ordered sequences of elements.
* #### Procedure: When a user goes to the Travel Recommendation page, they will be able to take a quiz that asks them questions about themselves(e.g. Their personalities and interests). Their responses will be stored in values, and at the end, these values will be added numerically. The quiz will then give a result that has a numerical range that the final numerical answer value is in.
* #### Parameters: Travel/Vacation spots are displayed after the user finishes the quiz.
* #### Iteration: Users are able to take the quiz multiple times.
* #### Output: After taking the quiz, users will be able to view their travel/vacation recommendation results based on their personalities.
* #### Sequencing: Sequencing will be primarily be shown in the JavaScript code.

# Two Code Snippets:
Code Snippet #1:

function loadPreviousQuestion() {
            currentQuestion--;
            score.pop();
            generateQuestions(currentQuestion);
        }

        function restartQuiz(e) {
            if(e.target.matches('button')) {
                currentQuestion = 0;
                score = [];
                location.reload();
            }

        }


        generateQuestions(currentQuestion);
        nextButton.addEventListener('click', loadNextQuestion);
        previousButton.addEventListener('click',loadPreviousQuestion);
        result.addEventListener('click',restartQuiz);

Code Snippet #2:

   let currentQuestion = 0;
        let score = [];
        let selectedAnswersData = [];
        const totalQuestions =questions.length;

        const container = document.querySelector('.quiz-container');
        const questionEl = document.querySelector('.question');
        const option1 = document.querySelector('.option1');
        const option2 = document.querySelector('.option2');
        const option3 = document.querySelector('.option3');
        const nextButton = document.querySelector('.next');
        const previousButton = document.querySelector('.previous');
        const restartButton = document.querySelector('.restart');
        const result = document.querySelector('.result');

        function generateQuestions (index) {

            const question = questions[index];
            const option1Total = questions[index].answer1Total;
            const option2Total = questions[index].answer2Total;
            const option3Total = questions[index].answer3Total;

            questionEl.innerHTML = `${index + 1}. ${question.question}`
            option1.setAttribute('data-total', `${option1Total}`);
            option2.setAttribute('data-total', `${option2Total}`);
            option3.setAttribute('data-total', `${option3Total}`);
            option1.innerHTML = `${question.answer1}`
            option2.innerHTML = `${question.answer2}`
            option3.innerHTML = `${question.answer3}`
        }
