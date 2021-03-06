# Data-Modeling-with-Postgres
Data Engineering Nanodegree Program

# Introduction
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

# Project Description
In this project, you'll apply what you've learned on data modeling with Postgres and build an ETL pipeline using Python. To complete the project, you will need to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.

# Python scripts

<a href="https://github.com/RashaAlamoud/Data-Modeling-with-Postgres/blob/main/create_tables.py">create_tables.py</a> : Clean previous schema and creates tables.

<a href="https://github.com/RashaAlamoud/Data-Modeling-with-Postgres/blob/main/sql_queries.py">sql_queries.py</a> : All queries used in the ETL pipeline.

<a href="https://github.com/RashaAlamoud/Data-Modeling-with-Postgres/blob/main/etl.py">etl.py</a> : Read JSON logs and JSON metadata and load the data into generated tables.



# Star Schema 
# Fact Table
songplays:Records in log data associated with song plays

# Dimension Table 
users: Users in the app

songs: Songs in music database

artists: Artists in music database

time: Timestamps of records in songplays broken down into specific units
