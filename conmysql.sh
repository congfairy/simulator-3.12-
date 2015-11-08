#!/bin/bash  
    MYSQL=mysql      
    USER=root    
    PASSWORD="2536"   
    DB=fits
    COMMAND="select cards from hdu"   
    COMMAND1="select headerallocated from hdu"   
    echo "keynumbers and headerallocated">mysql.txt
    declare count=`$MYSQL -u${USER} -p${PASSWORD} -D ${DB} -e "${COMMAND}" --skip-column-name`  
    declare count1=`$MYSQL -u${USER} -p${PASSWORD} -D ${DB} -e "${COMMAND1}" --skip-column-name`  
    for keys in $count   

     do
    echo "the keynumbers is:$keys" >>mysql.txt 
   done       
    for hdu in $count1                                                                                                     
       do
     echo "the headerallocated is:$hdu"  >>mysql.txt
   done       
