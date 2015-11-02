# coding:utf8
'''
Created on 2015年11月3日

@author: luozhangjie
'''

class TransferMoney(object):
    def __init__(self, conn):
        self.conn = conn
        
    def check_user(self, target_acctid):
        try:
            cursor = self.conn.cursor()
            sql = "select * from user where userid = %s" %target_acctid
            print sql
            cursor.execute(sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("user not esxit")
        finally:
            cursor.close()
    
    def check_money(self, source_acctid, money):
        try:
            cursor = self.conn.cursor()
            sql = "select money from user where userid = %s and money >= %s" %(source_acctid, money)
            print sql
            cursor.execute(sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("not enough money")
        finally:
            cursor.close()
    
    
    def reduce_money(self, source_acctid, money):
        try:
            cursor = self.conn.cursor()
            sql = "update user set money = money - %s where userid = %s" %(money, source_acctid)
            print sql
            cursor.execute(sql)
            if cursor.rowcount != 1:
                raise Exception("reduce_money")
        finally:
            cursor.close()
    
    
    def add_money(self, target_acctid, money):
        try:
            cursor = self.conn.cursor()
            sql = "update user set money = money + %s where userid = %s" %(money, target_acctid)
            print sql
            cursor.execute(sql)
            if cursor.rowcount != 1:
                raise Exception("add_money")
        finally:
            cursor.close()
    
    def transfer(self, source_acctid, target_acctid, money):
        try:
            self.check_user(target_acctid)
            self.check_user(source_acctid)
            self.check_money(source_acctid, money)
            self.reduce_money(source_acctid, money)
            self.add_money(target_acctid, money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e
