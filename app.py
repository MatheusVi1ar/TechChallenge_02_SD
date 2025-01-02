from datetime import datetime
import util.scrap as scrap
import util.constantes as constantes
import util.aws as aws

def main():
#def lambda_handler(event, context):
    try:
        datenow = datetime.today().strftime('%Y%m%d')

        # Extract HTML
        try:
            parquet_buffer = scrap.scrap_html(constantes.url, datenow)
        except Exception as e:
            print(f"Error extracting HTML: {e}")
            return

        # Upload Parquet file to S3
        try:
            aws.enviar_parquet_s3(  parquet_buffer, 
                                    datenow, 
                                    constantes.access_key, 
                                    constantes.secret_key, 
                                    constantes.session_token)
        except Exception as e:
            print(f"Error uploading to S3: {e}")
            return

    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == '__main__':
    main()