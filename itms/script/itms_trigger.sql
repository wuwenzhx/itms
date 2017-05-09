-- --------------------------------------------------------
-- Host:                         10.239.119.250
-- Server version:               5.5.43-0ubuntu0.14.04.1 - (Ubuntu)
-- Server OS:                    debian-linux-gnu
-- HeidiSQL Version:             8.3.0.4694
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Dumping database structure for itms_new
CREATE DATABASE IF NOT EXISTS `itms_new` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
USE `itms_new`;


-- Dumping structure for trigger itms_new.itms_testcase_result_after_delete
SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='';
DELIMITER //
CREATE TRIGGER `itms_testcase_result_after_delete` AFTER DELETE ON `itms_testcase_result` FOR EACH ROW BEGIN
IF upper(OLD.RESULT) = 'PASS' THEN
	UPDATE itms_testsuite_result SET PASSED = PASSED - 1 WHERE ID = OLD.TESTSUITE_RESULT_ID;
	UPDATE itms_testsuite_result SET NA = NA + 1 WHERE ID = OLD.TESTSUITE_RESULT_ID;
ELSEIF upper(OLD.RESULT) = 'FAIL' THEN
   UPDATE itms_testsuite_result SET FAILED = FAILED - 1 WHERE ID = OLD.TESTSUITE_RESULT_ID;
   UPDATE itms_testsuite_result SET NA = NA + 1 WHERE ID = OLD.TESTSUITE_RESULT_ID;
ELSEIF upper(OLD.RESULT) = 'BLOCK' THEN
	UPDATE itms_testsuite_result SET BLOCK = BLOCK - 1 WHERE ID = OLD.TESTSUITE_RESULT_ID;
	UPDATE itms_testsuite_result SET NA = NA + 1 WHERE ID = OLD.TESTSUITE_RESULT_ID;
END IF;

END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;


-- Dumping structure for trigger itms_new.itms_testcase_result_after_insert
SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='';
DELIMITER //
CREATE TRIGGER `itms_testcase_result_after_insert` AFTER INSERT ON `itms_testcase_result` FOR EACH ROW BEGIN

IF upper(NEW.RESULT) = 'PASS' THEN
	UPDATE itms_testsuite_result SET PASSED = PASSED + 1 WHERE ID = NEW.TESTSUITE_RESULT_ID;
	UPDATE itms_testsuite_result SET NA = NA - 1 WHERE ID = NEW.TESTSUITE_RESULT_ID;
ELSEIF upper(NEW.RESULT) = 'FAIL' THEN
    UPDATE itms_testsuite_result SET FAILED = FAILED + 1 WHERE ID = NEW.TESTSUITE_RESULT_ID;
    UPDATE itms_testsuite_result SET NA = NA - 1 WHERE ID = NEW.TESTSUITE_RESULT_ID;
ELSEIF upper(NEW.RESULT) = 'BLOCK' THEN
	UPDATE itms_testsuite_result SET BLOCK = BLOCK + 1 WHERE ID = NEW.TESTSUITE_RESULT_ID;
	UPDATE itms_testsuite_result SET NA = NA - 1 WHERE ID = NEW.TESTSUITE_RESULT_ID;
END IF;

END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;


-- Dumping structure for trigger itms_new.itms_testcase_result_after_update
SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='';
DELIMITER //
CREATE TRIGGER `itms_testcase_result_after_update` AFTER UPDATE ON `itms_testcase_result` FOR EACH ROW IF upper(NEW.RESULT) <> upper(OLD.result) THEN

IF upper(NEW.RESULT) = 'PASS' THEN
	UPDATE itms_testsuite_result SET PASSED = PASSED + 1 WHERE ID = NEW.TESTSUITE_RESULT_ID;
ELSEIF upper(NEW.RESULT) = 'FAIL' THEN
    UPDATE itms_testsuite_result SET FAILED = FAILED + 1 WHERE ID = NEW.TESTSUITE_RESULT_ID;
ELSEIF upper(NEW.RESULT) = 'BLOCK' THEN
	UPDATE itms_testsuite_result SET BLOCK = BLOCK + 1 WHERE ID = NEW.TESTSUITE_RESULT_ID;
ELSEIF upper(NEW.result) = 'NA' THEN
	UPDATE itms_testsuite_result SET NA = NA + 1 WHERE ID = NEW.TESTSUITE_RESULT_ID;
end if;

IF upper(OLD.RESULT) = 'PASS' then
	UPDATE itms_testsuite_result SET PASSED = PASSED - 1 WHERE ID = NEW.TESTSUITE_RESULT_ID;
ELSEIF upper(OLD.RESULT) = 'FAIL' then
	UPDATE itms_testsuite_result SET FAILED = FAILED - 1 WHERE ID = NEW.TESTSUITE_RESULT_ID;
ELSEIF upper(OLD.RESULT) = 'BLOCK' THEN
	UPDATE itms_testsuite_result SET BLOCK = BLOCK - 1 WHERE ID = NEW.TESTSUITE_RESULT_ID;
ELSEIF upper(OLD.result) = 'NA' THEN
	UPDATE itms_testsuite_result SET NA = NA - 1 WHERE ID = NEW.TESTSUITE_RESULT_ID;
end if;

END IF//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;


-- Dumping structure for trigger itms_new.itms_testexecution_after_insert
SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='';
DELIMITER //
CREATE TRIGGER `itms_testexecution_after_insert` AFTER INSERT ON `itms_testexecution` FOR EACH ROW BEGIN
DECLARE p_id int default 0;
DECLARE row_no_found int default 0; 
DECLARE suite_cursor CURSOR FOR (select testsuite_id from itms_testsuite_testplan where new.testplan_id = testplan_id);
DECLARE CONTINUE HANDLER FOR NOT FOUND SET row_no_found=1;
OPEN suite_cursor;
myloop: LOOP
	FETCH suite_cursor into p_id;
	IF row_no_found = 1 THEN
		LEAVE myloop;
	ELSE
		set @total = (select count(*) from itms_testcase_testsuite where testsuite_id = p_id);
		insert into itms_testsuite_result values (null,new.id, p_id, 0,0,0,@total,@total,now(),new.project_id);
	END IF;
END LOOP myloop;
CLOSE suite_cursor;
END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;


-- Dumping structure for trigger itms_new.itms_testexecution_before_delete
SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='';
DELIMITER //
CREATE TRIGGER `itms_testexecution_before_delete` BEFORE DELETE ON `itms_testexecution` FOR EACH ROW BEGIN
DECLARE p_id int default 0;
DECLARE row_no_found int default 0;
DECLARE suite_cursor CURSOR FOR (select id from itms_testsuite_result where testexecution_id=old.id);
DECLARE CONTINUE HANDLER FOR NOT FOUND SET row_no_found=1;
OPEN suite_cursor;
myloop: LOOP
	FETCH suite_cursor into p_id;
	IF row_no_found = 1 THEN
		LEAVE myloop;
	ELSE
		delete from itms_testcase_result where testsuite_result_id = p_id;
		delete from itms_testsuite_result where id = p_id;
	END IF;
END LOOP myloop;
CLOSE suite_cursor;
END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
