# Project 2 Reflection

## Attacks

### Attack 1 - HTTP Flood
The first attack I attempted was an HTTP flood attack, in which my server
would inundate Allison and Alicia's server with HTTP GET requests.
Initially, I tried to set up a while loop that repeatedly sent GET requests.
This did not work, because it was sending successive requests instead of concurrent requests.
Upon realizing this, I searched how to perform a DoS attack, and found this website: https://www.neuralnine.com/code-a-ddos-script-in-python/.
The DDoS script it provided used the threading library to multithread and
used ```socket.sendto()``` instead of ```requests.get()``` (which is what I originally used).
The script from www.neuralnine.com was more successful that my initial attempt,
in that it did not produce several errors.
However, it was only somewhat successful. Sometimes it seemed
to slow down Allison and Alicia's web server, but ultimately requests
were still going through.

### Attack 2 - HTTP Flood with IP Spoofing (Attempt)
Next, Allison and Alicia began implementing a way to filter
traffic based on IP address, so I tried to find a way to spoof
the IP address in the packets I was sending. My first attempt involved
generating a random IP address and including it in the host header of
the HTTP GET request. When I began the HTTP flood again, it did appear
that they were receiving packets from the randomized IP addresses. However,
at that point their IP filtration feature wasn't working yet so I was uncertain whether
the IP spoofing was successful against that type of defense.


Later on, I tried the IP spoofing on my own web server after I implemented IP filtration.
However, for some reason, the http flood script began producing errors
when the host headers were sent. The requests that did go through were all recorded as
originating from the same IP address. I find it strange that the same script
produced very different results, and I'm still not sure why.

A more sophisticated version of IP spoofing would involve
encoding the entire packet from scratch, as then I could directly alter the
source address in the IP header, instead of just in the HTTP request.

### Attack 3 - SYN Flood (Attempt)
The final attack I attempted was a SYN flood. As included in the reading,
the methodology behind the SYN flood attack is to initiate
TCP security handshakes, but never send back the final ACK.
Their server would be forced to wait for this ACK until it's
obvious that network congestion wasn't delaying it, and that
waiting would allow my script to take up resources on their server.
I used the script from this website (https://www.thepythoncode.com/article/syn-flooding-attack-using-scapy-in-python)
to initiate the SYN flood attack. However, I was unable to resolve errors that occurred
as a result of my inability to configure scapy correctly.
Afterward, I tried a different script I found on this website (https://systemweakness.com/ping-and-syn-flood-attacks-with-python-and-scapy-6e4515435492)
but unfortunately it also required the use of scapy and I could not figure
out why it was misconfigured on my laptop.

## Defense
The first person to attack my server was Elaine Z, who used an HTTP flood attack.
There wasn't much indication from my point of view, reading the server output,
that my server was being attacked. It looked like my server was rapidly
accepting requests; however, there were no errors or other output indicating
that my server was overwhelmed with get requests.

To counter the attack, I first modified my server so that it would not send data back
to an IP address which made two consecutive requests. However, this still required
my server to accept and read the IP address of the incoming request, and since I didn't
initially realize that I needed to close the connection, this still allowed my
server to become overwhelmed. Closing the connection socket seemed to work, as I was
able to access my server on my own device while Elaine Z was attacking it.

I then modified my server to use a more sophisticated method where it kept track
of IP addresses and the number of requests in a dictionary, and blacklisted IPs 
with more than a certain number of requests. However, strangely,
this implementation did not prevent Elaine Z from toppling my server. This makes
me wonder whether my initial method, of cancelling consecutive requests, actually worked,
or if I happened to get lucky when I was able to access my webpage from my phone during the attack.

After this, Allison and Alicia tried attacking my server, but none of the requests came through.
While I would love to think that was due to my filtration program, we're fairly certain
their attack script wasn't yet working.

Having read online about DoS attacks, my current understanding is that it can be difficult
to circumvent attacks against your own server from the vantage point of that server, because
it still has to read in information about incoming traffic to determine how to filter requests.
(https://developer.okta.com/books/api-security/dos/how/#rate-limiting) Several sources, including
developer.okta.com linked above, explain that an effective way to deal 
with DoS attacks is to use mitigation centers/services for filtering traffic, so that way your server
isn't responsible for checking every request. Thus, if my server was actually housing
an important website, I might choose to pay for one of those services.

## References
I received help from Phuong during TA hours. Additionally, I used the following
websites to find code for my attacks:
* https://www.neuralnine.com/code-a-ddos-script-in-python/
* https://www.thepythoncode.com/article/syn-flooding-attack-using-scapy-in-python
* https://systemweakness.com/ping-and-syn-flood-attacks-with-python-and-scapy-6e4515435492

I found general information about attack/defense methods from these sources:
* https://developer.okta.com/books/api-security/dos/how/#rate-limiting
* (Recommended reading) https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/