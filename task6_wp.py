import pywhatkit as pw
import datetime, sys

def get_data():
    # Get and validate data
    phone = input('Enter number: ')
    if not phone.startswith('+'):
        print('Invalid phone. Number must start with +234...')
        sys.exit()

    mail = input('Enter text: ').strip()
    tim = input('Enter time (Hr:Min): ')

    try:
         Hr, Mt = map(int, tim.split(':'))
    except ValueError:
        print('TIme format must be HH:MM (24hrs)')
        sys.exit()
    
    # Time validation
    now = datetime.datetime.now()
    if (Hr<=now.hour) or (Mt>=now.minute):
        print('Time must be at least 2mins greater than current time. ')
        exit

    return phone, mail, Hr, Mt

def auto_msg(phone, mail, Hr, Mt):
    try:
        pw.sendwhatmsg(phone, mail, Hr, Mt)
        print('Message sent successfully')
    except Exception as e:
        print(f'Error sending message {e}')

def main():
    p, m, h, min = get_data()
    auto_msg(p, m, h, min)

if __name__=='__main__':
    main()

    