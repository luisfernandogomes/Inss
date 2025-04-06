from tkinter.constants import CENTER

import flet as ft
from time import sleep

from flet.core.alignment import Alignment, center
from flet.core.app_bar import AppBar
from flet import AppBar, ElevatedButton, Page, Text, View
from flet.core.colors import Colors
from flet.core.textfield import TextField


def main(page: Page):
    page.title = "exemplo de rotas"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 375
    page.window_height = 667
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.EXPLORE, label="Regras"),
            ft.NavigationBarDestination(icon=ft.Icons.COMMUTE, label="Simulação"),
            ft.NavigationBarDestination(
                icon=ft.Icons.BOOKMARK_BORDER,
                selected_icon=ft.Icons.BOOKMARK,
                label="Explore",
            ),
        ]
    )

    pagelet = ft.Pagelet(
        navigation_bar=ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.EXPLORE, label="Inicio", ),
                ft.NavigationBarDestination(icon=ft.Icons.REPORT, label="Regras"),
                ft.NavigationBarDestination(
                    icon=ft.Icons.ACCOUNT_BOX,
                    selected_icon=ft.Icons.BOOKMARK,
                    label="Simulação",

                ),
            ],
            on_change=lambda e: page.go(["/", "/regras", "/simulacao"][e.control.selected_index])
        ), content=ft.Container(),
        height=500, expand=True,)

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    logo = ft.Image(src="senai.png")

    txt_inicio = ft.TextField(value="Bem vindo ao simulador de aposentadoria: INSS",max_lines=3
                                 ,color=Colors.WHITE,text_size=16,border_radius=40,border_color="cyan")


    txt_inicio2 = ft.Text(value="Neste simulador é possivel consultar de acordo com as legalidades do INSS,"
                                " quando será possivel se aposentar",text_align=CENTER,color=Colors.WHITE, size=14)


    txt_inicio3 = ft.Text(value="Ao navegar a página de regras será possível visualizar quais são os criterios,"
                                " nos quais permitem que você se aposente",text_align=CENTER,color=Colors.WHITE, size=14)

    txt_inicio4 = ft.Text(value="Após visualizar quais são os criterios,"
                                " prossiga para a pagina de simulação, aonde você deverá informar as informações"
                                " necessaria",text_align=CENTER,color=Colors.WHITE, size=14)



    def gerenciar_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(leading=logo, leading_width=100, center_title=True, title=Text("home"), bgcolor=Colors.CYAN, color=Colors.BLACK,
                           actions=[
                               ft.PopupMenuButton(items=
                               [
                                   ft.PopupMenuItem(text="Regras", on_click=lambda _: page.go("/regras")),
                                   ft.PopupMenuItem(text="Simulação",on_click=lambda _: page.go("/simulacao")),

                               ])

                               #    ElevatedButton(text="Regras", on_click=lambda _: page.go("/regras")),
                               # ElevatedButton(text="Simulação", on_click=lambda _: page.go("/simulacao")),
                           ]),
                    # ft.VerticalDivider(width=9, thickness=3),

                    # ft.ResponsiveRow(
                    #     [
                    #
                    #         ElevatedButton(text="Regras", on_click=lambda _: page.go("/regras")),
                    #         ElevatedButton(text="Simulação", on_click=lambda _: page.go("/simulacao")),
                    #         ft.ProgressBar(width=400, color="WHITE", bgcolor="PINK"),
                    #         txt_resultado,
                    #
                    #     ],
                    #     run_spacing={"xs": 10},
                    #
                    # ),
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column(
                                [
                                    ft.ListTile(
                                        leading=logo,
                                        title=ft.Text('Bem vindo')

                                    ),
                                    ft.Column(
                                        [

                                            txt_inicio,
                                            txt_inicio2,
                                            txt_inicio3,
                                            txt_inicio4,
                                        ]
                                    )
                                ]
                            ),
                            height=500,
                        )

                    ),

                    pagelet

                    # ft.Icon(name=ft.Icons.FAVORITE, color=ft.Colors.TERTIARY_CONTAINER),
                    # ft.Text("Linear progress indicator", style="headlineSmall"),
                    # ft.Column([ft.Text("Doing something..."), pb]),
                    # ft.Text("Indeterminate progress bar", style="headlineSmall"),

                ]
            )

        )

        if page.route == "/regras":
            page.views.append(
                View(
                    "/regras", [
                        AppBar(title=Text("regras"),leading=logo, bgcolor=Colors.CYAN, color=Colors.BLACK, center_title=True),
                        ft.ResponsiveRow(
                            [
                                ElevatedButton(text="Inicio", on_click=lambda _: page.go("/"), ),
                                ElevatedButton(text="Simulação", on_click=lambda _: page.go("/simulacao")),

                            ]
                        )

                    ]
                )
            )

        if page.route == "/resultado":
            page.views.append(
                View(
                    "/resultado", [
                        AppBar(title=Text("resultado"), bgcolor=Colors.SECONDARY_CONTAINER),
                        ElevatedButton(text="Inicio", on_click=lambda _: page.go("/")),
                        ElevatedButton(text="Regras", on_click=lambda _: page.go("/regras")),
                        ElevatedButton(text="Regras", on_click=lambda _: page.go("/simulacao"))

                    ]
                )
            )

        if page.route == "/simulacao":
            page.views.append(
                View(
                    "/simulacao", [
                        AppBar(title=Text("simulacao"), bgcolor=Colors.SECONDARY_CONTAINER),
                        # tenho que mudar esse butão que direciona para resultado para dentro de uma função
                        ElevatedButton(text="resultado", on_click=lambda _: page.go("/resultado")),
                        ElevatedButton(text="Inicio", on_click=lambda _: page.go("/inicio"))

                    ]
                )
            )

        page.update()

    page.on_route_change = gerenciar_rotas
    page.on_view_pop = voltar
    page.on_route_change = gerenciar_rotas
    page.go(page.route)


ft.app(main)
