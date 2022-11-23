**Python** для скриптов в которых используется наш код на питоне или какие-то пакеты (ros, pyuavcan, etc.)

**ZX** - в первую очередь полезен для скриптов где нужны переменные, if-ы, циклы, но хорош и для для всего остального - небольшие настроечные скрипты, повторяющиесы наборы команд и т.д

```bash
curl -fsSL https://deb.nodesource.com/setup_19.x | sudo -E bash - && sudo apt-get install -y nodejs
sudo npm i -g zx
```

---

**Bash + gum** - приколюха, если хочется то можно использовать для скриптов с вводом от пользователя, запросами подтверждений и т.д., для этого есть красивые обертки. Но выбивается из общей концепции, описанной выше.

```bash
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://repo.charm.sh/apt/gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/charm.gpg
echo "deb [signed-by=/etc/apt/keyrings/charm.gpg] https://repo.charm.sh/apt/ * *" | sudo tee /etc/apt/sources.list.d/charm.list
sudo apt update && sudo apt install gum
```
