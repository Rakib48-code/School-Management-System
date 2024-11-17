{
    'name': 'School Management System',
    'version': '1.0',
    'category': 'Education System',
    'summary': 'A complete school management system to manage students, teachers, courses, and more.',
    'author': 'Fahim Hasan',
    'depends': ['base'],
    'data': [
        'views/school_menu.xml',
        'views/student_view_menu.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'description': """
        This School Management System helps to manage students, teachers, courses, 
        and enrollments in a centralized system for educational institutions.

        Key Features:
        - Manage Student Information
        - Manage Teacher Information
        - Course Management
        - Enrollment System
        - Attendance Tracking
        - Grades and Reports
    """,
}
