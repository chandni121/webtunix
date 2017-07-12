#!/usr/bin/perl -I /usr/lib/x86_64-linux-gnu/perl/5.22.1/

use CGI qw(:standard);
use Date::Format;

print header(-type=>"text/html", -charset=>"UTF-8");

if(param){
	$feedback = param('feedback');
	$module = param('module');
}
        if (-e "/home/mandeep/SCL/tmp/SKT_TEMP"){
	        die "can't open file for writting $!" unless open(TMP,">>/home/mandeep/SCL/tmp/SKT_TEMP/feedback.txt");
	} else { mkdir "/home/mandeep/SCL/tmp/SKT_TEMP" or die "Error creating directory /home/mandeep/SCL/tmp/SKT_TEMP";
	         die "can't open file for writting $!" unless open(TMP,">>/home/mandeep/SCL/tmp/SKT_TEMP/feedback.txt");
        }


	print TMP  "$module : $feedback\n\n";
        print TMP  time2str("%a, %d %h %y %X %Z\n\n", time);
	close TMP;
	print "feedback posted";

