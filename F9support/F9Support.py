import os
import pickle
import base64
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import webbrowser
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass

# If modifying these scopes, delete the token.pickle file
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header(title):
    """Display a formatted header"""
    print("\n" + "=" * 60)
    print(f" {title} ".center(60, "="))
    print("=" * 60)

def get_gmail_service():
    """Shows basic usage of the Gmail API.
    Creates a Gmail API service object and returns it.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    # If there are no (valid) credentials available, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception as refresh_error:
                print(f"Token refresh failed: {refresh_error}")
                creds = None
        else:
            creds = None
    
    if not creds:
        # Check if credentials file exists
        if not os.path.exists('credentials.json'):
                 print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                 print("XX                                                                          XX")
                 print("XX   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   XX")
                 print("XX   MMMMMMMMMMMMMMMMMMMMMssssssssssssssssssssssssssMMMMMMMMMMMMMMMMMMMMM   XX")
                 print("XX   MMMMMMMMyy''                                            ''yyMMMMMMMM   XX")
                 print("XX   MMMMMy''                                                    ''yMMMMM   XX")
                 print("XX   MMMy'                                                          'yMMM   XX")
                 print("XX   Mh'                          SC : F91.1                          'hM   XX")
                 print("XX   -                                                                  -   XX")
                 print("XX                                                                          XX")
                 print("XX   ::                                                                ::   XX")
                 print("XX   MMhh.        ..hhhhhh..       FSOCIETY       ..hhhhhh..        .hhMM   XX")
                 print("XX   MMMMMh   ..hhMMMMMMMMMMhh.                .hhMMMMMMMMMMhh..   hMMMMM   XX")
                 print("XX   ---MMM .hMMMMdd:::dMMMMMMMhh..        ..hhMMMMMMMd:::ddMMMMh. MMM---   XX")
                 print("XX   MMMMMM MMmm''      'mmMMMMMMMMyy.  .yyMMMMMMMMmm'      ''mmMM MMMMMM   XX")
                 print("XX   ---mMM ''             'mmMMMMMMMM  MMMMMMMMmm'             '' MMm---   XX")
                 print("XX   yyyym'    .              'mMMMMm'  'mMMMMm'              .    'myyyy   XX")
                 print("XX   mm''    .y'     ..yyyyy..  ''''      ''''  ..yyyyy..     'y.    ''mm   XX")
                 print("XX           MN    .sMMMMMMMMMss.   .    .   .ssMMMMMMMMMs.    NM           XX")
                 print("XX           N`    MMMMMMMMMMMMMN   M    M   NMMMMMMMMMMMMM    `N           XX")
                 print("XX            +  .sMNNNNNMMMMMN+   `N    N`   +NMMMMMNNNNNMs.  +            XX")
                 print("XX              o+++     ++++Mo    M      M    oM++++     +++o              XX")
                 print("XX                                oo  J   oo                                XX")
                 print("XX           oM                 oo          oo                 Mo           XX")
                 print("XX         oMMo          R     /              \     O           oMMo        XX")
                 print("XX       +MMMM                 s             s                  MMMM+       XX")
                 print("XX      +MMMMM+  M         +++NNNN+     +NNNN+++         G     +MMMMM+      XX")
                 print("XX     +MMMMMMM+       ++NNMMMMMMMMN+    +NMMMMMMMMNN++       +MMMMMMM+     XX")
                 print("XX     MMMMMMMMMNN+++NNMMMMMMMMMMMMMMNNNNMMMMMMMMMMMMMMNN+++NNMMMMMMMMM     XX")
                 print("XX     yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy     XX")
                 print("XX   m  yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy  m   XX")
                 print("XX   MMm yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy mMM   XX")
                 print("XX   MMMm .yyMMMMMMMMMMMMMMMM     MMMMMMMMMM     MMMMMMMMMMMMMMMMyy. mMMM   XX")
                 print("XX   MMMMd   ''''hhhhh       odddo          obbbo        hhhh''''   dMMMM   XX")
                 print("XX   MMMMMd             'hMMMMMMMMMMddddddMMMMMMMMMMh'             dMMMMM   XX")
                 print("XX   MMMMMMd              'hMMMMMMMMMMMMMMMMMMMMMMh'              dMMMMMM   XX")
                 print("XX   MMMMMMM-               ''ddMMMMMMMMMMMMMMdd''               -MMMMMMM   XX")
                 print("XX   MMMMMMMM                   '::dddddddd::'                   MMMMMMMM   XX")
                 print("XX   MMMMMMMM-                                                  -MMMMMMMM   XX")
                 print("XX   MMMMMMMMM                                                  MMMMMMMMM   XX")
                 print("XX   MMMMMMMMMy                                                yMMMMMMMMM   XX")
                 print("XX   MMMMMMMMMMy.                                            .yMMMMMMMMMM   XX")
                 print("XX   MMMMMMMMMMMMy.                                        .yMMMMMMMMMMMM   XX")
                 print("XX   MMMMMMMMMMMMMMy.                                    .yMMMMMMMMMMMMMM   XX")
                 print("XX   MMMMMMMMMMMMMMMMs.                                .sMMMMMMMMMMMMMMMM   XX")
                 print("XX   MMMMMMMMMMMMMMMMMMss.           ....           .ssMMMMMMMMMMMMMMMMMM   XX")
                 print("XX   MMMMMMMMMMMMMMMMMMMMNo         oNNNNo         oNMMMMMMMMMMMMMMMMMMMM   XX")
                 print("XX                                                                          XX")
                 print ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                 print("XX                             - F9 Support -                               XX")
                 print("XX            To contact Visit https://guns.lol/F911 or SC:F91.1            XX")
                 print ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                 print("XX                                                                          XX")                 
                 print("XX               There is 2 ways to run this tool (API - SMTP)              XX")
                 print("XX                                                                          XX")
                 print("XX                   if u want to use api follow the steps                  XX")
                 print("XX               1. Go to https://console.cloud.google.com/                 XX")
                 print("XX                                                                          XX")
                 print("XX               2. Create a new project                                    XX")
                 print("XX                                                                          XX")
                 print("XX               3. Enable Gmail API                                        XX")
                 print("XX                                                                          XX")
                 print("XX               4. Create OAuth 2.0 credentials for a Desktop App          XX")
                 print("XX                                                                          XX")
                 print("XX               5. Download the credentials.json file                      XX")
                 print("XX                  and place it in the same folder                         XX")
                 print("XX                                                                          XX")
                 print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                 print("XX                                                                          XX")
                 print("XX                and to use smtp follow the steps                          XX")
                 print("XX                                                                          XX")
                 print("XX              1- Go to  https://myaccount.google.com/security             XX")
                 print("XX                                                                          XX")
                 print("XX              2- TURN ON 2-FAC and set (application password )            XX")
                 print("XX              u can use the search bar above the screen to find it        XX")
                 print("XX                                                                          XX")
                 print("XX              3- run the app with no cerdentials and when i ask you       XX")
                 print("XX              For password write the applications password                XX")
                 print("XX                                                                          XX")
                 print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


                 input("\nPress Enter after you've placed credentials.json in this folder OR when u are ready...")
        
        if os.path.exists('credentials.json'):
            try:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
                
                # Save the credentials for the next run
                with open('token.pickle', 'wb') as token:
                    pickle.dump(creds, token)
            except Exception as flow_error:
                print(f"Authentication flow failed: {flow_error}")
                return None
        else:
            print("credentials.json file not found. Falling back to SMTP.")
            return None
    
    try:
        service = build('gmail', 'v1', credentials=creds)
        return service
    except Exception as build_error:
        print(f"Failed to build Gmail service: {build_error}")
        return None

def create_message(to, subject, message_text):
    """Create a message for an email."""
    message = f"To: {to}\nSubject: {subject}\n\n{message_text}"
    return {'raw': base64.urlsafe_b64encode(message.encode('utf-8')).decode('utf-8')}

def send_message_api(service, message):
    """Send an email message using Gmail API."""
    try:
        result = service.users().messages().send(userId="me", body=message).execute()
        return result
    except Exception as error:
        print(f"Gmail API error: {error}")
        return None

def send_message_smtp(sender_email, password, to, subject, message_text):
    """Send an email message using SMTP fallback."""
    try:
        # Create email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(message_text, 'plain'))
        
        # Connect to Gmail's SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
        return True
    except Exception as e:
        print(f"SMTP error: {e}")
        return False

def send_support_email(platform, service):
    """Send email to support team for a specific platform"""
    # Platform-specific information
    platforms = {
        "instagram": {
            "email": "support@instagram.com",
            "name": "Instagram Support",
            "help_url": "https://help.instagram.com/",
            "tips": "• Include your Instagram username\n• Describe your issue in detail\n• Mention when the problem started"
        },
        "snapchat": {
            "email": "support@snapchat.com",
            "name": "Snapchat Support",
            "help_url": "https://support.snapchat.com/",
            "tips": "• Include your Snapchat username\n• Describe your device model\n• Explain what's not working"
        },
        "tiktok": {
            "email": "support@tiktok.com",
            "name": "TikTok Support",
            "help_url": "https://support.tiktok.com/",
            "tips": "• Include your TikTok username\n• Provide relevant video links\n• Describe the issue clearly"
        },
        "youtube": {
            "email": "support@youtube.com",
            "name": "YouTube Support",
            "help_url": "https://support.google.com/youtube/",
            "tips": "• Include your YouTube channel URL\n• Specify if you're a creator or viewer\n• Add video links if relevant"
        },
        "facebook": {
            "email": "support@fb.com",
            "name": "Facebook Support",
            "help_url": "https://www.facebook.com/help/",
            "tips": "• Include your Facebook profile URL\n• Specify if it's about an account, page, or ad\n• Mention any error messages"
        },
        "twitter": {
            "email": "support@twitter.com",
            "name": "Twitter Support",
            "help_url": "https://help.twitter.com/",
            "tips": "• Include your Twitter handle\n• Describe the issue clearly\n• Add tweet links if relevant"
        },
        "whatsapp": {
            "email": "support@whatsapp.com",
            "name": "WhatsApp Support",
            "help_url": "https://faq.whatsapp.com/",
            "tips": "• Include your phone number with country code\n• Describe your device model\n• Mention if it's about messages, calls, or account"
        },
        "linkedin": {
            "email": "support@linkedin.com",
            "name": "LinkedIn Support",
            "help_url": "https://www.linkedin.com/help/",
            "tips": "• Include your LinkedIn profile URL\n• Specify if it's about your account, job search, or connections\n• Mention any error codes"
        },
        "pinterest": {
            "email": "support@pinterest.com",
            "name": "Pinterest Support",
            "help_url": "https://help.pinterest.com/",
            "tips": "• Include your Pinterest profile URL\n• Describe your issue with boards or pins\n• Add links to problematic content"
        },
        "reddit": {
            "email": "support@reddit.com",
            "name": "Reddit Support",
            "help_url": "https://www.reddithelp.com/",
            "tips": "• Include your Reddit username\n• Specify if it's about your account, subreddit, or content\n• Add links to relevant posts"
        },
        "discord": {
            "email": "support@discord.com",
            "name": "Discord Support",
            "help_url": "https://support.discord.com/",
            "tips": "• Include your Discord username and tag\n• Describe your server or channel issue\n• Mention any error messages"
        },
        "telegram": {
            "email": "support@telegram.org",
            "name": "Telegram Support",
            "help_url": "https://telegram.org/support",
            "tips": "• Include your phone number with country code\n• Describe your device model\n• Specify if it's about messages, groups, or security"
        }
    }
    
    # Get platform data
    platform_data = platforms[platform]
    
    clear_screen()
    display_header(f"F9 {platform.upper()} SUPPORT")
    
    # Get user email
    sender_email = input("\nEnter your Gmail address: ").strip()
    
    # Compose email
    print("\n" + "-" * 60)
    print(f"Compose your message to {platform_data['name']}:")
    subject = input("\nSubject: ")
    message_text = input("\nDetailed message:\n")
    
    # Add platform-specific tips
    message_text += f"\n\n--- Additional Information ---\n{platform_data['tips']}"
    
    # Create message
    full_subject = f"{platform.upper()} SUPPORT REQUEST: {subject}"
    
    # Try to send using API
    api_success = False
    if service:
        message = create_message(platform_data["email"], full_subject, message_text)
        result = send_message_api(service, message)
        if result:
            api_success = True
    
    # Fallback to SMTP if API failed
    if not api_success:
        print("\n" + "=" * 60)
        print("UR SMTP INSTEAD".center(60))
        print("=" * 60)
        print("\nCouldn't use Gmail API. F9 Will use SMTP  FOR U <3 .")
        print("Note: u should use applications password .")
        print("in your Google Account security settings.")
        
        password = getpass.getpass("\nEnter your Gmail password to send ur tears : ")
        smtp_success = send_message_smtp(
            sender_email, password,
            platform_data["email"], full_subject, message_text
        )
        
        if not smtp_success:
            print("\n" + "=" * 60)
            print("MESSAGE FAILED TO SEND".center(60))
            print("=" * 60)
            print("\nBoth Gmail API and SMTP failed , Don't Play with ME BOY ! .")
            print("Fix  ur shit and come back.")
            return
    
    # Success message
    clear_screen()
    display_header("Tears SENT SUCCESSFULLY")
    print(f"\n✓ Your tears has been sent to {platform_data['name']}!")
    print(f"✓ Check your inbox at {sender_email} for responses within 24-48 hours.")
    
    # Additional help options
    print("\n" + "-" * 60)
    print("Need additional help?")
    print("u can dm me https://guns,lol/f911")
    print(f"• Visit {platform_data['name']} Help Center: {platform_data['help_url']}")
    print(f"• Check your spam folder in Gmail")
    print("• Contact through official social media channels")

def show_help_center(platform):
    """Open the help center for a platform"""
    help_centers = {
        "instagram": "https://help.instagram.com/",
        "snapchat": "https://support.snapchat.com/",
        "tiktok": "https://support.tiktok.com/",
        "youtube": "https://support.google.com/youtube/",
        "facebook": "https://www.facebook.com/help/",
        "twitter": "https://help.twitter.com/",
        "whatsapp": "https://faq.whatsapp.com/",
        "linkedin": "https://www.linkedin.com/help/",
        "pinterest": "https://help.pinterest.com/",
        "reddit": "https://www.reddithelp.com/",
        "discord": "https://support.discord.com/",
        "telegram": "https://telegram.org/support"
    }
    
    url = help_centers.get(platform, "https://google.com")
    print(f"\nOpening {platform.capitalize()} Help Center in your browser...")
    webbrowser.open(url)

def main():
    """Main program function"""
    # Get Gmail service
    service = None
    try:
        service = get_gmail_service()
        if service:
            print("Gmail API initialized successfully.")
        else:
            print("Using SMTP fallback for email sending.")
    except Exception as e:
        print(f"Error initializing Gmail service: {str(e)}")
        print("Falling back to SMTP for email sending.")
        service = None
    
    # Main menu
    while True:
        clear_screen()
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("XX                                                                          XX")
        print("XX   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   XX")
        print("XX   MMMMMMMMMMMMMMMMMMMMMssssssssssssssssssssssssssMMMMMMMMMMMMMMMMMMMMM   XX")
        print("XX   MMMMMMMMyy''                                            ''yyMMMMMMMM   XX")
        print("XX   MMMMMy''                                                    ''yMMMMM   XX")
        print("XX   MMMy'                                                          'yMMM   XX")
        print("XX   Mh'                          SC : F91.1                          'hM   XX")
        print("XX   -                                                                  -   XX")
        print("XX                                                                          XX")
        print("XX   ::                                                                ::   XX")
        print("XX   MMhh.        ..hhhhhh..       FSOCIETY       ..hhhhhh..        .hhMM   XX")
        print("XX   MMMMMh   ..hhMMMMMMMMMMhh.                .hhMMMMMMMMMMhh..   hMMMMM   XX")
        print("XX   ---MMM .hMMMMdd:::dMMMMMMMhh..        ..hhMMMMMMMd:::ddMMMMh. MMM---   XX")
        print("XX   MMMMMM MMmm''      'mmMMMMMMMMyy.  .yyMMMMMMMMmm'      ''mmMM MMMMMM   XX")
        print("XX   ---mMM ''             'mmMMMMMMMM  MMMMMMMMmm'             '' MMm---   XX")
        print("XX   yyyym'    .              'mMMMMm'  'mMMMMm'              .    'myyyy   XX")
        print("XX   mm''    .y'     ..yyyyy..  ''''      ''''  ..yyyyy..     'y.    ''mm   XX")
        print("XX           MN    .sMMMMMMMMMss.   .    .   .ssMMMMMMMMMs.    NM           XX")
        print("XX           N`    MMMMMMMMMMMMMN   M    M   NMMMMMMMMMMMMM    `N           XX")
        print("XX            +  .sMNNNNNMMMMMN+   `N    N`   +NMMMMMNNNNNMs.  +            XX")
        print("XX              o+++     ++++Mo    M      M    oM++++     +++o              XX")
        print("XX                                oo  J   oo                                XX")
        print("XX           oM                 oo          oo                 Mo           XX")
        print("XX         oMMo          R     /              \     O           oMMo        XX")
        print("XX       +MMMM                 s             s                  MMMM+       XX")
        print("XX      +MMMMM+  M         +++NNNN+     +NNNN+++         G     +MMMMM+      XX")
        print("XX     +MMMMMMM+       ++NNMMMMMMMMN+    +NMMMMMMMMNN++       +MMMMMMM+     XX")
        print("XX     MMMMMMMMMNN+++NNMMMMMMMMMMMMMMNNNNMMMMMMMMMMMMMMNN+++NNMMMMMMMMM     XX")
        print("XX     yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy     XX")
        print("XX   m  yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy  m   XX")
        print("XX   MMm yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy mMM   XX")
        print("XX   MMMm .yyMMMMMMMMMMMMMMMM     MMMMMMMMMM     MMMMMMMMMMMMMMMMyy. mMMM   XX")
        print("XX   MMMMd   ''''hhhhh       odddo          obbbo        hhhh''''   dMMMM   XX")
        print("XX   MMMMMd             'hMMMMMMMMMMddddddMMMMMMMMMMh'             dMMMMM   XX")
        print("XX   MMMMMMd              'hMMMMMMMMMMMMMMMMMMMMMMh'              dMMMMMM   XX")
        print("XX   MMMMMMM-               ''ddMMMMMMMMMMMMMMdd''               -MMMMMMM   XX")
        print("XX   MMMMMMMM                   '::dddddddd::'                   MMMMMMMM   XX")
        print("XX   MMMMMMMM-                                                  -MMMMMMMM   XX")
        print("XX   MMMMMMMMM                                                  MMMMMMMMM   XX")
        print("XX   MMMMMMMMMy                                                yMMMMMMMMM   XX")
        print("XX   MMMMMMMMMMy.                                            .yMMMMMMMMMM   XX")
        print("XX   MMMMMMMMMMMMy.                                        .yMMMMMMMMMMMM   XX")
        print("XX   MMMMMMMMMMMMMMy.                                    .yMMMMMMMMMMMMMM   XX")
        print("XX   MMMMMMMMMMMMMMMMs.                                .sMMMMMMMMMMMMMMMM   XX")
        print("XX   MMMMMMMMMMMMMMMMMMss.           ....           .ssMMMMMMMMMMMMMMMMMM   XX")
        print("XX   MMMMMMMMMMMMMMMMMMMMNo         oNNNNo         oNMMMMMMMMMMMMMMMMMMMM   XX")
        print("XX                                                                          XX")
        print ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("XX                                                                          XX")
        print("XX                             - F9 Support -                               XX")
        print("XX                                                                          XX")
        print("XX            To contact Visit https://guns.lol/F911 or SC:F91.1            XX")
        print("XX                                                                          XX")
        print ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("XX                                                                          XX")
        print("XX                    Choose a platform to start Crying :                   XX")
        print("XX                                                                          XX")
        print("XX                              1. Instagram                                XX")
        print("XX                              2. Snapchat                                 XX")
        print("XX                              3. TikTok                                   XX")
        print("XX                              4. YouTube                                  XX")
        print("XX                              5. Facebook                                 XX")
        print("XX                              6. Twitter                                  XX")
        print("XX                              7. WhatsApp                                 XX")
        print("XX                              8. LinkedIn                                 XX")
        print("XX                              9. Pinterest                                XX")
        print("XX                              10. Reddit                                  XX")
        print("XX                              11. Discord                                 XX")
        print("XX                              12. Telegram                                XX")
        print("XX                              13. Open Help Center  (No Email)            XX")
        print("XX                                                                          XX")
        print ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
        print("\nChoose a platform to contact support:")
        print(" 1. Instagram ")
        print(" 2. Snapchat ")
        print(" 3. TikTok ")
        print(" 4. YouTube ")
        print(" 5. Facebook ")
        print(" 6. Twitter ")
        print(" 7. WhatsApp ")
        print(" 8. LinkedIn ")
        print(" 9. Pinterest ")
        print("10. Reddit ")
        print("11. Discord Spport")
        print("12. Telegram ")
        print("13. Open Help Center (No Email)")
        print("14. Exit")
        
        choice = input("\nEnter your choice (1-14): ")
        
        platforms = [
            "instagram", "snapchat", "tiktok", "youtube",
            "facebook", "twitter", "whatsapp", "linkedin",
            "pinterest", "reddit", "discord", "telegram"
        ]
        
        try:
            choice_index = int(choice) - 1
            if 0 <= choice_index <= 11:
                send_support_email(platforms[choice_index], service)
            elif choice == "13":
                print("\nAvailable platforms:")
                for i, platform in enumerate(platforms, 1):
                    print(f"{i}. {platform.capitalize()}")
                platform_choice = input("\nEnter platform number to open help center: ")
                try:
                    platform_index = int(platform_choice) - 1
                    if 0 <= platform_index < len(platforms):
                        show_help_center(platforms[platform_index])
                    else:
                        print("Invalid platform number.")
                except:
                    print("Invalid input. Please enter a number.")
            elif choice == "14":
                print("\nThank you for using the support tool. Goodbye!")
                break
            else:
                print("Invalid choice! Please enter 1-14.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()