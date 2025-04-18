{
    "name":"Academic Information Management System v1.1",
    "summary":"Create and manage academic information",
    "description":"""
This Module is usage to manage academic information for educational purposes.
""", 
    "author":"Gatot Andi Gunawan",
    "website":"gatotandi.online",
    "category":"Education",
    "version":"1.1",
    "depends":["base"],
    "data":[
        "security/groups.xml",
        "security/ir.model.access.csv",
        "views/menu.xml",
        "views/course.xml",
        "views/session.xml",
        "views/attendee.xml",
        "views/partner.xml",
        "wizard/create_attendee.xml",
    ],
    "installable":True,
    "auto_install":False,
    "application":True,
}