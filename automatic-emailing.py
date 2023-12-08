import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Read your CSV file
csv_file_path = './Emails.csv'

# Email configuration
your_email = 'email@gmail.com'
your_password = password'
smtp_server = 'smtp.gmail.com'
smtp_port = 587

with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    
    # Skip the header if it exists
    header = next(reader, None)
    
    for row in reader:
        # Extract email from the CSV
        to_email = row[0]  # Assuming the email is in the first column

        # Create the email
        subject = 'Condidature pour un stage PFE'
        body = """Madame, Monsieur,

        Je me permets de vous adresser ma candidature pour un stage d'une durée de 6 mois au sein de votre entreprise, dans le domaine de l'informatique. Actuellement étudiant en 5ème année en ingénierie informatique et réseaux avec une spécialisation en Méthodes Informatiques Appliquées à la Gestion des Entreprises (MIAGE) à l'École Marocaine des Sciences de l'Ingénieur de Marrakech, je suis passionné par le domaine du logiciel et de l'ingénierie logicielle.

        Mon cursus académique m'a permis d'acquérir des compétences approfondies en génie logiciel et en développement informatique. J'ai une solide compréhension des principes de conception de logiciels, de développement d'applications, et de gestion de projets informatiques. Ma formation m'a également donné l'opportunité de travailler sur des projets concrets, tant en équipe qu'en autonomie, ce qui a renforcé ma capacité à résoudre des problèmes complexes et à prendre des décisions techniques éclairées.

        Je suis particulièrement intéressé par l'opportunité de mettre en pratique mes compétences et de contribuer à des projets innovants au sein de votre entreprise. J'apprécie votre réputation en tant qu'entreprise leader dans le domaine informatique, et je suis convaincu que travailler au sein de votre équipe me permettra de développer encore davantage mes compétences en ingénierie logicielle.

        L'opportunité de réaliser un stage au sein de votre entreprise est une étape importante dans ma formation et dans le développement de ma carrière professionnelle. Je suis enthousiaste à l'idée de rejoindre votre entreprise dynamique et de contribuer à son succès en tant que stagiaire en ingénierie logicielle.
        Je suis à votre disposition pour toute information complémentaire et je serais honoré de discuter de ma candidature en détail lors d'un entretien à votre convenance.

        Je vous remercie de l'attention que vous porterez à ma candidature et je vous prie d'agréer, Monsieur, l'expression de mes salutations distinguées.

        Cordialement,

        Aymane AIT EL BHIRI
        """

        msg = MIMEMultipart()
        msg['From'] = your_email
        msg['To'] = to_email
        msg['Subject'] = subject


        msg.attach(MIMEText(body, 'plain'))
        
        # Attach CV
        cv_path = './CV-AYMANE-AIT-EL-BHIRI-FRENCH.pdf'
        with open(cv_path, 'rb') as cv_file:
            cv_attachment = MIMEApplication(cv_file.read(), _subtype="pdf")
            cv_attachment.add_header('Content-Disposition', f'attachment; filename={cv_path}')
            msg.attach(cv_attachment)

        try:
            # Connect to the SMTP server and send the email
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(your_email, your_password)
                server.sendmail(your_email, to_email, msg.as_string())
                server.quit()
            print(f"Email sent successfully to {to_email}")
        except Exception as e:
            print(f"Error sending email to {to_email}: {e}")

