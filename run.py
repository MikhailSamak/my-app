try:
    from app import app
except ImportError as e:
    print(f"\u041e\u0448\u0438\u0431\u043a\u0430 \u0438\u043c\u043f\u043e\u0440\u0442\u0430: {e}")
    raise

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)



