-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 01, 2025 at 01:55 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `wesagn`
--

-- --------------------------------------------------------

--
-- Table structure for table `adoption`
--

CREATE TABLE `adoption` (
  `ID` int(11) NOT NULL,
  `userid` varchar(50) DEFAULT NULL,
  `Name` varchar(100) DEFAULT NULL,
  `second_name` varchar(100) DEFAULT NULL,
  `surname` varchar(100) DEFAULT NULL,
  `nation` varchar(100) DEFAULT NULL,
  `rigion` varchar(100) DEFAULT NULL,
  `zone` varchar(100) DEFAULT NULL,
  `wereda` varchar(100) DEFAULT NULL,
  `datee` varchar(58) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `barth`
--

CREATE TABLE `barth` (
  `ID` int(11) NOT NULL,
  `userid` varchar(50) DEFAULT NULL,
  `actuale_birth_date` varchar(100) DEFAULT NULL,
  `nation` varchar(100) DEFAULT NULL,
  `rigion` varchar(100) DEFAULT NULL,
  `zone` varchar(100) DEFAULT NULL,
  `wereda` varchar(100) DEFAULT NULL,
  `datee` datetime DEFAULT NULL,
  `surname` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `deth`
--

CREATE TABLE `deth` (
  `ID` int(11) NOT NULL,
  `userid` varchar(50) DEFAULT NULL,
  `nation` varchar(100) DEFAULT NULL,
  `rigion` varchar(100) DEFAULT NULL,
  `zone` varchar(100) DEFAULT NULL,
  `wereda` varchar(100) DEFAULT NULL,
  `actuale_dath_date` varchar(50) DEFAULT NULL,
  `actuale_birth_date` varchar(50) DEFAULT NULL,
  `datee` datetime DEFAULT NULL,
  `surname` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `devorce`
--

CREATE TABLE `devorce` (
  `ID` int(11) NOT NULL,
  `userid` varchar(58) NOT NULL,
  `actuale_birth_date` varchar(58) NOT NULL,
  `wife_name` varchar(55) NOT NULL,
  `wife_second_name` varchar(55) NOT NULL,
  `wife_surname` varchar(55) NOT NULL,
  `date_of_Divorcce` varchar(58) NOT NULL,
  `Nationality` varchar(55) NOT NULL,
  `Region` varchar(55) NOT NULL,
  `zone` varchar(55) NOT NULL,
  `wereda` varchar(58) NOT NULL,
  `surname` varchar(55) NOT NULL,
  `datee` varchar(55) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `emp`
--

CREATE TABLE `emp` (
  `ID` int(11) NOT NULL,
  `jobid` varchar(50) DEFAULT NULL,
  `cret_empid` varchar(50) DEFAULT NULL,
  `stu` varchar(5) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `sname` varchar(100) DEFAULT NULL,
  `datee` datetime DEFAULT NULL,
  `pw` varchar(58) NOT NULL,
  `cellphone` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `job`
--

CREATE TABLE `job` (
  `ID` int(11) NOT NULL,
  `jobname` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `keble`
--

CREATE TABLE `keble` (
  `ID` int(11) NOT NULL,
  `kname` varchar(100) DEFAULT NULL,
  `manger_empid` varchar(100) DEFAULT NULL,
  `datee` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `keble`
--

INSERT INTO `keble` (`ID`, `kname`, `manger_empid`, `datee`) VALUES
(1, '01', '0', '2024-10-22 13:11:46'),
(2, '02', '0', '2024-10-22 13:11:46');

-- --------------------------------------------------------

--
-- Table structure for table `merage`
--

CREATE TABLE `merage` (
  `ID` int(11) NOT NULL,
  `userid` varchar(50) DEFAULT NULL,
  `wife_name` varchar(100) DEFAULT NULL,
  `wife_second_name` varchar(100) DEFAULT NULL,
  `wife_surname` varchar(100) DEFAULT NULL,
  `nation` varchar(100) DEFAULT NULL,
  `rigion` varchar(100) DEFAULT NULL,
  `zone` varchar(100) DEFAULT NULL,
  `wereda` varchar(100) DEFAULT NULL,
  `date_of_Mirrage` varchar(50) DEFAULT NULL,
  `keble` varchar(100) DEFAULT NULL,
  `datee` datetime DEFAULT NULL,
  `surname` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `requset`
--

CREATE TABLE `requset` (
  `ID` int(11) NOT NULL,
  `userid` varchar(50) DEFAULT NULL,
  `requset_tayp` varchar(50) DEFAULT NULL,
  `stu` varchar(5) DEFAULT NULL,
  `kebleid` varchar(50) DEFAULT NULL,
  `upronved_empid` varchar(50) DEFAULT NULL,
  `datee` varchar(58) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `ID` int(11) NOT NULL,
  `username` varchar(100) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `sname` varchar(100) DEFAULT NULL,
  `tname` varchar(100) DEFAULT NULL,
  `sex` varchar(50) DEFAULT NULL,
  `keble` varchar(100) DEFAULT NULL,
  `tnmae` datetime DEFAULT NULL,
  `mother_name` varchar(100) NOT NULL,
  `mother_nationalty` varchar(100) NOT NULL,
  `father_nationalty` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `adoption`
--
ALTER TABLE `adoption`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `barth`
--
ALTER TABLE `barth`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `deth`
--
ALTER TABLE `deth`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `devorce`
--
ALTER TABLE `devorce`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `emp`
--
ALTER TABLE `emp`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `job`
--
ALTER TABLE `job`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `keble`
--
ALTER TABLE `keble`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `merage`
--
ALTER TABLE `merage`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `requset`
--
ALTER TABLE `requset`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `adoption`
--
ALTER TABLE `adoption`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `barth`
--
ALTER TABLE `barth`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `deth`
--
ALTER TABLE `deth`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `devorce`
--
ALTER TABLE `devorce`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `emp`
--
ALTER TABLE `emp`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `job`
--
ALTER TABLE `job`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `keble`
--
ALTER TABLE `keble`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `merage`
--
ALTER TABLE `merage`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `requset`
--
ALTER TABLE `requset`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
