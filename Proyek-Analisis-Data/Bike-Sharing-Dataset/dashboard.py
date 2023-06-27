import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


sns.set(style='dark')
sns.set_theme(style='whitegrid')


df = pd.read_csv('hour.csv')


def create_daily_orders_df(df):
    daily_orders_df = df.groupby('dteday').agg({
        'cnt': 'sum'
    }).reset_index()
    daily_orders_df.rename(columns={
        'dteday': 'order_date',
        'cnt': 'order_count'
    }, inplace=True)
    daily_orders_df['order_date'] = pd.to_datetime(daily_orders_df['order_date'])
    return daily_orders_df


def create_weather_df(df):
    weather_df = df.groupby('hr').agg({
        'temp': 'mean',
        'hum': 'mean',
        'windspeed': 'mean'
    }).reset_index()
    return weather_df


def create_hourly_orders_df(df):
    hourly_orders_df = df.groupby('hr').agg({
        'cnt': 'sum'
    }).reset_index()
    return hourly_orders_df


def create_season_orders_df(df):
    season_orders_df = df.groupby('season').agg({
        'cnt': 'sum'
    }).reset_index()
    season_orders_df['season'] = season_orders_df['season'].map({
        1: 'Spring',
        2: 'Summer',
        3: 'Fall',
        4: 'Winter'
    })
    return season_orders_df


def create_weekday_orders_df(df):
    weekday_orders_df = df.groupby('weekday').agg({
        'cnt': 'sum'
    }).reset_index()
    weekday_orders_df['weekday'] = weekday_orders_df['weekday'].map({
        0: 'Sunday',
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday'
    })
    return weekday_orders_df


def create_season_weekday_orders_df(df):
    season_weekday_orders_df = df.groupby(['season', 'weekday']).agg({
        'cnt': 'sum'
    }).reset_index()
    season_weekday_orders_df['season'] = season_weekday_orders_df['season'].map({
        1: 'Spring',
        2: 'Summer',
        3: 'Fall',
        4: 'Winter'
    })
    season_weekday_orders_df['weekday'] = season_weekday_orders_df['weekday'].map({
        0: 'Sunday',
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday'
    })
    return season_weekday_orders_df


def create_hourly_season_orders_df(df):
    hourly_season_orders_df = df.groupby(['hr', 'season']).agg({
        'cnt': 'sum'
    }).reset_index()
    hourly_season_orders_df['season'] = hourly_season_orders_df['season'].map({
        1: 'Spring',
        2: 'Summer',
        3: 'Fall',
        4: 'Winter'
    })
    return hourly_season_orders_df


def create_weather_orders_df(df):
    weather_orders_df = df.groupby('weathersit').agg({
        'cnt': 'sum'
    }).reset_index()
    weather_orders_df['weathersit'] = weather_orders_df['weathersit'].map({
        1: 'Clear',
        2: 'Mist',
        3: 'Light Rain/Snow',
        4: 'Heavy Rain/Snow'
    })
    return weather_orders_df

daily_orders_df = create_daily_orders_df(df)
weather_df = create_weather_df(df)
hourly_orders_df = create_hourly_orders_df(df)
season_orders_df = create_season_orders_df(df)
weekday_orders_df = create_weekday_orders_df(df)
season_weekday_orders_df = create_season_weekday_orders_df(df)
hourly_season_orders_df = create_hourly_season_orders_df(df)
weather_orders_df = create_weather_orders_df(df)



st.header('Bike Sharing Dashboard :bike:')
st.subheader('Daily Rents')


min_date = pd.to_datetime(df['dteday'].min())
max_date = pd.to_datetime(df['dteday'].max())
start_date, end_date = st.date_input(
    label='Date Range',
    min_value=min_date,
    max_value=max_date,
    value=[min_date, max_date]
)

filtered_df = df[(df['dteday'] >= start_date.strftime('%Y-%m-%d')) & (df['dteday'] <= end_date.strftime('%Y-%m-%d'))]


total_orders = filtered_df['cnt'].sum()
st.metric('Total Orders', value=total_orders)


fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(daily_orders_df['order_date'], daily_orders_df['order_count'], marker='o', linewidth=2, color='#90CAF9')
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)


st.subheader('Weather Information')
weather_df

weather_filter = st.selectbox('Filter by Weather', ['All', 'Clear', 'Mist', 'Light Rain/Snow', 'Heavy Rain/Snow'])
if weather_filter != 'All':
    filtered_df = filtered_df[filtered_df['weathersit'] == weather_filter]


st.subheader('Hourly Rents')
hourly_orders_df


st.subheader('Season Rents')
season_orders_df


st.subheader('Weekday Rents')
weekday_orders_df


st.subheader('Season and Weekday Rents')
season_weekday_orders_df


st.subheader('Hourly and Season Rents')
hourly_season_orders_df


st.subheader('Weather Rents')
weather_orders_df


st.subheader('Daily Orders Data')
st.dataframe(filtered_df)


st.subheader('Download Data')
if st.button('Download CSV'):
    filtered_df.to_csv('filtered_data.csv', index=False)
    st.success('Data berhasil diunduh')




st.caption('Bintang Margaretha Situmorang')
