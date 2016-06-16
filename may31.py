COMMISSION_UP_TO_200 = 0.05
COMMISSION_FROM_200_TO_1000 = 0.08
COMMISSION_FROM_1000_TO_2000 = 0.10
COMMISSION_OVER_2000 = 0.12

def main():
    proccess_another_sales_rep = 'y'

    while proccess_another_sales_rep == 'y':
        sales_volume = get_sales()
        report(sales_volume)
        proccess_another_sales_rep = input('Process another, (y/n)? ')

def get_sales():
    sales = float(input('Enter sales: '))
    return sales

def report(sales):
    print('Sales: ', sales, 'Commission: ', get_commission(sales))

def get_commission(sales):
    commission = 0
    if sales < 200:
        commission = sales * COMMISSION_UP_TO_200
    elif sales < 1000:
        commission = 200 * COMMISSION_UP_TO_200 \
                   + (sales - 200) * COMMISSION_FROM_200_TO_1000
    elif sales < 2000:
        commission = 200 * COMMISSION_UP_TO_200 \
                    + 800 * COMMISSION_FROM_200_TO_1000 \
                    + (sales - 1000) * COMMISSION_FROM_1000_TO_2000
    else:
        commission = 200 * COMMISSION_UP_TO_200 \
                     + 800 * COMMISSION_FROM_200_TO_1000 \
                     + 1000 * COMMISSION_FROM_1000_TO_2000 \
                     + (sales - 2000) * COMMISSION_OVER_2000
    
        
    return commission

main()

