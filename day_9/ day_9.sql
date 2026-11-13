
CREATE TABLE department (
    department_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL UNIQUE
);


CREATE TABLE designation (
    designation_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    designation_name VARCHAR(100) NOT NULL UNIQUE
);


CREATE TABLE manager (
    manager_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    manager_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE
);


CREATE TABLE employee (
    employee_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    age INTEGER CHECK (age >= 18),
    salary NUMERIC(12, 2) NOT NULL CHECK (salary >= 0),
    department_id INTEGER NOT NULL REFERENCES department(department_id),
    designation_id INTEGER NOT NULL REFERENCES designation(designation_id),
    manager_id INTEGER REFERENCES manager(manager_id)
);



INSERT INTO department (department_name)
VALUES
('Software Development'),
('Data Engineering'),
('Human Resources'),
('Finance'),
('Marketing'),
('Sales'),
('Operations'),
('Information Technology'),
('Cyber Security'),
('Quality Assurance');

INSERT INTO designation (designation_name)
VALUES
('Software Engineer'),
('Data Engineer'),
('HR Manager'),
('Finance Manager'),
('Marketing Executive'),
('Sales Executive'),
('Operations Manager'),
('DevOps Engineer'),
('Security Engineer'),
('QA Engineer');



INSERT INTO manager (manager_name, email)
VALUES
('Amit Sharma', 'amit@company.com'),
('Priya Singh', 'priya@company.com'),
('Rahul Verma', 'rahul@company.com'),
('Neeraj Kumar', 'neeraj@company.com'),
('Anjali Gupta', 'anjali@company.com'),
('Vivek Sharma', 'vivek@company.com'),
('Pooja Verma', 'pooja@company.com'),
('Rakesh Singh', 'rakesh@company.com'),
('Karan Mehta', 'karan@company.com'),
('Sneha Kapoor', 'sneha@company.com');




INSERT INTO employee
(employee_name, email, age, salary,
 department_id, designation_id, manager_id)
VALUES
('Rohit Singh', 'rohit@company.com', 22, 60000, 2, 2, 1),
('Neha Gupta', 'neha@company.com', 24, 55000, 1, 1, 1),
('Arjun Kumar', 'arjun@company.com', 25, 58000, 2, 2, 1),
('Kavya Sharma', 'kavya@company.com', 28, 65000, 3, 3, 2),
('Vikas Verma', 'vikas@company.com', 30, 70000, 4, 4, 3),
('Ankit Yadav', 'ankit@company.com', 23, 50000, 5, 5, 4),
('Simran Kaur', 'simran@company.com', 26, 52000, 6, 6, 5),
('Aditya Mehta', 'aditya@company.com', 27, 68000, 8, 8, 6),
('Nisha Patel', 'nisha@company.com', 29, 72000, 9, 9, 7),
('Manish Gupta', 'manish@company.com', 31, 62000, 10, 10, 8);


SELECT * FROM department;

SELECT * FROM designation;

SELECT * FROM manager;

SELECT * FROM employee;



SELECT
    e.employee_id,
    e.employee_name,
    e.email AS employee_email,
    e.age,
    e.salary,
    d.department_name,
    ds.designation_name,
    m.manager_name,
    m.email AS manager_email
FROM employee e
JOIN department d
    ON e.department_id = d.department_id
JOIN designation ds
    ON e.designation_id = ds.designation_id
LEFT JOIN manager m
    ON e.manager_id = m.manager_id
ORDER BY e.employee_id;



-- Q1
-- How many employees are currently working in the company?
SELECT COUNT(*) AS total_employees
FROM employee;


-- Q2
-- What is the total salary expense of the company?
SELECT SUM(salary) AS total_salary_expense
FROM employee;


-- Q3
-- What is the average salary of employees?
SELECT AVG(salary) AS average_salary
FROM employee;


-- Q4
-- What is the highest salary currently offered?
SELECT MAX(salary) AS highest_salary
FROM employee;


-- Q5
-- What is the lowest salary currently offered?
SELECT MIN(salary) AS lowest_salary
FROM employee;


-- Q6
-- Which employees earn more than 60000?
SELECT employee_name, salary
FROM employee
WHERE salary > 60000;


-- Q7
-- Which employees are older than 25?
SELECT employee_name, age
FROM employee
WHERE age > 25;


-- Q8
-- Which employees earn between 50000 and 70000?
SELECT employee_name, salary
FROM employee
WHERE salary BETWEEN 50000 AND 70000;


-- Q9
-- Which employees work in the Data Engineering department?
SELECT employee_name
FROM employee
WHERE department_id = 2;


