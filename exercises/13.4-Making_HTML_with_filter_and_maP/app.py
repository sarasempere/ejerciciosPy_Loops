all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def generate_li(item):
    return "<li>" + item["label"] + "</li>"

def filter_colors(item):
    if item["sexy"]:
        return item

expected = list(filter(filter_colors, all_colors))
expected_map = list(map(generate_li, expected))

print(expected_map)