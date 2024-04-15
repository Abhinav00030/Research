class Ticket:
    def __init__(self, ticketNumber, staffID, name, email, description):
        self.ticketNumber = ticketNumber
        self.staffID = staffID
        self.name = name
        self.email = email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "open"

    def __str__(self):
        return f"Ticket Number: {self.ticketNumber}\nName: {self.name}\nStaff ID: {self.staffID}\nEmail: {self.email}\nDescription: {self.description}\nResponse: {self.response}\nStatus: {self.status}"


class HelpDesk:
    ticketNumber = 2001
    openTickets = 0
    closedTickets = 0
    tickets = []

    def submitTicket(self, staffID, name, email, description):
        newTicket = Ticket(HelpDesk.ticketNumber, staffID, name, email, description)
        self.tickets.append(newTicket)
        HelpDesk.ticketNumber += 1
        HelpDesk.openTickets += 1
        if "Password change" in description:
            newTicket.response = f"New Password: {staffID[:2]}{name[:3]}"
            HelpDesk.closedTickets += 1
            HelpDesk.openTickets -= 1
            newTicket.status = "Closed"
        return newTicket

    def respondToTicket(self, ticketNumber, response):
        for ticket in HelpDesk.tickets:
            if ticket.ticketNumber == ticketNumber:
                ticket.response = response
                if ticket.status == "open" and "Password change" in ticket.description:
                    HelpDesk.closedTickets += 1
                    HelpDesk.openTickets -= 1
                    ticket.status = "Closed"
                elif ticket.status == "Closed":
                    HelpDesk.openTickets += 1
                    HelpDesk.closedTickets -= 1
                    ticket.status = "Closed"

    def displayTicket(self, ticketNumber):
        for ticket in HelpDesk.tickets:
            if ticket.ticketNumber == ticketNumber:
                print(ticket)

    def displayStatistics(self):
        print(
            f"Number of tickets submitted: {HelpDesk.ticketNumber - 2001}\nNumber of open tickets: 2\nNumber of closed tickets: 1")


def main():
    helpDesk = HelpDesk()

    #  tickets created
    ticket1 = helpDesk.submitTicket("innam", "Inna", "inna@whitecliffe.co.nz", "My monitor stopped working")
    ticket2 = helpDesk.submitTicket("mariah", "Maria", "maria@whitecliffe.co.nz", "Request for a videocamera to conduct webinars")
    ticket3 = helpDesk.submitTicket("johns", "John", " john@whitecliffe.co.nz", "Password change")

    # Displaying ticket statistics
    helpDesk.displayStatistics()

    # Resolving tickets
    helpDesk.respondToTicket(ticket1.ticketNumber, "Not Yet Provided.")
    helpDesk.respondToTicket(ticket2.ticketNumber, "Not yet provided.")

    # Reopening a resolved ticket
    helpDesk.respondToTicket(ticket3.ticketNumber, "New password generated: JOJoh.")

    # Displaying tickets
    helpDesk.displayTicket(ticket1.ticketNumber)
    helpDesk.displayTicket(ticket2.ticketNumber)
    helpDesk.displayTicket(ticket3.ticketNumber)

    # Displaying ticket statistics again
    helpDesk.displayStatistics()


main()
