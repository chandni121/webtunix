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

use strict;
use warnings;
#use Shell;
use CGI qw( :standard );
#use LWP::Simple qw/!head/;
#$VERSION = "2.0";
use Date::Format;
#use Log::Log4perl qw(:easy);
    if (! (-e "/home/mandeep/SCL/tmp/SKT_TEMP")){
        mkdir "/home/mandeep/SCL/tmp/SKT_TEMP" or die "Error creating directory /home/mandeep/SCL/tmp/SKT_TEMP";
    }

open(TMP1,">>/home/mandeep/SCL/tmp/SKT_TEMP/morph.log") || die "Can't open /home/mandeep/SCL/tmp/SKT_TEMP/morph.log for writing";

print header(-type=>"text/html" , -charset=>"utf-8");

#Declaration of all the variables
my $word1;
my $wordutf;
my $ans;
my $ans="";
my $encoding="";
my $rt;
my $rt_XAwu_gaNa;
my $XAwu;
my $gaNa;
my $lifga;
my $ref;

if (param()){ 
    $word1 = param('morfword');
    $encoding=param("encoding");
}
print "<script>\n";
print "function analyse_noun_forms(encod,word){
  window.open('http://localhost/cgi-bin2/scl/morph/morph.cgi?encoding='+encod+'&morfword='+word+'','popUpWindow','height=200,width=600,left=100,top=100,resizable=yes,scrollbars=yes,toolbar=yes,menubar=no,location=no,directories=no, status=yes').focus();}\n";

print "function generate_noun_forms(encod,prAwi,lifga,level){
  window.open('http://localhost/cgi-bin2/scl/skt_gen/noun/noun_gen.cgi?encoding='+encod+'&rt='+prAwi+'&gen='+lifga+'&level='+level+'','popUpWindow','height=500,width=400,left=100,top=100,resizable=yes,scrollbars=yes,toolbar=yes,menubar=no,location=no,directories=no, status=yes').focus();
}\n";

print "function generate_kqw_forms(encod,vb){
  window.open('http://localhost/cgi-bin2/scl/skt_gen/kqw/kqw_gen.cgi?encoding='+encod+'&vb='+vb+'','popUpWindow','height=500,width=400,left=100,top=100,resizable=yes,scrollbars=yes,toolbar=yes,menubar=no,location=no,directories=no, status=yes').focus();
}\n";

print "function generate_waxXiwa_forms(encod,rt,gen){
  window.open('http://localhost/cgi-bin2/scl/skt_gen/waxXiwa/waxXiwa_gen.cgi?encoding='+encod+'&rt='+rt+'&gen='+gen+'','popUpWindow','height=500,width=400,left=100,top=100,resizable=yes,scrollbars=yes,toolbar=yes,menubar=no,location=no,directories=no, status=yes').focus();
}\n";

print "</script>\n";

my $ans = `/home/mandeep/SCL/scl/SHMT/prog/morph/callmorph.pl $word1 $encoding LOCAL`;

print TMP1 $ENV{'REMOTE_ADDR'}."\t".$ENV{'HTTP_USER_AGENT'}."\n"."encoding:$encoding\t"."morfword:$word1\n"."output::wordutf:$wordutf\t"."tempnew_data:$ans\n############################\n\n";

