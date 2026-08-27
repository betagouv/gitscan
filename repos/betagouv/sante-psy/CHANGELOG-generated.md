## Changelog : sante-psy (30 derniers jours, au 26 août 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante avec le déploiement des versions 4 et 4.2 du module de gestion des étudiants. La plateforme a également été renforcée pour garantir une meilleure stabilité face aux services externes (API INE) et offrir une expérience utilisateur plus fluide, tant pour les étudiants que pour les professionnels de santé.

### Évolutions fonctionnelles
- Mise à jour majeure du parcours de gestion des étudiants (versions 4 et 4.2) [#876](https://github.com/betagouv/sante-psy/issues/876), [#877](https://github.com/betagouv/sante-psy/issues/877), [#887](https://github.com/betagouv/sante-psy/issues/887), [#888](https://github.com/betagouv/sante-psy/issues/888).
- Amélioration de l'interface pour les professionnels : ajout de cases à cocher pour identifier visuellement le premier rendez-vous de l'année avec un étudiant [#884](https://github.com/betagouv/sante-psy/issues/884).
- Optimisation de l'expérience de connexion en empêchant les clics multiples sur le bouton de validation [#886](https://github.com/betagouv/sante-psy/issues/886).

### Évolutions techniques
- Renforcement de la fiabilité de l'intégration avec l'API INE (ajout de timeouts, gestion unifiée des erreurs 400/404 et mise en place d'alertes de mitigation) [#874](https://github.com/betagouv/sante-psy/issues/874), [#880](https://github.com/betagouv/sante-psy/issues/880).
- Optimisation de la gestion des données patients et des rendez-vous (meilleure récupération des données et gestion des cas où l'INE est absent ou vide) [#883](https://github.com/betagouv/sante-psy/issues/883).
- Optimisation de la base de données : mise à jour des enregistrements patients existants au lieu de leur recréation lors d'une suppression [#878](https://github.com/betagouv/sante-psy/issues/878).
- Refactorisation du code pour améliorer la structure et la maintenance (organisation des données étudiants et nettoyage de l'API).

### Autres changements
- Création d'un script utilitaire pour le téléchargement groupé de certificats pour une liste d'étudiants [#882](https://github.com/betagouv/sante-psy/issues/882).
- Maintenance du code via des corrections de linting.
