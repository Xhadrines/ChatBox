-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema chatbox_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema chatbox_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `chatbox_db` ;
USE `chatbox_db` ;

-- -----------------------------------------------------
-- Table `chatbox_db`.`user_roles`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `chatbox_db`.`user_roles` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NOT NULL,
  `description` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `chatbox_db`.`user_status`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `chatbox_db`.`user_status` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NOT NULL,
  `description` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `chatbox_db`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `chatbox_db`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(50) NOT NULL,
  `email` VARCHAR(100) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `role_id` INT NOT NULL,
  `status_id` INT NOT NULL,
  `last_login` DATETIME NULL DEFAULT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_users_role_id_idx` (`role_id` ASC) VISIBLE,
  INDEX `fk_users_status_id_idx` (`status_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_role_id`
    FOREIGN KEY (`role_id`)
    REFERENCES `chatbox_db`.`user_roles` (`id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  CONSTRAINT `fk_users_status_id`
    FOREIGN KEY (`status_id`)
    REFERENCES `chatbox_db`.`user_status` (`id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `chatbox_db`.`plan_types`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `chatbox_db`.`plan_types` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NOT NULL,
  `description` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `chatbox_db`.`plans`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `chatbox_db`.`plans` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NOT NULL,
  `price` DECIMAL(8,2) NOT NULL,
  `type_id` INT NOT NULL,
  `duration_days` INT NULL DEFAULT NULL,
  `name_llm_prm` VARCHAR(50) NOT NULL,
  `daily_prm_msg` INT NULL DEFAULT NULL,
  `name_llm_std` VARCHAR(50) NOT NULL,
  `daily_std_msg` INT NULL DEFAULT NULL,
  `daily_file_limit` INT NULL DEFAULT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_plans_1_idx` (`type_id` ASC) VISIBLE,
  CONSTRAINT `fk_plans_type_id`
    FOREIGN KEY (`type_id`)
    REFERENCES `chatbox_db`.`plan_types` (`id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `chatbox_db`.`user_plans`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `chatbox_db`.`user_plans` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `plan_id` INT NOT NULL,
  `start_date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `end_date` TIMESTAMP NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_user_plans_user_id_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_user_plans_plan_id_idx` (`plan_id` ASC) VISIBLE,
  CONSTRAINT `fk_user_plans_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `chatbox_db`.`users` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_user_plans_plan_id`
    FOREIGN KEY (`plan_id`)
    REFERENCES `chatbox_db`.`plans` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `chatbox_db`.`files`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `chatbox_db`.`files` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `file_name` VARCHAR(255) NOT NULL,
  `file_path` VARCHAR(255) NOT NULL,
  `uploaded_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_files_user_id_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_files_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `chatbox_db`.`users` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `chatbox_db`.`messages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `chatbox_db`.`messages` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `user_msg` TEXT NOT NULL,
  `llm_resp` TEXT NOT NULL,
  `llm_used` VARCHAR(50) NOT NULL,
  `uploaded_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_messages_user_id_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_messages_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `chatbox_db`.`users` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `chatbox_db`.`user_usage`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `chatbox_db`.`user_usage` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `date` DATE NOT NULL,
  `messages_sent` INT NOT NULL,
  `files_uploaded` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_user_usage_user_id_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_user_usage_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `chatbox_db`.`users` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
