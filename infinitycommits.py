import time
import os

class Achievement:
    def __init__(self, name, description, threshold):
        self.name = name
        self.description = description
        self.threshold = threshold

    def __str__(self):
        return f"🏆 {self.name} — {self.description}"


class User:
    def __init__(self, username):
        self.username = username
        self.commits = 0
        self.achievements = []
        self.achievement_definitions = [
            Achievement("🚀 Primeiro Passo!", "Você realizou seu primeiro commit. Que comece a jornada!", 1),
            Achievement("🔥 Commitando sem Parar", "Você alcançou 50 commits. Persistência é tudo!", 50),
            Achievement("🎯 Commit Maniac", "100 commits! Você está dominando o jogo!", 100),
            Achievement("🌌 Além do Infinito", "200 commits? Você é uma estrela no GitHub!", 200)
        ]

    def make_commit(self):
        self.commits += 1
        print(f"🔧 Commit #{self.commits} por {self.username}")
        self.check_achievements()

    def check_achievements(self):
        for ach in self.achievement_definitions:
            if self.commits == ach.threshold and ach.name not in [a.name for a in self.achievements]:
                self.unlock_achievement(ach)

    def unlock_achievement(self, achievement):
        self.achievements.append(achievement)
        print(f"\n✨ NOVA CONQUISTA DESBLOQUEADA!")
        print(f"{achievement}\n")
        time.sleep(0.5)

    def status(self):
        print("\n" + "═" * 40)
        print(f"📊 STATUS DE {self.username.upper()}")
        print("═" * 40)
        print(f"📦 Commits Realizados: {self.commits}")
        print("🎖️ Conquistas:")
        if self.achievements:
            for ach in self.achievements:
                print(f"   ✔️ {ach.name}")
        else:
            print("   Nenhuma conquista até agora.")
        print("═" * 40 + "\n")


# --------- Simulação ---------

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

user = User("dev_gamer")

# Simula 100 commits com leve delay
for _ in range(100):
    user.make_commit()
    time.sleep(0.01)

user.status()
