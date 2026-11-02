import flet as ft
from datetime import datetime



#Sliding side panel & Hamburger button
def SlidingPanel_HamburgerButton(page, student_info, history_records):

    PANEL_WIDTH = 280

    def open_drawer(e):
        scrim.visible = True
        panel.left = 0
        page.update()

    def close_drawer(e=None):
        scrim.visible = False
        panel.left = -PANEL_WIDTH
        page.update()

    def on_item(name):
        def handler(e):

            close_drawer()

            if name == "History":
                page.clean()
                History_Screen(page, student_info, history_records)

            elif name == "Student Profile":
                page.clean()
                Student_Profile_Screen(page, student_info, history_records)

            elif name == "About":
                page.clean()
                About_Screen(page, student_info, history_records)

            elif name == "Help":
                page.clean()
                Help_Screen(page, student_info, history_records)

        return handler

    hamburger_button = ft.Container(
        content=ft.IconButton(
            icon=ft.Icons.MENU,
            icon_color="#6E0101",
            icon_size=30,
            on_click=open_drawer,
        ),
        padding=10,
        left=0,
        top=15,
    )

    # tap to closes the drawer
    scrim = ft.Container(
        bgcolor="#80000000",
        left=0, top=0, right=0, bottom=0,
        on_click=close_drawer,
        visible=False,
    )
    # starts to the left and slides in
    panel = ft.Container(
        width=PANEL_WIDTH,
        left=-PANEL_WIDTH,
        top=0,
        bottom=0,
        bgcolor="#FFFFFF",
        padding=ft.Padding(left=0, top=0, right=0, bottom=0),
        border_radius=ft.BorderRadius(
            top_left=0,
            top_right=15,
            bottom_left=0,
            bottom_right=15,
        ),

        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        animate_position=ft.Animation(250, ft.AnimationCurve.EASE_OUT),

        content=ft.Stack(
            controls=[

                # Background image
                ft.Container(
                    content=ft.Image(
                        src="sidebar_background.png",
                        fit=ft.BoxFit.COVER,
                        width=float("inf"),
                        height=float("inf"),
                    ),
                    left=0,
                    top=0,
                    right=0,
                    bottom=0,
                ),

                ft.Container(
                    padding=ft.Padding(
                        left=0,
                        top=100,
                        right=0,
                        bottom=0,
                    ),
                    content=ft.Column(
                        spacing=0,
                        controls=[
                            ft.ListTile(
                                leading=ft.Icon(
                                    ft.Icons.ACCOUNT_CIRCLE_OUTLINED,
                                    color="#6E0101",
                                ),
                                title=ft.Text("Student Profile", color="#6E0101"),
                                on_click=on_item("Student Profile"),
                            ),
                            ft.Divider(
                                thickness=1,
                                color="#6E0101",
                                leading_indent = 11,
                                trailing_indent = 12,
                            ),
                            ft.ListTile(
                                leading=ft.Icon(
                                    ft.Icons.HISTORY_OUTLINED,
                                    color="#6E0101",
                                ),
                                title=ft.Text("History", color="#6E0101"),
                                on_click=on_item("History"),
                            ),
                            ft.ListTile(
                                leading=ft.Icon(
                                    ft.Icons.HELP_OUTLINE,
                                    color="#6E0101",
                                ),
                                title=ft.Text("Help", color="#6E0101"),
                                on_click=on_item("Help"),
                            ),
                            ft.ListTile(
                                leading=ft.Icon(
                                    ft.Icons.INFO_OUTLINED,
                                    color="#6E0101",
                                ),
                                title=ft.Text("About", color="#6E0101"),
                                on_click=on_item("About"),
                            ),
                        ],
                    ),
                ),
            ],
            expand=True,
        ),
    )

    return [hamburger_button, scrim, panel]

