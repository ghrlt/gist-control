from gist_control import Gist


gctrl = Gist( input("Oauth Token? ") )



# Get a gist
g = gctrl.get(gist_id=input("Gist ID? "))

# Star a gist
gctrl.star(gist_id=g['id'])

# Unstar a gist
gctrl.unstar(gist_id=g['id'])



#		 ~ GISTS COMMENTS ~ 		#

# Get gist comments
comments = gctrl.get_comments(gist_id=g['id'])

# Add a comment to gist
c = gctrl.comment(gist_id=g['id'], content="Waouh! That is awsome.")

# Get gist comment
c = gctrl.get_comment(gist_id=g['id'], comment_id=c['id'])

# Edit a gist comment you made
c = gctrl.edit_comment(gist_id=g['id'], comment_id=c['id'], new_content="Waouh! That's awesome!")

# Delete a gist comment
gctrl.delete_comment(gist_id=g['id'], comment_id=c['id'])



#		 ~ YOUR GISTS ~ 		#

# Create a gist
g = gctrl.create(
	description="Created using ghrlt/gist-control",
	files=[
		{
			"name": "my-example-file.py",
			"content": "import gist_control\n\ngists = gist_control.Gist(input('Token: '))"
		}
	],
	public=False
)


# Update a gist description
g_obj = gctrl.update(gist_id=g['id'], description="Updated using ghrlt/gist-control")


# Update a gist file
g_obj = gctrl.update_file(
	gist_id=g['id'], filename="my-example-file.py",
	new_name="my-example-file-2.py"
)


# Add a file to gist | /!\ If filename already exists, it'll edit existing file!
g_obj = gctrl.add_file(
	gist_id=g['id'],
	filename="my-example-file-3.py",
	content="print('hi')\nfor _ in range(25):\n\tprint('^', end='')"
)


# Delete a file from gist
g_obj = gctrl.delete_file(gist_id=g['id'], filename="my-example-file-2.py")


# Delete a gist
gctrl.delete(g['id'])
