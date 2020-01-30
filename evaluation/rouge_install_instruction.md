## Rouge Installation Instruction on Ubuntu

### Step 1
Check perl version to make sure perl version is above 5.6.0 and upgrade perl version if necessary:
```bash
perl -v
```

### Step 2
Download rouge.zip from google drive https://drive.google.com/open?id=1i-K3TddTOffBC85gWh0sXxUad_cGXl1Z and unzip:
```
unzip rouge.zip
```

### Step 3
Install XML::Parser:
```
cd rouge
tar -zxvf XML-Parser-2.44.tar.gz
cd XML-Parser-2.44
perl Makefile.PL 
make 
make test  # if %%%Result all pass, then success, otherwise, pay attention the reported wrong cases
sudo make install  # sudo if necessary 
```

### Step 4
Install XML::RegExp:
```
cd ..
tar -zxvf XML-RegExp-0.04.tar.gz
cd XML-RegExp-0.04
perl Makefile.PL 
make 
make test  # if %%%Result all pass, then success, otherwise, pay attention the reported wrong cases
sudo make install  # sudo if necessary 
```

### Step 5
Install LWP::UserAgent:
```
sudo apt-get update
sudo apt-get install libwww-perl
```

### Step 6
Install XML::Parser::PerlSAX:
```
sudo apt-get install libxml-perl
```

### Step 7
Install XML::DOM:
```
cd ..
tar -zxvf XML-DOM-1.46.tar.gz
cd XML-DOM-1.46
perl Makefile.PL 
make 
make test  # if %%%Result all pass, then success, otherwise, pay attention the reported wrong cases
sudo make install  # sudo if necessary 
```
If not pass while make test (messages shown below):
```
Test Summary Report
-------------------
t/build_dom.t       (Wstat: 512 Tests: 1 Failed: 1)
  Failed test:  1
  Non-zero exit status: 2
  Parse errors: Bad plan.  You planned 2 tests but ran 1.
Files=21, Tests=128,  2 wallclock secs ( 0.07 usr  0.01 sys +  1.56 cusr  0.10 csys =  1.74 CPU)
Result: FAIL
Failed 1/21 test programs. 1/128 subtests failed.
Makefile:968: recipe for target 'test_dynamic' failed
make: *** [test_dynamic] Error 255
```
Try to fix with:
```
sudo apt-get install -f
sudo apt-get update --fix-missing 
```

### Step 8
Install DB_File:
```
cd ..
tar -zxvf DB_File-1.835.tar.gz
cd DB_File-1.835
perl Makefile.PL 
make 
make test  # if %%%Result all pass, then success, otherwise, pay attention the reported wrong cases
sudo make install  # sudo if necessary 
```
If report error while make (message shown below):
```
version.c:30:16: fatal error: db.h
compilation terminated.
Makefile:360: recipe for target 'version.o' failed
make: *** [version.o] Error 1
```
It means Berkeley DB library is not installed or not installed correctly. Try to solve with:
```
sudo apt-get install libdb-dev
```
If still not working, it might be a problem with wrong version. First check current Berkeley DB library version with:
```
sudo apt-cache search libdb
```
In this case correct version is 5.3 since the result from previous command contains a line says:
```
libdb5.3-dev - Berkeley V5.3 Database Libraries [development]
```
Then install corresponding version:
```
sudo apt-get install libdb5.3-dev  
``` 

### Step 9
Unzip ROUGE-1.5.5:
```
cd ..
tar -zxvf ROUGE-1.5.5.tgz
``` 
Add path variable to profile (assume rouge file directory is under /home/usr/):
```
export ROUGE_EVAL_HOME="$ROUGE_EVAL_HOME:/home/usr/rouge/RELEASE-1.5.5/data"
```
Add variable to this file works for current user:
```
~/.profile
```
Add variable to this file works for all users:
```
/etc/profile
```

