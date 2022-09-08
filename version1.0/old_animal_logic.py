"""        

        for number in scores:
            if number > first:
                third = second
                second = first
                first = number
            if number > second and number < first:
                third = second
                second = number
            if number > third and number < second:
                third = number

        i = 0
        draw1 = 0
        draw2 = 0
        draw3 = 0
        for score in scores:
            if score == first and draw1 == 0 and score > 0:
                first_place = animal_images[i]
                draw1 += 1
            elif score == second and draw2 == 0 and score > 0:
                second_place = animal_images[i]
                draw2 += 1
            elif score == third and draw3 == 0 and score > 0:
                third_place = animal_images[i]
                draw3 += 1

            elif score == first and draw1 > 0:
                draw1 += 1
            elif score == second and draw2 > 0:
                draw2 += 1
            elif score == third and draw3 > 0:
                draw3 += 1

            i += 1


        if draw1 == 1:
            first_place = pygame.transform.scale(first_place,(180,180))
            screen.blit(first_place, (50, 300))
        if draw2 == 1:
            second_place = pygame.transform.scale(second_place,(100,100))
            screen.blit(second_place, (350,380))
        if draw3 == 1:
            third_place = pygame.transform.scale(third_place,(70,70))
            screen.blit(third_place, (650,420))

        x = 0
        index = 0
        if draw1 > 1:
            for score in scores:
                if score == first:
                    animal_images[x] = pygame.transform.scale(animal_images[x],(130,130))
                    screen.blit(animal_images[x], (30 + index*130,350))
                    index += 1
                x += 1

        x = 0
        index = 0
        if draw2 > 1:
            for score in scores:
                if score == second:
                    animal_images[x] = pygame.transform.scale(animal_images[x],(100,100))
                    screen.blit(animal_images[x], (300 + index*100,380))
                    index += 1
                x += 1

        x = 0
        index = 0
        if draw3 > 1:
            for score in scores:
                if score == third:
                    animal_images[x] = pygame.transform.scale(animal_images[x],(70,70))
                    screen.blit(animal_images[x], (600 + index*70,420))
                    index += 1
                x += 1

"""