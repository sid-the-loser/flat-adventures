# Generate obfuscated code


# Generate a spec file for PyInstaller
pyi-makespec --onefile --noconsole --icon="./assets/icon.ico" \
    --add-data "assets:assets" ./dist/main.py

echo "please move the assets to .dist folder"