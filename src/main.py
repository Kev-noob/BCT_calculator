
import flet as ft



#Codes for Designs>
def Top_Container_codes(page):
    # -----------------------------------TITTLE--------------------------------------------
    tittle = ft.Text(
        "WELCOME!",
        size=35,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.LEFT,
        color="#6E0101",
    )
    tittle_under = ft.Text(
        "BCT Tuition Calculator",
        size=16,
        text_align=ft.TextAlign.LEFT,
        color="#6E0101",
    )

    # -----------------------------------TEXTBOXES--------------------------------------------

    txtBox_1 = ft.TextField(
        label="Total Units",
        hint_text="No.of total units (1-25).",

        bgcolor="#FFFFFF",
        border_color="#6E0101",
        focused_border_color="#FFFFFF",
        label_style=ft.TextStyle(color="#6E0101"),
        hint_style=ft.TextStyle(color="#888888"),
        text_style=ft.TextStyle(color="#6E0101"),
        keyboard_type=ft.KeyboardType.NUMBER,
    )
    txtBox_2 = ft.TextField(
        label="Laboratory Subjects",
        hint_text="No. of lab subjects (1-5).",

        bgcolor="#FFFFFF",
        border_color="#6E0101",
        focused_border_color="#FFFFFF",
        label_style=ft.TextStyle(color="#6E0101"),
        hint_style=ft.TextStyle(color="#888888"),
        text_style=ft.TextStyle(color="#6E0101"),
        keyboard_type=ft.KeyboardType.NUMBER,
    )
    txtBox_3 = ft.TextField(
        label="Hands-on Subjects",
        hint_text="No. of hands-on subjects (1-5).",

        bgcolor="#FFFFFF",
        border_color="#6E0101",
        focused_border_color="#FFFFFF",
        label_style=ft.TextStyle(color="#6E0101"),
        hint_style=ft.TextStyle(color="#888888"),
        text_style=ft.TextStyle(color="#6E0101"),
        keyboard_type=ft.KeyboardType.NUMBER,
    )
    txtBox_4 = ft.TextField(
        label="Down Payment (Optional)",
        hint_text="Enter amount.",

        bgcolor="#FFFFFF",
        border_color="#6E0101",
        focused_border_color="#FFFFFF",
        label_style=ft.TextStyle(color="#6E0101"),
        hint_style=ft.TextStyle(color="#888888"),
        text_style=ft.TextStyle(color="#6E0101"),
        keyboard_type=ft.KeyboardType.NUMBER,
    )
    # -----------------------------------BUTTONS--------------------------------------------

    btn_calculate = ft.Button(
        content="Calculate",
        width=float("inf"),
        style=ft.ButtonStyle(
            bgcolor={
                ft.ControlState.DEFAULT: "#FFFFFF",
                ft.ControlState.HOVERED: "#C50D0D",
            },
            color={
                ft.ControlState.DEFAULT: "#6E0101",
                ft.ControlState.HOVERED: "#FFFFFF",
            },
            shape=ft.RoundedRectangleBorder(radius=5),
        ),
    )
    calculate_btn_container = ft.Container(
        content=btn_calculate,
        expand=3,
        border_radius=5,
        shadow=ft.BoxShadow(
            spread_radius=0,
            blur_radius=2,
            color="#6E0101",
            offset=ft.Offset(0, 2),
        ),
    )

    reset_btn = ft.Button(
        content="Reset",
        width=float("inf"),
        style=ft.ButtonStyle(
            bgcolor={
                ft.ControlState.DEFAULT: "#FFFFFF",
                ft.ControlState.HOVERED: "#C50D0D",
            },
            color={
                ft.ControlState.DEFAULT: "#6E0101",
                ft.ControlState.HOVERED: "#FFFFFF",
            },
            shape=ft.RoundedRectangleBorder(radius=5),
        ),
    )
    reset_btn_container = ft.Container(
        content=reset_btn,
        border_radius=5,
        expand=2,
        shadow=ft.BoxShadow(
            spread_radius=0,
            blur_radius=2,
            color="#6E0101",
            offset=ft.Offset(0, 2),
        ),
    )

    # -----------------------------------MAIN CONTAINER--------------------------------------------
    top_margin = round((page.height or 852) * 0.10)

    main_container = ft.Container(
        content=ft.Column(
            [
                ft.Column(
                    [
                        tittle,
                        tittle_under,
                    ],
                    spacing=0,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                ),
                ft.Divider(
                    color="#6E0101",
                    thickness=1,
                ),

                txtBox_1,
                txtBox_2,
                txtBox_3,
                txtBox_4,

                ft.Divider(
                    color="#6E0101",
                    thickness=1,
                ),

                ft.Row(
                    controls=[
                        calculate_btn_container,
                        reset_btn_container,
                    ],
                    spacing=15,
                ),

            ],
            tight=True,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            spacing=8,
        ),
        padding=20,
        margin=ft.Margin(
            left=20,
            bottom=0,
            right=20,
            top=top_margin,
        ),
        border_radius=10,
        bgcolor="#CCFFFFFF",


        shadow=ft.BoxShadow(
            spread_radius=5,
            blur_radius=4,
            color="#40000000",
            offset=ft.Offset(0, 3)

        ),
    )
    return {
        "container": main_container,
        "units": txtBox_1,
        "labs": txtBox_2,
        "hands": txtBox_3,
        "dp": txtBox_4,
        "calculate": btn_calculate,
        "reset": reset_btn,
    }
