+++
title = "5 Reasons Why You Should Use CloudFlare With Your Website"
description = ""
date = 2015-11-03T00:55:13
updated = 2018-08-22T08:21:16
draft = false
slug = "5-reasons-why-you-should-use-cloudflare-with-your-website"
aliases = ['2015/11/03/5-reasons-why-you-should-use-cloudflare-with-your-website/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = ["Cloudflare", "Hosting"]
+++


Recently I migrated this blog from GoDaddy to a Virtual Machine on Microsoft
Azure. Migration is not an easy process. What I feared the most during the
migration is the downtime. I had kept the original domain name with me. But
since, I was migrating from one host to another host with entirely different
platform (From Apache on shared web hosting to NGINX on a virtual private
server), I was hoping that the users would notice at least few hours of downtime
since it takes some time for DNS to propagate.

But, I was completely wrong. Since I was using Cloudflare, the downtime was
reduced to a single minute. Since I was so impressed with Cloudflare, I thought
that it would be a good idea to write an article on why you should also use
Cloudflare with your website.

1. Migration made easy
Like I said before, it took only a minute for the site to get back up and
running on a completely different host. Cloudflare has got 63 data centers
[https://www.cloudflare.com/network-map/] (as of writing) and is constantly
adding more data centers to that list. During my first setup with GoDaddy, I had
configured the Name Servers of the domain (omgdebugging.com
[http://omgdebugging.com]) to point towards the Name Servers of Cloudflare. So,
all I did was simply going to the Cloudflare dashboard and edit the existing DNS
record to point to the newly provisioned Virtual Private Server. No more waiting
for DNS to propagate. Furthermore, you can enable/disable Cloudflare with a
single button click.

[![Cloudflare](http://i0.wp.com/omgdebugging.com/wp-content/uploads/2015/11/Cloudflare-DNS-1024x449.png?fit=730%2C320)](http://i0.wp.com/omgdebugging.com/wp-content/uploads/2015/11/Cloudflare-DNS.png)How
Cool is that huh?## 2. Advanced Protection & AnalyticsCloudflare provides
advanced blocking of threats and superior DDOS protection. Cloudflare allows to
enable advanced DDOS mitigation at the single click of a button on the
dashboard. There is the story of the largest DDOS attack which almost broke the
internet in which Cloudflare mitigated the attack and the site owner did not
even notice that the site was under attack. It also blocks malicious users from
trying to hack your website. Cloudflare also provides vivid analytics in the
form of graphs, pie charts and tables which help you in understanding the kind
of traffic you are getting from around the world.

[![Cloudflare](http://i0.wp.com/omgdebugging.com/wp-content/uploads/2015/11/Cloudflare-Analytics-1024x448.png?fit=730%2C319)](http://i1.wp.com/omgdebugging.com/wp-content/uploads/2015/11/Cloudflare-Analytics.png)A
view of the Analytics section of the Cloudflare Dashboard.## 3. CDN (Content
Delivery Network)One more advantage of using Cloudflare is that it caches the
websites and serves the cached content to the visitors so that the host machine
has to do less work. It also automatically minifies the HTML, JS and CSS so that
the user experience is improved. One more advantage is that the outbound data
transfer is reduced (which is chargeable in Azure after a certain limit) due to
caching which helps me in keeping the costs down. The biggest benefit is that
even if your website goes down in case of some unforeseen circumstances or you
are simply performing an upgrade, Cloudflare would automatically serve the pages
from its cache so your visitors do not experience any kind of downtime.

4. SSL Certificate
Yep. Cloudflare provides SSL certificates to the websites it supercharges. So,
without any setup, I can have the visitors visit this blog on a secure
connection. Try accessing this blog using https://omgdebugging.com . It works!
(Some images might be broken. I will fix them once the weekend comes). Best
thing about this is that you do not have to buy and setup a SSL certificate from
the known vendors which again costs around $100. One thing to remember is that
the SSL connection provided is between the user and Cloudflare. The SSL
connection is not established between Cloudflare and the Host by default (You
need to set it up manually). In case you would like to set up the SSL
certificate, I would suggest following Troy Hunt’s blog post over here – 
http://www.troyhunt.com/2015/04/how-to-get-your-ssl-for-free-on-shared.html

[![Cloudflare](http://i2.wp.com/omgdebugging.com/wp-content/uploads/2015/11/Cloudflare-SSL-1024x524.png?fit=730%2C374)](http://i0.wp.com/omgdebugging.com/wp-content/uploads/2015/11/Cloudflare-SSL.png)Free
SSL Certificate. Much WoW!## 5. It’s FREEAll of the above features mentioned are
free in the FREE Tier of Cloudflare. Yep. This is the best part. Even the SSL
Certificate is provided for free. There are paid tiers as well but my needs are
fulfilled by the Free Tier. You can add unlimited number of websites to the Free
Tier. There are paid plans as well which you can check over here – 
https://www.cloudflare.com/plans/

In case you would like to set up Cloudflare for your website, feel free to
follow the instructions at this link – 
https://support.cloudflare.com/hc/en-us/articles/201720164-Step-2-Create-a-CloudFlare-account-and-add-a-website

If you have any doubts or queries, feel free to post in the comments. Have a
nice day!