class User:
    """Simple class representing user in WebApp"""

    def __init__(self, first_name, last_name, age, email, status) -> None:
        """Initialize attributes to describe a user."""
        self.first = first_name
        self.last = last_name
        self.age = age
        self.email = email
        self.status = status
        self.login_attempts = 0
    
    def describe_user(self):
        """User the attibutes of the user and describe it."""
        print(f"Hello {self.first} {self.last}, we're glad that you're {self.status}. You have logged in {self.login_attempts} in last 24 hours.")

    def increment_login(self, increment):
        """Add number of logins to default value."""
        self.login_attempts += increment

    def restart_login_counter(self):
        """Restart to counter back to default value."""
        self.login_attempts = 0

class Admin(User):
    """Simple subclass of User class defining a special case of user."""

    def __init__(self, first_name, last_name, age, email, status) -> None:
        """Initialize the admin user using the parent class attributes and adding more."""
        super().__init__(first_name, last_name, age, email, status)

        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_priviledges(self):
        """Name all the actions that admin can do."""

        print("Admin can do all this:")
        for action in self.privileges:
            print(f"- {action}")


peter_the_admin = Admin('Peter', 'TheAdmin', 28, 'peter@admin.com', 'Online')
peter_the_admin.describe_user()
peter_the_admin.show_priviledges()
