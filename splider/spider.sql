/*
Navicat MySQL Data Transfer

Source Server         : Test
Source Server Version : 80016
Source Host           : localhost:3306
Source Database       : spider

Target Server Type    : MYSQL
Target Server Version : 80016
File Encoding         : 65001

Date: 2021-09-29 22:16:58
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `bs_theme_product`
-- ----------------------------
DROP TABLE IF EXISTS `bs_theme_product`;
CREATE TABLE `bs_theme_product` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '编号',
  `title` varchar(255) NOT NULL COMMENT '标题',
  `logo` varchar(255) NOT NULL COMMENT '封面',
  `url` varchar(255) NOT NULL COMMENT '详情地址',
  `preview` varchar(255) NOT NULL COMMENT '预览地址',
  `cate` varchar(100) NOT NULL COMMENT '分类',
  `price` decimal(6,2) NOT NULL COMMENT '价格',
  `createdAt` datetime NOT NULL COMMENT '保存时间',
  `updatedAt` datetime NOT NULL COMMENT '修改时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='bootstrap主题产品表';

-- ----------------------------
-- Records of bs_theme_product
-- ----------------------------
