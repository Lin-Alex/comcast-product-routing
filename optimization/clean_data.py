import pandas as pd
import numpy as np

#2020 PO Data
po_20 = pd.read_excel("2020 PO Data.xlsx")
#remove unnecessary columns
po_20 = po_20.drop(columns=['PO Number', 'VENDOR_NAME', 'locDiv', 'PO Creation Date', 'CIFA'])
#rename columns
po_20 = po_20.rename(columns = {'locRegion':'d', 'Fiscal':'t_month', 'cpeItem':'p', 'Qty Ordered':'a'})
po_20['t_year'] = 2020
po_20['vendor'] = np.nan
#encode regions
po_20['d'] = np.where((po_20.d == 'CALIFORNIA REGION'),0,po_20.d)
po_20['d'] = np.where((po_20.d == 'DAVENPORT HUB'),1,po_20.d)
po_20['d'] = np.where((po_20.d == 'GREAT LAKES HUB'),2,po_20.d)
po_20['d'] = np.where((po_20.d == 'GREATER BOSTON & WNE REGION'),3,po_20.d)
po_20['d'] = np.where((po_20.d == 'HOUSTON REGION'),4,po_20.d)
po_20['d'] = np.where((po_20.d == 'SIK AURORA'),5,po_20.d)
po_20['d'] = np.where((po_20.d == 'SIK NASHVILLE'),6,po_20.d)
po_20['d'] = np.where((po_20.d == 'SIK PORTLAND'),7,po_20.d)
po_20['d'] = np.where((po_20.d == 'SWEDESBORO'),8,po_20.d)
po_20['d'] = np.where((po_20.d == 'CORPORATE'),9,po_20.d)

#encode months
po_20['t_month'] = np.where((po_20.t_month == '2020-01'),1,po_20.t_month)
po_20['t_month'] = np.where((po_20.t_month == '2020-02'),2,po_20.t_month)
po_20['t_month'] = np.where((po_20.t_month == '2020-03'),3,po_20.t_month)
po_20['t_month'] = np.where((po_20.t_month == '2020-04'),4,po_20.t_month)
po_20['t_month'] = np.where((po_20.t_month == '2020-05'),5,po_20.t_month)
po_20['t_month'] = np.where((po_20.t_month == '2020-06'),6,po_20.t_month)
po_20['t_month'] = np.where((po_20.t_month == '2020-07'),7,po_20.t_month)
po_20['t_month'] = np.where((po_20.t_month == '2020-08'),8,po_20.t_month)
po_20['t_month'] = np.where((po_20.t_month == '2020-09'),9,po_20.t_month)
po_20['t_month'] = np.where((po_20.t_month == '2020-10'),10,po_20.t_month)
po_20['t_month'] = np.where((po_20.t_month == '2020-11'),11,po_20.t_month)
po_20['t_month'] = np.where((po_20.t_month == '2020-12'),12,po_20.t_month)

#clean product names
po_20['vendor'] = np.where((po_20.p == 'CGA4131COM'), 'Technicolor', po_20.vendor)
po_20['p'] = np.where((po_20.p == 'CGA4131COM'), 'CBR', po_20.p)

po_20['vendor'] = np.where((po_20.p == 'AX061AEI'), 'CommScope', po_20.vendor)
po_20['p'] = np.where((po_20.p == 'AX061AEI'), 'Xi6', po_20.p)

po_20['vendor'] = np.where((po_20.p == 'CGM4331COM'), 'Technicolor', po_20.vendor)
po_20['p'] = np.where((po_20.p == 'CGM4331COM'), 'XB7', po_20.p)

po_20['vendor'] = np.where((po_20.p == 'TG4482G'), 'CommScope', po_20.vendor)
po_20['p'] = np.where((po_20.p == 'TG4482G'), 'XB6', po_20.p)

po_20['vendor'] = np.where((po_20.p == 'TX061AEI'), 'Technicolor', po_20.vendor)
po_20['p'] = np.where((po_20.p == 'TX061AEI'), 'Xi6', po_20.p)

#groupby product, dc, month
po_20 = po_20.groupby(['p', 'd', 't_month', 't_year', 'vendor'], as_index=False)['a'].sum()

#turn into dict with product, dc, month, year as key
po_20_dict = po_20.set_index(['p', 'd', 't_month', 't_year']).T.to_dict('list')

#2019 PO Data
po_19 = pd.read_excel("2019 PO Data.xlsx")

#remove unnecessary columns
po_19 = po_19.drop(columns=['locDiv','PO Number', 'VENDOR_NAME', 'Truckloads', 'Cost (standard)', 'PO Creation Date', 'CIFA' ])

#rename columns
po_19 = po_19.rename(columns = {'locRegion':'d', 'Fiscal':'t_month', 'ITEM_DESCRIPTION':'p', 'Qty Ordered':'a'})
po_19['t_year'] = 2019
po_19['vendor'] = np.nan

#encode regions
po_19['d'] = np.where((po_19.d == 'CALIFORNIA REGION'),0,po_19.d)
po_19['d'] = np.where((po_19.d == 'DAVENPORT HUB'),1,po_19.d)
po_19['d'] = np.where((po_19.d == 'GREAT LAKES HUB'),2,po_19.d)
po_19['d'] = np.where((po_19.d == 'GREATER BOSTON & WNE REGION'),3,po_19.d)
po_19['d'] = np.where((po_19.d == 'HOUSTON REGION'),4,po_19.d)
po_19['d'] = np.where((po_19.d == 'SIK AURORA'),5,po_19.d)
po_19['d'] = np.where((po_19.d == 'SIK NASHVILLE'),6,po_19.d)
po_19['d'] = np.where((po_19.d == 'SIK PORTLAND'),7,po_19.d)
po_19['d'] = np.where((po_19.d == 'SWEDESBORO'),8,po_19.d)
po_19['d'] = np.where((po_19.d == 'CORPORATE'),9,po_19.d)

