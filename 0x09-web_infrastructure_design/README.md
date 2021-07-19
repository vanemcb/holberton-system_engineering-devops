<div class="project row">
  <div class="col-xs-12 col-md-10 col-lg-8 contains-images">
<h1 class="gap">0x09. Web infrastructure design</h1>
<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to explain to anyone</a>, <strong>without the help of Google</strong>:</p>
<h3>General</h3>
<ul>
<li>You must be able to draw a diagram covering the web stack you built with the sysadmin/devops track projects</li>
<li>You must be able to explain what each component is doing</li>
<li>You must be able to explain system redundancy</li>
<li>Know all the mentioned acronyms: LAMP, SPOF, QPS</li>
</ul>
## Tasks
<h3 class="panel-title">
      0. Simple web stack
    </h3>
<img src="https://i.imgur.com/9s7Y4ZJ.jpg"width="900" height="500"></img>
<div>
<span class="label label-info">
<h4>Mandatory</h4>
</span>
</div>
  </div>
  <div class="panel-body">
    <span id="user_id" data-id="2867"></span>
<p>On a whiteboard, design a one server web infrastructure that hosts the website that is reachable via <code>www.foobar.com</code>. Start your explanation by having a user wanting to access your website.</p>
<p>Requirements:</p>
<ul>
<li> You must use:
<ul>
<li>1 server</li>
<li>1 web server (Nginx)</li>
<li>1 application server</li>
<li>1 application files (your code base)</li>
<li>1 database (MySQL)</li>
<li>1 domain name <code>foobar.com</code> configured with a <code>www</code> record that points to your server IP <code>8.8.8.8</code></li>
</ul></li>
<li>You must be able to explain some specifics about this infrastructure:
<ul>
<li>What is a server</li>
<li>What is the role of the domain name</li>
<li>What type of DNS record <code>www</code> is in <code>www.foobar.com</code></li>
<li>What is the role of the web server</li>
<li>What is the role of the application server</li>
<li>What is the role of the database</li>
<li>What is the server using to communicate with the computer of the user requesting the website</li>
</ul></li>
<li>You must be able to explain what the issues are with this infrastructure:
<ul>
<li>SPOF</li>
<li>Downtime when maintenance needed (like deploying new code web server needs to be restarted)</li>
<li>Cannot scale if too much incoming traffic</li>
</ul></li>
</ul>
<p>Please, remember that everything must be written in English to further your technical ability in a variety of settings.</p>
  </div>
  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. Distributed web infrastructure
    </h3>
<img src="https://i.imgur.com/TUoYo9m.jpg"width="900" height="500"></img>
<div>
        <span class="label label-info">
<h4>Mandatory</h4>
        </span>
    </div>
  </div>
  <div class="panel-body">
    <span id="user_id" data-id="2867"></span>
<p>On a whiteboard, design a three server web infrastructure that hosts the website <code>www.foobar.com</code>.</p>
<p>Requirements:</p>
<ul>
<li> You must add:
<ul>
<li>2 servers</li>
<li>1 web server (Nginx)</li>
<li>1 application server</li>
<li>1 load-balancer (HAproxy)</li>
<li>1 set of application files (your code base)</li>
<li>1 database (MySQL)</li>
</ul></li>
<li>You must be able to explain some specifics about this infrastructure:
<ul>
<li>For every additional element, why you are adding it</li>
<li>What distribution algorithm your load balancer is configured with and how it works</li>
<li>Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both</li>
<li>How a database Primary-Replica (Master-Slave) cluster works</li>
<li>What is the difference between the Primary node and the Replica node in regard to the application</li>
</ul></li>
<li>You must be able to explain what the issues are with this infrastructure:
<ul>
<li>Where are SPOF</li>
<li>Security issues (no firewall, no HTTPS)</li>
<li>No monitoring</li>
</ul></li>
</ul>
<p>Please, remember that everything must be written in English to further your technical ability in a variety of settings.</p>
  </div>
    <div data-role="task1756" data-position="3" id="task-num-2">
      <div class="panel panel-default task-card " id="task-1756">
  <span id="user_id" data-id="2867"></span>
  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      2. Secured and monitored web infrastructure
    </h3>
<img src="https://i.imgur.com/gZex2hU.jpg"width="900" height="500"></img>
<div>
        <span class="label label-info">
<h4>Mandatory</h4>
        </span>
    </div>
  </div>
  <div class="panel-body">
    <span id="user_id" data-id="2867"></span>
<!-- Progress vs Score -->
<!-- Task Body -->
<p>On a whiteboard, design a three server web infrastructure that hosts the website <code>www.foobar.com</code>, it must be secured, serve encrypted traffic, and be monitored.</p>
<p>Requirements:</p>
<ul>
<li> You must add:
<ul>
<li>3 firewalls </li>
<li>1 SSL certificate to serve <code>www.foobar.com</code> over HTTPS</li>
<li>3 monitoring clients (data collector for Sumologic or other monitoring services)</li>
</ul></li>
<li>You must be able to explain some specifics about this infrastructure:
<ul>
<li>For every additional element, why you are adding it</li>
<li>What are firewalls for</li>
<li>Why is the traffic served over HTTPS</li>
<li>What monitoring is used for</li>
<li>How the monitoring tool is collecting data</li>
<li>Explain what to do if you want to monitor your web server QPS</li>
</ul></li>
<li>You must be able to explain what the issues are with this infrastructure:
<ul>
<li>Why terminating SSL at the load balancer level is an issue</li>
<li>Why having only one MySQL server capable of accepting writes is an issue</li>
<li>Why having servers with all the same components (database, web server and application server) might be a problem</li>
</ul></li>
</ul>
<p>Please, remember that everything must be written in English to further your technical ability in a variety of settings.</p>
