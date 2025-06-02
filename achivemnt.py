import time

class User:
    def __init__(self, username):
        self.username = username
        self.commits = 0
        self.achievements = []

    def make_commit(self):
        self.commits += 1
        print(f"🔧 {self.username} fez um commit! Total: {self.commits}")
        self.check_achievements()

    def check_achievements(self):
        if self.commits >= 100 and "Commit Maniac" not in self.achievements:
            self.unlock_achievement("Commit Maniac", "🎯 Fez 100 commits!")

    def unlock_achievement(self, name, description):
        self.achievements.append(name)
        print(f"\n🏆 Conquista desbloqueada: {name}")
        print(f"   {description}\n")

    def status(self):
        print(f"\n👤 Usuário: {self.username}")
        print(f"💾 Commits: {self.commits}")
        print("🎖️ Conquistas:")
        for ach in self.achievements:
            print(f"   - {ach}")
        print()

# --------- Exemplo de uso ---------

user = User("dev_gamer")

# Simula 100 commits
for _ in range(100):
    user.make_commit()
    time.sleep(0.01)  # pequena pausa pra simular tempo

user.status()