#encode months
po_19['t_month'] = np.where((po_19.t_month == '2019-01'),1,po_19.t_month)
po_19['t_month'] = np.where((po_19.t_month == '2019-02'),2,po_19.t_month)
po_19['t_month'] = np.where((po_19.t_month == '2019-03'),3,po_19.t_month)
po_19['t_month'] = np.where((po_19.t_month == '2019-04'),4,po_19.t_month)
po_19['t_month'] = np.where((po_19.t_month == '2019-05'),5,po_19.t_month)
po_19['t_month'] = np.where((po_19.t_month == '2019-06'),6,po_19.t_month)
po_19['t_month'] = np.where((po_19.t_month == '2019-07'),7,po_19.t_month)
po_19['t_month'] = np.where((po_19.t_month == '2019-08'),8,po_19.t_month)
po_19['t_month'] = np.where((po_19.t_month == '2019-09'),9,po_19.t_month)
po_19['t_month'] = np.where((po_19.t_month == '2019-10'),10,po_19.t_month)
po_19['t_month'] = np.where((po_19.t_month == '2019-11'),11,po_19.t_month)
po_19['t_month'] = np.where((po_19.t_month == '2019-12'),12,po_19.t_month)

#clean product names
po_19['vendor'] = np.where((po_19.p == 'XB6. WIRELESS GATEWAY. TECHNICOLOR. PN# CGM4140COM'), 'Technicolor', po_19.vendor)
po_19['p'] = np.where((po_19.p == 'XB6. WIRELESS GATEWAY. TECHNICOLOR. PN# CGM4140COM'), 'XB6', po_19.p)

po_19['vendor'] = np.where((po_19.p == 'Xi6. Technicolor TX061AEI'), 'Technicolor', po_19.vendor)
po_19['p'] = np.where((po_19.p == 'Xi6. Technicolor TX061AEI'), 'Xi6', po_19.p)

po_19['vendor'] = np.where((po_19.p == 'Arris XB6 P2. PN# 1000605'), 'Arris', po_19.vendor)
po_19['p'] = np.where((po_19.p == 'Arris XB6 P2. PN# 1000605'), 'XB6', po_19.p)

po_19['vendor'] = np.where((po_19.p == 'Xi6. ARRIS. AX061AEI'), 'Arris', po_19.vendor)
po_19['p'] = np.where((po_19.p == 'Xi6. ARRIS. AX061AEI'), 'Xi6', po_19.p)

po_19['vendor'] = np.where((po_19.p == 'WIRELESS GATEWAY. TECHNICOLOR. PN# CGM4331COM. TCH XB7'), 'Technicolor', po_19.vendor)
po_19['p'] = np.where((po_19.p == 'WIRELESS GATEWAY. TECHNICOLOR. PN# CGM4331COM. TCH XB7'), 'XB7', po_19.p)

#groupby product, dc, month
po_19 = po_19.groupby(['p', 'd', 't_month', 't_year', 'vendor'], as_index=False)['a'].sum()

#turn into dict with product, dc, month as key
po_19_dict = po_19.set_index(['p', 'd', 't_month']).T.to_dict('list')

#combine 2019 and 2020 data
po_data= po_19.append([po_20])

#po_dict
po_dict = po_data.set_index(['p', 'd', 't_month', 't_year']).T.to_dict('list')

#Forecast Data
forecast = pd.read_excel("Actuals December 2020.xlsx", sheet_name = 'Data-12.23')

#drop unnecessary columns
forecast = forecast.drop(columns=['Subscriber_Type', 'Account Trans _ Pro', 'TOTAL PRO INSTALLS', 'TOTAL FC', 'SIK_DIRECT_SHIP_CNT', 'TOTAL DEPLOYMENTS', 'Division.1', 'Xi3/XiD', 'Trend', 'Flex'])
forecast['d'] = np.nan

#get dcs
forecast['d'] = np.where((forecast.Region == 'California Region'),0,forecast.d)
forecast['d'] = np.where((forecast.Region == 'Florida Region'),1,forecast.d)
forecast['d'] = np.where((forecast.Region == 'Chicago Region'),2,forecast.d)
forecast['d'] = np.where((forecast.Region == 'Heartland Region'),2,forecast.d)
forecast['d'] = np.where((forecast.Region == 'Greater Boston Region'),3,forecast.d)
forecast['d'] = np.where((forecast.Region == 'Western New England Region'),3,forecast.d)
forecast['d'] = np.where((forecast.Region == 'Houston Region'),4,forecast.d)
forecast['d'] = np.where((forecast.Region == 'Mountain West Region'),5,forecast.d)
forecast['d'] = np.where((forecast.Region == 'Twin Cities Region'),5,forecast.d)
forecast['d'] = np.where((forecast.Region == 'Big South Region'),6,forecast.d)
forecast['d'] = np.where((forecast.Region == 'Portland Region'),7,forecast.d)
forecast['d'] = np.where((forecast.Region == 'Seattle Region'),7,forecast.d)
forecast['d'] = np.where((forecast.Region == 'Beltway Region'),8,forecast.d)
forecast['d'] = np.where((forecast.Region == 'Freedom Region'),8,forecast.d)
forecast['d'] = np.where((forecast.Region == 'Keystone Region'),8,forecast.d)

#drop columns
forecast = forecast.drop(columns=['Region', 'Division'])
