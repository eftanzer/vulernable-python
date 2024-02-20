import psycopg2
# SQL Injection vulnerabilities
def is_admin_sql_injection(username):
    # This function is vulnerable to SQL injection because it directly
    # inserts the username into the SQL query without proper sanitization.
    # An attacker could exploit this by providing a malicious input,
    # such as "admin' --", to gain unauthorized access.
    connection = psycopg2.connect(
        host="localhost",
        database="test",
        user="postgres",
        password="password"
    )
    cursor = connection.cursor()
    query = f"SELECT admin FROM users WHERE username = '{username}'"
    cursor.execute(query)
    result = cursor.fetchone()
    if result is not None:
        return result[0]
    else:
        return False
def update_user_sql_injection(username, new_admin_status):
    # This function is also vulnerable to SQL injection for the same
    # reason as the previous function. An attacker could exploit this
    # to change the admin status of any user.
    connection = psycopg2.connect(
        host="localhost",
        database="test",
        user="postgres",
        password="password"
    )
    cursor = connection.cursor()
    query = f"UPDATE users SET admin = {new_admin_status} WHERE username = '{username}'"
    cursor.execute(query)
    connection.commit()
def delete_user_sql_injection(username):
    # This function is vulnerable to SQL injection for the same
    # reason as the previous functions. An attacker could exploit this
    # to delete any user's account.
    connection = psycopg2.connect(
        host="localhost",
        database="test",
        user="postgres",
        password="password"
    )
    cursor = connection.cursor()
    query = f"DELETE FROM users WHERE username = '{username}'"
    cursor.execute(query)
    connection.commit()
# XSS vulnerabilities
def display_username_xss(username):
    # This function is vulnerable to XSS attacks because it directly
    # inserts the username into the HTML response without proper sanitization.
    # An attacker could exploit this by providing a malicious input,
    # such as "<script>alert('XSS')</script>", to execute arbitrary
    # JavaScript code in the user's browser.
    print(f"<p>Hello, {username}!</p>")
def search_users_xss(search_query):
    # This function is also vulnerable to XSS attacks for the same
    # reason as the previous function. An attacker could exploit this
    # to steal the user's session token or perform other malicious actions.
    print(f"<p>Search results for '{search_query}':</p>")
    print("<ul>")
    print("  <li>User 1</li>")
    print("  <li>User 2</li>")
    print("  <li>User 3</li>")
    print("</ul>")