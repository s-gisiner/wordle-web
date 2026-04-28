async function startGame(filename) {
    const response = await fetch(`/static/game/words/${filename}`);
    const text = await response.text();
    
    words = text.split('\n').map(w => w.trim().toUpperCase()).filter(w => w.length === 5);
    
    targetWord = words[Math.floor(Math.random() * words.length)];
    console.log("Original target word:", targetWord);
    targetWord = targetWord.normalize("NFD").replace(/\p{Diacritic}/gu, "");
    console.log("Target word:", targetWord);
    
    resetBoard();
}

function resetBoard() {
    attempts = 0;

    const board = document.getElementById("game-board");
    board.innerHTML = "";

    for (let i = 0; i < 6; i++) {
        const row = document.createElement("div");
        row.className = "game-row";
        row.id = `row-${i}`;

        for (let j = 0; j < 5; j++) {
            const tile = document.createElement("div");
            tile.className = "tile"; // Base styling
            row.appendChild(tile);
        }

        board.appendChild(row);
    }

    const input = document.getElementById("guess-input");
    input.value = "";
    input.hidden = false;
    input.focus();

    const submitButton = document.getElementById("submit-guess");
    submitButton.hidden = false;
}

function handleSubmission(){
    let word = document.getElementById("guess-input").value;
    
    if (word.length !== 5) {
        alert("Please enter a 5-letter word.");
        document.getElementById("guess-input").value = "";
        return;
    }

    word = word.normalize("NFD").replace(/\p{Diacritic}/gu, "");

    const letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
    word = word.toUpperCase();
    for (let i = 0; i < word.length; i++) {
        if (!letters.includes(word[i])) {
            alert("Please enter a valid 5-letter word.");
            document.getElementById("guess-input").value = "";
            return;
        }
    }

    if (!words.includes(word)) {
        alert("Word not in list. Please try again.");
        document.getElementById("guess-input").value = "";
        return;
    }

    document.getElementById("guess-input").value = "";

    const result = new Array(5).fill("gray");
    const targetArr = targetWord.split("");
    const guessArr = word.split("");

    for (let i = 0; i < 5; i++) {
        if (guessArr[i] === targetArr[i]) {
            result[i] = "green";
            targetArr[i] = null;
        }
    }

    for (let i = 0; i < 5; i++) {
        if (result[i] !== "green" && targetArr.includes(guessArr[i])) {
            result[i] = "yellow";
            targetArr[targetArr.indexOf(guessArr[i])] = null;
        }
    }

    const currentRow = document.getElementById(`row-${attempts}`);

    const tiles = currentRow.getElementsByClassName("tile");

    guessArr.forEach((letter, i) => {
        const tile = tiles[i];
        
        tile.textContent = letter;
        
        tile.classList.add(result[i]);
        
        tile.style.transitionDelay = `${i * 100}ms`;
    });

    if(word === targetWord) {
        alert("Congratulations! You've guessed the word!");
        document.getElementById("guess-input").hidden = true;
        document.getElementById("submit-guess").hidden = true;
    } else if (attempts === 5) {
        alert(`Game Over! The word was: ${targetWord}`);
        document.getElementById("guess-input").hidden = true;
        document.getElementById("submit-guess").hidden = true;
    }

    attempts++;
}

window.startGame = startGame;