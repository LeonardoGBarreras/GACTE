<?php

$host = "localhost";
$user = "postgres";
$password = "3946";
$dbname = "GACTE";

$con = pg_connect ("host=$host dbname=$dbname user=$user password=$password");

if (!$con){
    die("Connection failed")
}