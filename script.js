const versions = {
    1: {
        title: "Version 1.0",
        badge: "Basic Arithmetic",
        supportsMemory: false,
        supportsHistory: false,
        operations: [
            { key: "add", label: "Add", a: "First Number", b: "Second Number" },
            { key: "subtract", label: "Subtract", a: "First Number", b: "Second Number" },
            { key: "multiply", label: "Multiply", a: "First Number", b: "Second Number" },
            { key: "divide", label: "Divide", a: "First Number", b: "Second Number" }
        ]
    },
    2: {
        title: "Version 2.0",
        badge: "Advanced Operations",
        supportsMemory: false,
        supportsHistory: false,
        operations: [
            { key: "add", label: "Add", a: "First Number", b: "Second Number" },
            { key: "subtract", label: "Subtract", a: "First Number", b: "Second Number" },
            { key: "multiply", label: "Multiply", a: "First Number", b: "Second Number" },
            { key: "divide", label: "Divide", a: "First Number", b: "Second Number" },
            { key: "power", label: "Power", a: "Base", b: "Exponent" },
            { key: "squareRoot", label: "Square Root", a: "Number", single: true },
            { key: "percentage", label: "Percentage", a: "Number", b: "Percent" }
        ]
    },
    3: {
        title: "Version 3.0",
        badge: "Memory and History",
        supportsMemory: true,
        supportsHistory: true,
        operations: [
            { key: "add", label: "Add", a: "First Number", b: "Second Number" },
            { key: "subtract", label: "Subtract", a: "First Number", b: "Second Number" },
            { key: "multiply", label: "Multiply", a: "First Number", b: "Second Number" },
            { key: "divide", label: "Divide", a: "First Number", b: "Second Number" },
            { key: "power", label: "Power", a: "Base", b: "Exponent" },
            { key: "squareRoot", label: "Square Root", a: "Number", single: true }
        ]
    },
    4: {
        title: "Version 4.0",
        badge: "Scientific Calculator",
        supportsMemory: true,
        supportsHistory: true,
        operations: [
            { key: "add", label: "Add", a: "First Number", b: "Second Number" },
            { key: "subtract", label: "Subtract", a: "First Number", b: "Second Number" },
            { key: "multiply", label: "Multiply", a: "First Number", b: "Second Number" },
            { key: "divide", label: "Divide", a: "First Number", b: "Second Number" },
            { key: "power", label: "Power", a: "Base", b: "Exponent" },
            { key: "squareRoot", label: "Square Root", a: "Number", single: true },
            { key: "sine", label: "Sine", a: "Angle (Degrees)", single: true },
            { key: "cosine", label: "Cosine", a: "Angle (Degrees)", single: true },
            { key: "tangent", label: "Tangent", a: "Angle (Degrees)", single: true },
            { key: "logarithm", label: "Logarithm (Base 10)", a: "Number", single: true },
            { key: "naturalLog", label: "Natural Log", a: "Number", single: true },
            { key: "factorial", label: "Factorial", a: "Whole Number", single: true }
        ]
    }
};

const state = {
    version: 1,
    result: 0,
    memory: 0,
    history: []
};

const versionTitle = document.getElementById("version-title");
const featureBadge = document.getElementById("feature-badge");
const versionGrid = document.getElementById("version-grid");
const operationSelect = document.getElementById("operation-select");
const labelA = document.getElementById("label-a");
const labelB = document.getElementById("label-b");
const fieldB = document.getElementById("field-b");
const inputA = document.getElementById("input-a");
const inputB = document.getElementById("input-b");
const calculateBtn = document.getElementById("calculate-btn");
const resultDisplay = document.getElementById("result-display");
const resultExpression = document.getElementById("result-expression");
const memoryValue = document.getElementById("memory-value");
const memoryNote = document.getElementById("memory-note");
const historyList = document.getElementById("history-list");
const memoryAddBtn = document.getElementById("memory-add-btn");
const memorySubtractBtn = document.getElementById("memory-subtract-btn");
const memoryRecallBtn = document.getElementById("memory-recall-btn");
const memoryClearBtn = document.getElementById("memory-clear-btn");
const clearHistoryBtn = document.getElementById("clear-history-btn");

