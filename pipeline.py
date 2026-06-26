import pandas as pd
import os

# إعدادات المسارات
BASE_FILE = 'fomo_prototype_data.csv'
NEW_DATA_FILE = 'your_new_kaggle_file.csv'  # تأكد من وضع اسم الملف الجديد الذي حملته هنا

def clean_data(df):
    """وظيفة لتنظيف البيانات من أي قيم فارغة"""
    return df.dropna().drop_duplicates()

def run_pipeline():
    print("--- بدء عملية Pipeline ---")
    
    # 1. التحقق من وجود الملفات
    if not os.path.exists(NEW_DATA_FILE):
        print(f"خطأ: ملف {NEW_DATA_FILE} غير موجود.")
        return

    # 2. قراءة البيانات
    try:
        df_base = pd.read_csv(BASE_FILE)
        df_new = pd.read_csv(NEW_DATA_FILE)
        
        # 3. المعالجة (Cleaning)
        df_new_cleaned = clean_data(df_new)
        
        # 4. الدمج (Merging)
        final_df = pd.concat([df_base, df_new_cleaned], ignore_index=True)
        
        # 5. الحفظ (Loading)
        final_df.to_csv(BASE_FILE, index=False)
        
        print(f"تمت العملية بنجاح!")
        print(f"تم إضافة {len(df_new_cleaned)} صف جديد للبيانات الأساسية.")
        
    except Exception as e:
        print(f"حدث خطأ أثناء التنفيذ: {e}")

if __name__ == "__main__":
    run_pipeline()