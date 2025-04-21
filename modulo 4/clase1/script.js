// Elementos del DOM
const settingsContainer = document.querySelector('.settings');
const gameContainer = document.querySelector('.game-container');
const resultsContainer = document.querySelector('.results');

const difficultySelect = document.getElementById('difficulty');
const operationCheckboxes = {
    suma: document.getElementById('suma'),
    resta: document.getElementById('resta'),
    multiplicacion: document.getElementById('multiplicacion'),
    division: document.getElementById('division')
};

const startBtn = document.getElementById('start-btn');
const submitBtn = document.getElementById('submit-btn');
const nextBtn = document.getElementById('next-btn');
const endBtn = document.getElementById('end-btn');
const playAgainBtn = document.getElementById('play-again-btn');

const num1Element = document.getElementById('num1');
const num2Element = document.getElementById('num2');
const operatorElement = document.getElementById('operator');
const answerInput = document.getElementById('answer');
const feedbackElement = document.getElementById('feedback');
const scoreElement = document.getElementById('score');
const timeElement = document.getElementById('time');
const finalScoreElement = document.getElementById('final-score');
const problemsSolvedElement = document.getElementById('problems-solved');
const problemsWrongElement = document.getElementById('problems-wrong');

// Estado del juego
let gameState = {
    score: 0,
    time: 60,
    problemsSolved: 0,
    problemsWrong: 0,
    currentProblem: null,
    timer: null,
    isGameActive: false
};

// Configuración de dificultad
const difficultySettings = { 
    easy: {
        max: 10,
        min: 1,
        divisionMaxDivisor: 5,
        points: 1
    },
    medium: {
        max: 50,
        min: 10,
        divisionMaxDivisor: 10,
        points: 2
    },
    hard: {
        max: 100,
        min: 20,
        divisionMaxDivisor: 20,
        points: 3
    }
};

// Iniciar juego
startBtn.addEventListener('click', startGame);

// Verificar respuesta
submitBtn.addEventListener('click', checkAnswer);
answerInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        checkAnswer();
    }
});

// Siguiente problema
nextBtn.addEventListener('click', generateProblem);

// Terminar juego
endBtn.addEventListener('click', endGame);

// Jugar de nuevo
playAgainBtn.addEventListener('click', resetGame);

// Función para iniciar el juego
function startGame() {
    // Verificar que al menos una operación está seleccionada
    const hasSelectedOperation = Object.values(operationCheckboxes).some(checkbox => checkbox.checked);
    
    if (!hasSelectedOperation) {
        alert('Por favor, selecciona al menos una operación');
        return;
    }
    
    // Inicializar estado del juego
    gameState.score = 0;
    gameState.time = 60;
    gameState.problemsSolved = 0;
    gameState.problemsWrong = 0;
    gameState.isGameActive = true;
    
    // Actualizar UI
    scoreElement.textContent = '0';
    timeElement.textContent = '60';
    
    // Mostrar la sección de juego
    settingsContainer.style.display = 'none';
    gameContainer.style.display = 'block';
    resultsContainer.style.display = 'none';
    
    // Generar el primer problema
    generateProblem();
    
    // Iniciar temporizador
    gameState.timer = setInterval(() => {
        gameState.time--;
        timeElement.textContent = gameState.time;
        
        if (gameState.time <= 0) {
            endGame();
        }
    }, 1000);
    
    // Enfocar el campo de respuesta
    answerInput.focus();
}

