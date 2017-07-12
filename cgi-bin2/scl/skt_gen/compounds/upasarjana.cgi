#!/usr/bin/perl

my $myPATH = "/home/mandeep/SCL/scl/skt_gen/compounds";
require "$myPATH/cnvrt2utf.pl";
require "$myPATH/cnvrt2utfr.pl";

use warnings;
use CGI ':standard';

my $cgi = new CGI;

print $cgi->header(-type    => 'text/html',
                   -charset => 'utf-8');

if (param) {
  my $encodingupasarjana = param("encodingupasarjana");
  my $avigrahaupasarjana = param("vigrahaupasarjana");
  my $p1upasarjana = param("p1upasarjana");
  my $p2upasarjana = param("p2upasarjana");
  my $s1upasarjana = param("s1upasarjana");
  my $s2upasarjana = param("s2upasarjana");
  my $samAsaprakAraupasarjana = param("samAsaprakAraupasarjana");
  my $samAsAnwaupasarjana = param("samAsAnwaupasarjana");
  my $viXAyakasUwraupasarjana = param("viXAyakasUwraupasarjana"); # Not needed
  my $positionupasarjana = param("positionupasarjana");
  my $dividupasarjana = param("dividupasarjana");
  my $ansupasarjana = param("ansupasarjana");

  # print "in upasarjana.cgi samAsAnwa = $samAsAnwaupasarjana<br />";
  my $p1utf = &cnvrt2utf($p1upasarjana);
  my $p2utf = &cnvrt2utf($p2upasarjana);
  my $avigraha2utf = &cnvrt2utf($avigrahaupasarjana);
  my $samAsAnwautf = &cnvrt2utf($samAsAnwaupasarjana);

  if ($encodingupasarjana eq "RMN") {
    $p1utfr = &cnvrt2utfr($p1utf);
    $p2utfr = &cnvrt2utfr($p2utf);
    $avigraha2utfr = &cnvrt2utfr($avigraha2utf);
    $samAsAnwautfr = &cnvrt2utfr($samAsAnwautf);
  }

  $dividupasarjana =~ s/^#output//;
  $dividupasarjana++;

  print "<table>";
 #  if ($ansupasarjana eq "No") {$positionupasarjana = 3 - $positionupasarjana;} # 1 -> 2; 2 -> 1
  if ($ansupasarjana eq "No") { print "असामर्थ्यात् समासो न भवति"; exit (0);}
  if ($ansupasarjana eq "NoCont") {$positionupasarjana = 3 - $positionupasarjana;}
  if ($positionupasarjana == 3) { $positionupasarjana = 0;}

  if ($encodingupasarjana eq "RMN") {
     print "<tr><td><font color=\"blue\">$avigraha2utfr $samAsAnwautfr</font></td>";
    } else {
     print "<tr><td><font color=\"blue\">$avigraha2utf $samAsAnwautf</font></td>";
    }
  if ($positionupasarjana == 1) { 
    if ($encodingupasarjana eq "RMN") {
      print "<td><font color=\"green\"> upasarjanasaṃjñā : $p1utfr <font></td>";
    } else {
      print "<td><font color=\"green\"> उपसर्जनसञ्ज्ञा : $p1utf <font></td>";
    }
  }
  elsif ($positionupasarjana == 2) { 
    if ($encodingupasarjana eq "RMN") {
      print "<td><font color=\"green\"> upasarjanasaṃjñā : $p2utfr <font></td>";
    } else {
      print "<td><font color=\"green\"> उपसर्जनसञ्ज्ञा : $p2utf <font></td>";
    }
      # Vigraha vAkya with changed word order
      $avigrahaupasarjana = $p2upasarjana;
      if($s2upasarjana ne "") {$avigrahaupasarjana .= "+".$s2upasarjana;}
      $avigrahaupasarjana .= " ".$p1upasarjana;
      if($s1upasarjana ne "") {$avigrahaupasarjana .= "+".$s1upasarjana;}
      $avigraha2utf = &cnvrt2utf($avigrahaupasarjana);
  
      if ($encodingupasarjana eq "RMN") {
          $avigraha2utfr = &cnvrt2utfr($avigraha2utf);
      }

      $tmp = $p1upasarjana;
      $p1upasarjana = $p2upasarjana;
      $p2upasarjana = $tmp;

      $p1utf = &cnvrt2utf($p1upasarjana);
      if ($encodingupasarjana eq "RMN") {
         $p1utfr = &cnvrt2utfr($p1utf);
      }

      $tmp = $s1upasarjana;
      $s1upasarjana = $s2upasarjana;
      $s2upasarjana = $tmp;
  }
  elsif ($positionupasarjana eq "0") { 
        print "Can not decide the upasarjana saFjFA. <br>";
        print "Compound can not be formed.<br>";
        print "Exiting ...";
        exit;
  } 
  if ($encodingupasarjana eq "RMN") {
    print "<td> <font color=\"red\"> prathamānirdiṣṭaṃ samāsa upasarjanam1.2.43 </td></font>"; 
  } else {
    print "<td> <font color=\"red\"> प्रथमानिर्दिष्टं समास उपसर्जनम् 1.2.43 </td></font>";
 }
  print "</tr>";
  if ($encodingupasarjana eq "RMN") {
    print "<tr><td><font color=\"blue\">$avigraha2utfr $samAsAnwautfr</font></td>";
  } else {
    print "<tr><td><font color=\"blue\">$avigraha2utf $samAsAnwautf</font></td>";
  }
  if ($encodingupasarjana eq "RMN"){
    print "<td><font color=\"green\"> pūrvanipātaḥ: $p1utfr</font></td>";
  } else {
    print "<td><font color=\"green\"> पूर्वनिपातः  $p1utf</font></td>";
  }
  if ($encodingupasarjana eq "RMN") {
    print "<td><font color=\"red\"> upasarjanaṃ pūrvam  2.2.30</font></td>";
  } else {
    print "<td><font color=\"red\"> उपसर्जनं पूर्वम् 2.2.30</font></td>";
  }

 #print "calling aluk with samAsAnwa = $samAsAnwaupasarjana<br/>";
  # Note the changed word order of components
  my $cmd = "$myPATH/aluk.out \"$encodingupasarjana\" \"$avigrahaupasarjana\" \"$p1upasarjana\" \"$s1upasarjana\" \"$p2upasarjana\" \"$s2upasarjana\" \"$samAsaprakAraupasarjana\" \"$samAsAnwaupasarjana\" $dividupasarjana";
  system($cmd);
}
