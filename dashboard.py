import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Definir o layout da página como "wide"
st.set_page_config(layout="wide")

# Carregar o arquivo Parquet
df_vendas = pd.read_parquet('data/vendas.parquet')

# Definir a cor de fundo cinza escuro usando CSS
st.markdown(
    """
    <style>
    .stApp {
        background-color: #1a1a1a;  /* Cor de fundo cinza escuro */
        height: 100vh;  /* Altura do fundo definida para 100% da tela */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título do dashboard
st.title("Dashboard de Vendas")

# Criar quatro colunas para os gráficos
col1, col2, col3, col4 = st.columns(4)

# Gráfico 1: Evolução das Vendas ao Longo do Tempo
with col1:
    st.markdown("<h3 style='color: white;'>Evolução das Vendas ao Longo do Tempo</h4>", unsafe_allow_html=True)
    vendas_tempo = df_vendas.groupby('data_venda')['preco_total'].sum().reset_index()
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=vendas_tempo['data_venda'], y=vendas_tempo['preco_total'], mode='lines+markers', line=dict(color='blue')))  # Cor azul royal
    fig1.update_layout(plot_bgcolor='#595959', paper_bgcolor='#595959', font_color='green')  # Cor de fundo
    st.plotly_chart(fig1, use_container_width=True)

# Gráfico 2: Análise de Vendas por Cliente
with col2:
    st.markdown("<h3 style='color: white;'>Análise de Vendas por Cliente</h4>", unsafe_allow_html=True)
    vendas_cliente = df_vendas.groupby('id_cliente')['preco_total'].sum().reset_index()
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(x=vendas_cliente['id_cliente'], y=vendas_cliente['preco_total'], marker_color='darkorange'))  # Cor laranja escuro
    fig2.update_layout(plot_bgcolor='#595959', paper_bgcolor='#595959', font_color='white')  # Cor de fundo
    st.plotly_chart(fig2, use_container_width=True)

# Gráfico 3: Top 5 Produtos Mais Vendidos
with col3:
    st.markdown("<h3 style='color: white;'>Top 5 Produtos Mais Vendidos</h4>", unsafe_allow_html=True)
    top5_produtos = df_vendas.groupby('produto')['preco_total'].sum().nlargest(5).reset_index()
    fig3 = go.Figure()
    fig3.add_trace(go.Bar(x=top5_produtos['produto'], y=top5_produtos['preco_total'], marker_color='forestgreen'))  # Cor verde floresta
    fig3.update_layout(plot_bgcolor='#595959', paper_bgcolor='#595959', font_color='white')  # Cor de fundo
    st.plotly_chart(fig3, use_container_width=True)

# Gráfico 4: Total de Vendas por Categoria de Produto
with col4:
    st.markdown("<h3 style='color: white;'>Total de Vendas por Categoria de Produto</h4>", unsafe_allow_html=True)
    vendas_categoria = df_vendas.groupby('categoria')['preco_total'].sum().reset_index()
    fig4 = go.Figure()
    fig4.add_trace(go.Bar(x=vendas_categoria['categoria'], y=vendas_categoria['preco_total'], marker_color='crimson'))  # Cor carmesim
    fig4.update_layout(plot_bgcolor='#595959', paper_bgcolor='#595959', font_color='white')  # Cor de fundo
    
    st.plotly_chart(fig4, use_container_width=True)
