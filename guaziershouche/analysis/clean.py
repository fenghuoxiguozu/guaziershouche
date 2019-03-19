# mongoexport -h 127.0.0.1 -d guazi -c ershouche -f car_brand,car_url,buy_year,mile,sale_price,original_price --csv -o guaziershouche.csv
import pandas as pd
import jieba

df=pd.read_csv(r'F:\guaziershouche\guaziershouche.csv')
df.dropna(axis=0,how='any',inplace=True)

jieba.load_userdict(r'F:\guaziershouche\word.txt')
def get_name(x):
        names="/".join(jieba.cut(x))
        names =names.split('/')
        return names[0]
df['car_brand']=df['car_brand'].apply(get_name)

df['buy_year']=df['buy_year'].str.extract(r'(\d+)',expand=True)
df['original_price']=df['original_price'].str.extract(r'(\d+\.\d)',expand=True)
mile=df['mile'].str.replace('200公里','0.2').replace('300公里','0.3').replace('400公里','0.4').replace('500公里','0.5')\
        .replace('600公里','0.6').replace('700公里','0.7').replace('800公里','0.8').replace('900公里','0.9').replace('100公里','0.1')
df['mile']=mile.str.extract(r'(\d+\.\d)',expand=True)


data=df[['car_brand','buy_year','mile','sale_price','original_price']]

data.to_csv(r'F:\guaziershouche\cleaned_data.csv')
