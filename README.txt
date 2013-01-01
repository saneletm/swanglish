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
  *******************************************
CREATE TABLE swanglish (
    id bigserial primary key,
    siswati_version varchar(255),
    english_version varchar(255),
    created timestamp default now()
);


Rules for translating:
*******************************************
  English to Siswati
  englih, type, siswati, siswati, siswati ...
  ',' seperate translations
  ';' seperate (n,v, adv) translations
  '()' are used for prefixes that can differ a lot,
                    (explanations)

 '/' are used for or

