import psycopg2
import pymysql.cursors

"""データベース設定※settings.pyのデータベース情報も変更必要"""
conn = pymysql.connect(host='localhost',  # 測定値データホスト
                       user='vrest',  # 測定値データユーザー名
                       password='vrest',  # 測定値データパスワード
                       db='ofa_system',  # 測定値データベース名
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)
host_temp = 'localhost'  # 一時データホスト
user_temp = 'postgres'  # 一時データユーザー名
password_temp = 'postgres'  # 一時データパスワード
database_temp = 'postgres'  # 一時データデータベース名
port_temp = '5432'  # 一時データポート番号
connection_config2 = psycopg2.connect(host='124.146.154.219',  # MAPデータホスト
                                      dbname='safety_mobility',  # MAPデータベース名
                                      user='syssoft_admin',  # MAPデータユーザー名
                                      password='Sk4gADca')  # MAPデータパスワード
conn2 = psycopg2.connect(host=host_temp,
                         port=port_temp,
                         dbname=database_temp,
                         user=user_temp,
                         password=password_temp)
"""モデルデータ設定"""
model_equip_id = 3  # モデルデータの車体識別番号
model_run_start_date = ''  # モデルデータの走行開始日時
"""block_no設定"""
A_block_no_dep = 1  # 発着所
A_block_no_curve = 2  # カーブ
A_block_no_cross = 3  # 交差点
A_block_no_top = 4  # 頂上
A_block_no_slope = 5  # 坂道
"""CAN設定"""
position_right = 1  # ウィンカー右
position_left = 2  # ウィンカー左
position_center = 3  # ウィンカー中心
level_right = 10  # ハンドル右閾値
level_left = -10  # ウィンカー左閾値
blake_sw_on_val = 1  # ブレーキON
accel_on_val = 10  # アクセルON
"""データ許容最小数"""
num_axis_min = 1000  # ９軸センサ
num_can_min = 1000  # CAN
num_gps_min = 1000  # GPS
block_e_percent = 0.5  # ブロックナンバー割り当て成功割合
"""測定値閾値"""
slowly_speed = 10  # 徐行速度
slowly_speed_dif = 5  # 徐行速度違反時オーバースピード

reverse_s_val = 10  # 逆行距離小
reverse_m_val = 15  # 逆行距離中
reverse_l_val = 20  # 逆行距離大
speed_fast_s_val = 5  # 速度速すぎ小
speed_fast_m_val = 10  # 速度速すぎ大
speedover_s_val = 45  # 速度超過小
speedover_m_val = 50  # 速度超過中
speedover_l_val = 60  # 速度超過大
speedover_c_s_val = 0.3  # 速度速すぎカーブ小
speedover_c_m_val = 0.4  # 速度速すぎカーブ大
blake_uneven_val = 0.4  # ブレーキむら重力加速度
accel_uneven_val = 0.4  # アクセルむら重力加速度
sudden_handle_val = 0.3  # ハンドル操作むら重力加速度
sudden_brake_val = 0.4  # 急ブレーキ重力加速度
dep_fail_to_signal_time_val = 30  # 発着所ウィンカー操作継続時間
dep_fail_to_signal_return_val = 50  # 発着所ウィンカー操作長すぎ判定時間
cross_fail_to_signal_time_val = 30  # 交差点ウィンカー操作継続時間
cross_fail_to_signal_return_val = 50  # 交差点ウィンカー操作長すぎ判定時間

"""点数"""
reverse_s_point = 5  # 逆行小
reverse_m_point = 20  # 逆行中
reverse_l_point = 50  # 逆行大
speed_fast_s_point = 20  # 速度速すぎ小
speed_fast_m_point = 20  # 速度速すぎ大
slow_down_cross_point = 20  # 徐行速度違反交差点
slow_down_top_point = 20  # 徐行速度違反頂上
slow_down_slope_point = 20  # 徐行速度違反坂道
speedover_s_point = 5  # 速度超過小
speedover_m_point = 20  # 速度超過中
speedover_l_point = 50  # 速度超過大
speedover_c_s_point = 5  # 速度超過カーブ小
speedover_c_m_point = 20  # 速度超過カーブ大
blake_uneven_point = 5  # ブレーキむら
accel_uneven_point = 5  # アクセルむら
sudden_handle_point = 20  # 急ハンドル
sudden_brake_point = 5  # 急ブレーキ違反
dep_fail_to_signal_not_point = 5  # 発着所合図しない
dep_fail_to_signal_time_point = 5  # 発着所合図短い
dep_fail_to_signal_return_point = 5  # 発着所合図長すぎ
cross_fail_to_signal_not_point = 5  # 交差点合図しない
cross_fail_to_signal_time_point = 5  # 交差点合図短い
cross_fail_to_signal_return_point = 5  # 交差点合図長すぎ

"""その他"""
significant_digits_vec = 6  # 有効数字
apihost = 'localhost'

connection_config1 = {'user': user_temp,
                      'database': database_temp,
                      'password': password_temp,
                      'host': host_temp,
                      'port': port_temp,}
