-- Database keepindoors
create database if not exists keepindoors;

-- Table docs
-- docno: id
-- json_info: information of the doc, for example : url,docno,contenttitle,content,date
create table if not exists keepindoors.docs(docno string,json_info string);

-- Table doc pairs
-- docno1: id1
-- docno2: id2
create table if not exists keepindoors.doc_pairs(docno1 string,docno2 string);