-- Q10
-- Who are the top 3 highest-paid employees?
SELECT employee_name, salary
FROM employee
ORDER BY salary DESC
LIMIT 3;


-- Q11
-- Who are the youngest employees in the company?
SELECT employee_name, age
FROM employee
ORDER BY age ASC
LIMIT 3;


-- Q12
-- Which employees have a salary above the company average?
SELECT employee_name, salary
FROM employee
WHERE salary > (
    SELECT AVG(salary)
    FROM employee
);


-- Q13
-- How many employees are there in each department?
SELECT department_id, COUNT(*) AS employee_count
FROM employee
GROUP BY department_id;


-- Q14
-- What is the total salary expense for each department?
SELECT department_id, SUM(salary) AS total_salary
FROM employee
GROUP BY department_id;


-- Q15
-- What is the average salary in each department?
SELECT department_id, AVG(salary) AS average_salary
FROM employee
GROUP BY department_id;


-- Q16
-- What is the highest salary in each department?
SELECT department_id, MAX(salary) AS highest_salary
FROM employee
GROUP BY department_id;


-- Q17
-- What is the lowest salary in each department?
SELECT department_id, MIN(salary) AS lowest_salary
FROM employee
GROUP BY department_id;


-- Q18
-- Which departments have more than 1 employee?
SELECT department_id, COUNT(*) AS employee_count
FROM employee
GROUP BY department_id
HAVING COUNT(*) > 1;


-- Q19
-- Which departments have an average salary above 55000?
SELECT department_id, AVG(salary) AS average_salary
FROM employee
GROUP BY department_id
HAVING AVG(salary) > 55000;


-- Q20
-- Which departments have a total salary expense above 100000?
SELECT department_id, SUM(salary) AS total_salary
FROM employee
GROUP BY department_id
HAVING SUM(salary) > 100000;


-- Q21
-- How many employees report to each manager?
SELECT manager_id, COUNT(*) AS employee_count
FROM employee
GROUP BY manager_id
ORDER BY employee_count DESC;


-- Q22
-- Which managers have more than 1 employee reporting to them?
SELECT manager_id, COUNT(*) AS employee_count
FROM employee
GROUP BY manager_id
HAVING COUNT(*) > 1;


-- Q23
-- Which employees report to Amit Sharma?
SELECT
    e.employee_name,
    m.manager_name
FROM employee e
JOIN manager m
    ON e.manager_id = m.manager_id
WHERE m.manager_name = 'Amit Sharma';


-- Q24
-- Which employees work in each department?
SELECT
    e.employee_name,
    d.department_name
FROM employee e
JOIN department d
    ON e.department_id = d.department_id;


-- Q25
-- What designation does each employee have?
SELECT
    e.employee_name,
    des.designation_name
FROM employee e
JOIN designation des
    ON e.designation_id = des.designation_id;


-- Q26
-- Which employees earn more than 60000 and work in Data Engineering?
SELECT
    e.employee_name,
    e.salary,
    d.department_name
FROM employee e
JOIN department d
    ON e.department_id = d.department_id
WHERE e.salary > 60000
  AND d.department_name = 'Data Engineering';


-- Q27
-- Which employee has the highest salary in the company?
SELECT employee_name, salary
FROM employee
WHERE salary = (
    SELECT MAX(salary)
    FROM employee
);


-- Q28
-- Which department has the highest total salary expense?
SELECT
    d.department_name,
    SUM(e.salary) AS total_salary
FROM employee e
JOIN department d
    ON e.department_id = d.department_id
GROUP BY d.department_name
ORDER BY total_salary DESC
LIMIT 1;


-- Q29
-- How many employees are working under each manager?
SELECT
    m.manager_name,
    COUNT(e.employee_id) AS employee_count
FROM manager m
JOIN employee e
    ON m.manager_id = e.manager_id
GROUP BY m.manager_name
ORDER BY employee_count DESC;


-- Q30
-- Which departments have more than 1 employee and what is their average salary?
SELECT
    d.department_name,
    COUNT(e.employee_id) AS employee_count,
    AVG(e.salary) AS average_salary
FROM employee e
JOIN department d
    ON e.department_id = d.department_id
GROUP BY d.department_name
HAVING COUNT(e.employee_id) > 1;

-- Q31
-- Who are all the employees currently working in the company?
SELECT *
FROM employee;


-- Q32
-- What department and designation does each employee have?
SELECT
    e.employee_name,
    d.department_name,
    des.designation_name,
    e.salary
FROM employee e
JOIN department d
    ON e.department_id = d.department_id
JOIN designation des
    ON e.designation_id = des.designation_id;





