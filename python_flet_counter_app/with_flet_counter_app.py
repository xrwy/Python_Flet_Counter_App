import flet as ft

def Counter(page: ft.Page):
    page.title = "Flet Counter Example"
    page.vertical_alignment = "center"

    txtNumber = ft.TextField(value="0", text_align="center", width=100)
    txtNumber.read_only = True


    def decrement(e):
        try:
            txtNumber.value = int(txtNumber.value) - 1
            page.update()
        except ValueError as  error:
            print(f"Error : {error}")

    def increment(e):
        try:
            txtNumber.value = int(txtNumber.value) + 1
            page.update()
        except ValueError as error:
            print(f"Error : {error}")

    def windowClose(e):
        page.window_close()


    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=decrement),
                txtNumber,
                ft.IconButton(ft.icons.ADD, on_click=increment),
            ],
            alignment="center",
        ),
        ft.Row (
            [
                ft.IconButton(ft.icons.CLOSE, on_click=windowClose)
            ],
            alignment="center"
        )
    )


ft.app(target=Counter)