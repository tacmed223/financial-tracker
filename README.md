<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Financial Tracker</title>
  <link rel="stylesheet" href="styles.css" />
</head>
<body>
  <div class="app-shell">
    <header class="app-header">
      <div>
        <h1>Financial Tracker</h1>
        <p>Track income, expenses, and savings in one place.</p>
      </div>
      <div class="summary-cards">
        <div class="card income-card">
          <span>Income</span>
          <strong id="income-value">$0.00</strong>
        </div>
        <div class="card expense-card">
          <span>Expenses</span>
          <strong id="expense-value">$0.00</strong>
        </div>
        <div class="card balance-card">
          <span>Balance</span>
          <strong id="balance-value">$0.00</strong>
        </div>
      </div>
    </header>

    <main>
      <section class="add-transaction">
        <h2>Add Transaction</h2>
        <form id="transaction-form">
          <div class="form-grid">
            <label>
              Description
              <input id="description" type="text" placeholder="e.g. Grocery, Salary" required />
            </label>
            <label>
              Amount
              <input id="amount" type="number" step="0.01" placeholder="e.g. 45.00" required />
            </label>
            <label>
              Date
              <input id="date" type="date" required />
            </label>
            <label>
              Type
              <select id="type" required>
                <option value="income">Income</option>
                <option value="expense">Expense</option>
              </select>
            </label>
          </div>
          <button type="submit" class="primary-btn">Add Transaction</button>
        </form>
      </section>

      <section class="transaction-list">
        <div class="list-header">
          <h2>Transactions</h2>
          <div class="filters">
            <input id="search" type="search" placeholder="Search description" />
            <select id="filter-type">
              <option value="all">All</option>
              <option value="income">Income</option>
              <option value="expense">Expenses</option>
            </select>
          </div>
        </div>
        <div class="table-wrapper">
          <table>
            <thead>
              <tr>
                <th>Date</th>
                <th>Description</th>
                <th>Type</th>
                <th>Amount</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody id="transaction-table"></tbody>
          </table>
        </div>
      </section>
    </main>
  </div>

  <script src="script.js"></script>
</body>
</html>
