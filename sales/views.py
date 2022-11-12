from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Sale
from .forms import SaleSearchForm
import pandas as pd 
from reports.forms import ReportForm
from .utils import get_customer_from_id, get_salesman_from_id, get_chart



# Create your views here.
def home_view(request):
    sales_df =None
    position_df =None
    merged_df=None  
    main_df = None
    chart = None
    no_data = None
    # results_by = None
    form = SaleSearchForm(request.POST or None)
    report_form = ReportForm()
    if request.method=='POST':
        date_from =     request.POST.get('date_from')
        date_to =       request.POST.get('date_to')
        chart_type =    request.POST.get('chart_type')
        results_by =    request.POST.get('results_by')
        # print(date_from,date_to,chart_type,results_by)
        sales=Sale.objects.all()

        obj=Sale.objects.filter(created__date__lte=date_to, created__date__gte =date_from)
        if len (obj) > 0:   
            df = pd.DataFrame(obj.values())
            df['customer_id'] = df['customer_id'].apply(get_customer_from_id)
            df['salesman_id'] = df['salesman_id'].apply(get_salesman_from_id)
            df['created'] = df['created'].apply(lambda x:x.strftime('%Y-%m-%d'),)
            df['updated'] = df['updated'].apply(lambda x:x.strftime('%Y-%m-%d'),)
            df = df.rename({'customer_id':'customer','salesman_id':'salesman','id':'sales_id'},axis=1)
            position_data = []    
            for sale in obj:
                for pos in sale.get_positions():
                    obj = {
                        'position_id':pos.id,
                        'product':pos.product.name,
                        'quantity':pos.quantity,
                        'price':pos.price,
                        'sales_id':pos.get_sales_id(),
                        'chart':chart
                    }
                    position_data.append(obj)

            position_df = pd.DataFrame(position_data)
            merged_df =   pd.merge(df, position_df , on='sales_id')

            main_df = merged_df.groupby('transaction_id', as_index=False)['price'].agg('sum')

            chart = get_chart(chart_type, df, results_by)
            # results_by = get_chart(chart_type, main_df,labels=main_df['transaction_id'].values)
            
            
            # chart = get_chart(chart_type,  main_df)
                
            sales_df =  df.to_html()
            position_df = position_df.to_html()
            merged_df = merged_df.to_html()
            main_df = main_df.to_html()
        else:
            no_data = 'No Data is Available in this Date Range'
    param_dict= {
        'form':form,
        'sales_df':sales_df,
        'position_df': position_df,
        'merged_df': merged_df,
        'main_df': main_df,
        'chart':chart,
        'report_form':report_form,
        'no_data':no_data,
    }
    return render (request, 'sales/home.html', param_dict)


class SalesView(ListView):
    model = Sale
    template_name = 'sales/main.html' 

class SalesDetailView(DetailView):
    model = Sale
    template_name = 'sales/details.html' 