// Función para generar un problema matemático
function generateProblem() {
    const difficulty = difficultySelect.value;
    const settings = difficultySettings[difficulty];
    
    // Determinar qué operaciones están seleccionadas
    const availableOperations = [];
    if (operationCheckboxes.suma.checked) availableOperations.push('+');
    if (operationCheckboxes.resta.checked) availableOperations.push('-');
    if (operationCheckboxes.multiplicacion.checked) availableOperations.push('*');
    if (operationCheckboxes.division.checked) availableOperations.push('/');
    
    // Seleccionar una operación aleatoria
    const operation = availableOperations[Math.floor(Math.random() * availableOperations.length)];
    
    // Generar números según la operación y dificultad
    let num1, num2, result;
    
    switch (operation) {
        case '+':
            num1 = getRandomNumber(settings.min, settings.max);
            num2 = getRandomNumber(settings.min, settings.max);
            result = num1 + num2;
            break;
        case '-':
            num1 = getRandomNumber(settings.min, settings.max);
            num2 = getRandomNumber(settings.min, Math.min(num1, settings.max));
            result = num1 - num2;
            break;
        case '*':
            num1 = getRandomNumber(settings.min, Math.min(settings.max / 2, 12));
            num2 = getRandomNumber(settings.min, Math.min(settings.max / 2, 12));
            result = num1 * num2;
            break;
        case '/':
            // Para división, generamos primero el divisor (num2)
            num2 = getRandomNumber(2, settings.divisionMaxDivisor);
            // Luego generamos un resultado entero
            const quotient = getRandomNumber(settings.min, settings.max / num2);
            // Calculamos el dividendo (num1)
            num1 = quotient * num2;
            result = num1 / num2;
            break;
    }
    
    // Mostrar problema en la UI
    num1Element.textContent = num1;
    num2Element.textContent = num2;
    operatorElement.textContent = getOperatorSymbol(operation);
    answerInput.value = '';
    feedbackElement.textContent = '';
    feedbackElement.className = 'feedback';
    
    // Guardar problema actual
    gameState.currentProblem = {
        num1,
        num2,
        operation,
        result,
        points: settings.points
    };
    
    // Ocultar botón siguiente
    nextBtn.style.display = 'none';
    submitBtn.style.display = 'inline-block';
    
    // Enfocar el campo de respuesta
    answerInput.focus();
}

// Función para verificar la respuesta
function checkAnswer() {
    if (!gameState.isGameActive) return;
    
    const userAnswer = parseFloat(answerInput.value);
    
    if (isNaN(userAnswer)) {
        feedbackElement.textContent = 'Por favor, ingresa un número';
        feedbackElement.className = 'feedback incorrect';
        return;
    }
    
    const correctAnswer = gameState.currentProblem.result;
    
    // Verificar si la respuesta es correcta
    if (Math.abs(userAnswer - correctAnswer) < 0.001) { // Tolerancia para divisiones
        feedbackElement.textContent = '¡Correcto!';
        feedbackElement.className = 'feedback correct';
        gameState.score += gameState.currentProblem.points;
        gameState.problemsSolved++;
        scoreElement.textContent = gameState.score;
    } else {
        feedbackElement.textContent = `Incorrecto. La respuesta correcta es ${correctAnswer}`;
        feedbackElement.className = 'feedback incorrect';
        gameState.problemsWrong++;
    }
    
    // Mostrar botón siguiente
    submitBtn.style.display = 'none';
    nextBtn.style.display = 'inline-block';
}

// Función para terminar el juego
function endGame() {
    clearInterval(gameState.timer);
    gameState.isGameActive = false;
    
    // Actualizar resultados finales
    finalScoreElement.textContent = gameState.score;
    problemsSolvedElement.textContent = gameState.problemsSolved;
    problemsWrongElement.textContent = gameState.problemsWrong;
    
    // Mostrar pantalla de resultados
    gameContainer.style.display = 'none';
    resultsContainer.style.display = 'block';
}

// Función para reiniciar el juego
function resetGame() {
    resultsContainer.style.display = 'none';
    settingsContainer.style.display = 'block';
}

// Función para obtener un número aleatorio entre min y max
function getRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Función para convertir el operador interno a símbolo
function getOperatorSymbol(operator) {
    switch (operator) {
        case '+': return '+';
        case '-': return '-';
        case '*': return '×';
        case '/': return '÷';
    }
} 