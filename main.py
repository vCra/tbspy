""" GUI version of the program """

import settings
import os.path
if os.path.exists(settings.SQLiteDBLocation):
    pass
    import mainWindow

    mainWindow.run()
else:
    print("Database does not exist")
    print("Please check that the database file location set in settings.py is correct")
    print("Do you want to create a new database now? y/n")
    if input() == "y" or "Y":
        import sql
        print("Imported SQL Module")
        print("Creating Tables")
        try:
            sql.createTables()
            print("Tables Created")
        except:
            print("Unable to create Tables")
        print("Starting GUI")
        import mainWindow
        mainWindow.run()
        print("GUI started")

    else:  
        import os
        os.close()
        