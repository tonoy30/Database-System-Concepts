create table doctor (
	id serial not null unique,
	name varchar(20) not null,
	email varchar(20) unique not null,
	phone_number varchar(14) unique,
	degree varchar(40),
	address varchar(30),
	primary key (id, name, email, phone_number)
);

create table test (
	id int not null unique,
	test_name varchar(20) not null unique,
	price numeric(6, 2) not null,
	type varchar(10),
	description text,
	normal_value numeric(5, 1),
	upto_value numeric(5, 1),
	primary key (id, test_name, price)	
);
/*
 foreign key (test_name=test, ref_by=doctor.id)
*/

create table patient (
	id serial not null unique,
	patient_name varchar(20) not null,
	patient_gender varchar(1) check (patient_gender in ('F', 'M', 'O')) not null,
	patient_age numeric(3) not null,
	phone_number varchar(14) unique not null,
	test_id int, 
	ref_by int,
	address varchar(30),
	speciman_type varchar(10),
	primary key (id, patient_name, phone_number, test_id, ref_by),
	foreign key (test_id) references test(id) on delete cascade,
	foreign key (ref_by) references doctor(id) on delete cascade
);

create table worker (
	id serial not null unique,
	name varchar(20),
	email varchar(20) unique not null,
	phone_number varchar(14) unique,
	address varchar(30),
	primary key (id, name, email, phone_number)
);

create table report(
	id serial not null,
	patient_id int,
	ref_by varchar(20),
	address varchar(30),
	speciman_type varchar(10),
	report_type varchar(30),
	test_id int ,
	doctor varchar(20) unique,
	worker varchar(20) unique,
	primary key (id, patient_id, test_id, doctor, worker),
	foreign key (patient_id) references patient(id),
	foreign key (test_id) references test(id)
);