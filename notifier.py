
from win10toast import ToastNotifier

n = ToastNotifier()

n.show_toast("GEEKSFORGEEKS", "Notification body", duration = 20,
icon_path ="https://media.geeksforgeeks.org/wp-content/uploads/geeks.ico")
