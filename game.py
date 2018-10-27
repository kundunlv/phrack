import random
def djigurda_vs_zombies(z):
    # z - zombies count , in this func djigurda fight against zombies
    # TODO: implement djigurdin ( more attack, if low hp)
    djigurda_hp = 100
    djigurda_attack = 3,7
    zombie_hp = 5, 15
    # TODO: add hit chance
    zombie_attack = 2, 10 
    for x in range(z):
        zombie = random.randint(zombie_hp[0],zombie_hp[1])
        print(
            "!!!New zombie with {} hp, {} zombies left, {} zombies died".format(
                zombie, z - x, x
        ))
        while zombie > 0 or djigurda_hp > 0:
            dj_attack = random.randint(djigurda_attack[0],djigurda_attack[1])
            zombie -= dj_attack
            print("djigurda hits zombie by {}, zombies_hp {}".format(dj_attack,zombie))
            if zombie < 0:
                print("zombie has been destroyed by mighty Djiguuurdaaa")
                break
            z_attack = random.randint(zombie_attack[0],zombie_attack[1])
            djigurda_hp -= z_attack
            print("zombie hits djigurda by {}, djigurdas_hp {}".format(z_attack, djigurda_hp))
            if djigurda_hp < 0:
                print("Djigurda let zombie win")
                return 
djigurda_vs_zombies(10)