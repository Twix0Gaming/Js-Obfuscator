// A simple test program
function startTest() {
    console.log("Welcome to the JavaScript Test!");
    console.log("Answer the following questions:");

    // Question 1
    let question1 = prompt("What is 5 + 3?");
    if (question1 == "8") {
        console.log("Correct! 5 + 3 is 8.");
    } else {
        console.log("Oops! The correct answer is 8.");
    }

    // Question 2
    let question2 = prompt("What is the capital of France?");
    if (question2.toLowerCase() == "paris") {
        console.log("Correct! The capital of France is Paris.");
    } else {
        console.log("Oops! The correct answer is Paris.");
    }

    // Question 3
    let question3 = prompt("What is the square root of 16?");
    if (question3 == "4") {
        console.log("Correct! The square root of 16 is 4.");
    } else {
        console.log("Oops! The correct answer is 4.");
    }

    // Final message
    console.log("Thanks for taking the test! Try again to improve your score.");
}

// Start the test
startTest();
