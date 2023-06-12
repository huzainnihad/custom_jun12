from odoo import models
import string
import calendar
from datetime import date, datetime, timedelta

class TruckWiseExcelReport(models.AbstractModel):
    _name = 'report.bi_truck_wise_report.report_truck_wise_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, sale):
        sheet = workbook.add_worksheet('Truck Wise Report')       

        merge_format_1 = workbook.add_format({
                                        'bold': 1,
                                        'align': 'center',
                                        'color': 'red',
                                        'font_size':16,
                                        })
        merge_format_2 = workbook.add_format({
                                        'bold': 1,
                                        'align': 'center',
                                        'fg_color':'#515a5a',
                                        'font_size':11,
                                        })
        format_1 = workbook.add_format({
                                    'align': 'center',
                                    'bold':1,
                                    'bg_color':'#fdebd0',
                                    'border':1,
                                    'text_wrap':'true'
                                        })
        format_2 = workbook.add_format({
                                    'align': 'center',
                                    'bold':1,
                                    'bg_color':'#27ae60',
                                    'border':1,
                                    'text_wrap':'true'
                                        })
        
        date_from = data["form"]["date_from"]
        date_to = data["form"]["date_to"]
        year = int(data["form"]["year"])

        from_date_month_num = datetime.strptime(date_from, '%b').month
        to_date_month_num = datetime.strptime(date_to, '%b').month
        other_val, num_days = calendar.monthrange(year, to_date_month_num)
                
        start_date = datetime(year, from_date_month_num, 1)
        last_date = datetime(year, to_date_month_num, num_days)

        months_list=[]
        for month in range(start_date.month, last_date.month + 1):
            month_date = datetime(start_date.year, month, 1)
            months_list.append(month_date.strftime('%b'))
        month_length = len(months_list)
        middle_num = month_length / 2
        starting_col = 2 + (middle_num * 7)
        starting_col = round(starting_col)
        
        alphabets = list(string.ascii_uppercase)
        letters = list(string.ascii_uppercase)
        for a in alphabets:
            for b in alphabets:
                letters.append("{}{}".format(a, b))

        sheet.set_column('A:A',13)
        sheet.set_column('B:B',1)
        sheet.set_column('C:C',10)
        sheet.set_column('D:D',8)
        sheet.set_column('E:E',10)
        sheet.set_column('F:F',10)
        sheet.set_column('G:G',10)
        sheet.set_column('H:H',10)
        sheet.set_column('I:I',10)
        sheet.set_column('J:J',1)
        sheet.set_column('R:R',1)
        sheet.set_column('J:J',1)
        sheet.set_column('Z:Z',1)
        sheet.set_column('AH:AH',1)
        sheet.set_column('AX:AX',1)
        sheet.set_column('BF:BF',1)
        sheet.set_column('BN:BN',1)
        sheet.set_column('BV:BV',1)
        sheet.set_column('CD:CD',1)
        sheet.set_column('CL:CL',1)
        sheet.set_column('AP:AP',1) 
        sheet.set_column('CT:CT',1)
        sheet.set_column('P:P',10)
        sheet.set_column('X:X',10)
        sheet.set_column('AF:AF',10)
        sheet.set_column('AN:AN',10)
        sheet.set_column('AV:AV',10)
        sheet.set_column('BD:BD',10)
        sheet.set_column('BL:BL',10)
        sheet.set_column('BT:BT',10)
        sheet.set_column('CB:CB',10)
        sheet.set_column('CJ:CJ',10)
        sheet.set_column('CR:CR',10)
        sheet.set_column('CZ:CZ',10)

        sheet.set_row(0,20)
        sheet.set_row(2,32)
        
        sheet.freeze_panes(3,2)

        sheet.merge_range('A2:A3','Truck No',merge_format_2)
        sheet.merge_range('B1:B200','') 
        sheet.merge_range('J1:J200','')    
        sheet.merge_range('R1:R200','')  
        sheet.merge_range('Z1:Z200','') 
        sheet.merge_range('CL1:CL200','')    
        sheet.merge_range('AP1:AP200','')  
        sheet.merge_range('AH1:AH200','') 
        sheet.merge_range('AX1:AX200','')  
        sheet.merge_range('BF1:BF200','') 
        sheet.merge_range('BN1:BN200','')    
        sheet.merge_range('BV1:BV200','') 
        sheet.merge_range('CD1:CD200','') 
        sheet.merge_range('CT1:CT200','')

        alphabets = list(string.ascii_uppercase)
        letters = list(string.ascii_uppercase)
        for a in alphabets:
            for b in alphabets:
                letters.append("{}{}".format(a, b))
        
        head_row = 1
        n = 2
        row = 2 
        sheet.merge_range(f"{letters[starting_col]}{head_row}:{letters[starting_col+6]}{head_row}",'FIRST QUARTER TRUCK INCOME',merge_format_1)

        for mnth in months_list:
            if months_list[0]==mnth:
                col = 2
            else:
                col += 8
            sheet.merge_range(f"{letters[n]}{row}:{letters[n+6]}{row}",mnth, format_1)
            sheet.write(f"{letters[n]}{row+1}:{letters[n+6]}{row+1}",'Income',format_1)
            sheet.write(f"{letters[n+1]}{row+1}:{letters[n+6]}{row+1}",'Salary',format_1)
            sheet.write(f"{letters[n+2]}{row+1}:{letters[n+6]}{row+1}",'Diesel',format_1)
            sheet.write(f"{letters[n+3]}{row+1}:{letters[n+6]}{row+1}",'Repair',format_1)
            sheet.write(f"{letters[n+4]}{row+1}:{letters[n+6]}{row+1}",'Mulkiya/Service',format_1)
            sheet.write(f"{letters[n+5]}{row+1}:{letters[n+6]}{row+1}",'Total Cost',format_1)
            sheet.write(f"{letters[n+6]}{row+1}:{letters[n+6]}{row+1}",'Profit',format_1)
            n = n+6+2
            truck_row = 3
            truck_col = 0
            month_num = datetime.strptime(mnth, '%b').month
            other_val, num_days = calendar.monthrange(year, month_num)
            month_start_date = datetime(year, month_num, 1)
            month_last_date = datetime(year, month_num, num_days)
            sale_ids = self.env['sale.order'].search([('date_order','>=',month_start_date),('date_order','<=',month_last_date)])
            if sale_ids:
                query = """
                SELECT  aaa.name as truck_name,sum(ste.driver_expense) as driver_expense,sum(ste.fuel_expense) as fuel_expense from sale_order so
                left join so_truck_expense ste  on (ste.sale_truck_id = so.id)
                left join account_analytic_account aaa on (aaa.id = ste.truck_expense_analytic_id)
                where so.id in %s
                group by truck_name
                ORDER BY truck_name
                """

                self.env.cr.execute(query, [tuple(sale_ids.ids)])
                docs = self.env.cr.dictfetchall()
                # grand_driver_expense = 0
                for inv in docs:
                    sheet.write(truck_row, truck_col,inv['truck_name'],format_1 )
                    sheet.write(truck_row, col,"",format_1 )
                    col+=1
                    sheet.write(truck_row, col,inv['driver_expense'],format_1 )
                    col+=1
                    sheet.write(truck_row, col,inv['fuel_expense'],format_1 )
                    col+=1
                    sheet.write(truck_row, col,"",format_1 )
                    col+=1
                    sheet.write(truck_row, col,"",format_1 )
                    col+=1
                    sheet.write(truck_row, col,"",format_1 )
                    col+=1
                    sheet.write(truck_row, col,"",format_1 )
                    truck_row += 1 
                    col = col- 6
                    
                sheet.merge_range(f"{letters[n]}{row}:{letters[n+6]}{row}","GRAND TOTAL", format_2)
                sheet.write(f"{letters[n]}{row+1}:{letters[n+6]}{row+1}",'Income',format_2)
                sheet.write(f"{letters[n+1]}{row+1}:{letters[n+6]}{row+1}",'Salary',format_2)
                sheet.write(f"{letters[n+2]}{row+1}:{letters[n+6]}{row+1}",'Diesel',format_2)
                sheet.write(f"{letters[n+3]}{row+1}:{letters[n+6]}{row+1}",'Repair',format_2)
                sheet.write(f"{letters[n+4]}{row+1}:{letters[n+6]}{row+1}",'Mulkiya/Service',format_2)
                sheet.write(f"{letters[n+5]}{row+1}:{letters[n+6]}{row+1}",'Total Cost',format_2)
                sheet.write(f"{letters[n+6]}{row+1}:{letters[n+6]}{row+1}",'Profit',format_2)

                # sheet.write(truck_row, col,"",format_1 )
                # col+=1
                # sheet.write(truck_row, col,grand_driver_expense,format_2)
                # col+=1
                # sheet.write(truck_row, col,"",format_1 )
                # col+=1
                # sheet.write(truck_row, col,"",format_1 )
                # col+=1
                # sheet.write(truck_row, col,"",format_1 )
                # col+=1
                # sheet.write(truck_row, col,"",format_1 )
                # col+=1
                # sheet.write(truck_row, col,"",format_1 )
                # truck_row += 1 