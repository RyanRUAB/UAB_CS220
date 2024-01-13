function RockFunction() {
    let cpuinput = Math.floor(Math.random() * 3);
    switch (true) {
        case cpuinput == 0:
            document.getElementById("result").innerHTML = "You chose Rock. Computer chose Rock. It's a tie.";
            document.getElementById("result").style.color = "yellow"; 
            break;
        case cpuinput == 1:
            document.getElementById("result").innerHTML = "You chose Rock. Computer chose Paper. You lose.";
            document.getElementById("result").style.color = "red"; 
            break;
        case cpuinput == 2:
            document.getElementById("result").innerHTML = "You chose Rock. Computer chose Scissors. You Win!";
            document.getElementById("result").style.color = "greenyellow"; 
            break;
    }
}

function PaperFunction() {
    let cpuinput = Math.floor(Math.random() * 3);
    switch (true) {
        case cpuinput == 0:
            document.getElementById("result").innerHTML = "You chose Paper. Computer chose Rock. You Win!";
            document.getElementById("result").style.color = "greenyellow"; 
            break;
        case cpuinput == 1:
            document.getElementById("result").innerHTML = "You chose Paper. Computer chose Paper. It's a tie.";
            document.getElementById("result").style.color = "yellow"; 
            break;
        case cpuinput == 2:
            document.getElementById("result").innerHTML = "You chose Paper. Computer chose Scissors. You lose.";
            document.getElementById("result").style.color = "red"; 
            break;
    }
}

function ScissorsFunction() {
    let cpuinput = Math.floor(Math.random() * 3);
    switch (true) {
        case cpuinput == 0:
            document.getElementById("result").innerHTML = "You chose Scissors. Computer chose Rock. You lose.";
            document.getElementById("result").style.color = "red"; 
            break;
        case cpuinput == 1:
            document.getElementById("result").innerHTML = "You chose Scissors. Computer chose Paper. You Win!";
            document.getElementById("result").style.color = "greenyellow"; 
            break;
        case cpuinput == 2:
            document.getElementById("result").innerHTML = "You chose Scissors. Computer chose Scissors. It's a tie.";
            document.getElementById("result").style.color = "yellow"; 
            break;
    }
}