#Codes for Designs>
def Top_Container_codes(page, student_info, history_records):
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
        border_radius=8,
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
        border_radius=8,
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
        border_radius=8,
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
        border_radius=8,
        label_style=ft.TextStyle(color="#6E0101"),
        hint_style=ft.TextStyle(color="#888888"),
        text_style=ft.TextStyle(color="#6E0101"),
        keyboard_type=ft.KeyboardType.NUMBER,
    )
    # -----------------------------------BUTTONS--------------------------------------------

    # Button for Back/return button
    def back_to_student_info(e):
        page.clean()
        Student_info_screen(page, student_info, history_records)
        page.update()

    back_button = ft.Container(
        content=ft.IconButton(
            icon=ft.Icons.ARROW_BACK,
            icon_color="#6E0101",
            icon_size=26,
            on_click=back_to_student_info,
            tooltip="Back",
        ),
        padding=10,
        left=50,
        top=17,
    )


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
        "back": back_button,
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
def Stack_Background_codes(page, student_info, history_records):

    # -----------------------------------BACKGROUND IMAGE--------------------------------------------
    background = ft.Container(
        content=ft.Image(
            src="background_bct_prime.png",
            fit=ft.BoxFit.COVER,
            width=float("inf"),
            height=float("inf"),
        ),
        left=0, top=0, right=0, bottom=0,
    )

    top = Top_Container_codes(page, student_info, history_records)
    bottom = Bottom_Container_codes(page)

    main_container = top["container"]
    result_container = bottom["container"]

    brain_codes(page, top, bottom, student_info, history_records)

    #Button for the sliding panel
    hamburger_controls = SlidingPanel_HamburgerButton(page, student_info, history_records)
    back_button = top["back"]

    # display the containers
    layout = ft.Stack(
        controls=[
            background,

            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Stack(
                            controls=[
                                main_container,
                                back_button,
                                hamburger_controls[0],
                            ],
                        ),
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
            hamburger_controls[1],
            hamburger_controls[2],
        ],
        expand=True,
    )

    # --------AVOID BACKGROUND SHIFT WHEN KEYBOARD POPS UP------------------------
    start_height = page.height or 852

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
    page.color = "#6E0101"
    on_resize(None)

