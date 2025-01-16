import subprocess
from datetime import datetime

def make_commits(num_commits: int):
    for i in range(num_commits):
        # Get the current date and time dynamically
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Append some text to the file
        with open('data.txt', 'a') as file:
            file.write(f'Commit {i + 1} on {current_date}\n')
        
        try:
            # Stage the file
            subprocess.run(['git', 'add', 'data.txt'], check=True)
            
            # Commit with a unique message and date
            subprocess.run(
                ['git', 'commit', '--date', current_date, '-m', f'Commit {i + 1} on {current_date}'], 
                check=True
            )
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")
            break
    
    # Push all commits after the loop
    try:
        subprocess.run(['git', 'push'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to push commits: {e}")

# Call the function with the desired number of commits
make_commits(10)
