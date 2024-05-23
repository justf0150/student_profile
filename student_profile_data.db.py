import sqlite3

# Connect to the database
conn = sqlite3.connect('student_profile_data.db')
c = conn.cursor()

# Fetch all records from the students table
c.execute("SELECT * FROM students")
rows = c.fetchall()

# Print the fetched records
for row in rows:
    print(row)

# Close the connection
conn.close()