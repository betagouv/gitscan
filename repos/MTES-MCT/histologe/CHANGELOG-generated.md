## Changelog : histologe (30 derniers jours, au 02/10/2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur l'amélioration de l'ergonomie de l'interface, notamment via la transition des fenêtres surgissantes vers des panneaux latéraux pour une navigation plus fluide. Le projet a également renforcé la fiabilité des parcours de signalement (validation des adresses, gestion des erreurs) et a introduit des fonctionnalités essentielles de gestion de compte, comme la réinitialisation de mot de passe.

### Évolutions fonctionnelles
- **Interface & Expérience Utilisateur** :
    - Transition progressive des modales vers des panneaux latéraux dans le back-office (lots 2, 3 et 4) [#6254](https://github.com/MTES-MCT/histologe/issues/6254), [#6274](https://github.com/MTES-MCT/histologe/issues/6274), [#6275](https://github.com/MTES-MCT/histologe/issues/6275).
    - Amélioration de la clarté des textes (wording) [#6346](https://github.com/MTES-MCT/histologe/issues/6346) et corrections d'affichage de l'interface [#6350](https://github.com/MTES-MCT/histologe/issues/6350).
- **Gestion des Signalements & Dossiers** :
    - Augmentation de la capacité de recherches sauvegardées dans le back-office [#6369](https://github.com/MTES-MCT/histologe/issues/6369).
    - Ajout d'une vue liste pour l'historique des adresses [#6152](https://github.com/MTES-MCT/histologe/issues/6152).
    - Optimisation de l'affectation des partenaires dans les dossiers [#6295](https://github.com/MTES-MCT/histologe/issues/6295).
    - Possibilité d'exporter des données sans géolocalisation [#6302](https://github.com/MTES-MCT/histologe/issues/6302).
    - Amélioration de la recherche de signalements sans relation d'adresse [#6256](https://github.com/MTES-MCT/histologe/issues/6256).
- **Parcours Utilisateur (Front-office)** :
    - Rendre la validation de l'adresse obligatoire lors du signalement [#6268](https://github.com/MTES-MCT/histologe/issues/6268).
    - Possibilité de fermer les suggestions d'adresse dans les formulaires [#6298](https://github.com/MTES-MCT/histologe/issues/6298).
    - Correction de l'affichage des informations saisies par les déclarants [#6294](https://github.com/MTES-MCT/histologe/issues/6294).
- **Authentification & Sécurité** :
    - Mise en place de la réinitialisation de mot de passe pour les utilisateurs (FO) et via email [#6281](https://github.com/MTES-MCT/histologe/issues/6281), [#6283](https://github.com/MTES-MCT/histologe/issues/6283).
    - Correction du processus de connexion ProConnect [#6332](https://github.com/MTES-MCT/histologe/issues/6332).
- **Interconnexion & Notifications** :
    - Prise en compte des arrêtés modificatifs pour l'interconnexion Esabora (Santé Habitat) [#6317](https://github.com/MTES-MCT/histologe/issues/6317), [#6296](https://github.com/MTES-MCT/histologe/issues/6296).
    - Amélioration du tri dans la liste des notifications [#6409](https://github.com/MTES-MCT/histologe/issues/6409).
    - Renforcement de la confidentialité en masquant les destinataires dans certains emails de notification [#6307](https://github.com/MTES-MCT/histologe/issues/6307).

### Évolutions techniques
- **Architecture & Refactoring** :
    - Réorganisation des repositories de données (Notification, Partner, EmailDeliveryIssue) [#6323](https://github.com/MTES-MCT/histologe/issues/6323).
- **Performance & Stabilité** :
    - Gestion optimisée des timeouts via des variables d'environnement (Axios) [#6412](https://github.com/MTES-MCT/histologe/issues/6412), [#6351](https://github.com/MTES-MCT/histologe/issues/6351).
    - Résolution de problèmes d'engorgement des workers [#6327](https://github.com/MTES-MCT/histologe/issues/6327).
    - Correction de dépassements de dates (date overflow) [#6408](https://github.com/MTES-MCT/histologe/issues/6408).
- **Outils & CI/CD** :
    - Installation du package `rev` pour les déploiements Scalingo [#6373](https://github.com/MTES-MCT/histologe/issues/6373).
    - Création d'une commande pour l'archivage des signalements [#6365](https://github.com/MTES-MCT/histologe/issues/6365).
    - Implémentation d'un outil de détection et de suppression de code mort [#6311](https://github.com/MTES-MCT/histologe/issues/6311).
    - Isolation de Lighthouse dans un package npm dédié [#6299](https://github.com/MTES-MCT/histologe/issues/6299).
- **Tests** :
    - Corrections apportées à la suite de tests [#6314](https://github.com/MTES-MCT/histologe/issues/6314).

### Autres changements
- **Documentation** : Ajout d'un fichier postmortem [#6308](https://github.com/MTES-MCT/histologe/issues/6308).
- **Frontend** : Mise à jour des composants front-end WikiSI [#6316](https://github.com/MTES-MCT/histologe/issues/6316).
