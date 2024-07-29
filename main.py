"""
Aplikasi Dashboard Monitoring
"""
import gempaterkini

if __name__ == '__main__':
    print('Aplikasi Utama')
    results = gempaterkini.ekstraksi_data()
    gempaterkini.tampilkan_data(results)