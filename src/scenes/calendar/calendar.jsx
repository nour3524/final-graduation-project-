import { useState } from "react";
import FullCalendar, { formatDate } from "@fullcalendar/react";
import dayGridPlugin from "@fullcalendar/daygrid";
import timeGridPlugin from "@fullcalendar/timegrid";
import interactionPlugin from "@fullcalendar/interaction";
import listPlugin from "@fullcalendar/list";
import {
  Box,
  List,
  ListItem,
  ListItemText,
  Typography,
  useTheme,
} from "@mui/material";
import Header from "../../components/Header";
import { tokens } from "../../theme";

const Calendar = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const [currentEvents, setCurrentEvents] = useState([]);

  // Abnormal behavior types based on UEBA research
  const abnormalBehaviors = [
    // November 2024 - Privileged account misuse & high-risk actions
    {
      id: "nov-1",
      title: "Privileged Account Misuse Detected",
      start: "2024-11-03",
      color: "hsl(348, 70%, 50%)",
      description: "Administrator account accessed by unauthorized user, possible insider threat."
    },
    {
      id: "nov-2",
      title: "Excessive Data Export",
      start: "2024-11-08",
      color: "hsl(0, 70%, 50%)",
      description: "User exported a high volume of data (over 500 GB) from the system within a short period."
    },
    {
      id: "nov-3",
      title: "Accessing Unusual Timeframes",
      start: "2024-11-12",
      color: "hsl(207, 70%, 50%)",
      description: "User accessed the system during midnight, which is unusual for this user."
    },
    {
      id: "nov-4",
      title: "Multiple Unsuccessful Login Attempts",
      start: "2024-11-18",
      color: "hsl(50, 70%, 50%)",
      description: "More than 10 failed login attempts detected for user within 15 minutes."
    },

    // December 2024 - Data breach attempts & high-risk user activities
    {
      id: "dec-1",
      title: "Sensitive Data Transfer Detected",
      start: "2024-12-04",
      color: "hsl(0, 70%, 50%)",
      description: "Suspicious transfer of sensitive data from internal server to external IP address."
    },
    {
      id: "dec-2",
      title: "Abnormal Data Deletion Attempt",
      start: "2024-12-06",
      color: "hsl(348, 70%, 50%)",
      description: "User attempted to delete important database records without authorization."
    },
    {
      id: "dec-3",
      title: "Privilege Escalation Detected",
      start: "2024-12-10",
      color: "hsl(50, 70%, 50%)",
      description: "A non-admin user attempted to escalate privileges to access administrator controls."
    },
    {
      id: "dec-4",
      title: "Suspicious User Activity on Server",
      start: "2024-12-13",
      color: "hsl(207, 70%, 50%)",
      description: "User logged into a server unexpectedly, and accessed multiple sensitive files."
    },

    // February 2025 - Abnormal login times, access attempts, and system behaviors
    {
      id: "feb-1",
      title: "Unusual Login Time Detected",
      start: "2025-02-01",
      color: "hsl(348, 70%, 50%)",
      description: "User logged in at an unusual time (2:30 AM), outside of normal hours."
    },
    {
      id: "feb-2",
      title: "Multiple Failed Login Attempts",
      start: "2025-02-02",
      color: "hsl(0, 70%, 50%)",
      description: "User failed to login 6 times in a row within a 5-minute period."
    },
    {
      id: "feb-3",
      title: "Suspicious Device Access",
      start: "2025-02-03",
      color: "hsl(207, 70%, 50%)",
      description: "User accessed their account from a previously unknown device."
    },
    {
      id: "feb-4",
      title: "Privileged Account Misuse Attempt",
      start: "2025-02-04",
      color: "hsl(50, 70%, 50%)",
      description: "Admin account accessed by a user with regular privileges, unauthorized attempt."
    },
    {
      id: "feb-5",
      title: "Anomalous File Transfer Detected",
      start: "2025-02-05",
      color: "hsl(0, 70%, 50%)",
      description: "Large file transfer (over 500MB) initiated from internal server to external source."
    },
    {
      id: "feb-6",
      title: "Data Access Outside of Normal Working Hours",
      start: "2025-02-06",
      color: "hsl(50, 70%, 50%)",
      description: "User accessed confidential company data at midnight, which is inconsistent with their usual pattern."
    },
    {
      id: "feb-7",
      title: "Unusual Login From Different Location",
      start: "2025-02-07",
      color: "hsl(348, 70%, 50%)",
      description: "Login detected from a location where the user has not logged in before."
    },
    {
      id: "feb-8",
      title: "Excessive Failed Attempt to Access Restricted Area",
      start: "2025-02-08",
      color: "hsl(0, 70%, 50%)",
      description: "User attempted to access a restricted section of the system 3 times in a short time."
    },
    {
      id: "feb-9",
      title: "Unusual Data Deletion Attempt",
      start: "2025-02-09",
      color: "hsl(207, 70%, 50%)",
      description: "User attempted to delete critical data that they do not have authorization to remove."
    },
    {
      id: "feb-10",
      title: "Privileged Access Escalation Attempt",
      start: "2025-02-10",
      color: "hsl(50, 70%, 50%)",
      description: "Non-privileged user tried escalating privileges to gain access to administrator controls."
    },
    {
      id: "feb-11",
      title: "Suspicious Activity Detected on User Account",
      start: "2025-02-11",
      color: "hsl(348, 70%, 50%)",
      description: "Multiple login attempts detected on a user account from different locations within an hour."
    },
  ];

  const handleDateClick = (selected) => {
    const title = prompt("Please enter a new title for your event");
    const calendarApi = selected.view.calendar;
    calendarApi.unselect();

    if (title) {
      calendarApi.addEvent({
        id: `${selected.dateStr}-${title}`,
        title,
        start: selected.startStr,
        end: selected.endStr,
        allDay: selected.allDay,
      });
    }
  };

  const handleEventClick = (selected) => {
    if (
      window.confirm(
        `Are you sure you want to delete the event '${selected.event.title}'`
      )
    ) {
      selected.event.remove();
    }
  };

  return (
    <Box m="20px">
      <Header title="Calendar" subtitle="Full Calendar Interactive Page" />

      <Box display="flex" justifyContent="space-between">
        {/* CALENDAR SIDEBAR */}
        <Box
          flex="1 1 20%"
          backgroundColor={colors.primary[400]}
          p="15px"
          borderRadius="4px"
        >
          <Typography variant="h5">Events</Typography>
          <List>
            {currentEvents.map((event) => (
              <ListItem
                key={event.id}
                sx={{
                  backgroundColor: colors.greenAccent[500],
                  margin: "10px 0",
                  borderRadius: "2px",
                }}
              >
                <ListItemText
                  primary={event.title}
                  secondary={
                    <Typography>
                      {formatDate(event.start, {
                        year: "numeric",
                        month: "short",
                        day: "numeric",
                      })}
                    </Typography>
                  }
                />
              </ListItem>
            ))}
          </List>
        </Box>

        {/* CALENDAR */}
        <Box flex="1 1 100%" ml="15px">
          <FullCalendar
            height="75vh"
            plugins={[
              dayGridPlugin,
              timeGridPlugin,
              interactionPlugin,
              listPlugin,
            ]}
            headerToolbar={{
              left: "prev,next today",
              center: "title",
              right: "dayGridMonth,timeGridWeek,timeGridDay,listMonth",
            }}
            initialView="dayGridMonth"
            editable={true}
            selectable={true}
            selectMirror={true}
            dayMaxEvents={true}
            select={handleDateClick}
            eventClick={handleEventClick}
            eventsSet={(events) => setCurrentEvents(events)}
            initialEvents={abnormalBehaviors}
          />
        </Box>
      </Box>
    </Box>
  );
};

export default Calendar;