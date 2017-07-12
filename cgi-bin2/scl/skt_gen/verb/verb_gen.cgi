#!/usr/bin/perl -I /usr/lib/x86_64-linux-gnu/perl/5.22.1/

#  Copyright (C) 2010-2016 Amba Kulkarni (ambapradeep@gmail.com)
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either
#  version 2 of the License, or (at your option) any later
#  version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

package main;
use CGI qw/:standard/;

    if (! (-e "/home/mandeep/SCL/tmp/SKT_TEMP")){
        mkdir "/home/mandeep/SCL/tmp/SKT_TEMP" or die "Error creating directory /home/mandeep/SCL/tmp/SKT_TEMP";
    }
    open(TMP1,">>/home/mandeep/SCL/tmp/SKT_TEMP/verb.log") || die "Can't open /home/mandeep/SCL/tmp/SKT_TEMP/verb.log for writing";
      if (param) {

      $word=param("vb");
      $prayoga=param("prayoga");
      $encoding=param("encoding");

      my $cgi = new CGI;
      print $cgi->header (-charset => 'UTF-8');
print "<head>\n";
      print "<script type=\"text/javascript\">\n";
      print "function show(word){\n";
      print "window.open('http://localhost/cgi-bin2/scl/SHMT/options1.cgi?word='+word+'','popUpWindow','height=500,width=400,left=100,top=100,resizable=yes,scrollbars=yes,toolbar=no,menubar=no,location=no,directories=no, status=yes');\n }\n </script>";

 print "</head>\n";
      print "<body onload=\"register_keys()\"> <script src=\"/html/scl/SHMT/wz_tooltip.js\" type=\"text/javascript\"></script>\n";

      my $result = `/home/mandeep/SCL/scl/skt_gen/verb/gen_verb.pl $encoding $prayoga $word LOCAL`;
      print $result;
      print TMP1 "running:","calling gen_verb.pl from noun generator";
      print TMP1 $ENV{'REMOTE_ADDR'}."\t".$ENV{'HTTP_USER_AGENT'}."\n"."word:$word\t"."prayoga:$prayoga\n#######################\n\n";
      }
      close(TMP1);