### Step 10
Test if successfully installed rouge:
```
cd ROUGE-1.5.5
perl runROUGE-test.pl
```
If test file returns following messages and contents exist under sample-out directories, rouge is good to go:
```
../ROUGE-1.5.5.pl -e ../data -c 95 -2 -1 -U -r 1000 -n 4 -w 1.2 -a ROUGE-test.xml > ../sample-output/ROUGE-test-c95-2-1-U-r1000-n4-w1.2-a.out
../ROUGE-1.5.5.pl -e ../data -c 95 -2 -1 -U -r 1000 -n 4 -w 1.2 -a -m ROUGE-test.xml > ../sample-output/ROUGE-test-c95-2-1-U-r1000-n4-w1.2-a-m.out
../ROUGE-1.5.5.pl -e ../data -c 95 -2 -1 -U -r 1000 -n 4 -w 1.2 -a -m -s ROUGE-test.xml > ../sample-output/ROUGE-test-c95-2-1-U-r1000-n4-w1.2-a-m-s.out
../ROUGE-1.5.5.pl -e ../data -c 95 -2 -1 -U -r 1000 -n 4 -w 1.2 -l 10 -a ROUGE-test.xml > ../sample-output/ROUGE-test-c95-2-1-U-r1000-n4-w1.2-l10-a.out
../ROUGE-1.5.5.pl -e ../data -c 95 -2 -1 -U -r 1000 -n 4 -w 1.2 -l 10 -a -m ROUGE-test.xml > ../sample-output/ROUGE-test-c95-2-1-U-r1000-n4-w1.2-l10-a-m.out
../ROUGE-1.5.5.pl -e ../data -c 95 -2 -1 -U -r 1000 -n 4 -w 1.2 -l 10 -a -m -s ROUGE-test.xml > ../sample-output/ROUGE-test-c95-2-1-U-r1000-n4-w1.2-l10-a-m-s.out
../ROUGE-1.5.5.pl -e ../data -c 95 -2 -1 -U -r 1000 -n 4 -w 1.2 -b 75 -a ROUGE-test.xml > ../sample-output/ROUGE-test-c95-2-1-U-r1000-n4-w1.2-b75-a.out
../ROUGE-1.5.5.pl -e ../data -c 95 -2 -1 -U -r 1000 -n 4 -w 1.2 -b 75 -a -m ROUGE-test.xml > ../sample-output/ROUGE-test-c95-2-1-U-r1000-n4-w1.2-b75-a-m.out
../ROUGE-1.5.5.pl -e ../data -c 95 -2 -1 -U -r 1000 -n 4 -w 1.2 -b 75 -a -m -s ROUGE-test.xml > ../sample-output/ROUGE-test-c95-2-1-U-r1000-n4-w1.2-b75-a-m-s.out
../ROUGE-1.5.5.pl -e ../data -3 HM -z SIMPLE DUC2002-BE-F.in.26.lst 26 > ../sample-output/DUC2002-BE-F.in.26.lst.out
../ROUGE-1.5.5.pl -e ../data -3 HM DUC2002-BE-F.in.26.simple.xml 26 > ../sample-output/DUC2002-BE-F.in.26.simple.out
../ROUGE-1.5.5.pl -e ../data -3 HM -z SIMPLE DUC2002-BE-L.in.26.lst 26 > ../sample-output/DUC2002-BE-L.in.26.lst.out
../ROUGE-1.5.5.pl -e ../data -3 HM DUC2002-BE-L.in.26.simple.xml 26 > ../sample-output/DUC2002-BE-L.in.26.simple.out
../ROUGE-1.5.5.pl -e ../data -n 4 -z SPL DUC2002-ROUGE.in.26.spl.lst 26 > ../sample-output/DUC2002-ROUGE.in.26.spl.lst.out
../ROUGE-1.5.5.pl -e ../data -n 4 DUC2002-ROUGE.in.26.spl.xml 26 > ../sample-output/DUC2002-ROUGE.in.26.spl.out
```

