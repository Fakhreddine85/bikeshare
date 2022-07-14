import time
import pandas as pd
import numpy as np

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=''
    while city not in CITY_DATA:
        city = input('please enter a valid city name:').lower()
    

    # TO DO: get user input for month (all, january, february, ... , june)
    months = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month=''
    while month not in months:
        month = input('please enter a valid month:').lower()
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day=''
    while day not in days:
        day = input('please enter a valid day of week:').lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #print(df)
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if S
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        print(df)
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        print (day.title())
        df = df[df['day_of_week'] == day.title()]
        print(df)
    #print(df)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print (df['month'])
    # TO DO: display the most common month
    print('the most common month is:'+ str(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print('the most common day of week is:'+df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    
    df['hour'] = df['Start Time'].dt.hour
    print('the most common start hour is:'+str(df['hour'].mode()[0]))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('the most used start station is:'+df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('the most used end station is:'+df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    print("The most frequent combination of trips are from ."+df['Start To End'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time is: '+str(df['Trip Duration'].sum(axis=0)))

    # TO DO: display mean travel time
    print('total travel time is: '+str(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('counts of user types: '+str(df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print('counts of gender: '+str(df['Gender'].value_counts()))
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print('the most common year of birth is: '+str(df['Birth Year'].mode()[0]))
    else:
        print('Birth Year stats cannot be calculated because Birth Year does not appear in the dataframe')

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
