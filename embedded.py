
#-*- coding: utf-8-*-

import MySQLdb as mdb #Embedded Program 작성을 위한 라이브러리 

con = mdb.connect('localhost', 'root', 'conios1', 'homework1');

with con: 

	# 1. select branch name
	print "1. branch table에서 지점이름 검색." 
	
        cur = con.cursor()
        cur.execute("SELECT branch_name \
                     FROM branch")

        rows = cur.fetchall()

        branch_names = []
	for row in rows:
                branch_names.append(row[0])
                print row[0]
                
	# 2. project client's name & balance each by branch name
        print "2. 각 지점별로 고객의 이름과 예금잔액 검색." 

	cur = con.cursor()
	cur.execute("SELECT name, SUM(balance), branch_name \
                     FROM deposit NATURAL JOIN client   	\
                     GROUP BY ssn, branch_name ORDER BY name ASC")

        rows = cur.fetchall()

        for bname in branch_names:
                print "[%s]" % bname
                print "|%11s |%14s|" %  ("이름","예금잔액")
                for row in rows:
                        if (row[2]==bname):
                                print "|%12s |%10s|" %  (row[0],row[1])







