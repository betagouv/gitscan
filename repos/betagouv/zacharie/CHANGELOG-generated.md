## Changelog : zacharie (30 derniers jours, au 11 juin 2026)

### Résumé
Ce mois-ci, l'équipe a continué d'améliorer l'application Zacharie, en se concentrant sur l'expérience utilisateur, notamment pour les chasseurs et les administrateurs. Des améliorations ont été apportées à la gestion des carcasses, des fiches, et des utilisateurs, avec un accent particulier sur la simplification des flux de travail et la correction de bugs. Des travaux de refactoring et de nettoyage du code ont également été réalisés pour améliorer la maintenabilité et la performance de l'application.

### Évolutions fonctionnelles
- **Gestion des carcasses :**
    - Affichage des sous-totaux de carcasses par espèce. [#424](https://github.com/betagouv/zacharie/issues/424)
    - Possibilité de modifier le numéro de bracelet ou d'ajouter une carcasse à un examen initial. [#383](https://github.com/betagouv/zacharie/issues/383)
    - Regroupement des carcasses par destinataire dans la vue chasseur. [#409](https://github.com/betagouv/zacharie/issues/409)
    - Page dédiée à la visualisation détaillée des carcasses. [#353](https://github.com/betagouv/zacharie/issues/353)
- **Gestion des fiches :**
    - Ajout d'un filtre "Saison" (1er juin - 31 mai) sur les pages fiches. [#427](https://github.com/betagouv/zacharie/issues/427)
    - Affichage du destinataire choisi par le premier détenteur. [#423](https://github.com/betagouv/zacharie/issues/423)
- **Gestion des utilisateurs et des rôles :**
    - Ajout d'un bouton pour supprimer un utilisateur depuis l'interface d'administration. [#429](https://github.com/betagouv/zacharie/issues/429)
    - Amélioration de l'interface utilisateur pour la gestion des rôles administrateur. [#430](https://github.com/betagouv/zacharie/issues/430)
    - Un utilisateur ne peut plus changer son propre rôle. [#416](https://github.com/betagouv/zacharie/issues/416)
    - Gestion du statut "clôturée" d'une FEI via ses carcasses. [#414](https://github.com/betagouv/zacharie/issues/414)
    - Page listant les utilisateurs ayant interagi avec l'ETG. [#415](https://github.com/betagouv/zacharie/issues/415)
- **Onboarding et examen initial :**
    - Correction pour rendre le choix de la formation obligatoire lors de l'examen initial. [#422](https://github.com/betagouv/zacharie/issues/422)
    - Amélioration de l'UI pour la création d'associations de chasse lors de l'onboarding et du profil utilisateur. [#380](https://github.com/betagouv/zacharie/issues/380)
- **Divers :**
    - Correction de l'affichage de l'entité premier détenteur au lieu de la personne. [#442](https://github.com/betagouv/zacharie/issues/442)
    - Correction pour ne pas renvoyer les informations d'un membre d'une entité en continu. [#443](https://github.com/betagouv/zacharie/issues/443)
    - Correction du quiz Gamefair. [#437](https://github.com/betagouv/zacharie/issues/437)
    - Ajout d'un bandeau pour le Gamefair.
    - Ajout d'un redirect pour la page 404.
    - Amélioration du wording pour les carcasses et les lots. [#398](https://github.com/betagouv/zacharie/issues/398)

### Évolutions techniques
- **Refactoring et nettoyage du code :**
    - Suppression de code legacy (tipimail, vieux liens backend).
    - Simplification des contrôleurs utilisateurs et des fonctions de synchronisation.
    - Division des contrôleurs d'administration.
    - Optimisation des appels et gestion des filtres.
    - Ajout de Prettier dans le workflow CI/CD. [#393](https://github.com/betagouv/zacharie/issues/393)
- **Infrastructure et tests :**
    - Ajout de specs pour le modèle de données trichine. [#389](https://github.com/betagouv/zacharie/issues/389)
    - Tests de non-régression pour préparer le renversement du GET FEI vers GET carcasses. [#384](https://github.com/betagouv/zacharie/issues/384)
    - Amélioration du cache et de la déconnexion. [#402](https://github.com/betagouv/zacharie/issues/402)
    - Ajout d'un tracker sur les pages 404.
- **Backend :**
    - Début du développement du modèle de données et du backend pour la trichinose. [#434](https://github.com/betagouv/zacharie/issues/434)
    - Changement de la méthode de chargement des fiches pour utiliser les carcasses au lieu des fiches. [#392](https://github.com/betagouv/zacharie/issues/392)

### Autres changements
- Mise à jour de la documentation pour les emails.
- Mise à jour du fichier claude.md.
- Activation du cron de relance de complétion de profil.
- Amélioration du layout de la sidebar d'administration. [#440](https://github.com/betagouv/zacharie/issues/440)
- Gestion du scroll to top pour le quiz.
- Changement de logo pour une meilleure lisibilité. [#431](https://github.com/betagouv/zacharie/issues/431)
- Correction de bugs mineurs liés à l'onboarding et aux mailings. [#428](https://github.com/betagouv/zacharie/issues/428)
- Correction de problèmes d'affichage sur les pages de détails d'administration.
- Correction de l'affichage responsive des formulaires d'adresse. [#403](https://github.com/betagouv/zacharie/issues/403)
- Amélioration du style du dashboard chasseur. [#401](https://github.com/betagouv/zacharie/issues/401)
- Correction de faux positifs dans les alertes Sentry. [#417](https://github.com/betagouv/zacharie/issues/417)
- Mise à jour des scopes des départements utilisateurs. [#412](https://github.com/betagouv/zacharie/issues/412), [#411](https://github.com/betagouv/zacharie/issues/411)
