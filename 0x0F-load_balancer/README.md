# Load balancer

<p align="center">
  <img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/275/qfdked8.png"/>
</p>

## Resource

<details>
<summary>Load balancer</summary><br>
<ul>
  <li>Ever wonder how Facebook, Linkedin, Twitter and other web giants are handling such huge amounts of traffic? They don’t have just one server, but tens of thousands of them. In order to achieve this, web traffic needs to be distributed to these servers, and that is the role of a load-balancer.

  <p align="center">
   <img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/6cefdd14b2f8c36789cba132bd5a10d42d88a177.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220111%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220111T181845Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=792a403303cb0d1faf98b4886f11e22013fa58b709f00d84029ac5877beb6aab" />
  </p>
  <ul>
      <li><a href="https://www.thegeekstuff.com/2016/01/load-balancer-intro/">Load-balancing</a></li>
      <li><a href="https://devcentral.f5.com/s/articles/intro-to-load-balancing-for-developers-ndash-the-algorithms">Load-balancing algorithms</a></li>
  </ul>
  </li>
</ul>
</details>

<details>
<summary>Web stack debugging</summary><br>
<ul>
  <li>Intro
  <ul>Debugging usually takes a big chunk of a software engineer’s time. The art of debugging is tough and it takes years, even decades to master, and that is why seasoned software engineers are the best at it… experience. They have seen lots of broken code, buggy systems, weird edge cases and race conditions.</ul>

  <p align="center">
   <img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/45dffb0b1da8dc2ce47e340d7f88b05652c0f486.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220105%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220105T050302Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d499fde872931932fc76dedd39b4298797482fd9b7ca1fc09f0a885ea8aa1cae" />
  </p>
  </li>
</ul>

<details>
<summary>Test and verify your assumptions</summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/rFMtkCt8/image.png' border='0' alt='image'/></a>
</details>

<ul>
  <li>Debugging is fun
  <ul>Debugging can be frustrating, but it will definitely be part of your job, it requires experience and methodology to become good at it. The good news is that bugs are never going away, and the more experienced you become, trickier bugs will be assigned to you! Good luck 😃</ul>

  <p align="center">
   <img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/bae58c9f066a9668001ef4b4c39778407439d2f9.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220105%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220105T050302Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=67d4c1d736b92bef534ab94427ff3bef2c8ad4b498cafb512fbe6f6ddefec9ba" />
  </p>
  </li>
</ul>

</details>

- [Introduction to load-balancing and HAproxy](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)
- [HAProxy Configuration Basics: Load Balance Your Servers](https://www.haproxy.com/blog/haproxy-configuration-basics-load-balance-your-servers/)
- [The Four Essential Sections of an HAProxy Configuration](https://www.haproxy.com/blog/the-four-essential-sections-of-an-haproxy-configuration/)
- [HTTP Header](https://www.techopedia.com/definition/27178/http-header)
- [Debian/Ubuntu HAProxy packages](https://haproxy.debian.net/)


In this project, I continued to build up the configuration of the web server
issued in project 0x0B. I was issued two additional servers, one to replicate
the Nginx configuration of my original server, and another to set up an HAproxy
load balancer on to manage both web servers.

## Tasks :page_with_curl:

* **0. Double the number of webservers**
  * [0-custom_http_response_header](./0-custom_http_response-header): Bash
  script that installs and configures Nginx on a server with a custom HTTP
  response header.
    * The name of the HTTP header is `X-Served-By`.
    * The value of the HTTP header is the hostname of the server.

* **1. Install your load balancer**
  * [1-install_load_balancer](./1-install_load_balancer): Bash script that
  installs and configures HAproxy version 2.6.6 on a server.
    * Enables management via the init script.
    * Requests are distributed using a round-robin algorithm.
 