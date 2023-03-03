'''websocket通信によるタイマー送出


'''
import sys
import numpy as np
import websockets
import asyncio
import time
import datetime
import json

main_timer_trigger_path = "main_decide.txt"

def trigger_init():
    #初回ロード時にタイマーのトリガーをfalseに設定しておく
    with open(main_timer_trigger_path, encoding="utf-8") as f:
        data_lines = f.read()
        
        if data_lines == 'True':
            # 文字列置換
            data_lines = data_lines.replace('True', 'False')
            # 同じファイル名で保存
            with open(main_timer_trigger_path, mode="w", encoding="utf-8") as f:
                f.write(data_lines)
    
    return print('Trigger is OK.')
            


async def timer(websocket):
    while True:
        '''スタートボタンPUSHまで以下
        0.1秒間隔でpathのトリガー状態を監視
        同時にカウントスタート用の時間計測を実施
        '''
        with open(main_timer_trigger_path, encoding="utf-8") as f:
            main_data_lines = f.read()
            print("main trigger -> ",main_data_lines)
            await asyncio.sleep(0.1) 
            
            #計測開始時間
            start_time = time.perf_counter()
            behind_time = 0
            
        '''メインタイマー起動'''
        if main_data_lines == 'True':
            
            #メインタイマーのループ
            while True:
                intermediate_time = time.perf_counter()
                diff_main = np.round(intermediate_time - start_time)
                await websocket.send(json.dumps(['main', str(datetime.timedelta(seconds = diff_main))]))
                
                '''メインタイマー起動'''
                #1秒のカウント
                await asyncio.sleep(1)

                with open(main_timer_trigger_path, encoding="utf-8") as f:
                    data_lines = f.read()

                    # 両タイマー非表示
                    if data_lines == 'False':
                        # jsサイドにfalseシグナルを送って非表示にする
                        await websocket.send(json.dumps(["False"]))
                        
                        trigger_init()
                        
                        #print('TIMER CLOSED')
                        #sys.exit()
                        break
                    
                        

                    
                    
async def main():
    async with websockets.serve(timer, "localhost", 1234):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    trigger_init()
    asyncio.run(main())