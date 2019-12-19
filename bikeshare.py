import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
                  'new york': 'new_york_city.csv',
                  'washington': 'washington.csv' }

def get_filters():
    

    #    """
    #    Asks user to specify a city, month, and day to analyze.

     #   Returns:
     #       (str) city - name of the city to analyze
     #       (str) month - name of the month to filter by, or "all" to apply no month filter
     #       (str) day - name of the day of week to filter by, or "all" to apply no day filter
      #  """ 
    print('Hello! Let\'s explore some US bikeshare data!')
    i = 0
    while i!=3:

        # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs 
        try:
            city = input("Would you like to see data for Chicago, New York, or Washington \n")
            city = city.lower() 
            df = pd.read_csv(CITY_DATA[city]) # test the input

        except KeyError:
            if city.isalpha():
                print("You have entered one of the proposed cities.")
                continue
            else:
                print("You have not entered one of the proposed cities. Your entry contains numbers, spaces or special characters.")
                continue

        choise = input("Would you like to filter the data by month, day, both or not at all? Type ""none"" for no time filter")
        if choise =="month":
            # get user input for month (all, january, february, ... , june)

            month = input(" Which month - january, february, march, april, may, june ?\n").lower()
            month_list = ["january", "february", "march", "april", "may", "june" ]
                 
            # test the input
            if month in month_list: 
                 print("just few moment ...Loading data")

            else:
                print("You have not entered one of the proposed month.")
                continue

            day = 'all'
            i = 3

        elif choise =="day":
            # get user input for day of week (all, monday, tuesday, ... sunday)
            day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday ? \n").lower()
            day_list = ["monday", "tuesday", "wednesday","thursday", "friday", "saturday","sunday" ]
                 # test the input

            if day in day_list: 
                 print("just few moment ... Loading data.")

            else:
                print("You have not entered one of the proposed day.")
                continue
            month = 'all'
            i = 3

        elif choise =="both":
            # get user input for month (all, january, february, ... , june)
            month = input(" Which month - January, February, March, April, May, or June ?\n").lower()
            month_list = ["january", "february", "march", "april", "may", "june" ]
                 # test the input

            if month in month_list: 
                 print("You have choise one valide month.")

            else:
                print("You have not entered one of the proposed month.")
                continue

            # get user input for day of week (all, monday, tuesday, ... sunday)
            day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday ?\n").lower()
            day_list = ["monday", "tuesday", "wednesday","thursday", "friday", "saturday","sunday" ]
                 # test the input

            if day in day_list: 
                 print("just few moment ... Loading data.")

            else:
                print("You have not entered one of the proposed day.")
                continue
            i = 3

        elif choise == "all":
            month='all'
            day='all'
            i = 3
        elif choise =="none":
            i = 3
        else:
            print("please answer the questions with the choices provided")
            continue
            
    return city, month, day;
        
        

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
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
     
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # display the most common month

    # extract month from the Start Time column to create an months column
    df['months'] = df['Start Time'].dt.month

    # find the most popular month
    popular_month = df['months'].mode()[0]

    print('Most Popular Start month:', popular_month)

    # display the most common day of week
    
    # extract day from the Start Time column to create an day column
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # find the most popular day
    popular_day_of_week = df['day_of_week'].mode()[0]

    print('Most Popular Start day of week:', popular_day_of_week)

    # display the most common start hour
    
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("Most start station: ",df['Start Station'].mode()[0])

    # display most  commonly used end station
    print("Most end station: ",df['End Station'].mode()[0])         

    # display most frequent combination of start station and end station trip
    Station_combination = df['Start Station'] + "--"+ df['End Station']
    print("Most frequent combination of start station and end station trip:\n",(Station_combination).mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    

def Duration(times):
    """Displays the days, hours, minutes and seconds from the provided seconds."""
    
    day = times // (24 * 3600)  # convert input times in day
    time = times % (24 * 3600)  
    hour = times // 3600	# convert input time in hour 
    time %= 3600
    minutes = times // 60	# convert input time in minutes
    time %= 60
    seconds = times		# convert input times in seconds
    
    print("{} days, {}h : {}m : {}s".format(int(day), int(hour), int(minutes), int(seconds)));
    
    

def trip_duration_stats(df,month,day):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display Trip Duration in function the day and the month
     
    if month == 'all' and day == 'all':
        # display total travel time
        print('what was the total duration traveling done for 2017 through june ?')
        Duration(df['Trip Duration'].sum())
        
        # display mean travel time
        print('what was the the average time spent on each trip ?')
        Duration(df['Trip Duration'].mean())
        
    elif day == 'all':
        # display total travel time
        print('what was the total duration traveling done in {} 2017 ? :'.format(month))
        Duration(df['Trip Duration'].sum())
        
        # display mean travel time
        print('what was the the average time spent on each trip ?')
        Duration(df['Trip Duration'].mean())
        
    elif month == 'all':
        # display total travel time
        print('what was the total duration traveling done all {}s for 2017 through june ? :'.format(day))
        Duration(df['Trip Duration'].sum())
        
        # display mean travel time
        print('what was the the average time spent on each trip ?')
        Duration(df['Trip Duration'].mean())
        
    else:
        # display total travel time
        print('what was the total duration traveling done {} in {} 2017 ? :'.format(day,month))
        Duration(df['Trip Duration'].sum())
        
        # display mean travel time
        print('what was the the average time spent on each trip ?')
        Duration(df['Trip Duration'].mean())
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    

def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()

    print(user_types)

    if (city == 'new york' or city == 'chicago'):
        
        # Display counts of gender
        print('\nCalculating Gender...\n')
        print(df['Gender'].value_counts())
        
        # Display earliest, most recent, and most common year of birth
        print('\nCalculating birth_year...\n')
        # We drop any rows with NaN values
        df = df.dropna(axis = 0)
        
        #most common year of birth
        t = df['Birth Year'].value_counts().to_frame().reset_index()
        print("most common year of birth: {}, count: {} ".format(int(t.loc[t.index[0], 'index']),int(t.loc[t.index[0], 'Birth Year'])))
       
        #sorts dates of birth in descending order
        Birth = t.sort_values(by = 'index',ascending = False)
        print('most recent year of birth: ',int(t.loc[t.index[0], 'index']))
        print('earliest year of birth: ',int(t.loc[t.index[-1], 'index']))
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df, month, day)
        user_stats(df, city)
        
        n = 0
        answer = input('\nwould you like to view Individual trip data ? type ''yes'' or ''no''.\n')
        
        # if they want to see 5 lines of raw data
        while answer.lower() == "yes":
            n += 1
            print('°'*40)
            
            while n%5 != 0:
                if city =='washington':
                    print("-- '{}' --\n- Birth Year:'{}'\n- End station: '{}'\n- End Time: '{}'\n- Gender: '{}'\n- Star station: '{}'\n- Star time: '{}'\n- Trip Duration: '{}'\n- User Type: '{}' \n\n".format(int(df.loc[df.index[n-1], 'Unnamed: 0']),'',df.loc[df.index[n-1], 'End Station'],df.loc[df.index[n-1], 'End Time'],'',df.loc[df.index[n-1], 'Start Station'],df.loc[df.index[n-1], 'Start Time'],int(df.loc[df.index[n-1], 'Trip Duration']),df.loc[df.index[n-1], 'User Type']))
                    
                else:    
                    print("-- '{}' --\n- Birth Year:'{}'\n- End station: '{}'\n- End Time: '{}'\n- Gender: '{}'\n- Star station: '{}'\n- Star time: '{}'\n- Trip Duration: '{}'\n- User Type: '{}' \n\n".format(int(df.loc[df.index[n-1], 'Unnamed: 0']),int(df.loc[df.index[n-1], 'Birth Year']),df.loc[df.index[n-1], 'End Station'],df.loc[df.index[n-1], 'End Time'],df.loc[df.index[n-1], 'Gender'],df.loc[df.index[n-1], 'Start Station'],df.loc[df.index[n-1], 'Start Time'],int(df.loc[df.index[n-1], 'Trip Duration']),df.loc[df.index[n-1], 'User Type']))
                n += 1
                
            print('°'*40)    
            answer = input('\nwould you like to view Individual trip data ? type ''yes'' or ''no''.\n')
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
