import psycopg2 
week = psycopg2.connect(dbname = 'exam', user = 'myexam', password = '1234', host = 'localhost', port = '5432')
cursor = week.cursor()
week.autocommit = True


#cursor.execute('create table countries(id serial primary key,name varchar , regionid int)')
# cursor.execute('alter table countries add column contryid varchar')
# print('таблица есть')

# conn = [('AR', 'Argentina', '2'),('AU', 'Australia', '3'),
# ('BE', 'Belgium', '1'),
# ('BR', 'Brazil', '2'),
# ('CA', 'Canada', '2'),
# ('CH', 'Switzerland', '1'),
# ('CN', 'China', '3'),
# ('DE', 'Germany', '1'),
# ('DK', 'Denmark', '1'),
# ('EG', 'Egypt', '4'),
# ('FR', 'France', '1'),
# ('HK', 'HongKong', '3'),
# ('IL', 'Israel', '4'),
# ('IN', 'India', '3'),
# ('IT', 'Italy', '1'),
# ('JP', 'Japan', '3'),]

# cursor.executemany('insert into countries(contryid,name, region) values (%s, %s, %s)', conn)
# cursor.execute('select * from countries')
# print(cursor.fetchall())

# cursor.close()
# week.close()

# cursor.execute('create table departments(id serial primary key,department_name varchar ,department_name varchar, location_id varchar)')
# print('таблица есть')
# dep =('10', 'Administration', '200', '1700'),
# ('20', 'Marketing', '201', '1800'),
# ('30', 'Purchasing', '114', '1700'),
# ('40', 'Human Resources', '203', '2400'),
# ('50', 'Shipping', '121', '1500'),
# ('60', 'IT', '103', '1400'),
# ('70', 'Public Relations', '204', '2700'),
# ('80', 'Sales', '145', '2500'),
# ('90', 'Executive', '100', '1700'),
# ('100', 'Finance', '108', '1700'),
# ('110', 'Accounting', '205', '1700'),
# ('120', 'Treasury', '0', '1700'),
# ('130', 'Corporate Tax', '0', '1700'),
# ('140', 'Control And Credit', '0', '1700'),
# ('150', 'Shareholder Services', '0', '1700'),
# ('160', 'Benefits', '0', '1700'),
# ('170', 'Manufacturing', '0', '1700'),
# ('180', 'Construction', '0', '1700'),
# ('190', 'Contracting', '0', '1700'),
# ('200', 'Operations', '0', '1700')

# cursor.executemany('insert into departments(department_name, department_name, locationid )values (%s, %s, %s, %s)', dep)
# cursor.execute('select * from departments')
# print(cursor.fetchall())
# cursor.close()
# week.close()

# cursor.execute('create table employees(id serial primary key, first_name varchar, last_name varchar, email varchar, phone_num varchar, hire_date varchar, job_id varchar, salary varchar, comission_pct varchar, mananger_id varchar, department_id varchar)')
# print('таблица есть')

baztable =('101', 'Neena', 'Kochhar', 'NKOCHHAR', '515.123.4568', '1987-06-18', 'AD_VP', '17000.00', '0.00', '100', '90'),
('102', 'Lex', 'De Haan', 'LDEHAAN', '515.123.4569', '1987-06-19', 'AD_VP', '17000.00', '0.00', '100', '90'),
('103', 'Alexander', 'Hunold', 'AHUNOLD', '590.423.4567', '1987-06-20', 'IT_PROG', '9000.00', '0.00', '102', '60'),
('104', 'Bruce', 'Ernst', 'BERNST', '590.423.4568', '1987-06-21', 'IT_PROG', '6000.00', '0.00', '103', '60'),
('105', 'David', 'Austin', 'DAUSTIN', '590.423.4569', '1987-06-22', 'IT_PROG', '4800.00', '0.00', '103', '60'),
('106', 'Valli', 'Pataballa', 'VPATABAL', '590.423.4560', '1987-06-23', 'IT_PROG', '4800.00', '0.00', '103', '60'),
('107', 'Diana', 'Lorentz', 'DLORENTZ', '590.423.5567', '1987-06-24', 'IT_PROG', '4200.00', '0.00', '103', '60'),
('108', 'Nancy', 'Greenberg', 'NGREENBE', '515.124.4569', '1987-06-25', 'FI_MGR', '12000.00', '0.00', '101', '100'),
('109', 'Daniel', 'Faviet', 'DFAVIET', '515.124.4169', '1987-06-26', 'FI_ACCOUNT', '9000.00', '0.00', '108', '100'),
('110', 'John', 'Chen', 'JCHEN', '515.124.4269', '1987-06-27', 'FI_ACCOUNT', '8200.00', '0.00', '108', '100'),
('111', 'Ismael', 'Sciarra', 'ISCIARRA', '515.124.4369', '1987-06-28', 'FI_ACCOUNT', '7700.00', '0.00', '108', '100'),
('112', 'Jose Manuel', 'Urman', 'JMURMAN', '515.124.4469', '1987-06-29', 'FI_ACCOUNT', '7800.00', '0.00', '108', '100'),
('113', 'Luis', 'Popp', 'LPOPP', '515.124.4567', '1987-06-30', 'FI_ACCOUNT', '6900.00', '0.00', '108', '100'),
('114', 'Den', 'Raphaely', 'DRAPHEAL', '515.127.4561', '1987-07-01', 'PU_MAN', '11000.00', '0.00', '100', '30'),
('115', 'Alexander', 'Khoo', 'AKHOO', '515.127.4562', '1987-07-02', 'PU_CLERK', '3100.00', '0.00', '114', '30'),
('116', 'Shelli', 'Baida', 'SBAIDA', '515.127.4563', '1987-07-03', 'PU_CLERK', '2900.00', '0.00', '114', '30')

#cursor.executemany('insert into employees(id,first_name, last_name, email, phone_num, hire_date,job_id, salary, comission_pct, mananger_id,department_id) values (%s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s)',baztable)
#cursor.execute('select first_name, last_name from employees')
#cursor.execute('select * from employees')
#cursor.execute('select * from employees order by first_name desc')
#cursor.execute('select * from employees order by salary asc')
#cursor.execute('select sum (first_name)from employees')
#cursor.execute('select * from employees where salary between '10000' and '15000')')
# cursor.execute('update select first_name, last_name from employees')
#cursor.execute('select hire_date from employees') 
#cursor.execute('SELECT EXTRACT(mounth from 3 month ::interval)')
#cursor.execute('SELECT EXTRACT(MONTH FROM 3 month INTERVAL ' )
#cursor.execute('select * job_id where department_id=90, DOY FROM TIMESTAMP hire_date where department_id=90 ,from employees')
#cursor.execute('select min (salary) from employees')
#cursor.execute('select avg (salary), count (*)from employees where department_id=90 ')
cursor.execute()



print(cursor.fetchall())
cursor.close()
week.close()

