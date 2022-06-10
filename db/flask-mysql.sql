-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jun 10, 2022 at 04:12 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.0.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flask-mysql`
--

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(4) UNSIGNED ZEROFILL NOT NULL,
  `nama` varchar(100) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `nama`, `username`, `password`) VALUES
(0038, 'gege', 'gege', 'gege'),
(0039, 'gege', 'gege', 'gege'),
(0040, 'gege', 'gege', 'gege'),
(0041, 'gege', 'gege', 'gege'),
(0042, 'gege', 'gege', 'gege'),
(0043, 'gege', 'gege', 'gege'),
(0044, 'gege', 'gege', 'gege'),
(0045, 'gege', 'gege', 'gege'),
(0046, 'gege', 'gege', 'gege'),
(0047, 'gege', 'gege', 'gege'),
(0048, 'gege', 'gege', 'gege'),
(0049, 'gege', 'gege', 'gege'),
(0050, 'gege', 'gege', 'gege'),
(0051, 'gege', 'gege', 'gege'),
(0052, 'gege', 'gege', 'gege'),
(0053, 'gege', 'gege', 'gege'),
(0054, 'gege', 'gege', 'gege'),
(0055, 'gege', 'gege', 'gege'),
(0056, 'gege', 'gege', 'gege'),
(0057, 'gogo', 'gogo', 'gogo'),
(0058, 'gege', 'gege', 'gege'),
(0059, 'gege', 'gege', 'gege'),
(0062, 'gege', 'gege', 'gege'),
(0063, 'gege', 'gege', 'gege'),
(0064, 'gege', 'gege', 'gege'),
(0065, 'gege', 'gege', 'gege'),
(0066, 'gege', 'gege', 'gege');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(4) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=67;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
