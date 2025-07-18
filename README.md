# 🕒 Employee Working Hours Calculator 📅

<img src="https://raw.githubusercontent.com/your-username/your-repo/main/working_hours_diagram.png" alt="Working Hours Diagram" width="700"/>

A mini project using **MySQL stored procedures** and **Python (Streamlit)** to calculate total working hours between two dates—excluding **Sundays**, **1st and 2nd Saturdays** (unless they are start or end dates).

---

## 📌 Objective

🎯 Build a solution that:
- 📥 Takes date range inputs.
- 📊 Calculates working hours.
- 🚫 Excludes weekends intelligently.
- 💾 Stores results in a MySQL table.

## 🌐 Live Demo

🚀 Try it now:  
**🔗 [celebal-project-rohit-wakchaure.streamlit.app](http://celebal-project-rohit-wakchaure.streamlit.app/)**

---
<img width="1360" height="685" alt="Screenshot 2025-07-17 150327" src="https://github.com/user-attachments/assets/60581b23-797f-4838-9cfa-169f1c1c12f8" />
<img width="1364" height="647" alt="Screenshot 2025-07-17 150410" src="https://github.com/user-attachments/assets/a23a66a5-66c9-4aa6-83e7-2de90f713992" />
<img width="1092" height="416" alt="Screenshot 2025-07-17 150420" src="https://github.com/user-attachments/assets/57374d79-bec9-409f-b517-b551a7691c79" />

---
## 📊 Power BI Dashboard

In addition to the Streamlit version, this project is also implemented using **Power BI Desktop**.

![Power BI Dashboard](https://img.shields.io/badge/Visualization-Power%20BI-yellow?style=flat-square&logo=powerbi)

📁 [Download Power BI Project File (.pbix)](https://github.com/rohitwakchaure/Celebal-Project-SQL-Working-Hours/blob/main/PowerBi%20Dashboard/Celebal%20project.pbix)

📷 **Dashboard Previews**:

<img width="928" height="552" alt="PowerBi Dashboard" src="https://github.com/user-attachments/assets/e734b94c-0812-43d1-aa9f-4951ebd3732b" />


## 🛠️ Tech Stack

| 🧩 Layer       | 🔧 Technology            |
|---------------|--------------------------|
| Backend       | MySQL (Stored Procedure) |
| Frontend      | Python + Streamlit       |
| Notebook Dev  | Jupyter (.ipynb)         |

---

## 🧠 Problem Statement

🧾 **Inputs**:  
- `START_DATE` (e.g., `2023-07-01`)  
- `END_DATE` (e.g., `2023-07-17`)  

✅ **Rules**:
- Exclude Sundays and 1st/2nd Saturdays from total working hours.
- If start or end date **is** a Sunday or 1st/2nd Saturday, **include** that date.

🕒 Working hours per valid day = **12**

📤 **Outputs** (Stored in `counttotalworkinhours`):

| START_DATE   | END_DATE     | NO_OF_HOURS |
|--------------|--------------|--------------|
| 2023-07-01   | 2023-07-17   | 288          |
| 2023-07-12   | 2023-07-13   | 24           |

---

## 🧮 SQL Stored Procedure

```sql
DELIMITER $$

CREATE PROCEDURE calculateWorkingHours(IN start_date DATE, IN end_date DATE)
BEGIN
    DECLARE current_date DATE;
    DECLARE working_hours INT DEFAULT 0;
    DECLARE isWeekend BOOLEAN;

    SET current_date = start_date;

    WHILE current_date <= end_date DO
        SET isWeekend = (
            (DAYOFWEEK(current_date) = 1) OR
            ((DAYOFWEEK(current_date) = 7) AND (DAY(current_date) <= 14))
        );

        IF NOT isWeekend OR current_date = start_date OR current_date = end_date THEN
            SET working_hours = working_hours + 12;
        END IF;

        SET current_date = DATE_ADD(current_date, INTERVAL 1 DAY);
    END WHILE;

    INSERT INTO counttotalworkinhours (START_DATE, END_DATE, NO_OF_HOURS)
    VALUES (start_date, end_date, working_hours);
END$$

DELIMITER ;
