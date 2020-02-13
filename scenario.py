import simpy
from agents import victime, attaquant, SI
from configparser import ConfigParser

parser = ConfigParser()
parser.read('dev.ini')


victime1 = victime(name="victime1", os="Windows")
victime2 = victime(name="victime2", os="Windows")
victime3 = victime(name="victime3", os="Windows")
victime4 = victime(name="victime4", os="Windows")
victime5 = victime(name="victime5", os="Windows")


attaquant1 = attaquant(name="attaquant1",
                       os="Kali Linux", TypeOfAttack="Phishing email")
attaquant2 = attaquant(name="attaquant2",
                       os="Kali Linux", TypeOfAttack="Phishing email")


def main():
    victimes = [victime1, victime2, victime3, victime4, victime5]
    env = simpy.Environment()
    env.process(scenario(env, attaquants=[attaquant1], victimes=victimes, speed=1))
    env.process(scenario(env, attaquants=[attaquant2], victimes=victimes, speed=3))
    env.run(until=6)


def scenario(env, attaquants, victimes, speed):

    while True:
        my_SI = SI(attaquants, victimes)
        connexions = my_SI.build_connexions()

        for couple in connexions:
            if connexions[couple] == 1 and couple[1].vulnerable == 1:
                print(f"L\'attaquant {couple[0].name} a initié une attaque sur {couple[1].name} de type {couple[0].TypeOfAttack} à {env.now}.\n")
                yield env.timeout(speed)
                print(f"La victime {couple[1].name} a reçu le mail de phishing envoyé par l'attaquant {couple[0].name} et a clické deçu à {env.now}.\n")
                connexions[couple] = 0


if __name__ == "__main__":
    main()


"""f = open("warning.txt", "w+")
            f.write(victime.name + ", You are Hacked.")
            f.close()
            subprocess.run(["open", "warning.txt"])"""
