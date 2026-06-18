## Changelog : zacharie (30 derniers jours, au 17 juin 2026)

### Résumé
Ce mois-ci, l'équipe a continué d'améliorer l'application Zacharie, en se concentrant sur l'expérience utilisateur, notamment dans l'interface d'administration et pour les chasseurs. Des améliorations ont été apportées à la gestion des carcasses, des fiches, et des examens initiaux. Des corrections de bugs et des optimisations de performance ont également été réalisées.

### Évolutions fonctionnelles
- Possibilité d'exporter de manière modulaire les fiches de traçabilité. [#445](https://github.com/betagouv/zacharie/issues/445)
- Ajout d'un filtre "Saison" (1er juin - 31 mai) sur les pages de gestion des fiches. [#427](https://github.com/betagouv/zacharie/issues/427)
- Amélioration de l'affichage des informations sur les FEI (Fiche d'Examen Initial) : affichage du dernier intermédiaire avant l'ETG. [#433](https://github.com/betagouv/zacharie/issues/433)
- Possibilité de grouper les carcasses par destinataire dans la vue chasseur. [#409](https://github.com/betagouv/zacharie/issues/409)
- Ajout d'un bouton pour supprimer un utilisateur depuis l'interface d'administration. [#429](https://github.com/betagouv/zacharie/issues/429)
- Amélioration de l'affichage des sous-totaux de carcasses par espèce. [#424](https://github.com/betagouv/zacharie/issues/424)
- Possibilité de modifier le numéro de bracelet ou d'ajouter une carcasse à un examen initial. [#383](https://github.com/betagouv/zacharie/issues/383)
- Amélioration de l'onboarding : le choix de la formation est désormais obligatoire lors de l'examen initial. [#422](https://github.com/betagouv/zacharie/issues/422)
- Affichage de l'entité premier détenteur au lieu de la personne. [#442](https://github.com/betagouv/zacharie/issues/442)
- Simplification du calcul du BPH (Bonus Prélèvement Harcèlement) et de ses constantes. [#456](https://github.com/betagouv/zacharie/issues/456)

### Évolutions techniques
- Refonte de la gestion du cache lors de la déconnexion pour une meilleure performance. [#402](https://github.com/betagouv/zacharie/issues/402)
- Modification de la manière dont Zacharie est chargé : désormais via les carcasses plutôt que les fiches, avec une protection accrue des routes. [#392](https://github.com/betagouv/zacharie/issues/392)
- Amélioration de la gestion des scopes de département pour les utilisateurs. [#411](https://github.com/betagouv/zacharie/issues/411)
- Ajout de tests pour la transmission des carcasses depuis l'examinateur initial. [#400](https://github.com/betagouv/zacharie/issues/400)
- Suppression du code legacy lié à l'ancien tableau de bord partagé. [#391](https://github.com/betagouv/zacharie/issues/391)
- Optimisation des appels et de la gestion des filtres pour améliorer la performance. [#390](https://github.com/betagouv/zacharie/issues/390)
- Ajout de Prettier dans le workflow CI/CD pour garantir la cohérence du code. [#393](https://github.com/betagouv/zacharie/issues/393)
- Modification de la logique de transmission des carcasses depuis l'examinateur initial. [#399](https://github.com/betagouv/zacharie/issues/399)

### Autres changements
- Amélioration continue du panel d'administration. [#460](https://github.com/betagouv/zacharie/issues/460)
- Amélioration de l'UI/UX pour la création de fiches et les demandes de modifications. [#444](https://github.com/betagouv/zacharie/issues/444)
- Mise à jour de la documentation pour les emails. [#425](https://github.com/betagouv/zacharie/issues/425)
- Ajout de scripts de démo pour simuler l'activité d'un ETG. [#388](https://github.com/betagouv/zacharie/issues/388)
- Corrections de bugs et améliorations diverses de l'interface utilisateur.
- Renommage de `FeiIntermediaire` en `CarcassesIntermediaire`. [#451](https://github.com/betagouv/zacharie/issues/451)
- Mise à jour du wording de l'application. [#457](https://github.com/betagouv/zacharie/issues/457)
- Ajout d'une page 404 personnalisée. [#394](https://github.com/betagouv/zacharie/issues/394)
- Ajout d'un tracker sur les pages 404.
- Amélioration de l'affichage des villes, les plus récentes apparaissent en premier. [#461](https://github.com/betagouv/zacharie/issues/461)
- Correction de l'affichage du destinataire choisi par le premier détenteur. [#423](https://github.com/betagouv/zacharie/issues/423)
- Correction du problème de redirection vers le bon tableau de bord après la connexion. [#453](https://github.com/betagouv/zacharie/issues/453)
- Correction de la redirection du panel d'administration.
- Correction d'un problème avec les tests E2E. [#459](https://github.com/betagouv/zacharie/issues/459)
- Correction d'un bug empêchant la suppression d'un utilisateur lors de la suppression de sa relation avec un ETG. [#450](https://github.com/betagouv/zacharie/issues/450)
- Correction d'un bug lié à la vérification de la connectivité réseau. [#449](https://github.com/betagouv/zacharie/issues/449)
- Correction d'un problème avec le quiz Gamefair. [#437](https://github.com/betagouv/zacharie/issues/437)
- Correction d'un bug empêchant l'affichage correct des informations des membres d'une entité. [#443](https://github.com/betagouv/zacharie/issues/443)
- Correction d'un problème d'affichage du logo dans l'interface d'administration. [#431](https://github.com/betagouv/zacharie/issues/431)
- Correction d'un problème de mailing concernant l'onboarding. [#428](https://github.com/betagouv/zacharie/issues/428)
- Correction d'un problème avec le bandeau Gamefair.
- Correction d'un problème de reset du state initial.
- Correction d'un bug empêchant un utilisateur de changer son rôle. [#416](https://github.com/betagouv/zacharie/issues/416)
- Correction de faux positifs dans les alertes Sentry. [#417](https://github.com/betagouv/zacharie/issues/417)
- Correction de l'affichage du dernier intermédiaire sur la FEI. [#433](https://github.com/betagouv/zacharie/issues/433)
