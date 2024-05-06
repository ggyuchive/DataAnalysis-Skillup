# Write your MySQL query statement below
select Ea.name as Employee from Employee as Ea join Employee as Eb on Ea.managerId = Eb.id
where Ea.salary > Eb.salary;