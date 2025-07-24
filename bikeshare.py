import time
import pandas as pd
import numpy as np
# git project
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
    City_list = ["chicago", "new york city", "washington"]
    months_list = ['january', 'february', 'march', 'april', 'may', 'june', 'all']    
    days_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Enter city name (Chicago, New york city, Washington)").lower()
        if city in City_list:
            break
        else:
            print("Invalid name city")
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter month (all, january, february, ... , june)").lower()
        if month in months_list:
            break
        else:
            print("Invalid month")        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter day (all, monday, tuesday, ... sunday)").lower()
        if day in days_list:
            break
        else:
            print("Invalid day") 

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
    df['month'] = pd.to_datetime(df['Start Time']).dt.month_name()
    df['month'] = df['month'].str.lower()
    df['day'] = pd.to_datetime(df['Start Time']).dt.day_name()
    df['day'] = df['day'].str.lower()
    if month != 'all':
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day'] == day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    most_common_month = df['Start Time'].dt.month.value_counts().idxmax()
    print('Most common month (1=January, ..., 6=june): ', most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['Start Time'].dt.dayofweek.value_counts().idxmax()
    print('Most common day of week (0=Monday, ..., 6=Sunday): ', most_common_day) 

    # TO DO: display the most common start hour
    most_common_hour = df['Start Time'].dt.hour.value_counts().idxmax()
    print('Most common start hour (0-23): ', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print('Most common start station: ', most_common_start_station)
    
    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print('Most common end station: ', most_common_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    df['St End Comb'] = df['Start Station'] + " to " + df['End Station']
    most_common_trip = df['St End Comb'].value_counts().idxmax()
    print('Most common trip: ', most_common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    print('The total travel time in seconds): ', total_duration)

    # TO DO: display mean travel time
    mean_duration = df['Trip Duration'].mean()
    print('The average travel time in seconds): ', mean_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types: ', user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        counts_gender = df['Gender'].value_counts()
        print('Gender Counts: ', counts_gender)
    else:
        print('Gender data not available.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest = int(df['Birth Year'].min())
        print('Earliest year:', earliest)
        most_recent = int(df['Birth Year'].max())
        print('Most recent year:', most_recent)        
        most_common = int(df['Birth Year'].mode()[0])
        print('Most common year:', most_common)
    else:
        print('Birth Year data not available.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


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
