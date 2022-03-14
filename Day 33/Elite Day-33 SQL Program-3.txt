/*Write an SQL query to display all the details of employees who are in sales dept 
and grade is 3.

Sample Output:
-------------
empno   ename   job       mgr     hiredate      sal      comm    deptno                                                  
7698    BLAKE   MANAGER   7839    1992-06-11    2850.00  NULL    30                                                      

*/

select * from emp where sal>=(select losal from salgrade where grade=3) and sal<=(select hisal from salgrade where grade=3) and deptno=(select deptno from dept where dname='SALES');
