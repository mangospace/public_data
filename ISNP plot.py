import pandas as pd
import plotly.express as px

url1=r"https://raw.githubusercontent.com/mangospace/public_data/main/2022%20Institutional%20residents%20KFF.csv"
url2=r"https://raw.githubusercontent.com/mangospace/public_data/main/ISNP%20members%20by%20state.csv"
df1=pd.read_csv(url1)
df1
df2=pd.read_csv(url2)
df2


df=df1.merge(df2, left_on="Location", right_on="Location")

dfs=pd.read_html('https://www23.statcan.gc.ca/imdb/p3VD.pl?Function=getVD&TVD=53971')
dfs1=dfs[0]
dfs1=dfs1[['State','Alpha code']]

df=df.merge(dfs1, left_on="Location", right_on="State")


df.columns
df.rename(columns={"Number of Nursing Facility Residents": "NF_residents", "Institutional SNP Enrollment": "ISNP_enroll"}, inplace=True)
df['proportion']=round(df['ISNP_enroll']*100/df['NF_residents'],1)


fig = px.choropleth(df, locations='Alpha code', locationmode="USA-states", color='proportion',
                           color_continuous_scale="Viridis",
                           range_color=(0, 25),
                           scope="usa",
                           labels={'proportion':' I-SNP enrollees / NF residents, as %'}
                          )
fig.show()