print "<table style=\"border-collapse: collapse;\" bordercolor='brown' valign='middle' bgcolor='#297e96' border='1' cellpadding='2' cellspacing='2' >
<tr>";
chomp($ans);
$ans =~ s/</{/g;
$ans =~ s/>/}/g;
$ans =~ s/{वर्गः:ना}//g;
$ans =~ s/\$//g;
my @ans=split(/\//,$ans);
my $i = 0;
if($ans ne "") {
 foreach $ans (@ans) {
   $ans =~ s/:/ /g;
   if($ans =~ /^[^{]+{लेवेल् 4}/) { $ans =~ s/^[^{]+{लेवेल् 4}//;}
   $ans =~ s/^([^ ]+) / /;
   $rt = $1;
   if($ans =~ /लेवेल् 2/) { $ans =~ s/लेवेल् 2/कृदन्त/;}
   if($ans =~ /लेवेल् 3/) { $ans =~ s/लेवेल् 3/तद्धित/;}
   if($ans =~ /लेवेल् [01]/) { $ans =~ s/{लेवेल् [01]}//;}

   if($ans =~ /कृत्_प्रत्ययः/ ){
     if($ans =~ /{धातुः ([^}]+)/) { $XAwu = $1;}
     if($ans =~ /{गणः ([^}]+)/) { $gaNa = $1;}
      $rt_XAwu_gaNa = $rt."_".$XAwu."_".$gaNa;
 #   $ref = "<a href=\"http://localhost/cgi-bin2/scl/skt_gen/kqw/kqw_gen.cgi?encoding=Unicode&vb=$rt_XAwu_gaNa\" target=\"_blank\">$rt</a>";
      if($rt ne $word1) {
         $ref = "<a href=\"javascript:generate_kqw_forms('Unicode','$rt_XAwu_gaNa')\">$rt</a>";
      } else { $ref = $rt;}
      if(($rt ne "") && ($ans ne "")) {
        print "<td bgcolor='lavendar'>",$ref,$ans,"</td>";
      }
    }elsif ($ans =~ /तद्धित_प्रत्यय/){
      if($rt ne $word1) {
       $ref = "<a href=\"javascript:generate_waxXiwa_forms('Unicode','$rt','$lifga')\">$rt</a>";
      } else { $ref = $rt;}
  #  $ref = "<a href=\"http://localhost/cgi-bin2/scl/skt_gen/waxXiwa/waxXiwa_gen.cgi?encoding=Unicode&rt=$rt&gen=$lifga\" target=\"_blank\">$rt</a>";
       if(($rt ne "") && ($ans ne "")) {
         print "<td bgcolor=''>",$ref,$ans,"</td>";
       }
     } elsif ($ans =~ /(पुं|नपुं|स्त्री)/) {
       $lifga = $1;
       if($ans =~ /कृदन्त|तद्धित/) { 
          if($rt ne $word1) {
             $ref = "<a href=\"javascript:analyse_noun_forms('Unicode','$rt')\">$rt</a>";
          } else { $ref = $rt;}
    # $ref = "<a href=\"http://localhost/cgi-bin2/scl/morph/morph.cgi?encoding=Unicode&morfword=$rt\">$rt</a>";
       } else {
  #    $ref = "<a href=\"http://localhost/cgi-bin2/scl/skt_gen/noun/noun_gen.cgi?encoding=Unicode&rt=$rt&gen=$lifga\" target=\"morfoutput\" onclick=\"window.open('http://localhost/cgi-bin2/scl/skt_gen/noun/noun_gen.cgi?encoding=Unicode&rt=$rt&gen=$lifga')\">$rt</a>";
      if(($rt ne $word1) && ($ans !~ /{धातुः ([^}]+)/) ){
         $ref = "<a href=\"javascript:generate_noun_forms('Unicode','$rt','$lifga','1')\">$rt</a>";
      } else { $ref = $rt;}
       }
       if(($rt ne "") && ($ans ne "")) {
           print "<td bgcolor='skyblue'>",$ref,$ans,"</td>";
       }
     }
     elsif ($ans =~ /(लट्|लिट्|लुट्|लोट्|लृट्|लङ्|लृङ|लुङ्|लिङ्)/) {
        if($ans =~ /{धातुः ([^}]+)/) { $XAwu = $1;}
        if($ans =~ /{गणः ([^}]+)/) { $gaNa = $1;}
        $rt_XAwu_gaNa = $rt."_".$XAwu."_".$gaNa;
    #$ref = "<a href=\"http://localhost/cgi-bin2/scl/skt_gen/verb/verb_gen.cgi?encoding=Unicode&vb=$rt_XAwu_gaNa&prayoga=कर्तरि\" target=\"_blank\">$rt</a>";
        $ref = $rt; # verb generator needs mng also. Hence temporarily disconnected
        if(($rt ne "") && ($ans ne "")) {
            print "<td bgcolor='pink'>",$ref,$ans,"</td>";
        }
     }
     else {
        if(($rt ne "") && ($ans ne "")) {
            print "<td bgcolor='lightgreen'>",$rt,$ans,"</td>";
        }
     }
 $i++;
 if($i % 6 == 0) { print "</tr><tr>";}
} # endof foreach
} else { print "No answer found\n";}
print "</table>\n";

close(TMP1);
