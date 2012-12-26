tutorial README
==================

Getting Started
---------------

- cd <directory containing this file>

- $venv/bin/python setup.py develop

- $venv/bin/populate_tutorial development.ini

- $venv/bin/pserve development.ini


Load csv file to postgres
\copy swanglish(siswati_version, english_version) from /home/sanele/Desktop/swang.csv with delimiter ',' csv;


create table

CREATE TABLE swanglish (
    id bigserial primary key,
    siswati_version varchar(255),
    english_version varchar(255),
    created timestamp default now()
);
