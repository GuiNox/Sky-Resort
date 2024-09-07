Before starting the program, remove the two files from the "Código" folder and place them in the same directory where the "data" folder is located.

To start the program:

Open Idle; Open the file modoCliente.py or modoOperador.py; Press F5 or Run. Choose an option:

Check the menu options; Choose and type the desired option; Example modoCliente.py

--- Menu --- 1 - List of Slopes 2 - List of Mechanical Means 3 - Consult Zones 4 - Consult Zone in Detail 5 - Consult Slope in Detail 6 - Search Slopes 7 - Search Mechanical Means Option:

If you chose option 1, a list of slopes will appear with the following information (SlopeCode, Name, StartZone, EndZone, Difficulty, Status);

If you chose option 2, a list of mechanical means will appear with the following information (Name, DepartureZone, ArrivalZone, Status, Type);

If you chose option 3, a list of zones will appear with the following information (ZoneCode, Name, Latitude, Longitude, Altitude, Description);

If you chose option 4, you must enter the zone code, and a list of amenities will appear;

If you chose option 5, you must enter the slope code, and a list of sections that are part of the slope will appear;

If you chose option 6, you must enter the type of search (Start Zone or Difficulty or Status);

--- Search Slope --- Search Type: 1 - Start Zone 2 - Difficulty 3 - Status Option:

If you selected option 1, you will need to enter the zone code, and the slopes that start in that zone will be listed. If you selected option 2, you will need to choose the difficulty from the menu, and the slopes with that difficulty will be listed. If you selected option 3, you will need to choose the status from the menu, and the slopes with that status will be listed. If you chose option 7, you must enter the zone code and then choose the type of alphabetical ordering through a menu, and the mechanical means that start in that zone will be listed in the defined order.

Example modoOperador.py

--- Menu --- 1 - Create Zone 2 - Create Amenities 3 - Create Section 4 - Create Mechanical Means 5 - Create Slope 6 - Change Slope/Mechanical Means Status 7 - Issue Ticket 8 - Issued Tickets 9 - Search Ticket by Period 10 - Search Ticket by Reference Option:

If you selected option 1, you must enter the zone code, which consists of four letters, then enter the zone name, latitude, longitude, altitude, and a description of the zone; If you selected option 2, you must enter the name of the amenity, the associated zone code, and a description of the amenity; If you selected option 3, you must enter the code of the zone where the section starts, then enter the code of the zone where the section ends; If you selected option 4, you must enter the name of the mechanical means, the departure zone code, the arrival zone code, choose the status through the menu (open/closed), and choose the type of mechanical means through another menu (ascending, descending, bidirectional); If you selected option 5, you must enter the name of the slope, the start zone code, the end zone code, select the difficulty through a menu, select the status (open/closed) through another menu, and identify which sections belong to the slope using the section code. When finished, type "fim" to exit; If you selected option 6, you must select Slope or Mechanical Means through a menu, then enter the code of the slope or mechanical means and select the status (open/closed) through a menu; If you selected option 7, you must enter the client's name, nationality, ticket type (d-daily, s-weekly, m-monthly, a-annual), and enter the start date (day, month, year) of validity; If you selected option 8, you will see a list of issued tickets with the following information (ticket reference, person name, nationality, ticket type, and validity); If you selected option 9, you must enter the time interval in the following format (dd/mm/yyyy-dd/mm/yyyy), and you will obtain a list of tickets that are valid during that entire period; If you selected option 10, you must enter the ticket reference, and you will see your ticket with the following information (ticket reference, person name, nationality, ticket type, and validity) and the respective QR code. Notes: To make the QR code function work, you need to install a library in the following way:

bash Copiar código pip install pyqrcode pip install pypng The distance between sections is automatically calculated based on the coordinates of the zones.

modoOperador.py is used by the resort operator with the following functionalities:

Add zones. Add amenities. Add sections. Add mechanical means. Add slopes. Change the status (open/closed) of a slope or mechanical means. Issue tickets. List issued tickets. List tickets issued for a specific day or for a period of days. Search for a ticket by reference. modoCliente.py is used by customers visiting the resort with the following functionalities:

List slopes. List mechanical means. Consult zones. Consult zones in detail (associated amenities). Consult slopes in detail (associated sections). Search for slopes. Search for mechanical means. Data Folder: tabelaZonas.txt (ZoneCode#Name#Latitude#Longitude#Altitude#Description) tabelaComodidades.txt (Name#AssociatedZone#Description) tabelaSeccoes.txt (SectionCode#StartZone#EndZone#Distance) tabelaPistas.txt (SlopeCode#Name#StartZone#EndZone#Difficulty#Status) tabelaSeccoesPistas.txt (AssociatedSlope#AssociatedSection) tabelaMeiosMecanicos.txt (Name#DepartureZone#ArrivalZone#Status#Type) tabelaBilhetes.txt (TicketReference#PersonName#Nationality#TicketType#StartDay#StartMonth#StartYear#EndDay#EndMonth#EndYear) tabelaTipoBilhete.txt (TicketTypeCode#Name#Duration#Description)