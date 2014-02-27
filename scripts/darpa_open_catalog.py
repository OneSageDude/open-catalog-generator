#!/usr/bin/python
def logo():
  return """
<table><tr><td><img height=50 src="darpa.png"></td><td valign=center><h2><a href='index.html' class='topheaderlink'>Open Catalog</a></h2></td></tr></table>
"""

def catalog_splash_content():
  return """
<p>Welcome to the DARPA Open Catalog, which contains a curated list of DARPA-sponsored software and peer-reviewed publications. DARPA funds fundamental and applied research in a variety of areas including data science, cyber, anomaly detection, etc., which may lead to experimental results and reusable technology designed to benefit multiple government domains.</p>
<p>The DARPA Open Catalog organizes publically releasable material from DARPA programs, beginning with the <a href='http://www.darpa.mil/Our_Work/I2O/Programs/XDATA.aspx'>XDATA</a> program in the Information Innovation Office (I2O).  XDATA is developing an open source software library for big data. DARPA has an open source strategy through XDATA and other I2O programs to help increase the impact of government investments.</p>
<p>DARPA is interested in building communities around government-funded software and research. If the R&D community shows sufficient interest, DARPA will continue to make available information generated by DARPA programs, including software, publications, data and experimental results. Future updates are scheduled to include components from other I2O programs such as <a href='http://www.darpa.mil/Our_Work/I2O/Programs/Broad_Operational_Language_Translation_%28BOLT%29.aspx'>Broad Operational Language Translation (BOLT)</a> and <a href='http://www.darpa.mil/Our_Work/I2O/Programs/Visual_Media_Reasoning_%28VMR%29.aspx'>Visual Media Reasoning (VMR)</a>.</p>
<p>The DARPA Open Catalog contains two tables:</p>
<ul>
<li>The Software Table lists performers with one row per piece of software. Each piece of software has a link to an external project page, as well as a link to the code repository for the project. The software categories are listed; in the case of XDATA, they are Analytics, Visualization and Infrastructure. A description of the project is followed by the applicable software license. Finally, each entry has a link to the publications from each team's software entry.</li>
<li>The Publications Table contains author(s), title, and links to peer-reviewed articles related to specific DARPA programs.</li>
</ul>
<p>Report a problem: opencatalog@darpa.mil<p>
"""

def splash_table_header():
  return """
<h2>Catalog Programs:</h2>
<table id='splash' class='tablesorter'> 
<thead> 
<tr> 
    <th>DARPA Program</th> 
    <th>Description</th> 
</tr> 
</thead> 
<tbody> 
"""

def splash_table_footer():
  return """
</tbody> 
</table>
<br>
"""


def software_table_header():
  return """
<table id='software' class='tablesorter'> 
<thead> 
<tr> 
    <th>XDATA Team</th> 
    <th>Software</th> 
    <th>Category</th>
    <th>Instructional Material</th>
    <th>Code</th> 
    <th>Description</th> 
    <th>License</th> 
</tr> 
</thead> 
<tbody> 
"""

def software_table_footer():
  return """
</tbody> 
</table>
<br>
"""

def pubs_table_header():
  return """
<table id='pubs' class='tablesorter'> 
<thead> 
<tr> 
    <th>Team</th> 
    <th>Title</th> 
    <th>Link</th>
</tr> 
</thead> 
<tbody> 
"""

def pubs_table_footer():
  return """
</tbody> 
</table>
<br>
"""

def catalog_page_header(): 
  return """
<html>
<link rel='stylesheet' href='style.css' type='text/css'/>
<script type='text/javascript' src='jquery-latest.js'></script> 
<script type='text/javascript' src='jquery.tablesorter.min.js'></script> 
<script type='text/javascript'>
$(document).ready(function() 
    { 
        $('#software').tablesorter({
		// sort on the first column and second column, order asc 
        	sortList: [[0,0],[1,0]] 
    	}); 
        $('#pubs').tablesorter({
        	sortList: [[0,0],[1,0]] 
    	});
        $('#splash').tablesorter({
		// sort on the first column, order asc 
        	sortList: [[0,0]] 
    	});
    } 
);
function jump(h){
    var url = location.href;
    location.href = "#"+h;
        history.replaceState(null,null,url)
}   
</script>
"""

def catalog_page_footer():
  return """
<br><br><br>
<hr>
<p><a href='http://www.darpa.mil/FOIA.aspx'>FOIA</a> | <a href='http://www.darpa.mil/Privacy_Security_Notice.aspx'>Privacy and Security</a> | 
<a href='http://www.darpa.mil/NoFearAct.aspx'>No Fear Act</a> | <a href='http://www.darpa.mil/External_Link.aspx?url=http://dodcio.defense.gov/DoDSection508/Std_Stmt.aspx'>Accessibility/Section 508</a></p>
</html>
"""