"""Shared cell corrections for distributed planning workbooks and their generator."""


def checked_product(left, right, rate=True):
    maximum = f',{right}<=1' if rate else ''
    return (f'=IF(COUNT({left},{right})<>2,"incomplete",'
            f'IF(AND({left}>=0,{right}>=0{maximum}),{left}*{right},"invalid input"))')


def planning_cell_updates(kind):
    if kind == 'demand':
        updates = {'Demand plan': {}, 'Teaching fill': {}}
        s = updates['Demand plan']
        s['A3'] = 'Output (all channels)'
        s['B3'] = 'SQO'
        s['A2'] = ('Two-step chain: volume × intermediate yield × intermediate-to-SQO rate. '
                   'Combine any intervening stage rates. Zero is a valid input; clear an unknown input. '
                   'Define SQO consistently across channels. Copyright © 2026 Ivan Xu.')
        for start in [6, 11, 16, 21, 26]:
            event = start == 21
            s[f'C{start+3}'] = 'Lead → SQO (combined)' if event else 'MQL → SQO (combined)'
            s[f'C{start+4}'] = 'Intermediate count × SQO rate'
            for col in 'DEFGHIJKLMNO':
                s[f'{col}{start+2}'] = checked_product(f'{col}{start}', f'{col}{start+1}', rate=not event)
                s[f'{col}{start+4}'] = checked_product(f'{col}{start+2}', f'{col}{start+3}')
        for col in 'DEFGHIJKLMNO':
            refs = ','.join(f'{col}{row}' for row in [10,15,20,25,30])
            s[f'{col}31'] = f'=IF(COUNT({refs})<>5,"incomplete",SUM({refs}))'
            s[f'{col}34'] = (f'=IF(COUNT({col}31,{col}33)<>2,"incomplete",'
                             f'IF({col}33<0,"invalid input",IF({col}31=0,"",{col}33/{col}31)))')
        t=updates['Teaching fill']
        t['B3']='Fictional single-channel test: set other channel inputs to zero. Clear inputs whose values are unknown.'
        t['B4']='8,000 clicks × 0.02 click-to-MQL × 0.10 MQL-to-SQO = 16 SQOs. Combined 0.10 = 0.25 MQL-to-SQL × 0.40 SQL-to-SQO. These rates are invented.'
        t['B5']='Events: 2 events × 100 leads/event × 0.05 lead-to-SQO = 10 SQOs. Lead-to-SQO includes any MQL and SQL stages. Compare demand SQOs with capacity at the same entry stage, not directly with closed-won deals.'
        return updates
    if kind != 'capacity':
        raise ValueError(kind)
    updates={'Assumptions':{},'Waterfall':{},'Renewals':{}}
    a=updates['Assumptions']
    a['A5']='Final output (map demand to entry stage)'
    a['A30']='Retention proxy (not measured NRR)'
    a['A31']='Equal starting revenue per customer assumed; excludes contraction. Use revenue cohorts for actual NRR.'
    for c in 'BC':
        a[f'{c}30']=(f'=IF(COUNT({c}26:{c}27)<>2,"incomplete",'
                      f'IF(AND({c}26>=0,{c}26<=1,{c}27>=0,{c}27<=1),'
                      f'(1-{c}26)*(1+{c}27),"invalid input"))')
        updates['Renewals'][f'{c}4']=f'=IF(ISNUMBER(Assumptions!{c}28),IF(Assumptions!{c}28>=0,Assumptions!{c}28,"invalid input"),"incomplete")'
        updates['Renewals'][f'{c}6']=(f'=IF(COUNT({c}5,Assumptions!{c}26)<>2,"incomplete",'
                                      f'IF(AND({c}5>=0,Assumptions!{c}26>=0,Assumptions!{c}26<=1),'
                                      f'{c}5*(1-Assumptions!{c}26),"invalid input"))')
    for c in 'BCDEFGHIJKLM':
        for row,assumption in [(6,16),(7,17),(8,18)]:
            updates['Waterfall'][f'{c}{row}']=checked_product(f'{c}{row-1}',f'Assumptions!B{assumption}')
        updates['Waterfall'][f'{c}10']=checked_product(f'{c}8','Assumptions!B11',rate=False)
    updates['Waterfall']['A12']='Map demand SQOs to the matching entry stage. Compare wins with roster capacity separately; apply sales-cycle timing.'
    updates['Renewals']['A7']='Retention proxy'
    updates['Renewals']['A9']='If the proxy is below 100%, review revenue churn and contraction before forecasting.'
    return updates


def apply_planning_updates(workbook, kind):
    for name,cells in planning_cell_updates(kind).items():
        for address,value in cells.items():
            workbook[name][address]=value
    if kind=='capacity':
        for sheet,addresses in [('Assumptions',['B30','C30']),('Renewals',['B7','C7'])]:
            for address in addresses:workbook[sheet][address].number_format='0.0%'
        workbook['Assumptions']['A31'].alignment=__import__('openpyxl').styles.Alignment(wrap_text=True,vertical='top')
        workbook['Assumptions'].row_dimensions[31].height=32
