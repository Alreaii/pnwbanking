import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
import pnwkit
kit = pnwkit.QueryKit("")

allianceId = 3339
checkterm = ["loan", "repay", "holdings"]
nid = 107477
#list of all nations in aa

allnations = kit.query("nations", {"alliance_id": allianceId}, "id nation_name").get()
allnationslist = [i.id for i in allnations.nations]
allnationsid = [i.nation_name for i in allnations.nations]
newdf = pd.DataFrame(columns=['nation_name', 'money', 'coal', 'oil', 'uranium', 'iron', 'bauxite', 'gasoline', 'munitions', 'steel', 'aluminum', 'food'])

st.title("Alliance Bank")
st.write("Total Nation Money Holdings")

for nation in range(1): #len(allnationslist)
    allnationslist[nation] = nid
    try:
        nMemberBankTotal = kit.query("bankrecs", {"sid": allnationslist[nation], "rid": allianceId}, "id receiver_id date note money coal oil uranium iron bauxite gasoline munitions steel aluminum food").get()
        nMemberName = kit.query("nations", {"id": allnationslist[nation]}, "nation_name").get()
        allwithdrawal = kit.query("bankrecs", {"rid": allnationslist[nation], "sid": allianceId}, "id receiver_id date note money coal oil uranium iron bauxite gasoline munitions steel aluminum food").get()
        if any(x in nMemberBankTotal.bankrecs[0].note.lower() for x in checkterm):
            newdf = newdf.append({'nation_name': nMemberName.nations[0].nation_name, 'money': (sum(i.money for i in nMemberBankTotal.bankrecs) - sum(i.money for i in allwithdrawal.bankrecs)), 'coal': nMemberBankTotal.bankrecs[0].coal, 'oil': nMemberBankTotal.bankrecs[0].oil, 'uranium': nMemberBankTotal.bankrecs[0].uranium, 'iron': nMemberBankTotal.bankrecs[0].iron, 'bauxite': nMemberBankTotal.bankrecs[0].bauxite, 'gasoline': nMemberBankTotal.bankrecs[0].gasoline, 'munitions': nMemberBankTotal.bankrecs[0].munitions, 'steel': nMemberBankTotal.bankrecs[0].steel, 'aluminum': nMemberBankTotal.bankrecs[0].aluminum, 'food': nMemberBankTotal.bankrecs[0].food}, ignore_index=True)
    except IndexError:
        pass

st.dataframe(newdf)

for i in nMemberBankTotal.bankrecs:
    st.write(i.money, i.note)

for i in allwithdrawal.bankrecs:
    st.write(i.money, i.note)
