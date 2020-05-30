import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

month_lst = ['all','january','february','march','april','may','june']

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
    city_lst = ['chicago','new york city','washington']
    print('\n')
    city = input('Please enter the name of the city:')
    while city not in city_lst:
        city =input('Please enter the name of city from the list (Chicago, new york city, washington):')

    # TO DO: get user input for month (all, january, february, ... , june) the month input should be written with initial small letter
    
    month = input('Please enter the month from the list(all,january,february,march,april,may,june):')
    


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please enter the day of week. If it is all day, please enter all as input:')


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
    
    df['day'] = df['Start Time'].dt.weekday_name
    
    df['start_hour'] = df['Start Time'].dt.hour
    
    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    temp = df['month'].value_counts().idxmax()
    print('The most common month is {}'.format(month_lst[temp]))
    


    # TO DO: display the most common day of week
    
    temp_day = df['day'].value_counts().idxmax()
    print('The most common day of the week is {}'.format(temp_day))
    


    # TO DO: display the most common start hour
    
    temp_hour = df['start_hour'].value_counts().idxmax()
    print('The most common start hour is {}'.format(temp_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    temp_start_station = df['Start Station'].value_counts().idxmax()
    
    print('The most commonly used start station is {}'.format(temp_start_station))


    # TO DO: display most commonly used end station
    
    temp_end_station = df['End Station'].value_counts().idxmax()
    
    print('The most commonly used end station is {}'.format(temp_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    
    df['most_fre_com'] = df['Start Station'] + ' '+ 'to' + ' ' + df['End Station']
    
    temp = df['most_fre_com'].value_counts().idxmax()
    
    print('The most frequent combination of start station and end station trip is {}'.format(temp))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time_travel = df['Trip Duration'].value_counts().sum()
    
    print('The total travel time is {}'.format(total_time_travel))
    


   
    # TO DO: display mean travel time
    
    mean_time_travel = df['Trip Duration'].value_counts().mean()
    
    print('The mean travel time is {}'.format(mean_time_travel))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print(df.head(5))
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    count_user_type = df['User Type'].unique()
    
    print('The number of different user type is {}'.format(len(count_user_type)))


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        
        count_gender_type = df['Gender'].unique()
        print('The number of different gender types is {}'.format(len(count_gender_type)))
    else:
        print('The data has not any information about gender')

    # TO DO: Display earliest, most recent, and most common year of birth
    city = str(get_filters()[0])
    if city == 'washington':
        print('There is no information about year of birth')
        
    else:
    
        earliest_year_birth = df['Birth Year'].min()
    
        recent_year_birth = df['Birth Year'].max()
    
        most_common_year = df['Birth Year'].value_counts().idxmax()
    
        print('The earliest, most recent, and most common year of birth are {}, {}, {}, respectively'.format(earliest_year_birth, recent_year_birth, most_common_year))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print(df.head(5))

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
