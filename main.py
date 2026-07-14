"""
main.py

Entry Point for
AI Student Assessment System
"""

from config.settings import (
    PROJECT_NAME,
    VERSION,
    AUTHOR
)

from src.pipeline import (
    run_complete_pipeline,
    generate_reports,
    generate_pdfs,
    generate_charts,
    send_emails,
    show_analytics
)


# ==========================================================
# Display Menu
# ==========================================================

def menu():

    print("\n" + "=" * 70)
    print(f"{PROJECT_NAME:^70}")
    print("=" * 70)
    print(f"Version : {VERSION}")
    print(f"Author  : {AUTHOR}")
    print("=" * 70)

    print("1. Run Complete Assessment Pipeline")
    print("2. Generate Excel Reports")
    print("3. Generate PDF Grade Cards")
    print("4. Generate Charts")
    print("5. Send Emails")
    print("6. View Analytics")
    print("0. Exit")

    print("=" * 70)


# ==========================================================
# Main Function
# ==========================================================

def main():

    while True:

        menu()

        choice = input("\nEnter your choice: ").strip()

        try:

            if choice == "1":

                print("\nRunning Complete Assessment Pipeline...\n")

                run_complete_pipeline()

                print("\n✓ Pipeline Completed Successfully.")

            elif choice == "2":

                print("\nGenerating Excel Reports...\n")

                generate_reports()

                print("\n✓ Excel Reports Generated Successfully.")

            elif choice == "3":

                print("\nGenerating PDF Grade Cards...\n")

                generate_pdfs()

                print("\n✓ PDF Grade Cards Generated Successfully.")

            elif choice == "4":

                print("\nGenerating Charts...\n")

                generate_charts()

                print("\n✓ Charts Generated Successfully.")

            elif choice == "5":

                print("\nSending Emails...\n")

                send_emails()

                print("\n✓ Emails Sent Successfully.")

            elif choice == "6":

                print("\nGenerating Analytics...\n")

                show_analytics()

            elif choice == "0":

                print("\n" + "=" * 70)
                print("Thank you for using AI Student Assessment System")
                print(f"Developed by {AUTHOR}")
                print("=" * 70)

                break

            else:

                print("\n❌ Invalid choice. Please enter a number between 0 and 6.")

        except KeyboardInterrupt:

            print("\n\nProgram interrupted by user.")
            break

        except Exception as e:

            print("\n" + "=" * 70)
            print("An error occurred while executing the selected operation.")
            print(f"Error: {e}")
            print("=" * 70)


# ==========================================================
# Start Application
# ==========================================================

if __name__ == "__main__":

    main()