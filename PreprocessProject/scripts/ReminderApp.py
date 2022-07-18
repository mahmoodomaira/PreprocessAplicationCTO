# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 18:51:21 2022

@author: E6410
"""

import datetime
import time

def enter_dates_in_lists(num_data):
    date_time_list = []
    regex = datetime.datetime.strptime
    format_date_time = "%d.%m.%Y %H:%M"
    while(len(date_time_list)<num_data):
        try:
            entered_date = input('please enter a date: ')
            assert regex(entered_date, '%d.%m.%Y')
            entered_time = input('please enter a time: ')
            assert regex(entered_time, '%H:%M')
            date_time_str = entered_date + " " + entered_time
            date_time_list.append(datetime.datetime.strptime(date_time_str,format_date_time))
        except ValueError:
            print('Please enter the date in the form "dd.mm.yyyy" and Please enter the time in the form "HH:MM"')
            
    date_time_list = sorted(date_time_list)
    
    return date_time_list

def difference_in_second(Date):
    CurrentDate = datetime.datetime.now()
    return (Date-CurrentDate).total_seconds()

def reminder(date_time_list):
    i=0
    while(i<len(date_time_list)):
        sleep_time = difference_in_second(date_time_list[i])
        if sleep_time>0:
            time.sleep(sleep_time)
            print('The {} date has been reached! {}'.format(i+1,date_time_list[i]))
        else:
            print('This date is from the past')
        i = i + 1 
            


def main():
    num_data = input('How much data do you want to enter: ')
    date_time_list = enter_dates_in_lists(int(num_data))
    reminder(date_time_list)
    

if __name__ == "__main__":
    main()