"""
Type:
start - to start the car
stop - to stop the car
quit - to exit
"""
guide ='Type: \nstart - to start the car \nstop - to stop the car and\nquit - to exit \n '
print(guide)
command = ''
started = False
while True:
    command = input('> ').lower()
    if command == 'start':
        if started:
            print('Car is already started.')
        else:
            started = True
            print('Car started...Ready to go!')
    elif command == 'stop':
        if not started:  # car is already stopped
            print('Car is already stopped')
        else:
            started = False
            print('Car stopped.')
    elif command == 'help':
        print(guide)
    elif command == 'quit':
        print('Goodbye')
        break
    else:
        print(f'Sorry, wrong input. {guide}')


