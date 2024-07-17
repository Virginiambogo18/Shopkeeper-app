<?php
session_start();
include 'db.php';

if ($_SESSION['user']['role'] != 'admin') {
    header("Location: login.php");
}

// Admin functionalities (CRUD for students, teachers, etc.)

?>