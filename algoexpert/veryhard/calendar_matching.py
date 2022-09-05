from datetime import datetime, timedelta


def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    # Write your code here.
    calendar1 = [ [format_time(c[0]),format_time(c[1])] for c in calendar1]
    calendar2 = [ [format_time(c[0]),format_time(c[1])] for c in calendar2]
    dailyBounds1 = [format_time(dailyBounds1[0]), format_time(dailyBounds1[1])]
    dailyBounds2 = [format_time(dailyBounds2[0]), format_time(dailyBounds2[1])]

    total_calendars = [*calendar1, *calendar2]
    total_calendars = sorted(total_calendars)
    daily_bounds = [max(dailyBounds1[0], dailyBounds2[0]),min(dailyBounds1[1], dailyBounds2[1])]

    if total_calendars:
        ans = []
        new_calendars = []
        cur = total_calendars[0]
        for ca in total_calendars[1:]:
            if ca[0] > cur[1]:
                new_calendars.append(cur)
                cur = ca
            else:
                cur[1] = max(ca[1], cur[1])
        new_calendars.append(cur)
        total_calendars = new_calendars
        cur = daily_bounds[0]
        for meeting in total_calendars:
            if add_time(cur, meetingDuration) <= meeting[0]:
                ans.append([cur, meeting[0]])
            cur = max(meeting[1], cur)
        if add_time(cur, meetingDuration) <= daily_bounds[1]:
            ans.append([cur, daily_bounds[1]])
        ans = [[re_format(a[0]), re_format(a[1])] for a in ans]
        return ans
    else:
        if add_time(daily_bounds[0], meetingDuration) > daily_bounds[1]:
            return []
        else:
            return [daily_bounds]


def add_time(orig_time, add_time):
    return (datetime.strptime(orig_time, "%H:%M") + timedelta(minutes=add_time)).strftime("%H:%M")

def format_time(orig_time):
    return orig_time if len(orig_time.split(":")[0]) == 2 else f"0{orig_time}"

def re_format(orig_time):
    return orig_time[1:] if orig_time.startswith("0") else orig_time


print(add_time("10:00", 30))


data = {
  "calendar1": [
    ["7:00", "7:45"],
    ["8:15", "8:30"],
    ["9:00", "10:30"],
    ["12:00", "14:00"],
    ["14:00", "15:00"],
    ["15:15", "15:30"],
    ["16:30", "18:30"],
    ["20:00", "21:00"]
  ],
  "calendar2": [
    ["9:00", "10:00"],
    ["11:15", "11:30"],
    ["11:45", "17:00"],
    ["17:30", "19:00"],
    ["20:00", "22:15"]
  ],
  "dailyBounds1": ["6:30", "22:00"],
  "dailyBounds2": ["8:00", "22:30"],
  "meetingDuration": 30
}
print(calendarMatching(data["calendar1"],data["dailyBounds1"], data["calendar2"], data["dailyBounds2"],data["meetingDuration"]))
