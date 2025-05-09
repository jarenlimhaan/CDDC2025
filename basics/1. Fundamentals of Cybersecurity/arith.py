import socket

def solve_problem(problem):
    try:
        parts = problem.split()
        num1 = int(parts[0])
        operator = parts[1]
        num2 = int(parts[2])

        if operator == '+':
            return str(num1 + num2)
        elif operator == '-':
            return str(num1 - num2)
        elif operator == '*':
            return str(num1 * num2)
        elif operator == '/':
            return str(num1 / num2)
        else:
            return "Invalid operator"
    except (ValueError, IndexError):
        return "Invalid problem format"

def main():
    host = '52.76.13.43'
    port = 8084

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((host, port))
            print(f"Connected to {host}:{port}")
            count = 0
            while True:
                count += 1
                data = s.recv(1024).decode('utf-8').strip()
                if not data:
                    break
                print(f"Received: {data}")

                if data.startswith("What is"):
                    problem = data[len("What is"):].strip().replace("=", "").strip()
                    solution = solve_problem(problem)
                    response = solution + "\n"
                    s.sendall(response.encode('utf-8'))
                    print(f"Sent: {solution}")
                else:
                    problem = data.replace("=", "").strip()
                    solution = solve_problem(problem)
                    response = solution + "\n"
                    s.sendall(response.encode('utf-8'))
                    print(f"Sent: {solution}")
                    
            print(count)
        except ConnectionRefusedError:
            print("Connection refused. Is the server running?")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()