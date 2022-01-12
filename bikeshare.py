import time
import numpy as np
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    list_of_cities = ['chicago','washington','new york city']
    city = ''
    while city  not in list_of_cities :
        city = input("Kindly enter any of these cities i.e chicago or new york city or washington : ").lower()
        
        if city in list_of_cities:
            print("Great! now it is time to enter the month of your choice")             

    # get user input for month (all, january, february, ... , june)
    list_of_month = ['all','january','february','march','april','may','june' ]

    month = ''
    while month  not in list_of_month :
        month = input("Kindly enter any of the  months of the year not beyond June or all  :").lower()
        
        if month in list_of_month:
            print("Great!,input the day of your choice") 

    # get user input for day of week (all, monday, tuesday, ... sunday)
    list_of_day_of_the_week = ['all','sunday','monday','tuesday','wednesday','thursday','friday','saturday']
    day = ''
    while day not in list_of_day_of_the_week :
        day = input("Kindly enter the day of the week or enter 'all' for all days  :  ")

        if day in list_of_day_of_the_week:
            print("Thats all. Your request will be made available in no time") 

    print('-'*40)
    return city, month, day


def load_data(city, month, day):

    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day

    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1

         # filter by month to create the new dataframe
        df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]

    print('Most common month:', common_month)

    # display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]

    print('Most common day of week:', common_day_of_week)

    # To display the most common start hour

    # we create a hour cloumn
    df['hour'] = df['Start Time'].dt.hour

    # And we display the most common start hour
    common_start_hour = df['hour'].mode()[0]

    print('Most common start hour:', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_used_startstation = df['Start Station'].mode()[0]

    print('most commonly used start station:', most_used_startstation)

    # display most commonly used end station
    most_used_endstation = df['End Station'].mode()[0]

    print('most commonly used end station:', most_used_endstation)

    # display most frequent combination of start station and end station trip
    most_used_start_and_end_station = (df['Start Station'] + df['End Station']).mode()[0]

    print('most commonly used  start station and end station:', most_used_start_and_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()

    print('Total travel time:',total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print('mean travel time:',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts_of_usertypes = df['User Type'].value_counts()

    print('counts of user types:',counts_of_usertypes)

    # Display counts of gender
    if "Gender" in df.columns:
        counts_of_gender = df['Gender'].value_counts()
        print('counts of genders:',counts_of_gender)
    else: print('Gender not found')

    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        earliest_date_of_birth = df['Birth Year'].min()
        latest_date_of_birth = df['Birth Year'].max()
        most_common_date_of_birth = df['Birth Year'].mode()
        print(' earliest, most recent, and most common year of birth:',earliest_date_of_birth,latest_date_of_birth,most_common_date_of_birth )
    else:print('Birth Year does not exist"')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    p = 0
    q = 5
    while True:
        viewData = input("Would you like to see the raw data? Type 'Yes' or 'No'.").lower()
        if viewData == "yes":
            print(df.iloc[p:q])
        df.reset_index()
        p += 5
        q += 5     
        if viewData== 'no':
            break   

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
    

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()