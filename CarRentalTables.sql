-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 08, 2022 at 06:48 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `CAR_RENTALS_GALINDOJ`
--

-- --------------------------------------------------------

--
-- Table structure for table `CARS`
--

CREATE TABLE `CARS` (
  `DAILYRATE` int(11) DEFAULT NULL,
  `WEEKLYRATE` int(11) DEFAULT NULL,
  `VEHICLEID` int(11) NOT NULL,
  `MODEL` varchar(50) DEFAULT NULL,
  `TYPE` varchar(50) DEFAULT NULL,
  `MADE` year(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `CARS`
--

INSERT INTO `CARS` (`DAILYRATE`, `WEEKLYRATE`, `VEHICLEID`, `MODEL`, `TYPE`, `MADE`) VALUES
(100, 600, 1, 'Acura MDX', 'SUV', 2022),
(100, 600, 2, 'Audi Q3 Quattro Sport', 'SUV', 2021),
(100, 600, 3, 'Land Rover Range Rover', 'SUV', 2020),
(100, 600, 4, 'Nissan Murano', 'SUV', 2023),
(100, 600, 5, 'Toyota FJ Cruiser', 'SUV', 2009),
(100, 600, 6, 'Hyundai Tucson', 'SUV', 2020),
(50, 250, 7, 'Honda Partner', 'Compact', 2023),
(50, 250, 8, 'BMW 320 TC', 'Compact', 2018),
(50, 250, 9, 'Hyundai Mistra', 'Compact', 2021),
(80, 350, 10, 'Subaru Legacy', 'Medium', 2023),
(80, 350, 11, 'Kia K5', 'Medium', 2020),
(80, 350, 12, 'Audi A6', 'Medium', 2023),
(80, 350, 13, 'Chevrolet Malibu', 'Medium', 2021),
(100, 600, 14, 'Cadillac XTS', 'Large', 2019),
(100, 600, 15, 'Dodge Charger', 'Large', 2015),
(100, 600, 16, 'Chrysler 300', 'Large', 2009),
(150, 850, 17, 'GMC Sierra', 'Truck', 2018),
(150, 850, 18, 'RAM 3500', 'Truck', 2021),
(150, 850, 19, 'Ford Ranger', 'Truck', 2022),
(150, 850, 20, 'Nissan Titan', 'Truck', 2023),
(150, 850, 21, 'Nissan Navara', 'Truck', 2012),
(100, 700, 22, 'Toyota HiAce', 'Van', 2017),
(100, 700, 23, 'Ford Galaxy', 'Van', 2015),
(100, 700, 24, 'RAM ProMaster', 'Van', 2016),
(500, 1000, 30, 'Batmobile', 'Super', 2022);

-- --------------------------------------------------------

--
-- Table structure for table `CUSTOMER`
--

CREATE TABLE `CUSTOMER` (
  `IDNo` int(11) NOT NULL,
  `PHONE` varchar(12) DEFAULT NULL,
  `NAME` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `CUSTOMER`
--

INSERT INTO `CUSTOMER` (`IDNo`, `PHONE`, `NAME`) VALUES
(1, '313-321-123', 'W.Smith'),
(2, '777-543-1234', 'M.Miller'),
(3, '455-818-8822', 'A.Luck'),
(4, '999-574-2222', 'R.Wilson'),
(5, '333-987-0789', 'J.Chan'),
(6, '541-234-5645', 'I.Martinez'),
(7, '123-456-7890', 'P.Parker'),
(8, '945-344-5435', 'A.Davis'),
(9, '101-011-1111', 'M.Freeman'),
(10, '303-414-5466', 'E.Cartman');

-- --------------------------------------------------------

--
-- Table structure for table `DAILYRENTAL`
--

CREATE TABLE `DAILYRENTAL` (
  `RENTALID` int(11) DEFAULT NULL,
  `NUMOFDAYS` int(11) DEFAULT NULL,
  `STARTDATE` date DEFAULT NULL,
  `RETURNDATE` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `RENTAL`
--

CREATE TABLE `RENTAL` (
  `RENTALID` int(11) NOT NULL,
  `RENTALTYPE` varchar(40) DEFAULT NULL,
  `AMOUNTDUE` int(11) DEFAULT NULL,
  `CUSTOMERID` int(11) DEFAULT NULL,
  `VEHICLEID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `WEEKLYRENTAL`
--

CREATE TABLE `WEEKLYRENTAL` (
  `RENTALID` int(11) DEFAULT NULL,
  `NUMOFWEEKS` int(11) DEFAULT NULL,
  `STARTDATE` date DEFAULT NULL,
  `RETURNDATE` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `CARS`
--
ALTER TABLE `CARS`
  ADD PRIMARY KEY (`VEHICLEID`);

--
-- Indexes for table `CUSTOMER`
--
ALTER TABLE `CUSTOMER`
  ADD PRIMARY KEY (`IDNo`);

--
-- Indexes for table `DAILYRENTAL`
--
ALTER TABLE `DAILYRENTAL`
  ADD KEY `RENTALID` (`RENTALID`);

--
-- Indexes for table `RENTAL`
--
ALTER TABLE `RENTAL`
  ADD PRIMARY KEY (`RENTALID`),
  ADD KEY `CUSTOMERID` (`CUSTOMERID`),
  ADD KEY `VEHICLEID` (`VEHICLEID`);

--
-- Indexes for table `WEEKLYRENTAL`
--
ALTER TABLE `WEEKLYRENTAL`
  ADD KEY `RENTALID` (`RENTALID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `CARS`
--
ALTER TABLE `CARS`
  MODIFY `VEHICLEID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `CUSTOMER`
--
ALTER TABLE `CUSTOMER`
  MODIFY `IDNo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `RENTAL`
--
ALTER TABLE `RENTAL`
  MODIFY `RENTALID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `DAILYRENTAL`
--
ALTER TABLE `DAILYRENTAL`
  ADD CONSTRAINT `dailyrental_ibfk_1` FOREIGN KEY (`RENTALID`) REFERENCES `RENTAL` (`RENTALID`);

--
-- Constraints for table `RENTAL`
--
ALTER TABLE `RENTAL`
  ADD CONSTRAINT `rental_ibfk_1` FOREIGN KEY (`CUSTOMERID`) REFERENCES `CUSTOMER` (`IDNo`),
  ADD CONSTRAINT `rental_ibfk_2` FOREIGN KEY (`VEHICLEID`) REFERENCES `CARS` (`VEHICLEID`);

--
-- Constraints for table `WEEKLYRENTAL`
--
ALTER TABLE `WEEKLYRENTAL`
  ADD CONSTRAINT `weeklyrental_ibfk_1` FOREIGN KEY (`RENTALID`) REFERENCES `RENTAL` (`RENTALID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
