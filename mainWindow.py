import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkObjects import MultiListbox as MultiListBox
import sql
root = tk.Tk()
def run():
    """ Create and run GUI """
    global root
    def onExit():
        root.destroy()
    def onViewEvents():
        eventList()
    def onViewVenues():
        pass
    def onBookTickets():
        pass
    def onSearch():
        SearchScreen()
    def onAdmin():
        AdminMenu()
    def onBookEventTicket():
        ##This is for when the button below the Events selector is pressed
        pass
    logo = tk.PhotoImage(file="Untitled.png")
    w = tk.Label(root, image=logo)
    w.grid(row=1,column = 1, columnspan = 6)
    BtnViewVenues = tk.Button(root, text=('View Venues'), command=onViewVenues, width=10)
    BtnViewEvents = tk.Button(root, text=('View Events'), command=onViewEvents, width=10)
    BtnBookTickets = tk.Button(root, text=('Book Tickets'), command=onBookTickets, width=10)
    BtnSearch = tk.Button(root, text=('Search'), command=onSearch, width=10)
    BtnAdmin = tk.Button(root, text=('Admin'), command=onAdmin, width=10)

    BtnViewVenues.grid(row = 2, column = 1)
    BtnViewEvents.grid(row = 2, column = 2)
    BtnBookTickets.grid(row = 2, column = 3)
    BtnSearch.grid(row = 2, column = 5)
    BtnAdmin.grid(row = 2, column = 6)

    LblEvents = tk.Label(root, text="Events")
    LblEvents.grid(row=3,column =1)

    LblMyOrder = tk.Label(root, text="My Order")
    LblMyOrder.grid(row=3,column =4)

    LblMyOrder = tk.Label(root, text="Venues")
    LblMyOrder.grid(row=5,column =1)

    ###Events Selector

    MlbEvents = MultiListBox(root, (('ID', 3), ('Event', 30)))
    for i in sql.event.all():
        MlbEvents.insert(tk.END, (i[0],i[1]))
    MlbEvents.grid(row=4,column = 1, columnspan=3)
    
    ## Current Order List

    MlbOrder = MultiListBox(root, (('ID', 3), ('Event',20), ('Qnty', 4)))
    #for i in sql.event.all():
    #    MlbOrder.insert(tk.END, (i[0],i[1]))
    MlbOrder.grid(row=4,column = 5, columnspan=2, rowspan = 1)

    ## Venue Selector

    MlbVenue = MultiListBox(root, (('ID', 3), ('Venue', 30)))
    for i in sql.venue.all():
        MlbVenue.insert(tk.END, (i[0],i[1]))
    MlbVenue.grid(row=6,column = 1, columnspan=3)

    root.resizable(0,0)


    root.title("Event Booking System")
    root.mainloop()
    
def SearchScreen():
    window = tk.Toplevel()
    window.title("Search")
    def onSearch():
        searchTerm = EntSearch.get()
        print(searchTerm)
        if searchFor == 1:
            ## Searching for an event
            pass
        elif searchFor == 2:
            ## Searching for a venue
            pass
    searchTerm = ""
    EntSearch = tk.Entry(window)
    searchFor = 1
    # 1 is Event
    # 2 is Venue
    LblSearchFor = tk.Label(window,text="Search For")
    RdoEvent = tk.Radiobutton(window, text="Event", variable=searchFor, value=1)
    RdoVenue = tk.Radiobutton(window, text="Venue", variable=searchFor, value=2)
    BtnSearch = tk.Button(window,text="Search", command=onSearch, width=10)

    LblSearchFor.grid(row=1,column=1)
    EntSearch.grid(row=1,column=2)
    RdoEvent.grid(row=3,column=1)
    RdoVenue.grid(row=3,column=2)
    BtnSearch.grid(row=4,column=2)
    window.resizable(0,0)
def AdminMenu():
    master = tk.Toplevel()
    master.title("Admin Interface")
    def onCreateEvent():
        eventDetails(None)
    def onCreateVenue():
        pass
    def onGotoEvent():
        event=input("Event ID: ")
        eventDetails(event)
        pass
    tk.Label(master, text="some stuff goes here").pack()
    tk.Button(master, text = "Add Event", command= onCreateEvent).pack()
    tk.Button(master, text = "Add Venues", command= onCreateVenue).pack()
    tk.Button(master, text = "Goto Event", command= onGotoEvent).pack()
    master.resizable(0,0)
def eventDetails(event):
    def onSubmit():
        if Valid():
            if event==None:
                ###Create a new event
                pass
            else:
                ### Event already exists, append the event, rather than createing a new event
                sql.event
    def Valid():
        return True
    master = tk.Toplevel()
    master.title("Event Details")
    tk.Label(master, text="Name").grid(row=0)
    tk.Label(master, text="Details").grid(row=1)
    tk.Label(master, text="Date").grid(row=2)
    tk.Label(master, text="Time").grid(row=3)
    tk.Label(master, text="Venue").grid(row=4)
    tk.Label(master, text="Website").grid(row=5)
    tk.Button(master, text="Submit").grid(row=6, column = 0)
    e1 = tk.Entry(master)
    e2 = tk.Entry(master)
    e3 = tk.Button(master, text = "Calender")
    e4 = tk.Entry(master)
    e5 = tk.Button(master, text="Venues")
    e6 = tk.Entry(master)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    e5.grid(row=4, column=1)
    e6.grid(row=5, column=1)
    master.resizable(0,0)
    if event == None:
        pass
    else:
        print("hi")
        event=sql.event.get(event)
        e=event[0]
        e1.insert(tk.END,string=str(e[1]))
        e2.insert(tk.END,string=str(e[2]))
        e4.insert(tk.END,string=str(e[4]))
        e6.insert(tk.END,string=str(e[6]))
        

def onViewVenues():
    pass

def calender():
    import sys
    from tkObjects import Calendar
    import calendar as date
    window = tk.Toplevel()
    window.title('Ttk Calendar')
    ttkcal = Calendar(firstweekday=date.SUNDAY, master=window)
    ttkcal.pack(expand=1, fill='both')

    if 'win' not in sys.platform:
        style = ttk.Style()
        style.theme_use('clam')
    def onOK():
        print(ttkcal.selection_get())
    okButton = tk.Button(window, text = ("Ok"), command = onOK, width=10).pack(side=tk.BOTTOM)
    window.resizable(0,0)
def eventList():
    global root
    from tkObjects import MultiListbox as MultiListBox
    import sql
    def onGo():
        try:
            ## If nothing is selected, it will break... We need to prevent this...
            selected = mlb.curselection()
            selectedEvent = mlb.get(selected)[0]
            eventDetails(selectedEvent)
        except:
            errorBox("Nothing is selected")
    window = tk.Toplevel(root)
    mlb = MultiListBox(window, (('ID', 3), ('Event', 40), ('Date', 10)))
    for i in sql.event.all():
        mlb.insert(tk.END, (i[0],i[1],i[2]))
    mlb.pack(expand=tk.YES,fill=tk.BOTH)
    goButton = tk.Button(window, text = ("Go"), command = onGo, width=10).pack(side=tk.BOTTOM)
    window.resizable(0,0)

def errorBox(text):
    title = "Error"
    messagebox.showwarning(title,text)

def nothing():
    print("Nothing happened")
    pass