def Bottom_Container_codes(page):

    # -----------------------------------TITTLE--------------------------------------------
    tittle = ft.Text(
        "Results are shown here!",
        style=ft.TextStyle(
            decoration_color="#6E0101",
        ),
        size=22,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
        color="#6E0101",
    )
    tittle_under = ft.Text(
        '"The cost is temporary, but the education is permanent."'
        "\n""-Benjamin Franklin",
        italic=True,
        size=13,
        text_align=ft.TextAlign.CENTER,
        color="#6E0101",
    )

    # -----------------------------------RESULTS CONTAINER--------------------------------------------

    result_content = ft.Column(
        [
            ft.Column(
                [
                    tittle,
                    tittle_under,
                ],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),

        ],
        horizontal_alignment=ft.CrossAxisAlignment.START,
        tight=True,
        spacing=4,

    )

    result_container = ft.Container(
        content=result_content,
        padding=20,
        margin=ft.Margin(
            left=20,
            bottom=30,
            right=20,
            top=12,
        ),
        border_radius=10,
        bgcolor="#FFFFFF",

        shadow=ft.BoxShadow(
            spread_radius=5,
            blur_radius=4,
            color="#40000000",
            offset=ft.Offset(0, 3)

        ),
    )
    return {
        "container": result_container,
        "content": result_content,
    }
