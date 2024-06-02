from almondz_app.models import UserModel
from almondz_app.utils import get_per_user_detail
from almondz_app.s3Services import upload_to_s3
import csv
import os

def convert_to_csv(data):

    """
    Convert data to a CSV file.

    Args:
    - data (dict): Dictionary containing expense data.

    Returns:
    str: Path to the generated CSV file.
    """

    csv_file_path = 'output.csv'

    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow(['Type', 'Name', 'Amount'])
        writer.writerow(['expense', '', data['expense']])
        
        for name, amount in data['final_taken_amount_from_users']:
            writer.writerow(['final_taken_amount_from_users', name, amount])
        
        for name, amount in data['final_given_amount_to_users']:
            writer.writerow(['final_given_amount_to_users', name, amount])

    return csv_file_path


def get_user_data_and_upload_s3_csv():
    """
    Retrieve user data, convert it to CSV, and upload to S3.
    """
    
    try:
        user_ids = UserModel.objects.values_list("userId",flat=True)
        for id in user_ids:
            data = get_per_user_detail(id)
            csv_path = convert_to_csv(data)
            # s3url = upload_to_s3(csv_path)   # I dont have any s3 credential so it will not work.
            # os.remove(csv_path)
    except Exception as e:
        print(e.args[0])