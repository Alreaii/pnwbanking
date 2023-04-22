import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
import pnwkit
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
kit = pnwkit.QueryKit("")

allianceId = 3339
checkterm = ["repay", "loan", "holdings", "deposit"]

#api calls
allnations = kit.query("nations", {"alliance_id": allianceId}, "id nation_name").get()
allTransactions = kit.query("bankrecs", {"rid": allianceId}, "id receiver_id date note money coal oil uranium iron bauxite gasoline munitions steel aluminum food").get()

#lists & objects
allnationslist = [i.id for i in allnations.nations]
allnationsid = [i.nation_name for i in allnations.nations]
newdf = pd.DataFrame(columns=['nation_name', 'money', 'coal', 'oil', 'uranium', 'iron', 'bauxite', 'gasoline', 'munitions', 'steel', 'aluminum', 'food'])
transactiondf = pd.DataFrame(columns=['nation_name', 'money', 'coal', 'oil', 'uranium', 'iron', 'bauxite', 'gasoline', 'munitions', 'steel', 'aluminum', 'food'])


#functions
for nation in range(len(allnationslist)):
    for i in range(len(allnations.nations)):
        if allnationslist[nation] == allnations.nations[i].id:
            nation_name = allnations.nations[i].nation_name
            transactiondf = transactiondf.append({'nation_name': nation_name, 'money': allTransactions.bankrecs[nation].money, 'coal': allTransactions.bankrecs[nation].coal, 'oil': allTransactions.bankrecs[nation].oil, 'uranium': allTransactions.bankrecs[nation].uranium, 'iron': allTransactions.bankrecs[nation].iron, 'bauxite': allTransactions.bankrecs[nation].bauxite, 'gasoline': allTransactions.bankrecs[nation].gasoline, 'munitions': allTransactions.bankrecs[nation].munitions, 'steel': allTransactions.bankrecs[nation].steel, 'aluminum': allTransactions.bankrecs[nation].aluminum, 'food': allTransactions.bankrecs[nation].food}, ignore_index=True)


st.title("Alliance Bank")
st.dataframe(transactiondf)

