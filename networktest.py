import speedtest
import sys
import time

def format_speed(bps: float) -> float:
    """bps → Mbps に変換"""
    return round(bps / 1_000_000, 2)

def main():
    print("ネットワーク速度テストを開始します…")
    print("サーバーを検索中…")
    
    try:
        s = speedtest.Speedtest()
        s.get_servers()
        s.get_best_server()

        print("ダウンロード速度を計測中…")
        download_bps = s.download()

        print("アップロード速度を計測中…")
        upload_bps = s.upload()

        ping_ms = s.results.ping

    except Exception as e:
        print("エラーが発生しました:", str(e))
        sys.exit(1)

    print("\n===== 速度テスト結果 =====")
    print(f"Ping: {round(ping_ms, 2)} ms")
    print(f"Download: {format_speed(download_bps)} Mbps")
    print(f"Upload:   {format_speed(upload_bps)} Mbps")
    print("==========================")

if __name__ == "__main__":
    main()
