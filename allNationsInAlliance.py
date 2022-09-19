import pnwkit
kit = pnwkit.QueryKit("") #add ur own api key here

# 88039652 2022-09-18 16:58:02+00:00 Safekeeping  35000000 0 0 0 0 0 0 0 0 0 0 # example output

#constants
allianceId = 10498 #change alliance id here
allNationsInAllianceList = []
checkterm = "safekeeping"
#===============================================================================


#api queries

allNationsInAlliance = kit.query("nations", {"alliance_id": allianceId}, "id nation_name")
allNationsInAllianceResult = allNationsInAlliance.get()

#===============================================================================

def MemberDepositRecords(memberId):
  print(f"""
    ========= Tomtech Toaster Member Deposits Record =========
    | Member ID: {memberId}
    | Member Name: {nationNameResult.nations[0].nation_name}
    | Member Cash Total: {sum(i.money for i in result.bankrecs) - sum(i.money for i in accountforwithdrawalResult.bankrecs)}
    | Member Coal Total: {sum(i.coal for i in result.bankrecs) - sum(i.coal for i in accountforwithdrawalResult.bankrecs)}
    | Member Oil Total: {sum(i.oil for i in result.bankrecs)- sum(i.oil for i in accountforwithdrawalResult.bankrecs)}
    | Member Uranium Total: {sum(i.uranium for i in result.bankrecs)- sum(i.uranium for i in accountforwithdrawalResult.bankrecs)}
    | Member Iron Total: {sum(i.iron for i in result.bankrecs)- sum(i.iron for i in accountforwithdrawalResult.bankrecs)}
    | Member Bauxite Total: {sum(i.bauxite for i in result.bankrecs) - sum(i.bauxite for i in accountforwithdrawalResult.bankrecs)}
    | Member Gasoline Total: {sum(i.gasoline for i in result.bankrecs) - sum(i.gasoline for i in accountforwithdrawalResult.bankrecs)}
    | Member Munitions Total: {sum(i.munitions for i in result.bankrecs) - sum(i.munitions for i in accountforwithdrawalResult.bankrecs)}
    | Member Steel Total: {sum(i.steel for i in result.bankrecs) - sum(i.steel for i in accountforwithdrawalResult.bankrecs)}
    | Member Aluminum Total: {sum(i.aluminum for i in result.bankrecs) - sum(i.aluminum for i in accountforwithdrawalResult.bankrecs)}
    | Member Food Total: {sum(i.food for i in result.bankrecs) - sum(i.food for i in accountforwithdrawalResult.bankrecs)}
    ==========================================================

""")

#===============================================================================

for nation in allNationsInAllianceResult.nations:
    allNationsInAllianceList.append(nation.id)

for i in range(len(allNationsInAllianceList)):
  memberId = allNationsInAllianceList[i]
  print(memberId)
  nMemberBankTotal = kit.query("bankrecs", {"or_id": memberId, "rid": 10498}, "id receiver_id date note money coal oil uranium iron bauxite gasoline munitions steel aluminum food")
  result = nMemberBankTotal.get()

  nMemberName = kit.query("nations", {"id": memberId}, "nation_name")
  nationNameResult = nMemberName.get()

  accountforwithdrawal = kit.query("bankrecs", {"or_id": memberId, "sid": 10498}, "id receiver_id date note money coal oil uranium iron bauxite gasoline munitions steel aluminum food")
  accountforwithdrawalResult = accountforwithdrawal.get()
  if any(checkterm in x.note.lower() for x in result.bankrecs): # do not touch, this should not work but it does, anyone who knows why please tell me, do not show to competent python users
    MemberDepositRecords(allNationsInAllianceList[i])
  else:
    pass


#107477
