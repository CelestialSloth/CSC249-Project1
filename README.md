# Project 1 Details and Reflection
## File breakdown
### webserver.py
webserver.py has two methods: `thread` and `Main`.

The `thread` method contains all of the code that must be
executed in each thread, each time the server is used.
This includes receiving a message through the connection socket,
parsing the requested filename, and sending the file.

The `Main` method sets up the server socket.
Then, each time the server socket receives a connection request,
a new thread is created. Threading is managed by the concurrent.futures
library recommended by Minh Phuong Phan.

### client.py
client.py has just one main method. `main` requires three
arguments, inputted from the command line, and then uses
the `requests` library to request the inputted webpage.

I used `sys.argv` to grab arguments entered into the terminal.
If an incorrect number of arguments are entered, the program
assumes you are trying to access the `HelloWorld.html` file running
located on a server on your device.

## Notes
I assumed that the phrase "display the server response as an output"
means to print the requested page/other response to the console.
I also assumed that the user trying to access the wrong port was not
something that we needed to handle for this assignment.

## References
I worked on phases 1-2 of this project with Ramsha Rauf.

Minh Phuong Phan helped me a lot with the first two phases,
particularly phase 2, which involved threading. For phase 2,
I also found the [`concurrent.futures` documentation](https://docs.python.org/3/library/concurrent.futures.html)
to be useful.

Additionally, the following resources were used:
* This [stackoverflow post](https://stackoverflow.com/questions/8315209/sending-http-headers-with-python), 
which showed what types of messages to send through `connectionSocket`.
* Another [stackoverflow post](https://stackoverflow.com/questions/41852380/how-to-abort-a-python-script-and-return-a-404-error),
which showed how to set up a 404 error page.
* This [tutorialspoint page](https://www.tutorialspoint.com/python_network_programming/python_http_client.htm),
showing how to use `requests.get()`.
* Finally, another [tutorialspoint page](https://www.tutorialspoint.com/python/python_command_line_arguments.htm),
showing how to use the `sys` library to accept command line arguments.