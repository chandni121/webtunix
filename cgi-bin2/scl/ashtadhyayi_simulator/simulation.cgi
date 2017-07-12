#!/usr/bin/perl -I /usr/lib/x86_64-linux-gnu/perl/5.22.1/

my $myPATH = "/home/mandeep/SCL/scl";
package main;
use CGI qw/:standard/;
#use CGI::Carp qw(fatalsToBrowser);
      if (param) {
      $encoding=param("encoding");
      $pra=param("praatipadika");
      $vib=param("vibhakti");
      $lifga=param("linga");
      $vac=param("vacana");

      $pid = $$;
      
      $pra=~ s/\r//g;

      chomp($pra);
      chomp($vib);
      chomp($vac);

      system("$myPATH/ashtadhyayi_simulator/callrun.pl $encoding $pra $vib $lifga $vac $pid");
      }
