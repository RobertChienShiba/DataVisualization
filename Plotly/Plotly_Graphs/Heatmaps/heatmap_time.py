import plotly.express as px
import pandas as pd
import plotly.figure_factory as ff
import numpy as np
# Data put together by Gabe Salzer on data.world
# Data source: http://www.landofbasketball.com/nba_teams_year_by_year.htm
df = pd.read_csv("https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Plotly_Graphs/Heatmaps/Historical%20NBA%20Performance.csv")
df = df.pivot('Team','Year','Winning Percentage')
#print(df[:10])

df = df[df.index.isin(['Warriors', 'Knicks', 'Celtics', 'Bulls', 'Lakers',"Spurs"])]
# fig = px.imshow(df, color_continuous_scale=px.colors.sequential.YlOrBr,
#                 title="NBA Season Winning Percentage")
fig = ff.create_annotated_heatmap(np.round(df.values,2).tolist(),
                                  x=df.columns.values.tolist(),
                                  y=df.index.values.tolist(),
                                  showscale=True,
                                  colorscale="YlOrBr")
fig.update_layout(title_font={'size':27}, title_x=0.5,font=dict(size=7),
                  xaxis=dict(side="bottom",tickmode="array",ticktext=np.linspace(1950,2010,7),
                             title=dict(text="Year",font=dict(size=30)),
                             tickfont=dict(size=20))
                  ,yaxis=dict(tickfont=dict(size=20),title=dict(text="Team",font=dict(size=30)))
                 )
fig.update_traces(hoverongaps=False,
                  hovertemplate="Team: %{y}"
                                "<br>Year: %{x}"
                                "<br>Winning %: %{z:.2f}<extra></extra>",
                 colorbar=dict(tickfont=dict(size=15)))
#print(fig["layout"])
#fig.write_html("NBA.html")
fig.show()
