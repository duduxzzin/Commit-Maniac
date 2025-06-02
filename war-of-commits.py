import time
import os

class Achievement:
    """
    Representa uma conquista com nome, descrição e número de commits necessário.
    """
    def __init__(self, name: str, description: str, threshold: int):
        self.name = name
        self.description = description
        self.threshold = threshold

    def __str__(self):
        return f"🏆 {self.name} — {self.description}"


class User:
    """
    Representa um usuário que realiza commits e desbloqueia conquistas.
    """
    def __init__(self, username: str):
        self.username = username
        self.commits = 0
        self.achievements = []
        self.achievement_definitions = [
            Achievement("🚀 Primeiro Passo!", "Você realizou seu primeiro commit. Que comece a jornada!", 1),
            Achievement("🔥 Commitando sem Parar", "Você alcançou 50 commits. Persistência é tudo!", 50),
            Achievement("🎯 Commit Maniac", "100 commits! Você está dominando o jogo!", 100),
            Achievement("🌌 Além do Infinito", "200 commits? Você é uma estrela no GitHub!", 200),
        ]

    def make_commit(self):
        """
        Realiza um commit e verifica se alguma conquista foi desbloqueada.
        """
        self.commits += 1
        print(f"\033[94m🔧 Commit #{self.commits} por {self.username}\033[0m")
        self.check_achievements()

    def check_achievements(self):
        """
        Verifica se alguma conquista deve ser desbloqueada com base no número de commits.
        """
        for ach in self.achievement_definitions:
            if self.commits == ach.threshold and ach.name not in [a.name for a in self.achievements]:
                self.unlock_achievement(ach)

    def unlock_achievement(self, achievement: Achievement):
        """
        Adiciona uma conquista à lista do usuário e exibe uma mensagem.
        """
        self.achievements.append(achievement)
        print(f"\n\033[92m✨ NOVA CONQUISTA DESBLOQUEADA!\033[0m")
        print(f"{achievement}\n")
        time.sleep(0.4)

    def status(self):
        """
        Exibe o status atual do usuário, incluindo commits e conquistas.
        """
        print("\n\033[95m" + "═" * 40)
        print(f"📊 STATUS DE {self.username.upper()}")
        print("═" * 40 + "\033[0m")
        print(f"📦 Commits Realizados: \033[93m{self.commits}\033[0m")
        print("🎖️ Conquistas:")
        if self.achievements:
            for ach in self.achievements:
                print(f"   ✔️ \033[96m{ach.name}\033[0m")
        else:
            print("   (Nenhuma conquista ainda)")
        print("\033[95m" + "═" * 40 + "\n\033[0m")


def clear_console():
    """
    Limpa o terminal.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def simulate_commits(user: User, count: int = 100, delay: float = 0.01):
    """
    Simula a realização de commits pelo usuário.
    """
    for _ in range(count):
        user.make_commit()
        time.sleep(delay)


if __name__ == "__main__":
    clear_console()
    user = User("dev_gamer")
    simulate_commits(user, 100)
    user.status()