function formatNumber(value) {
    if (typeof value !== "number" || Number.isNaN(value)) {
        return String(value);
    }

    if (Number.isInteger(value)) {
        return value.toString();
    }

    return value.toFixed(8).replace(/\.?0+$/, "");
}

function getActiveVersion() {
    return versions[state.version];
}

function setVersion(version) {
    state.version = version;
    const config = getActiveVersion();

    versionTitle.textContent = config.title;
    featureBadge.textContent = config.badge;
    memoryNote.textContent = config.supportsMemory
        ? "Memory functions are active for this version."
        : "Memory features unlock in Version 3.0 and above.";

    [...versionGrid.querySelectorAll(".version-tile")].forEach((button) => {
        button.classList.toggle("active", Number(button.dataset.version) === version);
    });

    operationSelect.innerHTML = "";
    config.operations.forEach((operation) => {
        const option = document.createElement("option");
        option.value = operation.key;
        option.textContent = operation.label;
        operationSelect.appendChild(option);
    });

    updateOperationFields();
    renderHistory();
    updateMemoryControls();
}

function updateOperationFields() {
    const config = getActiveVersion();
    const operation = config.operations.find((item) => item.key === operationSelect.value) || config.operations[0];

    labelA.textContent = operation.a;
    inputA.placeholder = `Enter ${operation.a.toLowerCase()}`;

    if (operation.single) {
        fieldB.classList.add("hidden");
        inputB.value = "";
    } else {
        fieldB.classList.remove("hidden");
        labelB.textContent = operation.b;
        inputB.placeholder = `Enter ${operation.b.toLowerCase()}`;
    }
}

function addHistoryEntry(entry) {
    if (!getActiveVersion().supportsHistory) {
        return;
    }

    state.history.unshift(entry);
    renderHistory();
}

function renderHistory() {
    const supportsHistory = getActiveVersion().supportsHistory;
    historyList.innerHTML = "";

    if (!supportsHistory) {
        const item = document.createElement("li");
        item.className = "history-empty";
        item.textContent = "History unlocks in Version 3.0 and above.";
        historyList.appendChild(item);
        return;
    }

    if (state.history.length === 0) {
        const item = document.createElement("li");
        item.className = "history-empty";
        item.textContent = "No calculations yet.";
        historyList.appendChild(item);
        return;
    }

    state.history.forEach((entry) => {
        const item = document.createElement("li");
        item.textContent = entry;
        historyList.appendChild(item);
    });
}

function updateMemoryControls() {
    const enabled = getActiveVersion().supportsMemory;
    [memoryAddBtn, memorySubtractBtn, memoryRecallBtn, memoryClearBtn].forEach((button) => {
        button.disabled = !enabled;
        button.style.opacity = enabled ? "1" : "0.45";
        button.style.cursor = enabled ? "pointer" : "not-allowed";
    });
    memoryValue.textContent = `Memory: ${formatNumber(state.memory)}`;
}

function parseInput(input, label) {
    if (input === "") {
        throw new Error(`${label} is required.`);
    }

    const value = Number(input);
    if (Number.isNaN(value)) {
        throw new Error(`${label} must be a valid number.`);
    }
    return value;
}

