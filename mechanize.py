<title>All hail mecanize: A powerful python library</title>
		<link>http://www.security.securethelock.com/?p=221</link>
		<pubDate>Wed, 30 Nov -0001 00:00:00 +0000</pubDate>
		<guid isPermaLink="false">http://security.securethelock.com/?p=221</guid>
		<description></description>
		<content:encoded><![CDATA[
In this article will look at a very important functionality which can be used to emulate programmatically for 
web application security, which is parsing the form and its submission, and we will do this using Mechanize.

<strong>Mechanize</strong> is a very useful Python module for navigating through web forms. It is based on the 
Perl module WWW : Mechanize. It allows for stateful programming and browser emulation. It is a very powerful 
framework for doing stateful programming and inspection in web applications.
<pre class="lang:python decode:true">import mechanize

br = mechanize.Browser()

br.open('http://security.securethelock.com/')

for form in br.forms() :

    print form</pre>
First we will create a browser object by calling the function <strong>mechanize.browser()</strong>. We will use an 
external url and then open it. Here we will use the securethelock.com website for example purposes. To open the url,
use the <strong>br.open()</strong> function and as the argument pass the url that you want to open. The whole idea 
is to fill up the search field and submit the form and then to parse the response. So first select the specific 
element you are interested in.
<pre class="lang:python decode:true">br.select_form(nr=0)

br.form['s'] = 'python'

br.submit()</pre>
The function<strong> br.select_form(nr = 0)</strong> refers to selecting the first form, so all the activities will 
happen in the form's context. So to fill up the values, use br.form['s'] after selecting the specific form. After
filling the search field, you submit the form. To submit the form all you have to do is call the submit method 
(<strong>br.submit()</strong> )and then get a response.

To get the links that the form returns,
<pre class="lang:python decode:true">for link in br.links() :

    print link

for link in br.links() :

    print link.url + ' : ' + link.text      // list of links and the anchor texts which are used.</pre>
We can also see the external urls that the site links to. By using a library called htmldiff we can register the
changes by mining a static webpage which doesn't change. We would also be able to find the newer links that come in.

Now we will look at how to browse an application, replicate things like click links, form submission and maintain 
state using cookies via mechanize.
<pre class="lang:python decode:true">import mechanize

br = mechanize.Browser()

br.set_handle_robots(False)

br.open('https://accounts.google.com/ServiceLogin?service=mail&amp;passive=true&amp;rm=false&amp;continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&amp;ss=1&amp;scc=1&amp;ltmpl=default&amp;ltmplcache=2&amp;hl=en&amp;emr=1&amp;elo=1')

</pre>
We will use the url of gmail, to sign into our gmail account. While we try to login we might encounter the 
<strong>HTTP Error 403: request disallowed by robots.txt</strong> error, a way around this is to tell mechanize 
to ignore the robots.txt file. We can do this by using <strong>br.set_handle_robots(False). </strong>

&nbsp;
<pre class="lang:python decode:true">for form in br.forms() :

    print form

br.select_form(nr = 0)

br.form['Email'] = 'durga'     // this is for example purposes ;)

br.form['Passwd'] = 'password'

br.submit()</pre>
You can submit your actual email-id and password and after that we will view the response page to see if we have 
successfully logged in. And to make sure that we are inside we will print the link.
<pre class="lang:python decode:true ">print br.response.read()

for link in br.links() :

    print link.url + ' : ' + link.text</pre>
Now we have successfully logged into the application, and the cookie, the sessions are all taken care of by 
mechanize, and now we are browsing within the application. Now we will create a new link which we want to follow

Using<strong> click_link()</strong> we find the link that we are interested in and we have the browser to click it.

We can login to an application with usernames and passwords, and go ahead and follow links, click on them all in a
stateful way where mechanize takes care of things like the cookies.

Note:-

Mechanize is not installed by default, so you have to install it using easy_install.]]></content:encoded>