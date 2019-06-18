import csv
from trello import TrelloClient

# Put here your credentials
client = TrelloClient(
    api_key='API_KEY',
    token='TOKEN'
)

def get_label(labels, label_name):
    return next(filter(lambda label: label.name == label_name, labels))

# Put here your board id
board = client.get_board("BOARD_ID")

# Discover list
# for list in board.list_lists():
#     print(list.name + ": " + list.id)

board_labels = board.get_labels()

# Put here columns definition
todo_list = board.get_list("7d3895565ecd152b7d30d61e")
doing_list = board.get_list("4d189358d5f34a6eb0f41c8a")
done_list = board.get_list("2d08934c44d37b268a8a1ecd")

# Read file
with open('sample.csv') as csv_file:
    csv_dict = csv.DictReader(csv_file)

    for row in csv_dict:

        # Map CSV columns
        name = row["Summary"]
        description = row["Description"]
        status = row["Status"]
        issue_type = row["Issue Type"]

        # add card
        card = None
        if status == "To Do":
            card = todo_list.add_card(name=name, desc=description)
        elif status == "In Progress":
            card = doing_list.add_card(name=name, desc=description)
        elif status == "Done":
            card = done_list.add_card(name=name, desc=description)
        else:
            card = todo_list.add_card(name="Deleted issue")
            continue

        # Add labels indicating issue type
        card.add_label(get_label(board_labels, issue_type))

        print("Added card: " + name + " to " + status)


