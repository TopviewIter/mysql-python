# coding:utf8
import sys

import MySQLdb

from com.xluo.Bank import TransferMoney


if __name__ == "__main__":
    source_acctid = sys.argv[1]
    target_acctid = sys.argv[2]
    money = sys.argv[3]
    
    conn = MySQLdb.Connect(host="127.0.0.1", 
                           user="root", passwd="root", port=3306,
                           db="python")
    tr_money = TransferMoney(conn)
    
    try:
        tr_money.transfer(source_acctid, target_acctid, money)
        print "转帐成功"
    except Exception as e:
        print e
    finally:
        conn.close()