function runCalculation() {
    const operation = operationSelect.value;

    try {
        const a = parseInput(inputA.value, labelA.textContent);
        const b = fieldB.classList.contains("hidden") ? null : parseInput(inputB.value, labelB.textContent);
        let result;
        let expression;

        switch (operation) {
            case "add":
                result = a + b;
                expression = `${formatNumber(a)} + ${formatNumber(b)} = ${formatNumber(result)}`;
                break;
            case "subtract":
                result = a - b;
                expression = `${formatNumber(a)} - ${formatNumber(b)} = ${formatNumber(result)}`;
                break;
            case "multiply":
                result = a * b;
                expression = `${formatNumber(a)} × ${formatNumber(b)} = ${formatNumber(result)}`;
                break;
            case "divide":
                if (b === 0) {
                    throw new Error("Cannot divide by zero.");
                }
                result = a / b;
                expression = `${formatNumber(a)} ÷ ${formatNumber(b)} = ${formatNumber(result)}`;
                break;
            case "power":
                result = a ** b;
                expression = `${formatNumber(a)} ^ ${formatNumber(b)} = ${formatNumber(result)}`;
                break;
            case "squareRoot":
                if (a < 0) {
                    throw new Error("Square root of a negative number is undefined.");
                }
                result = Math.sqrt(a);
                expression = `√${formatNumber(a)} = ${formatNumber(result)}`;
                break;
            case "percentage":
                result = (a * b) / 100;
                expression = `${formatNumber(b)}% of ${formatNumber(a)} = ${formatNumber(result)}`;
                break;
            case "sine":
                result = Math.sin((a * Math.PI) / 180);
                expression = `sin(${formatNumber(a)}°) = ${formatNumber(result)}`;
                break;
            case "cosine":
                result = Math.cos((a * Math.PI) / 180);
                expression = `cos(${formatNumber(a)}°) = ${formatNumber(result)}`;
                break;
            case "tangent":
                result = Math.tan((a * Math.PI) / 180);
                expression = `tan(${formatNumber(a)}°) = ${formatNumber(result)}`;
                break;
            case "logarithm":
                if (a <= 0) {
                    throw new Error("Logarithm is only defined for numbers greater than zero.");
                }
                result = Math.log10(a);
                expression = `log(${formatNumber(a)}) = ${formatNumber(result)}`;
                break;
            case "naturalLog":
                if (a <= 0) {
                    throw new Error("Natural log is only defined for numbers greater than zero.");
                }
                result = Math.log(a);
                expression = `ln(${formatNumber(a)}) = ${formatNumber(result)}`;
                break;
            case "factorial":
                if (a < 0 || !Number.isInteger(a)) {
                    throw new Error("Factorial requires a non-negative whole number.");
                }
                result = factorial(a);
                expression = `${formatNumber(a)}! = ${formatNumber(result)}`;
                break;
            default:
                throw new Error("Please choose a valid operation.");
        }

        state.result = result;
        resultDisplay.textContent = formatNumber(result);
        resultExpression.textContent = expression;
        addHistoryEntry(expression);
        updateMemoryControls();
    } catch (error) {
        resultExpression.textContent = error.message;
    }
}

function factorial(value) {
    let total = 1;
    for (let i = 2; i <= value; i += 1) {
        total *= i;
    }
    return total;
}

versionGrid.addEventListener("click", (event) => {
    const button = event.target.closest(".version-tile");
    if (!button) {
        return;
    }
    setVersion(Number(button.dataset.version));
});

operationSelect.addEventListener("change", updateOperationFields);
calculateBtn.addEventListener("click", runCalculation);

memoryAddBtn.addEventListener("click", () => {
    if (!getActiveVersion().supportsMemory) {
        return;
    }
    state.memory += state.result;
    resultExpression.textContent = `Added ${formatNumber(state.result)} to memory.`;
    updateMemoryControls();
});

memorySubtractBtn.addEventListener("click", () => {
    if (!getActiveVersion().supportsMemory) {
        return;
    }
    state.memory -= state.result;
    resultExpression.textContent = `Subtracted ${formatNumber(state.result)} from memory.`;
    updateMemoryControls();
});

memoryRecallBtn.addEventListener("click", () => {
    if (!getActiveVersion().supportsMemory) {
        return;
    }
    state.result = state.memory;
    resultDisplay.textContent = formatNumber(state.memory);
    resultExpression.textContent = `Recalled memory value ${formatNumber(state.memory)}.`;
});

memoryClearBtn.addEventListener("click", () => {
    if (!getActiveVersion().supportsMemory) {
        return;
    }
    state.memory = 0;
    resultExpression.textContent = "Memory cleared.";
    updateMemoryControls();
});

clearHistoryBtn.addEventListener("click", () => {
    state.history = [];
    renderHistory();
    resultExpression.textContent = "History cleared.";
});

setVersion(1);
