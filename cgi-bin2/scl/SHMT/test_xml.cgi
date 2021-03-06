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

my $myPATH = "/home/mandeep/SCL/scl";
package main;
use CGI qw/:standard/;
#use CGI::Carp qw(fatalsToBrowser);
use CGI::Cookie;

use Date::Format;
    if (! (-e "/home/mandeep/SCL/tmp/SKT_TEMP")){
        mkdir "/home/mandeep/SCL/tmp/SKT_TEMP" or die "Error creating directory /home/mandeep/SCL/tmp/SKT_TEMP";
    }
    open(TMP1,">>/home/mandeep/SCL/tmp/SKT_TEMP/shmt.log") || die "Can't open /home/mandeep/SCL/tmp/SKT_TEMP/shmt.log for writing";

require "$myPATH/converters/convert.pl";

      if (param) {
      $encoding=param("encoding");
      $sentences=param("text");
      $splitter=param("splitter");
      $out_encoding=param("out_encoding");
      #$morph=param("morph");
      $parse=param("parse");
      $text_type=param("text_type");

      $mode="LOCAL";

      print TMP1 $ENV{'REMOTE_ADDR'}."\t".$ENV{'HTTP_USER_AGENT'}."\n"."encoding:$encoding\t"."sentences:$sentences\t"."splitter:$splitter\t"."out_encoding:$out_encoding\t"."parse:$parse\n#####################\n\n";

      if ($out_encoding eq "Devanagari") { $script = "DEV";}
      if ($out_encoding eq "Roman-Diacritic") { $script = "ROMAN";}
      if ($splitter eq "None") { $sandhi = "NO"; $morph = "UoHyd";}
      #if ($splitter eq "Heritage Splitter") { $sandhi = "YES"; $morph = "GH";}
      if ($splitter eq "Heritage Splitter") { $sandhi = "YES"; $morph = "GH-interactive";}
      #if ($splitter eq "Zen_Amba_Apte Splitter") { $sandhi = "YES"; $morph = "Zen_Amba";}
      if ($splitter eq "Anusaaraka Splitter") { $sandhi = "YES"; $morph = "UoHyd";}

      $pid = $$;

      $sentences =~ s/\r//g;
      $sentences =~ s/\n/#/g;
      $sentences =~ s/ ।/./g;
      $sentences =~ s/[ ]+\|/./g;
      $sentences =~ s/[ ]+([\.!\?])/$1/g;
      $sentences =~ s/:/ः/g;
      $sentences =~ s/\|[ ]+$/./g;
      $sentences =~ s/\.[ ]+$/./g;

      system("mkdir -p /home/mandeep/SCL/tmp/SKT_TEMP/tmp_in$pid");

      $sentences=&convert($encoding,$sentences);
      chomp($sentences);

      open(TMP,">/home/mandeep/SCL/tmp/SKT_TEMP/tmp_in$pid/wor.$pid") || die "Can't open /home/mandeep/SCL/tmp/SKT_TEMP/tmp_in$pid/wor.$pid for writing";
      print TMP $sentences,"\n";
      close(TMP);

      my $cgi = new CGI;
      if($morph eq "GH-interactive") {
         $cmd = "http://localhost/cgi-bin2/SKT/sktgraph?lex=SH\&cache=t\&st=t\&us=f\&cp=t\&text=$sentences\&t=WX\&topic=\&mode=g";
         print CGI-> redirect($cmd);
      } else {
         print $cgi->header (-charset => 'UTF-8');
         if($mode  eq "SERVER") {
           if(-e "/home/mandeep/SCL/tmp/skt_morph_daemonid"){
              $sentences = '"'. $sentences  . '"';
              system("$myPATH/SHMT/prog/shell/callmtshell.pl /home/mandeep/SCL/tmp/SKT_TEMP $sentences $encoding $pid $script $sandhi $morph $parse $text_type $mode");
              system("$myPATH/SHMT/prog/interface/display_output.pl $encoding $script $pid");
           } else {
             print "The Morph Daemon is not yet started. Report to the webmaster (ambapradeep\@gmail.com)\n";
           }
       } elsif ($mode eq "LOCAL") {
           $sentences = '"'. $sentences  . '"';
           system("$myPATH/SHMT/prog/shell/callmtshell.pl /home/mandeep/SCL/tmp/SKT_TEMP $sentences $encoding $pid $script $sandhi $morph $parse $text_type $mode");
           system("$myPATH/SHMT/prog/interface/display_output.pl $encoding $script $pid");
       }
      }
    }
    close(TMP1);
