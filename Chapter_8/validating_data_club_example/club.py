# club.py

# Club class

class Club:

    def __init__(self, club_name: str, max_members: int):
        self.club_name: str = club_name
        self.max_members: int = max_members
        self.members_list: list[str] = []

    def add_member(self, name: str) -> None:
        # Make sure that there is enough room left
        if len(self.members_list) < self.max_members:
            self.members_list.append(name)

            print(f"OK. {name} has been added to the {self.club_name} club.")

        else:
            print(f"Sorry, but we cannot add {name} to the {self.club_name} club.")
            print(f"This club already has the maximum of {self.max_members} members.")

    def report(self) -> None:
        print()
        print(f"Here are the {len(self.members_list)} members of the {self.club_name} club:")

        for name in self.members_list:
            print(f"    {name}")
            print()
