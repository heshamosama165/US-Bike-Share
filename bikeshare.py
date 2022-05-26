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
    cities = ['chicago', 'new york city', 'washington']
    city = input(" please enter one of three cities (chicago or new york city or washington in order to see it's data: ").lower()
    while city not in cities:
        city = input(" Wrong! Your input is not valid, please enter only one of the three cities: ").lower()
        if city in cities:
            break
        else:
            continue



    # TO DO: get user input for month (all, january, february, ... , june)
    months = ["all" , 'january', 'february', 'march', 'april', 'may', 'june']
    month = input(" Which month you want to filter in order to explore its data specifically: ").lower()
    while month not in months:
        month = input(" Wrong! Your input is not valid unfortunately, please choose a month from january to june: ").lower()
        if month in months:
            break
        else:
            continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ["all" , 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = input(" Which day in the week you want to filter in order to explore its data specifically: ").lower()
    while day not in days:
        day = input("Wrong! Your input is not valid unfortunately, please choose the day of the week correctly: ")
        if day in days:
            break
        else:
            continue



    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city] , parse_dates=['Start Time'])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # filter by month to create the new dataframe
        df = df[df['month'] == month.title()]


    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]


    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    populor_month = df["month"].mode()[0]
    print("The most popular month is: {} ".format(populor_month))

    # TO DO: display the most common day of week
    populor_day = df["day"].mode()[0]
    print("The most popular day is: {} ".format(populor_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    populor_hour = df["hour"].mode()[0]
    print("The most popular hour is: {} ".format(populor_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    populor_start_station = df["Start Station"].mode()[0]
    print("The most popular start station is: {} ".format(populor_start_station))

    # TO DO: display most commonly used end station
    populor_end_station = df["End Station"].mode()[0]
    print("The most popular end station is: {}".format(populor_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df["Start Station"] + " to " + df["End Station"]
    combination = df['trip'].mode()[0]
    print("The most frequent combination from start to end is: {}".format(combination))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration = df['Trip Duration'].sum()
    print("The total trip duration is: {} ".format(total_trip_duration))

    # TO DO: display mean travel time
    average_trip_duration = df['Trip Duration'].mean()
    print("The average trip duration is: {} ".format(average_trip_duration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_of_user_types = df['User Type'].value_counts()
    print("counts of user type are:\n{}".format(count_of_user_types))

    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        print("counts of Gender are:\n{}".format(df["Gender"].value_counts()))

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        print("The earliest year of births are: {}".format(int(df["Birth Year"].max())))
    if "Birth Year" in df.columns:
        print("The most recent year of births are: {}".format(int(df["Birth Year"].min())))
    if "Birth Year" in df.columns:
        print("The most common year of births are: {}".format(int(df["Birth Year"].mode())))
    else:
        print("Sorry we don't have the record for washington years of birth ")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(city):

    df = pd.read_csv(CITY_DATA[city])

    print('\nRaw data is available to check... \n')
    start_loc = 0
    while True:
        display_opt = input('To View the availbale raw data in chuncks of 5 rows type: Yes \n').lower()
        if display_opt not in ['yes', 'no']:
            print('That\'s invalid choice, pleas type yes or no')

        elif display_opt == 'yes':
            print(df.iloc[start_loc:start_loc+5])
            start_loc+=5

        elif display_opt == 'no':
            print('\nExiting...')
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()

