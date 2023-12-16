let num1 = Math.floor(Math.random() * 5 + 1);
let num2 = Math.floor(Math.random() * 5 + 1);

let answer = num1 * num2;

document.getElementById("problem").innerHTML = "What is " + num1 + " * " + num2 + "?";

document.getElementById("submit").onclick = function(){
    userAnswer = document.getElementById("userGuess").value;
    userAnswer = Number(userAnswer);
    if (answer === userAnswer){
        document.getElementById("response").innerHTML = "Correct!";
    } else{
        document.getElementById("response").innerHTML = "Incorrect. The correct answer is " + answer + ". You answered: " + userAnswer;
    }
}

document.getElementById("newNum").onclick = function(){
    num1 = Math.floor(Math.random() * 5 + 1);
    num2 = Math.floor(Math.random() * 5 + 1);
    answer = num1 * num2
    document.getElementById("problem").innerHTML = "What is " + num1 + " * " + num2 + "?";
    document.getElementById("response").innerHTML = "";

}