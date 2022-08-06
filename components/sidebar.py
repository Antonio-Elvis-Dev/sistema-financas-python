import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app

from datetime import datetime, date
import plotly.express as px
import numpy as np
import pandas as pd


# ========= Layout ========= #
layout = dbc.Col([
    html.H1("MyBudget", className="text-primary"),
    html.P("By ASIMOV", className="text-info"),
    html.Hr(),

    # Sessão de PERFIL -------------------------------------
    dbc.Button(id='botao_avatar',
               children=[html.Img(src='/assets/img_hom.png', id='avatar_change',
                                  alt='Avatar', className='perfil_avatar')],
               style={'background-color': 'transparent', 'border-color': 'transparent'}),

    # Sessão NOVO -------------------------------------


    dbc.Row([ # NOVA LINHA
        dbc.Col([  # NOVA COLUNA
                dbc.Button(color='success', id='open-novo-receita',
                           children=['+ Receita'])
                ], width=6),
        dbc.Col([
                dbc.Button(color='danger', id='open-novo-despesa',
                           children=['- Despesa'])
                ], width=6),
    ]),

    # Modal Receita
        dbc.Modal([
            dbc.ModalHeader(dbc.ModalTitle('Adicionar Receita')),
            dbc.ModalBody([
                dbc.Row([
                    dbc.Col([
                        dbc.Label('Descrição: '),
                        dbc.Input(placeholder="Ex.: dividendos da bolsa, herença...", id="txt-receita")
                    ],width=6),
                    
                    dbc.Col([
                    dbc.Label("Valor: "),
                    dbc.Input(placeholder="$100.00", id="valor_receita", value="")    
                    ], width=6)
                ]),
                dbc.Row([
                    dbc.Col([
                        dbc.Label("Data: "),
                        dcc.DatePickerSingle(id='date-receitas',
                                             min_date_allowed=date(2020,1,1),
                                             max_date_allowed=date(2030,1,1),
                                             date = datetime.today(),
                                             style={"width": "100%"}),
                    ],width=4),
                    
                    dbc.Col([
                        dbc.Label("Extras"),
                        dbc.Checklist(
                            options=[],
                            value=[],
                            id = 'switches-input-receita',
                            switch=True
                        )
                    ],width=4),
                    dbc.Col([
                        html.Label('Categoria da Receita'),
                        dbc.Select(id='select_receita', options=[],value=[]),
                    ],width=4),
                ], style={'margin-top':'25px'}),
                
                dbc.Row([
                    dbc.Accordion([
                        dbc.AccordionItem(children=[
                            dbc.Row([
                                dbc.Col([
                                    html.Legend("Adicionar Categoria", style={'color':'green'}),
                                    dbc.Input(type="text", placeholder="Nova Categoria", id="input-add-receita", value=""),
                                    html.Br(),
                                    dbc.Button("Adicionar", className="btn btn-success", id="add-category-receita", style={"margin-top":"20px"}),
                                    html.Br(),
                                    html.Div(id="category-div-add-receita", style={"":""}) # MINUTO 38:49
                                    
                                ])
                            ])
                        ])
                    ])
                ])
        
            ]),
        ], id='modal-novo-receita'),

    # Modal Despesa

        dbc.Modal([
            dbc.ModalHeader(dbc.ModalTitle('Adicionar Despesa')),
            dbc.ModalBody([
                
            ]),
        ], id='modal-novo-despesa'),

    # Seção de NAV ----------------------------------
    html.Hr(),

    dbc.Nav([
        dbc.NavLink("Dashboards", href="/dashboards", active="exact"), # LINKS DE NAVEGAÇÃO 
        dbc.NavLink("Extratos", href="/extratos", active="exact"),

    ], vertical=True, pills=True, id='nav_buttons', style={"margin-bottom": "50px"})

])


# =========  Callbacks  =========== #
# Pop-up receita
@app.callback(
    Output('modal-novo-receita', 'is_open'),
    Input('open-novo-receita', 'n_clicks'),
    State('modal-novo-receita','is_open')
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open

# Pop-up despesa
@app.callback(
    Output('modal-novo-despesa', 'is_open'),
    Input('open-novo-despesa', 'n_clicks'),
    State('modal-novo-despesa','is_open')
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open