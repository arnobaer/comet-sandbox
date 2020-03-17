import comet

def main():
    app = comet.Application(title="Sandbox", version="1.0")
    app.layout = comet.Label(text="Sandbox")
    app.run()

if __name__ == '__main__':
    main()
