CREATE DATABASE company_database;
USE company_database;

CREATE TABLE IF NOT EXISTS departments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

INSERT INTO departments (name) VALUES
('HR'),
('Engineering'),
('Sales'),
('Marketing');

CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department_id INT,
    email VARCHAR(255),
    salary DECIMAL(10,2),
    FOREIGN KEY (department_id) REFERENCES departments(id)
);

INSERT INTO employees (name, department_id, email, salary) VALUES
('Alice Johnson', 1, 'alice@company.com', 5000.00),
('Bob Smith', 2, 'bob@company.com', 7000.00),
('Charlie Brown', 2, 'charlie@company.com', 6500.00),
('Diana Prince', 3, 'diana@company.com', 5500.00),
('Ethan Hunt', 4, 'ethan@company.com', 6000.00);

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2)
);

INSERT INTO products (name, price) VALUES
('Laptop', 1200.00),
('Mouse', 25.00),
('Keyboard', 45.00),
('Monitor', 300.00),
('Chair', 150.00);

CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    employee_id INT,
    order_total DECIMAL(10,2),
    order_date DATE,
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);

INSERT INTO orders (customer_name, employee_id, order_total, order_date) VALUES
('John Doe', 1, 1250.00, '2025-09-01'),
('Jane Smith', 2, 1325.00, '2025-09-05'),
('Acme Corp', 3, 2500.00, '2025-09-10'),
('Globex Inc', 4, 1800.00, '2025-09-12'),
('Bob’s Burgers', 5, 750.00, '2025-09-15');
