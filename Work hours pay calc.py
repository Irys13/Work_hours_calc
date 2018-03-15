in_hours = float(input("clock in (hours): "))
in_min = float(input("clock in(min): "))
break_time = float(input("break(min): "))
pay = float(input("Hourly wage: "))
night_hours = str(input("Night shift? [y] / [n]: "))
night_hours_str = str(night_hours)
if night_hours == "y":
    out_hours_night = float(input("clock out(hours): "))
    out_min_night = float(input("clock out(min): "))
    night_pay = float(input("night pay: "))
    night_total_hours = float(((out_hours_night*60)+float(out_min_night))/60)
    day_total_hours = float(in_hours*60)
    day_total_hours2 = float(1440 - day_total_hours)
    day_total_hours3 = float(day_total_hours2/60)
    night_total_pay = float(night_total_hours*float(night_pay))
    day_total_pay = float(day_total_hours3*float(pay))
    day_night_total_pay = float(day_total_pay + night_total_pay)
    day_night_total_hours = float(day_total_hours3 + float(night_total_hours))
    print(" ")
    print("_____________________________________")
    print(" ")

    day_night_total_hours2 = int(day_night_total_hours)
    day_night_total_hours3 = float(day_night_total_hours - day_night_total_hours2)
    day_night_total_hours4 = int(day_night_total_hours3 * 60)
    print(str(day_night_total_hours2) + "h " + str(day_night_total_hours4) + "min")

    print("-------------------------------------")

    print("day hours: %0.2f" % day_total_hours3)
    print("day pay: £%0.2f" % day_total_pay)
    print("night hours: %0.2f" % night_total_hours)
    print("night total pay: £%0.2f" % night_total_pay)
    print("total hours: %0.2f" % day_night_total_hours)
    print("total shift pay: £%0.2f" % day_night_total_pay)

    print("_____________________________________")

else:
    out_hours = float(input("clock out(hours): "))
    out_min = float(input("clock out(min): "))

    start_hours = in_hours*60+in_min
    start_hours_deci = float(start_hours/60)

    end_hours = float(out_hours*60+out_min)
    end_hours_deci = float(end_hours/60.0)

    break_deci = break_time/60.0

    total_hours = float(end_hours_deci - (start_hours_deci + break_deci))
    total_income = float(total_hours*pay)

    print(" ")
    print("_____________________________________")
    print(" ")

    total_hours2 = int(total_hours)
    total_hours3 = float(total_hours-total_hours2)
    total_hours4 = int(total_hours3 * 60)

    print(str(total_hours2) + "h " + str(total_hours4) + "min")

    print("-------------------------------------")

    print("Total hours: %0.2f" % total_hours)
    print("Total income: £%0.2f" % total_income)

    print("_____________________________________")

    


