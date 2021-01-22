
DROP TABLE IF EXISTS `ContactAuthorDetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ContactAuthorDetails` (
  `id` int NOT NULL AUTO_INCREMENT,
  `General_Id` int(20) ,
  `Author` varchar(20) ,
  `AuthorEmail` varchar(100) ,
  `Telephone` varchar(20) ,
  `KeyWords` varchar(200) ,
  `FilePath` varchar(200) ,
    `PraperId` varchar(20) ,
  `status` BOOLEAN,
  `created_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;


-- Table structure for table `GeneralInformation`
--

DROP TABLE IF EXISTS `GeneralInformation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `GeneralInformation` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Volume` varchar(100) ,
  `PaperName` varchar(100) ,
  `FirstName` varchar(20) ,
  `LastName` varchar(20) ,
  `Country` varchar(20) ,
  `Organization` varchar(100) ,
  `Email` varchar(100) ,
  
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

