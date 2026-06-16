## Changelog : zacharie (30 derniers jours, au 15 juin 2026)

### Résumé
Ce mois-ci, l'équipe a continué d'améliorer l'application Zacharie avec un focus sur l'expérience utilisateur, notamment pour les chasseurs et les administrateurs. Des corrections de bugs et des améliorations de la navigation ont été apportées, ainsi que des fonctionnalités liées à la gestion des carcasses, des FEI et de la traçabilité. Des travaux préparatoires pour la gestion de la trichine ont également été initiés.

### Évolutions fonctionnelles
- Amélioration de la navigation : redirection automatique vers le bon tableau de bord après connexion, évitant les erreurs 404 [#453](https://github.com/betagouv/zacharie/issues/453).
- Affichage amélioré des informations : affichage du dernier intermédiaire avant l'ETG sur la FEI [#433](https://github.com/betagouv/zacharie/issues/433) et de l'entité premier détenteur au lieu de la personne [#442](https://github.com/betagouv/zacharie/issues/442).
- Gestion des carcasses :
    - Possibilité de regrouper les carcasses par destinataire (vue chasseur) [#409](https://github.com/betagouv/zacharie/issues/409).
    - Affichage des sous-totaux de carcasses par espèce [#424](https://github.com/betagouv/zacharie/issues/424).
    - Gestion du statut "clôturée" d'une FEI via ses carcasses [#414](https://github.com/betagouv/zacharie/issues/414).
    - Possibilité de modifier le numéro de bracelet ou d'ajouter une carcasse à un examen initial [#383](https://github.com/betagouv/zacharie/issues/383).
- Gestion des utilisateurs :
    - Ajout d'un bouton pour supprimer un utilisateur en tant qu'administrateur [#429](https://github.com/betagouv/zacharie/issues/429).
    - Correction d'un bug empêchant la suppression d'un utilisateur lors de la suppression de sa relation à un ETG [#450](https://github.com/betagouv/zacharie/issues/450).
    - Un utilisateur ne peut plus changer son rôle [#416](https://github.com/betagouv/zacharie/issues/416).
- Filtres : ajout d'un filtre "Saison" sur les pages fiches [#427](https://github.com/betagouv/zacharie/issues/427).
- Amélioration de l'onboarding : correction de l'obligation de choisir une formation lors de l'examen initial [#422](https://github.com/betagouv/zacharie/issues/422).
- Page utilisateurs : ajout d'une page listant les utilisateurs ayant interagi avec l'ETG [#415](https://github.com/betagouv/zacharie/issues/415).
- Ajout d'une page 404 personnalisée [#394](https://github.com/betagouv/zacharie/issues/394).

### Évolutions techniques
- Refonte de la gestion des utilisateurs partenaires : simplification du chargement des utilisateurs et protection des routes [#413](https://github.com/betagouv/zacharie/issues/413), [#410](https://github.com/betagouv/zacharie/issues/410).
- Préparation de la gestion de la trichine : ajout du modèle de données et début du développement backend [#434](https://github.com/betagouv/zacharie/issues/434).
- Amélioration de la gestion du cache lors de la déconnexion [#402](https://github.com/betagouv/zacharie/issues/402).
- Refactoring :
    - Renommage de `FeiIntermediaire` en `CarcassesIntermediaire` [#451](https://github.com/betagouv/zacharie/issues/451).
    - Nettoyage du code et suppression de code mort lié à l'ancien tableau de bord [#391](https://github.com/betagouv/zacharie/issues/391).
    - Simplification de la logique de vérification de la connectivité réseau [#449](https://github.com/betagouv/zacharie/issues/449).
- Ajout de tests pour la transmission des carcasses depuis l'examinateur initial [#400](https://github.com/betagouv/zacharie/issues/400).
- Ajout de prettier dans le workflow CI/CD [#393](https://github.com/betagouv/zacharie/issues/393).
- Amélioration des appels et de la gestion des filtres [#390](https://github.com/betagouv/zacharie/issues/390).

### Autres changements
- Mise à jour de la documentation pour les emails [#426](https://github.com/betagouv/zacharie/issues/426).
- Mise à jour du fichier `claude.md` [#426](https://github.com/betagouv/zacharie/issues/426).
- Ajout de scripts de démo pour simuler l'activité d'un ETG [#388](https://github.com/betagouv/zacharie/issues/388).
- Amélioration du logo pour une meilleure lisibilité [#431](https://github.com/betagouv/zacharie/issues/431).
- Correction de problèmes de responsive design sur les formulaires d'adresse [#403](https://github.com/betagouv/zacharie/issues/403).
- Amélioration du style du tableau de bord chasseur [#401](https://github.com/betagouv/zacharie/issues/401).
- Ajout d'un tracker pour les erreurs 404 [#418](https://github.com/betagouv/zacharie/issues/418).
- Correction de faux positifs dans les alertes Sentry [#417](https://github.com/betagouv/zacharie/issues/417).
- Mise à jour des scopes des départements [#412](https://github.com/betagouv/zacharie/issues/412) et [#411](https://github.com/betagouv/zacharie/issues/411).
- Ajout d'un bandeau pour le Gamefair [#408](https://github.com/betagouv/zacharie/issues/408).
