<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Financial Tracker Pro</title>

<style>
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:Arial,sans-serif;
}

body{
    background:#0f172a;
    color:white;
    padding:20px;
}

.container{
    max-width:1200px;
    margin:auto;
}

h1{
    text-align:center;
    margin-bottom:25px;
}

.summary{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
    gap:20px;
    margin-bottom:25px;
}

.card{
    padding:20px;
    border-radius:15px;
    text-align:center;
}

.income{background:#16a34a;}
.expenses{background:#dc2626;}
.balance{background:#2563eb;}

.card p{
    font-size:28px;
    margin-top:10px;
}

.form-box{
    background:#1e293b;
    padding:20px;
    border-radius:15px;
    margin-bottom:20px;
}

form{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(180px,1fr));
    gap:10px;
}

input,select,button{
    padding:12px;
    border:none;
    border-radius:10px;
}

button{
    background:#2563eb;
    color:white;
    cursor:pointer;
}

button:hover{
    opacity:.9;
}

#search{
    width:100%;
    margin-bottom:15px;
}

table{
    width:100%;
    border-collapse:collapse;
    background:#1e293b;
}

th,td{
    padding:15px;
    text-align:center;
}

th{
    background:#334155;
}

.delete-btn{
    background:#dc2626;
    color:white;
    border:none;
    padding:8px 12px;
    border-radius:8px;
    cursor:pointer;
}
</style>
</head>

<body>

<div class="container">

<h1>💰 Financial Tracker Pro</h1>

<div class="summary">
    <div class="card income">
        <h3>Total Income</h3>
        <p id="income">$0.00</p>
    </div>

    <div class="card expenses">
        <h3>Total Expenses</h3>
        <p id="expenses">$0.00</p>
    </div>

    <div class="card balance">
        <h3>Balance</h3>
        <p id="balance">$0.00</p>
    </div>
</div>

<div class="form-box">
    <h2>Add Transaction</h2>
    <br>

    <form id="transactionForm">
        <input type="text" id="description" placeholder="Description" required>

        <input type="number" id="amount" placeholder="Amount" step="0.01" required>

        <input type="date" id="date" required>

        <select id="type">
            <option value="income">Income</option>
            <option value="expense">Expense</option>
        </select>

        <button type="submit">Add Transaction</button>
    </form>
</div>

<input type="text" id="search" placeholder="Search transactions">

<table>
<thead>
<tr>
<th>Date</th>
<th>Description</th>
<th>Type</th>
<th>Amount</th>
<th>Delete</th>
</tr>
</thead>

<tbody id="transactionTable"></tbody>
</table>

</div>

<script>
const form = document.getElementById("transactionForm");
const table = document.getElementById("transactionTable");
const incomeEl = document.getElementById("income");
const expensesEl = document.getElementById("expenses");
const balanceEl = document.getElementById("balance");
const search = document.getElementById("search");

let transactions =
JSON.parse(localStorage.getItem("transactions")) || [];

function saveData(){
    localStorage.setItem(
        "transactions",
        JSON.stringify(transactions)
    );
}

function updateSummary(){

    let income = 0;
    let expenses = 0;

    transactions.forEach(t=>{
        if(t.type==="income"){
            income += t.amount;
        }else{
            expenses += t.amount;
        }
    });

    incomeEl.textContent =
        "$" + income.toFixed(2);

    expensesEl.textContent =
        "$" + expenses.toFixed(2);

    balanceEl.textContent =
        "$" + (income-expenses).toFixed(2);
}

function renderTransactions(filter=""){

    table.innerHTML="";

    transactions
    .filter(t =>
        t.description
        .toLowerCase()
        .includes(filter.toLowerCase())
    )
    .forEach((t,index)=>{

        const row=document.createElement("tr");

        row.innerHTML=`
            <td>${t.date}</td>
            <td>${t.description}</td>
            <td>${t.type}</td>
            <td>$${t.amount.toFixed(2)}</td>
            <td>
                <button class="delete-btn"
                onclick="deleteTransaction(${index})">
                Delete
                </button>
            </td>
        `;

        table.appendChild(row);
    });

    updateSummary();
}

function deleteTransaction(index){
    transactions.splice(index,1);
    saveData();
    renderTransactions();
}

form.addEventListener("submit",function(e){

    e.preventDefault();

    transactions.push({
        description:document.getElementById("description").value,
        amount:parseFloat(document.getElementById("amount").value),
        date:document.getElementById("date").value,
        type:document.getElementById("type").value
    });

    saveData();
    renderTransactions();
    form.reset();
});

search.addEventListener("input",function(){
    renderTransactions(this.value);
});

renderTransactions();
</script>

</body>
</html>