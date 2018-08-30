#!/usr/local/bin/perl
use CGI;
$query = new CGI;
print $query->header;
print $query->start_html(-title=>"Public Com #1");
print $query->startform;
print "Message: ",$query->textfield(-name=>'message');
print $query->endform;
print "<HR>";
if ($query->param('userName') ne "") {
        print "<HR>";
        print "Message: ",$query->param('message');
        }
print $query->end_html;
print $query->dump;
