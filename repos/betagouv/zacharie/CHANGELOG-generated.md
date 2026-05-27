## Changelog : zacharie (30 derniers jours, au 26 mai 2026)

### Résumé
Ce mois-ci, l'application Zacharie a bénéficié d'améliorations significatives pour les chasseurs et les examinateurs, notamment dans la gestion des carcasses, l'interface utilisateur et la traçabilité. Des corrections de bugs et des optimisations ont également été apportées pour améliorer la stabilité et la performance de l'application. L'application a également été préparée pour une utilisation hors ligne via Expo.

### Évolutions fonctionnelles
- **Gestion des carcasses :**
    - Regroupement des carcasses par destinataire pour les chasseurs. [#409](https://github.com/betagouv/zacharie/issues/409)
    - Possibilité de modifier le numéro de bracelet ou d'ajouter une carcasse à un examen initial. [#383](https://github.com/betagouv/zacharie/issues/383)
    - Page dédiée à la visualisation détaillée des carcasses. [#353](https://github.com/betagouv/zacharie/issues/353)
    - Affichage des commentaires des intermédiaires dans la modale de la carcasse. [#358](https://github.com/betagouv/zacharie/issues/358)
    - Amélioration de l'interface utilisateur pour la gestion des carcasses. [#373](https://github.com/betagouv/zacharie/issues/373)
- **Interface utilisateur :**
    - Amélioration du style du tableau de bord chasseur. [#401](https://github.com/betagouv/zacharie/issues/401)
    - Adaptation du formulaire d'adresse pour une meilleure réactivité. [#403](https://github.com/betagouv/zacharie/issues/403)
    - Ajout d'une page 404 personnalisée. [#394](https://github.com/betagouv/zacharie/issues/394)
    - Amélioration de l'UI/UX pour les carcasses. [#373](https://github.com/betagouv/zacharie/issues/373)
    - Uniformisation de l'interface pour la création d'associations de chasse. [#380](https://github.com/betagouv/zacharie/issues/380)
- **Autres améliorations :**
    - Ajout d'un quiz pour le prélèvement et l'assiette. [#361](https://github.com/betagouv/zacharie/issues/361)
    - Ajout d'une liste de lésions. [#331](https://github.com/betagouv/zacharie/issues/331)
    - Possibilité de filtrer les collecteurs. [#357](https://github.com/betagouv/zacharie/issues/357)
    - Ajout de scripts de démo pour simuler l'activité ETG. [#388](https://github.com/betagouv/zacharie/issues/388)

### Évolutions techniques
- **Refactoring et nettoyage du code :**
    - Suppression du code mort lié à l'ancien tableau de bord partagé. [#391](https://github.com/betagouv/zacharie/issues/391)
    - Simplification du contrôleur utilisateur. [#364](https://github.com/betagouv/zacharie/issues/364)
    - Nettoyage des contrôleurs et des fonctions de synchronisation. [#371](https://github.com/betagouv/zacharie/issues/371)
    - Suppression de vieux liens du backend. [#372](https://github.com/betagouv/zacharie/issues/372)
    - Suppression de code legacy. [#368](https://github.com/betagouv/zacharie/issues/368)
- **Tests :**
    - Ajout de tests de non-régression. [#384](https://github.com/betagouv/zacharie/issues/384)
    - Ajout de tests unitaires pour la transmission des carcasses. [#400](https://github.com/betagouv/zacharie/issues/400)
    - Ajout de nouveaux tests E2E. [#340](https://github.com/betagouv/zacharie/issues/340)
    - Correction de tests flaky. [#352](https://github.com/betagouv/zacharie/issues/352)
- **Infrastructure et CI/CD :**
    - Ajout de Prettier dans le workflow CI/CD. [#393](https://github.com/betagouv/zacharie/issues/393)
- **Autres :**
    - Changement du chargement de Zacharie par les carcasses au lieu des fiches pour optimiser les performances. [#392](https://github.com/betagouv/zacharie/issues/392)
    - Préparation pour l'utilisation hors ligne avec Expo. [#327](https://github.com/betagouv/zacharie/issues/327)

### Autres changements
- Correction du nettoyage du cache lors de la déconnexion. [#402](https://github.com/betagouv/zacharie/issues/402)
- Correction de l'orthographe de "carcasses" et "lots". [#398](https://github.com/betagouv/zacharie/issues/398)
- Correction du label du bouton "date du jour". [#396](https://github.com/betagouv/zacharie/issues/396)
- Ajustement de la timeline de transmission. [#397](https://github.com/betagouv/zacharie/issues/397)
- Correction du reset du store à la déconnexion. [#385](https://github.com/betagouv/zacharie/issues/385)
- Correction du timeout pour le nettoyage du cache. [#379](https://github.com/betagouv/zacharie/issues/379)
- Correction pour permettre à un chasseur de voir les destinataires des fiches de son association. [#378](https://github.com/betagouv/zacharie/issues/378)
- Correction pour masquer le bouton de création de fiche pour un simple chasseur. [#375](https://github.com/betagouv/zacharie/issues/375)
- Correction pour l'invitation des chasseurs. [#377](https://github.com/betagouv/zacharie/issues/377)
- Correction du toggle admin. [#376](https://github.com/betagouv/zacharie/issues/376)
- Correction du calcul du BPH. [#326](https://github.com/betagouv/zacharie/issues/326)
- Correction de l'activation/désactivation du SVI. [#335](https://github.com/betagouv/zacharie/issues/335)
- Correction du chemin initial. [#338](https://github.com/betagouv/zacharie/issues/338)
- Correction de l'URL initiale Expo. [#337](https://github.com/betagouv/zacharie/issues/337)
- Mise à jour des dépendances (fast-uri, ip-address, express-rate-limit, postcss).
