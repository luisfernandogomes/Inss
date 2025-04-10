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
            ft.NavigationBarDestination(icon=ft.Icons.REPORT, label="Simulação"),
            ft.NavigationBarDestination(
                icon=ft.Icons.ACCOUNT_BOX,
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
                    selected_icon=ft.Icons.ACCOUNT_BOX,
                    label="Simulação",

                ),
            ],
            on_change=lambda e: page.go(["/", "/regras", "/simulacao"][e.control.selected_index])
        ), content=ft.Container(),
        height=500, expand=True, )

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    logo = ft.Image(src="senai.png")

    txt_inicio = ft.TextField(value="Bem vindo ao simulador de aposentadoria: INSS", max_lines=3
                              , color=Colors.WHITE, text_size=16, border_radius=40, border_color="cyan")

    txt_inicio2 = ft.Text(value="Neste simulador é possivel consultar de acordo com as legalidades do INSS,"
                                " quando será possivel se aposentar", text_align=CENTER, color=Colors.WHITE, size=14)

    txt_inicio3 = ft.Text(value="Ao navegar a página de regras será possível visualizar quais são os criterios,"
                                " nos quais permitem que você se aposente", text_align=CENTER, color=Colors.WHITE,
                          size=14)

    txt_inicio4 = ft.Text(value="Após visualizar quais são os criterios,"
                                " prossiga para a pagina de simulação, aonde você deverá informar as informações"
                                " necessaria", text_align=CENTER, color=Colors.WHITE, size=14)


    idade = ft.TextField(label='informe sua quantos anos vc tem',
                         border_color=Colors.CYAN,
                         border_width=2,
                         border_radius=10,
                         focused_border_color=Colors.RED
                         )
    genero = ft.RadioGroup(content=ft.Row([
        ft.Radio(value='homem', label="Homem"),
        ft.Radio(value='mulher', label="Mulher"),
    ]))

    tempo_contribuicao = ft.TextField(label='Tempo de contribuição', border_color=Colors.CYAN, border_width=2,
                                      border_radius=10, focused_border_color=Colors.RED, )

    media_salarial = ft.TextField(label='Média salarial', border_color=Colors.CYAN, border_width=2,
                                  border_radius=10, focused_border_color=Colors.RED, )

    opcao = ft.RadioGroup(content=ft.Row([
        ft.Radio(value='tempo', label="Tempo de contribuição"),
        ft.Radio(value='idade', label="Idade")
    ]))

    txt_resultado = ft.Text('a')
    def simular_aposentadoria(e):
        if opcao.value == "tempo":
            if genero.value == "homem":
                try:
                    idade_int = int(idade.value)
                except ValueError:
                    txt_resultado.value = 'insira um valor numerico'
                    page.go("/resultado")
                    return
                try:
                    tempo_contri_int = int(tempo_contribuicao.value)
                except ValueError:
                    txt_resultado.value = 'insira um valor numerico'
                    page.go("/resultado")
                    return
                try:
                    media_salarial_int = float(media_salarial.value)
                except ValueError:
                    txt_resultado.value = 'insira um valor numerico'
                    page.go("/resultado")
                    return
                if media_salarial_int < 1100:
                    txt_resultado.value = 'Média salarial inserida não é valida'
                    page.go("/resultado")
                if tempo_contri_int < 35:

                    txt_resultado.value = ('aida não é possivel se aposentar seguindo as diretrizes de tempo de'
                                           ' contribuição')

            elif genero.value == "mulher":

        elif opcao.value == "idade":
            if genero.value == "homem":

            elif genero.value == "mulher":



        # page.go("/resultado")

    def gerenciar_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(leading=logo, leading_width=100, center_title=True, title=Text("home"), bgcolor=Colors.CYAN,
                           color=Colors.BLACK,
                           actions=[
                               ft.PopupMenuButton(items=
                               [
                                   ft.PopupMenuItem(text="Regras", on_click=lambda _: page.go("/regras")),
                                   ft.PopupMenuItem(text="Simulação", on_click=lambda _: page.go("/simulacao")),

                               ])


                           ]),


                    ft.ResponsiveRow([
                        txt_inicio, txt_inicio2, txt_inicio3, txt_inicio4,
                    ]
                        , vertical_alignment=CENTER, ),

                    pagelet


                ]
            )

        )

        if page.route == "/regras":
            page.views.append(
                View(
                    "/regras", [


                        AppBar(title=Text("regras"), leading=logo, bgcolor=Colors.CYAN, color=Colors.BLACK,
                               center_title=True, ),

                        Text(value="Regras Básicas de Aposentadoria:", color=Colors.WHITE,
                                 size=10, expand=True),
                        Text(value="Aposentadoria por Idade:",color=Colors.WHITE,size=10,
                                  expand=True),

                        ft.Row(
                            [
                                ft.Text('Homens:', size=10, expand=True),
                                ft.Text('Homens: 65 anos de idade e pelo menos 15 anos de contribuição.', size=9,
                                        expand=True),
                            ],
                            expand=True
                        ),

                        ft.Row([Text('Mulheres:', size=10, expand=True),
                                Text('Mulheres: 62 anos de idade e pelo menos'
                                     ' 15 anos de contribuição.', size=9, expand=True)], expand=True),

                        Text('Aposentadoria por Tempo de Contribuição:', expand=True),

                        ft.Row([Text('Homens:', expand=True, ),
                                Text('35 anos de contribuição.', size=9, expand=True), ], expand=True),

                        ft.Row([Text('Mulheres:', expand=True, ),
                                Text('Mulheres: 30 anos de contribuição.', size=9, expand=True), ], expand=True),

                        Text('Valor Estimado do Benefício:',  expand=True, ),
                        ft.Text('O valor da aposentadoria será uma média'
                                                             ' de 60% da média salarial informada,'
                                                             ' acrescido de 2% por ano que exceder'
                                                             ' o tempo mínimo de contribuição.',expand=True, size=8),
                        pagelet

                    ]

                )
            )

        if page.route == "/resultado":
            page.views.append(
                View(
                    "/resultado", [
                        AppBar(title=Text("resultado"), center_title=True, bgcolor=Colors.CYAN, color=Colors.BLACK,),
                        txt_resultado,

                    ]
                )
            )

        if page.route == "/simulacao":
            page.views.append(
                View(
                    "/simulacao", [
                        AppBar(title=Text("simulacao"), leading=logo, center_title=True, bgcolor=Colors.CYAN,
                               color=Colors.BLACK, ),
                        # tenho que mudar esse butão que direciona para resultado para dentro de uma função
                        idade,

                        genero,

                        tempo_contribuicao,
                        media_salarial,

                        opcao,

                        ft.FilledButton(text='Simular',icon=ft.Icons.ACCOUNT_CIRCLE, on_click=simular_aposentadoria),



                        pagelet,

                    ]
                )
            )

        page.update()


    page.on_route_change = gerenciar_rotas
    page.on_view_pop = voltar
    page.on_route_change = gerenciar_rotas
    page.go(page.route)


ft.app(main)