def Stack_Background_codes(page):

    # -----------------------------------BACKGROUND IMAGE--------------------------------------------
    top = Top_Container_codes(page)
    bottom = Bottom_Container_codes(page)

    main_container = top["container"]
    result_container = bottom["container"]

    brain_codes(page, top, bottom)

    background = ft.Container(
        content=ft.Image(
            src="background_bct_prime.png",
            fit=ft.BoxFit.COVER,
        ),
        left=0, top=0, right=0, bottom=0,
    )

    # display the containers
    layout = ft.Stack(
        controls=[
            background,
            ft.Container(
                content=ft.Column(
                    controls=[
                        main_container,
                        result_container,
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                    spacing=0,
                    expand=True,
                    scroll=ft.ScrollMode.AUTO,
                ),
                alignment=ft.Alignment(0, -1),
                left=0, top=0, right=0, bottom=0,
            ),
        ],
        expand=True,
    )

    # --------AVOID BACKGROUND SHIFT WHEN KEYBOARD POPS UP------------------------
    start_height = max(page.height or 0, 900)

    design_box = ft.Container(
        content=layout,
        height=start_height,
        width=float("inf"),
    )

    scroller = ft.Column(
        [design_box],
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        spacing=0,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
    )

    full_height = {"value": start_height}

    def on_resize(e):
        if page.height and page.height > full_height["value"]:
            full_height["value"] = page.height
            design_box.height = page.height
            design_box.update()

    page.on_resize = on_resize
    page.add(scroller)
    page.bgcolor = "#6E0101"
    on_resize(None)

#Codes for Calculations/Logics
def brain_codes(page, top, bottom):

    #rates-------------------------------------
    tuition_rate = 487
    lab_fee_per_subject = 3429.30
    hands_on_fee_per_subject = 2341.86
    misc_fee = 3739.98

    exam_split = [
        ("1st Prelim", 0.15),
        ("1st Grading", 0.25),
        ("2nd Prelim", 0.15),
        ("Midterm", 0.30),
        ("Finals", 0.15),
    ]

    def calculate(e):
        try:
            units = int(top["units"].value)
            labs = int(top["labs"].value)
            hands = int(top["hands"].value)
            dp = float(top["dp"].value or 0)
        except (ValueError, TypeError):
            bottom["content"].controls = [
                ft.Text("Please enter valid numbers in all required fields!",
                        color="#C50D0D")
            ]
            page.update()
            return

        if not 1 <= units <= 25:
            message = "Units must be between 1 and 25."
        elif not 1 <= labs <= 5:
            message = "Laboratory subjects must be between 1 and 5."
        elif not 1 <= hands <= 5:
            message = "Hands-on subjects must be between 1 and 5."
        elif labs > units or hands > units:
            message = "Subject counts cannot exceed total units."
        elif dp < 0:
            message = "Down Payment Invalid!"
        else:
            tuition = units * tuition_rate
            lab_fee = labs * lab_fee_per_subject
            hands_fee = hands * hands_on_fee_per_subject

            total = tuition + misc_fee + lab_fee + hands_fee
            down_payment = min(dp, total)
            balance = total - down_payment

            exam_rows = []
            paid = 0.0
            for i, (name, pct) in enumerate(exam_split):
                if i == len(exam_split) -1:
                    amount = round(balance - paid, 2)
                else:
                    amount = round(balance * pct, 2)
                paid += amount
                exam_rows.append(
                    ft.Text(f"{name} ({int(pct * 100)}%): ₱{amount:,.2f}")
                )

            bottom["content"].horizontal_alignment = ft.CrossAxisAlignment.START

            bottom["content"].controls = [
                ft.Text("TUITION ASSESSMENT", size=20,
                        weight=ft.FontWeight.BOLD, color="#6E0101"),
                ft.Text(f"Tuition Fee: ₱{tuition:,.2f}"),
                ft.Text(f"Miscellaneous Fee: ₱{misc_fee:,.2f}"),
                ft.Text(f"Laboratory Fee: ₱{lab_fee:,.2f}"),
                ft.Text(f"Hands-on Fee: ₱{hands_fee:,.2f}"),
                ft.Divider(color="#6E0101"),
                ft.Text(f"TOTAL: ₱{total:,.2f}",
                        weight=ft.FontWeight.BOLD, color="#6E0101"),
                ft.Text(f"Down Payment: ₱{down_payment:,.2f}"),
                ft.Text(f"Remaining Balance: ₱{balance:,.2f}"),
                ft.Divider(color="#6E0101"),
                ft.Text("PAYMENT PER EXAM", weight=ft.FontWeight.BOLD,
                        color="#6E0101"),
                *exam_rows,
            ]
            page.update()
            return

        bottom["content"].controls = [
            ft.Text(message, color="#C50D0D")
        ]

        page.update()

    def reset(e):
        top["units"].value = ""
        top["labs"].value = ""
        top["hands"].value = ""
        top["dp"].value = ""

        bottom["content"].horizontal_alignment = ft.CrossAxisAlignment.CENTER

        bottom["content"].controls = [
            ft.Column(
                [
                    ft.Text(
                        "Results are shown here!",
                        size=22,
                        weight=ft.FontWeight.BOLD,
                        color="#6E0101",
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Text(
                        '"The cost is temporary, but the education is permanent."\n'
                        '-Benjamin Franklin',
                        size=13,
                        italic=True,
                        text_align=ft.TextAlign.CENTER,
                        color="#6E0101",
                    ),
                ],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ]

        page.update()

    top["calculate"].on_click = calculate
    top["reset"].on_click = reset

#Main Method-------------------------------------------------------------------------------------------------------------------->
def main(page: ft.Page):

    page.title = "BCT calculator"
    page.assets_dir = "assets"
    page.padding = 0
    page.window.width = 393
    page.window.height = 852
    page.window.resizable = False


    #methods called is here >
    Stack_Background_codes(page)



if __name__ == "__main__":
    ft.run(
        main,
        assets_dir="assets"
    )
