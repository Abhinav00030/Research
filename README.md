# Research of Python
Class of Ticket:
The following characteristics of a support ticket are represented by this class:

ticketNumber: The ticket's special identification number.

staffID: The employee's ID that appears on the ticket that they submitted.

name: The staff member's name.

email: The staff member's email address.

description: An explanation of the problem or inquiry.

reply: The ticket's initial answer, which is by default set to "Not Yet Provided."

status: The ticket's current status, which was originally set to "open."

One unique method that specifies how the ticket object is rendered as a string and is helpful for printing is called __str__. 

Desk Course

These class characteristics are used to handle the ticket gathering process by this class:

ticketNumber: A class-level variable that increases by one with each new ticket, beginning in 2001.

openTickets: An indicator of how many tickets are still available.

closedTickets: A counter that shows how many tickets have been closed.

ticket objects are stored in a list called tickets.

There are various methods in the HelpDesk class:

submitTicket: Adds a new ticket to the list of tickets and creates it. It automatically generates a response, closes the case, and updates the counts if the description includes the phrase "Password change."

respondToTicket: Enables the help desk to reply to a ticket that is currently open. The ticket is closed and the counters are updated if the ticket relates to changing the password.

displayTicket: Prints a ticket's information along with its assigned ticket number.

displayStatistics: Outputs the overall number of tickets filed, together with the numbers of tickets that are open and closed.

Main Function

The primary function replicates the activities of a help desk by:
establishing a HelpDesk class instance.
submitting three tickets, each with a distinct problem.
putting ticket statistics on display.
answering the tickets.
bringing up a closed ticket again.
displaying specific ticket information.
presenting the most recent ticket numbers.
The entry point that runs the simulation is the primary function of the script, which is meant to be executed as a whole.
