# This Program is able to answer the Day on a particular Month and Year
days_coding={1:"Sunday",2:"Monday",3:"Tuesday",4:"Wednesday",5:"Thursday",6:"Friday",0:"Saturday"};

nonleap_year_coding={"jan":1,"feb":4,"mar":4,"apr":0,"may":2,"jun":5,"jul":0,"aug":3,"sep":6,"oct":1,"nov":4,"dec":6};

leap_year_coding={"jan":0,"feb":3,"mar":4,"apr":0,"may":2,"jun":5,"jul":0,"aug":3,"sep":6,"oct":1,"nov":4,"dec":6};
# Inputs :
print("You can choose years only between 1700 to 3000")
date=int(input("Enter date: "))
month_input=input("Enter Month with months first 3 letters:");
month=month_input.lower();
year=int(input("Enter Year"));

if (year%400==0) or (year%4==0 and year%100!=0):
    year_type="leap"
    # print(" leap")
else:
    year_type="nonleap"
month_code=0;
if year_type=="nonleap":
    month_code=nonleap_year_coding.get(month);
elif year_type=="leap":

    month_code=leap_year_coding.get(month)
    
# print(month_code)

last_two_digit=abs(year)%100;
rem_date=date%7;
quotient_year=last_two_digit//4;
rem_year=last_two_digit%7;

final_rem=rem_date+quotient_year+rem_year+int(month_code);
judge=final_rem%7;
if(year>=2000 and year<3000):
    judge-=1
elif (year>=1900):
    judge=judge
elif (year>=1800 and year<1900):
    judge+=2;


if(judge>7):
    judge%=7;
show_day=days_coding.get(judge);
show="The Day on {}-{}-{} is:{}"

print(show.format(date,month,year,show_day))





