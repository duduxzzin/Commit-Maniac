import time

class User:
    def __init__(self, username):
        self.username = username
        self.commits = 0
        self.achievements = []

    def make_commit(self):
        self.commits += 1
        print(f"🔧 {self.username} fez um commit! (Total: {self.commits})")
        self.check_achievements()

    def check_achievements(self):
        milestones = [
            (1, "🚀 Primeiro Passo!", "Você realizou seu primeiro commit. Que comece a jornada!"),
            (50, "🔥 Commitando sem Parar", "Você alcançou 50 commits. Persistência é tudo!"),
            (100, "🎯 Commit Maniac", "100 commits! Você está dominando o jogo!")
        ]
        for count, name, description in milestones:
            if self.commits == count and name not in self.achievements:
                self.unlock_achievement(name, description)

    def unlock_achievement(self, name, description):
        self.achievements.append(name)
        print(f"\n🏆 Conquista Desbloqueada: {name}")
        print(f"   📝 {description}\n")

    def status(self):
        print("\n📊 Status Atual do Usuário")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"👤 Usuário: {self.username}")
        print(f"💾 Total de Commits: {self.commits}")
        print("🎖️ Conquistas Desbloqueadas:")
        if self.achievements:
            for ach in self.achievements:
                print(f"   ✔️ {ach}")
        else:
            print("   (Nenhuma conquista ainda)")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

# --------- Simulação ---------

user = User("dev_gamer")

for _ in range(100):
    user.make_commit()
    time.sleep(0.01)

user.status()
