#!/usr/bin/perl -I /usr/lib/x86_64-linux-gnu/perl/5.22.1/

#  Copyright (C) 2002-2016 Amba Kulkarni (ambapradeep@gmail.com)
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
#use CGI::Carp qw(fatalsToBrowser);

      if (param) {
          $filename=param("filename");
          $sentnum=param("sentnum");
          my $cgi = new CGI;
          print $cgi->header (-charset => 'UTF-8');
	  print "<head>\n";
	  print "</head>\n<body>";
	  print "<div id=\"imgitems\" class=\"parsetrees\">\n<center>\n<ul id=\"trees\">\n"; 
          $filename =~ s/^..//;
          $filename =~ s/\/$//;
          if(-e "/home/mandeep/SCL/var2/www/html/SHMT/DEMO/$filename/$sentnum.dot") {
               system("/usr/bin/dot -Tjpg -o/home/mandeep/SCL/var2/www/html/SHMT/DEMO/$filename/$sentnum.jpg /home/mandeep/SCL/var2/www/html/SHMT/DEMO/$filename/$sentnum.dot");
               #print "<img src=\"http://localhost/cgi-bin2/scl/SHMT/software/webdot.pl/http://localhost/scl/SHMT/DEMO/$filename/$sentnum.dot.dot.jpg\" width=\"\" height=\"\" kddalt=\"graph from public webdot server\"></li>\n";
               print "<img src=\"http://localhost/scl/SHMT/DEMO/$filename/$sentnum.jpg\" width=\"\" height=\"\" kddalt=\"graph showing all relations\"></li>\n";
              }
           print "</ul> </center> </div> </body> </html>\n";
      }
