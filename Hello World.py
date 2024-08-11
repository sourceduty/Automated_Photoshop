from photoshop import Session

# Create a session to interact with Photoshop
with Session() as ps:
    # Create a new document
    doc = ps.app.documents.add()

    # Set the text layer properties
    text_layer = doc.artLayers.add()
    text_layer.kind = ps.LayerKind.TextLayer
    text_item = text_layer.textItem
    text_item.contents = "Hello World"
    text_item.position = [100, 100]
    text_item.size = 48
    text_item.font = "ArialMT"  # Directly set the font name

    # Set the text color (black in this case)
    text_color = ps.SolidColor()
    text_color.rgb.red = 0
    text_color.rgb.green = 0
    text_color.rgb.blue = 0
    text_item.color = text_color

    # Save the document
    saveOptions = ps.JPEGSaveOptions(quality=10)
    doc.saveAs(r"C:\path_to_save\hello_world.jpg", saveOptions, asCopy=True)