#Codes for Calculations/Logics
def brain_codes(page, top, bottom, student_info, history_records):

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

    #-------------------------BUTTONS----------------------------------
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

            exam_payments = []
            paid = 0.0

            for i, (name, pct) in enumerate(exam_split):
                if i == len(exam_split) - 1:
                    amount = round(balance - paid, 2)
                else:
                    amount = round(balance * pct, 2)

                paid += amount
                exam_payments.append(amount)

            #Save calculation to temporary history database
            full_name = " ".join(filter(None, [
                student_info["first_name"],
                student_info["middle_name"],
                student_info["last_name"],
            ]))
            history_record = {
                "date": datetime.now().strftime("%B %d, %Y"),
                "time": datetime.now().strftime("%I:%M %p"),

                "id_number": student_info["id_number"],
                "student_name": full_name,
                "course": student_info["course"],
                "year_level": student_info["year_level"],

                "units": units,
                "labs": labs,
                "hands": hands,
                "down_payment": down_payment,

                "tuition": tuition,
                "misc_fee": misc_fee,
                "lab_fee": lab_fee,
                "hands_fee": hands_fee,
                "total": total,
                "balance": balance,

                "prelim_payment": exam_payments[0],
                "grading_payment": exam_payments[1],
                "second_prelim_payment": exam_payments[2],
                "midterm_payment": exam_payments[3],
                "final_payment": exam_payments[4],
            }
            history_records.append(history_record)

            exam_rows = [
                ft.Row(
                    controls=[
                        ft.Text(
                            f"{name} ({int(pct * 100)}%)",
                            color="#333333",
                        ),
                        ft.Text(
                            f"₱{amount:,.2f}",
                            color="#333333",
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                )
                for name, pct, amount in [
                    (name, pct, exam_payments[i])
                    for i, (name, pct) in enumerate(exam_split)
                ]
            ]

            # STUDENT INFORMATION
            full_name = " ".join(filter(None, [
                student_info["first_name"],
                student_info["middle_name"],
                student_info["last_name"],
            ]))

            course_names = {
                "BSIT": "BS Information Technology",
                "BSCpE": "BS Computer Engineering",
                "BSIE": "BS Industrial Engineering",
                "BSIT-Electricity": "BS Industrial Technology - Electricity",
                "BSIT-Electronics": "BS Industrial Technology - Electronics",
                "BSIEd-Computer": "BS Industrial Education - Computer",
                "BSIEd-Electronics": "BS Industrial Education - Electronics",
                "BSIEd-Electricity": "BS Industrial Education - Electricity",
                "ACT": "Associate in Computer Technology",
                "AET-Electronics": "Associate in Electronics Technology",
                "AET-Electrical": "Associate in Electrical Technology",
            }

            course_name = course_names.get(
                student_info["course"],
                student_info["course"]
            )

            bottom["content"].horizontal_alignment = ft.CrossAxisAlignment.START

            bottom["content"].controls = [

                ft.Text(
                    "STUDENT INFORMATION",
                    size=18,
                    weight=ft.FontWeight.BOLD,
                    color="#6E0101",
                ),

                ft.Text(f"Student ID: {student_info['id_number']}"),
                ft.Text(f"Student Name: {full_name}"),
                ft.Text(f"Course: {course_name}"),
                ft.Text(f"Year Level: {student_info['year_level']}"),

                ft.Divider(color="#6E0101"),

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

# Tittle Page----------------------------------------------------------------------------------------------------------------------------
def Tittle_Screen(page, student_info, history_records):
    def start_app(e):
        page.clean()
        Student_info_screen(page, student_info, history_records)
        page.update()

    title_background = ft.Container(
        content=ft.Image(
            src="titlePage_background.png",
            fit=ft.BoxFit.COVER,
        ),
        left=0, top=0, right=0, bottom=0,
        on_click=start_app,
    )


    page.add(
        ft.Stack(
            controls=[
                title_background,
            ],
            expand=True,
        )
    )

# Student info Page----------------------------------------------------------------------------------------------------------------------------
def Student_info_screen(page, student_info, history_records):

    # -----------------------------------TEXT BOXES--------------------------------------------
    txt_id = ft.TextField(
        label="Student ID Number",
        value=student_info.get("id_number", ""),
        border_color="#6E0101",
        focused_border_color="#6E0101",
        border_radius=8,
    )

    txt_last = ft.TextField(
        label="Last Name",
        value=student_info.get("last_name", ""),
        border_color="#6E0101",
        focused_border_color="#6E0101",
        border_radius=8,
    )

    txt_first = ft.TextField(
        label="First Name",
        value=student_info.get("first_name", ""),
        border_color="#6E0101",
        focused_border_color="#6E0101",
        border_radius=8,
    )

    txt_middle = ft.TextField(
        label="Middle Name (Optional)",
        value=student_info.get("middle_name", ""),
        border_color="#6E0101",
        focused_border_color="#6E0101",
        border_radius=8,
    )
    # -----------------------------------DROP DOWN BOXES--------------------------------------------
    course_dropdown = ft.Dropdown(
        label="Course",
        value=student_info.get("course", ""),
        border_radius=8,
        menu_height=250,
        options=[
            ft.DropdownOption(key="BSIT", text="BS Information Technology"),
            ft.DropdownOption(key="BSCpE", text="BS Computer Engineering"),
            ft.DropdownOption(key="BSIE", text="BS Industrial Engineering"),
            ft.DropdownOption(key="BSIT-Electricity", text="BS Industrial Technology"),
            ft.DropdownOption(key="BSIT-Electronics", text="BS Industrial Technology"),
            ft.DropdownOption(key="BSIEd-Computer", text="BS Industrial Education"),
            ft.DropdownOption(key="BSIEd-Electronics", text="BS Industrial Education"),
            ft.DropdownOption(key="BSIEd-Electricity", text="BS Industrial Education"),
            ft.DropdownOption(key="ACT", text="Associate in Computer Technology"),
            ft.DropdownOption(key="AET-Electronics", text="Associate in Electronics Technology"),
            ft.DropdownOption(key="AET-Electrical", text="Associate in Electrical Technology"),
        ],
        border_color="#6E0101",

    )

    year_dropdown = ft.Dropdown(
        label="Year Level",
        value=student_info.get("year_level", ""),
        border_radius=8,
        options=[
            ft.DropdownOption(key="1st Year", text="1st Year"),
            ft.DropdownOption(key="2nd Year", text="2nd Year"),
            ft.DropdownOption(key="3rd Year", text="3rd Year"),
            ft.DropdownOption(key="4th Year", text="4th Year"),
        ],
        border_color="#6E0101",
    )

    error_message = ft.Text(
        "",
        color="#C50D0D",
        size=13,
    )

    # -----------------------------------INPUT VERIFICATION--------------------------------------------

    def continue_to_main_page(e):
        if not txt_id.value or not txt_last.value or not txt_first.value:
            error_message.value = "Please complete all required fields."

        elif not course_dropdown.value or not year_dropdown.value:
            error_message.value = "Please select your course and year level."

        else:
            student_info["id_number"] = txt_id.value.strip()
            student_info["last_name"] = txt_last.value.strip()
            student_info["first_name"] = txt_first.value.strip()
            student_info["middle_name"] = txt_middle.value.strip()
            student_info["course"] = course_dropdown.value
            student_info["year_level"] = year_dropdown.value

            page.clean()
            Stack_Background_codes(page, student_info, history_records)
            page.update()
            return

        page.update()

    # -----------------------------------BUTTONS-------------------------------------------

    def back_to_title(e):
        page.clean()
        Tittle_Screen(page, student_info, history_records)
        page.update()

    continue_btn = ft.Button(
        content="Continue",
        width=float("inf"),
        on_click=continue_to_main_page,
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
    continue_btn_container = ft.Container(
        content=continue_btn,
        expand=3,
        border_radius=5,
        shadow=ft.BoxShadow(
            spread_radius=0,
            blur_radius=2,
            color="#6E0101",
            offset=ft.Offset(0, 2),
        ),
    )

    # -----------------------------------DISPLAY CONTAINER--------------------------------------------

    top_margin = round((page.height or 852) * 0.10)

    student_form = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(
                    "STUDENT INFORMATION",
                    size=25,
                    weight=ft.FontWeight.BOLD,
                    color="#6E0101",
                ),

                ft.Text(
                    "Please enter your information to continue.",
                    size=13,
                    color="#6E0101",
                ),

                ft.Divider(
                    color="#6E0101",
                    thickness=1,
                ),

                txt_id,
                txt_last,
                txt_first,
                txt_middle,
                course_dropdown,
                year_dropdown,

                error_message,

                ft.Divider(
                    color="#6E0101",
                    thickness=1,
                ),

                continue_btn_container,

                ft.TextButton(
                    "← Back to Title Page",
                    on_click=back_to_title,
                    style=ft.ButtonStyle(
                        color="#6E0101",
                    ),
                ),

            ],
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            spacing=8,
            tight=True,
            scroll=ft.ScrollMode.AUTO,
        ),

        padding=ft.Padding(
            left=20,
            top=20,
            right=20,
            bottom=30,
        ),
        margin=ft.Margin(
            left=20,
            top=top_margin,
            right=20,
            bottom=0,
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
    start_height = page.height or 852

    layout = ft.Stack(
        controls=[
            ft.Container(
                content=ft.Image(
                    src="background_bct_prime.png",
                    fit=ft.BoxFit.COVER,
                    width=float("inf"),
                    height=float("inf"),
                ),
                left=0,
                top=0,
                right=0,
                bottom=0,
            ),

            ft.Container(
                content=student_form,
                left=0,
                right=0,
                top=0,
                alignment=ft.Alignment.TOP_CENTER,
            ),
        ],
        expand=True,
    )

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
    on_resize(None)

#HISTORY PAGE------------------------------------------------------------------------------------------------------------------
def History_Screen(page, student_info, history_records):

    def back_to_calculator(e):
        page.clean()
        Stack_Background_codes(page, student_info, history_records)
        page.update()

    # ---------------- HEADER ----------------
    header = ft.Row(
        controls=[
            ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                icon_color="#6E0101",
                icon_size=25,
                on_click=back_to_calculator,
                tooltip="Back to Calculator",
            ),
            ft.Text(
                "CALCULATION HISTORY",
                size=21,
                weight=ft.FontWeight.BOLD,
                color="#6E0101",
            ),
        ],
        spacing=5,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )
    header = ft.Container(
        content=header,
        padding=ft.Padding(
            left=0,
            top=70,
            right=0,
            bottom=5,
        ),
    )

    # ---------------- HISTORY RECORDS ----------------
    history_items = []

    if not history_records:
        history_items.append(
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Icon(
                            ft.Icons.HISTORY,
                            size=55,
                            color="#A66A6A",
                        ),
                        ft.Text(
                            "No History Yet",
                            size=18,
                            weight=ft.FontWeight.BOLD,
                            color="#6E0101",
                        ),
                        ft.Text(
                            "Your saved calculations will appear here.",
                            size=13,
                            color="#777777",
                            text_align=ft.TextAlign.CENTER,
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=8,
                ),
                padding=30,
                alignment=ft.Alignment.CENTER,
                bgcolor="#EFFFFFFF",
                border_radius=12,
            )
        )

    else:
        for index, record in enumerate(reversed(history_records), start=1):

            history_card = ft.Container(
                content=ft.Column(
                    controls=[

                        ft.Row(
                            controls=[
                                ft.Column(
                                    controls=[
                                        ft.Text(
                                            record["student_name"],
                                            size=17,
                                            weight=ft.FontWeight.BOLD,
                                            color="#6E0101",
                                        ),
                                        ft.Text(
                                            f"ID: {record['id_number']}",
                                            size=12,
                                            color="#777777",
                                        ),
                                    ],
                                    spacing=2,
                                    expand=True,
                                ),
                                ft.Text(
                                    f"#{index}",
                                    size=12,
                                    color="#FFFFFF",
                                    bgcolor="#6E0101",
                                ),
                            ],
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),

                        ft.Divider(color="#DDDDDD"),

                        ft.Text(
                            f"{record['course']} • {record['year_level']}",
                            size=13,
                            color="#6E0101",
                            weight=ft.FontWeight.W_500,
                        ),

                        ft.Text(
                            f"{record['date']}  |  {record['time']}",
                            size=12,
                            color="#888888",
                        ),

                        ft.Divider(color="#DDDDDD"),

                        ft.Text(
                            "SUBJECT DETAILS",
                            size=12,
                            weight=ft.FontWeight.BOLD,
                            color="#888888",
                        ),

                        ft.Row(
                            controls=[
                                ft.Text(f"Units: {record['units']}"),
                                ft.Text(f"Laboratory: {record['labs']}"),
                                ft.Text(f"Hands-on: {record['hands']}"),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),

                        ft.Divider(color="#DDDDDD"),

                        ft.Text(
                            "PAYMENT SUMMARY",
                            size=12,
                            weight=ft.FontWeight.BOLD,
                            color="#888888",
                        ),

                        ft.Row(
                            controls=[
                                ft.Text("Tuition Fee"),
                                ft.Text(f"₱{record['tuition']:,.2f}"),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),

                        ft.Row(
                            controls=[
                                ft.Text("Miscellaneous Fee"),
                                ft.Text(f"₱{record['misc_fee']:,.2f}"),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),

                        ft.Row(
                            controls=[
                                ft.Text("Laboratory Fee"),
                                ft.Text(f"₱{record['lab_fee']:,.2f}"),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),

                        ft.Row(
                            controls=[
                                ft.Text("Hands-on Fee"),
                                ft.Text(f"₱{record['hands_fee']:,.2f}"),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),

                        ft.Divider(color="#DDDDDD"),

                        ft.Row(
                            controls=[
                                ft.Text(
                                    "TOTAL ASSESSMENT",
                                    weight=ft.FontWeight.BOLD,
                                    color="#6E0101",
                                ),
                                ft.Text(
                                    f"₱{record['total']:,.2f}",
                                    weight=ft.FontWeight.BOLD,
                                    color="#6E0101",
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),

                        ft.Row(
                            controls=[
                                ft.Text("Down Payment"),
                                ft.Text(f"₱{record['down_payment']:,.2f}"),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),

                        ft.Text(
                            "PAYMENT PER EXAM",
                            size=12,
                            weight=ft.FontWeight.BOLD,
                            color="#888888",
                        ),

                        ft.Row(
                            controls=[
                                ft.Text("1st Prelim"),
                                ft.Text(f"₱{record.get('prelim_payment', 0):,.2f}"),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),

                        ft.Row(
                            controls=[
                                ft.Text("1st Grading"),
                                ft.Text(f"₱{record.get('grading_payment', 0):,.2f}"),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),

                        ft.Row(
                            controls=[
                                ft.Text("2nd Prelim"),
                                ft.Text(f"₱{record.get('second_prelim_payment', 0):,.2f}"),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),

                        ft.Row(
                            controls=[
                                ft.Text("Midterm"),
                                ft.Text(f"₱{record.get('midterm_payment', 0):,.2f}"),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),

                        ft.Row(
                            controls=[
                                ft.Text("Finals"),
                                ft.Text(f"₱{record.get('final_payment', 0):,.2f}"),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),

                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Text(
                                        "REMAINING BALANCE",
                                        weight=ft.FontWeight.BOLD,
                                        color="#FFFFFF",
                                        size=12,
                                    ),
                                    ft.Text(
                                        f"₱{record['balance']:,.2f}",
                                        weight=ft.FontWeight.BOLD,
                                        color="#FFFFFF",
                                        size=15,
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            ),
                            bgcolor="#6E0101",
                            padding=12,
                            border_radius=8,
                        ),
                    ],
                    spacing=8,
                ),
                padding=15,
                margin=ft.Margin(left=0, right=0, top=3, bottom=3),
                bgcolor="#FFFFFF",
                border_radius=12,
                shadow=ft.BoxShadow(
                    blur_radius=4,
                    color="#30000000",
                    offset=ft.Offset(0, 2),
                ),
            )

            history_items.append(history_card)

    # ---------------- MAIN CONTENT ----------------
    history_list = ft.Column(
        controls=history_items,
        spacing=10,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )

    main_content = ft.Container(
        content=ft.Column(
            controls=[
                header,
                ft.Divider(color="#6E0101"),
                history_list,
            ],
            spacing=10,
            expand=True,
        ),
        padding=ft.Padding(
            left=20,
            right=20,
            top=35,
            bottom=15,
        ),
        expand=True,
    )

    # ---------------- BACKGROUND ----------------
    background = ft.Container(
        content=ft.Image(
            src="common_pages_background.png",
            fit=ft.BoxFit.COVER,
            width=float("inf"),
            height=float("inf"),
        ),
        left=0,
        top=0,
        right=0,
        bottom=0,
    )

    layout = ft.Stack(
        controls=[
            background,
            main_content,
        ],
        expand=True,
    )

    page.add(layout)
    page.update()

#STUDENT PROFILE PAGE ----------------------------------------------------------------------------------------------------------------
def Student_Profile_Screen(page, student_info, history_records):

    def back_to_calculator(e):
        page.clean()
        Stack_Background_codes(page, student_info, history_records)
        page.update()

    #Convert course codes into readable names
    course_names = {
        "BSIT": "BS Information Technology",
        "BSCpE": "BS Computer Engineering",
        "BSIE": "BS Industrial Engineering",
        "BSIT-Electricity": "BS Industrial Technology - Electricity",
        "BSIT-Electronics": "BS Industrial Technology - Electronics",
        "BSIEd-Computer": "BS Industrial Education - Computer",
        "BSIEd-Electronics": "BS Industrial Education - Electronics",
        "BSIEd-Electricity": "BS Industrial Education - Electricity",
        "ACT": "Associate in Computer Technology",
        "AET-Electronics": "Associate in Electronics Technology",
        "AET-Electrical": "Associate in Electrical Technology",
    }

    full_name = " ".join(filter(None, [
        student_info.get("first_name", ""),
        student_info.get("middle_name", ""),
        student_info.get("last_name", ""),
    ]))

    course_name = course_names.get(
        student_info.get("course", ""),
        student_info.get("course", "")
    )

    # ---------------- HEADER ----------------
    header = ft.Row(
        controls=[
            ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                icon_color="#6E0101",
                icon_size=25,
                on_click=back_to_calculator,
                tooltip="Back to Calculator",
            ),
            ft.Text(
                "PROFILE",
                size=21,
                weight=ft.FontWeight.BOLD,
                color="#6E0101",
            ),
        ],
        spacing=5,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )
    header = ft.Container(
        content=header,
        padding=ft.Padding(
            left=0,
            top=70,
            right=0,
            bottom=5,
        ),
    )

    #Profile information
    profile_card = ft.Container(
        content=ft.Column(
            controls=[
                ft.Icon(
                    ft.Icons.ACCOUNT_CIRCLE,
                    size=85,
                    color="#6E0101",
                ),

                ft.Text(
                    full_name,
                    size=21,
                    weight=ft.FontWeight.BOLD,
                    color="#6E0101",
                    text_align=ft.TextAlign.CENTER,
                ),

                ft.Text(
                    student_info.get("id_number", ""),
                    size=14,
                    color="#777777",
                    text_align=ft.TextAlign.CENTER,
                ),

                ft.Divider(color="#DDDDDD"),

                ft.Text(
                    "PERSONAL INFORMATION",
                    size=13,
                    weight=ft.FontWeight.BOLD,
                    color="#888888",
                ),

                ft.Row(
                    controls=[
                        ft.Text("First Name"),
                        ft.Text(student_info.get("first_name", "")),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),

                ft.Row(
                    controls=[
                        ft.Text("Middle Name"),
                        ft.Text(student_info.get("middle_name", "") or "N/A"),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),

                ft.Row(
                    controls=[
                        ft.Text("Last Name"),
                        ft.Text(student_info.get("last_name", "")),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),

                ft.Divider(color="#DDDDDD"),

                ft.Text(
                    "ACADEMIC INFORMATION",
                    size=13,
                    weight=ft.FontWeight.BOLD,
                    color="#888888",
                ),

                ft.Row(
                    controls=[
                        ft.Text("Student ID"),
                        ft.Text(student_info.get("id_number", "")),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),

                ft.Row(
                    controls=[
                        ft.Text("Course"),
                        ft.Text(
                            course_name,
                            width=180,
                            text_align=ft.TextAlign.RIGHT,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),

                ft.Row(
                    controls=[
                        ft.Text("Year Level"),
                        ft.Text(student_info.get("year_level", "")),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
            ],
            spacing=12,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
        ),
        padding=20,
        bgcolor="#FFFFFF",
        border_radius=12,
        shadow=ft.BoxShadow(
            blur_radius=4,
            color="#30000000",
            offset=ft.Offset(0, 2),
        ),
    )

    main_content = ft.Container(
        content=ft.Column(
            controls=[
                header,
                ft.Divider(color="#6E0101"),
                profile_card,
            ],
            spacing=15,
            scroll=ft.ScrollMode.AUTO,
        ),
        padding=ft.Padding(
            left=20,
            right=20,
            top=70,
            bottom=20,
        ),
        expand=True,
    )

    background = ft.Container(
        content=ft.Image(
            src="common_pages_background.png",
            fit=ft.BoxFit.COVER,
            width=float("inf"),
            height=float("inf"),
        ),
        left=0,
        top=0,
        right=0,
        bottom=0,
    )

    layout = ft.Stack(
        controls=[
            background,
            main_content,
        ],
        expand=True,
    )

    page.add(layout)
    page.update()

#ABOUT PAGE-------------------------------------------------------------------------------------------------------------------------------
def About_Screen(page, student_info, history_records):

    def back_to_calculator(e):
        page.clean()
        Stack_Background_codes(page, student_info, history_records)
        page.update()
    # ---------------- HEADER ----------------
    header = ft.Row(
        controls=[
            ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                icon_color="#6E0101",
                icon_size=25,
                on_click=back_to_calculator,
                tooltip="Back to Calculator",
            ),
            ft.Text(
                "ABOUT",
                size=21,
                weight=ft.FontWeight.BOLD,
                color="#6E0101",
            ),
        ],
        spacing=5,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )
    header = ft.Container(
        content=header,
        padding=ft.Padding(
            left=0,
            top=0,
            right=0,
            bottom=5,
        ),
    )

    background = ft.Container(
        content=ft.Image(
            src="about_bg.png",
            fit=ft.BoxFit.COVER,
            width=float("inf"),
            height=float("inf"),
        ),
        left=0,
        top=0,
        right=0,
        bottom=0,
    )

    main_content = ft.Container(
        content=ft.Column(
            controls=[
                header,
                ft.Divider(color="#6E0101"),

            ],
            spacing=5,
            expand=True,
        ),
        padding=ft.Padding(
            left=20,
            right=20,
            top=100,
            bottom=15,
        ),
        expand=True,
    )

    layout = ft.Stack(
        controls=[
            background,
            main_content,
        ],
        expand=True,
    )
    page.add(layout)
    page.update()

#HELP PAGE-------------------------------------------------------------------------------------------------------------------------------
def Help_Screen(page, student_info, history_records):

    def back_to_calculator(e):
        page.clean()
        Stack_Background_codes(page, student_info, history_records)
        page.update()
    # ---------------- HEADER ----------------
    header = ft.Row(
        controls=[
            ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                icon_color="#6E0101",
                icon_size=25,
                on_click=back_to_calculator,
                tooltip="Back to Calculator",
            ),
            ft.Text(
                "HELP",
                size=21,
                weight=ft.FontWeight.BOLD,
                color="#6E0101",
            ),
        ],
        spacing=5,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )
    header = ft.Container(
        content=header,
        padding=ft.Padding(
            left=0,
            top=0,
            right=0,
            bottom=5,
        ),
    )

    background = ft.Container(
        content=ft.Image(
            src="help_bg.png",
            fit=ft.BoxFit.COVER,
            width=float("inf"),
            height=float("inf"),
        ),
        left=0,
        top=0,
        right=0,
        bottom=0,
    )

    main_content = ft.Container(
        content=ft.Column(
            controls=[
                header,
                ft.Divider(color="#6E0101"),

            ],
            spacing=5,
            expand=True,
        ),
        padding=ft.Padding(
            left=20,
            right=20,
            top=100,
            bottom=15,
        ),
        expand=True,
    )

    layout = ft.Stack(
        controls=[
            background,
            main_content,
        ],
        expand=True,
    )
    page.add(layout)
    page.update()

#Main Method-------------------------------------------------------------------------------------------------------------------->
def main(page: ft.Page):

    page.title = "BCT calculator"
    page.assets_dir = "assets"
    page.padding = 0
    page.window.width = 393
    page.window.height = 852
    page.window.resizable = False

    #Stores Student info
    student_info = {
        "id_number": "",
        "last_name": "",
        "first_name": "",
        "middle_name": "",
        "course": "",
        "year_level": "",
    }

    #Temporary database for history
    history_records = []

    #Calls Tittle Page
    Tittle_Screen(page, student_info,history_records)

    #methods called is here >
    #Stack_Background_codes(page)




if __name__ == "__main__":
    ft.run(
        main,
        assets_dir="assets"
    )
