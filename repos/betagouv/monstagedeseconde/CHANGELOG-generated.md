## Changelog : monstagedeseconde (30 derniers jours, au 29 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur et la correction de bugs, notamment concernant la gestion des candidatures, des offres et des établissements. Des améliorations de sécurité et des mises à jour techniques ont également été apportées pour assurer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- Possibilité pour un élève d'avoir deux stages valides simultanément [#836](https://github.com/betagouv/monstagedeseconde/issues/836).
- Correction du lien vers la FAQ [#841](https://github.com/betagouv/monstagedeseconde/issues/841).
- Amélioration du message de validation de candidature pour les élèves de lycée [#819](https://github.com/betagouv/monstagedeseconde/issues/819).
- Ajout de la possibilité de resoumettre une candidature [#898](https://github.com/betagouv/monstagedeseconde/issues/898).
- Affichage de l'URL des ressources pour les offres de stage [#872](https://github.com/betagouv/monstagedeseconde/issues/872).
- Ajout du préfixe téléphonique de la Guadeloupe pour une meilleure gestion des numéros de téléphone [#859](https://github.com/betagouv/monstagedeseconde/issues/859).
- Correction d'un bug empêchant une seule candidature par étudiant et par offre [#886](https://github.com/betagouv/monstagedeseconde/issues/886).
- Amélioration de la gestion des offres d'entreprise pour les opérateurs [#867](https://github.com/betagouv/monstagedeseconde/issues/867).
- Ajout de statistiques pour les maisons d'accueil [#848](https://github.com/betagouv/monstagedeseconde/issues/848).
- Correction de l'affichage des offres dans le tableau de bord pour les employeurs [#892](https://github.com/betagouv/monstagedeseconde/issues/892).

### Évolutions techniques
- Mise à jour de plusieurs dépendances (faraday, devise, nokogiri, webpack-dev-server, ip-address, babel/plugin-transform-modules-systemjs, view_component) pour bénéficier des dernières corrections et améliorations de sécurité.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Amélioration de la gestion des erreurs Sygne avec la création d'une classe d'erreur spécifique et la mise en place de mécanismes de retry [#888](https://github.com/betagouv/monstagedeseconde/issues/888).
- Mise à jour de la version de Ruby à 3.4.9 [#884](https://github.com/betagouv/monstagedeseconde/issues/884).
- Amélioration de la gestion des tests et correction de plusieurs tests défaillants.
- Correction de problèmes de sécurité XSS [#860](https://github.com/betagouv/monstagedeseconde/issues/860), [#869](https://github.com/betagouv/monstagedeseconde/issues/869).
- Amélioration de la gestion des autorisations avec cancancan.
- Correction de problèmes liés à la configuration de l'environnement.

### Autres changements
- Ajout d'un chatbot Crisp pour améliorer le support utilisateur [#879](https://github.com/betagouv/monstagedeseconde/issues/879).
- Amélioration de la documentation et des commentaires dans le code.
- Nettoyage du code et suppression de fichiers inutiles.
- Mise à jour de la configuration de l'environnement de développement.
- Correction de typos et amélioration de la qualité du code.
- Ajout de skills pour Claude (outil d'IA) pour améliorer l'assistance au développement.
- Correction de la gestion des erreurs dans les jobs asynchrones.
- Correction de problèmes liés au chargement des modèles.
- Amélioration de la gestion des adresses et de la géolocalisation.
- Correction de bugs mineurs et amélioration de la stabilité de la plateforme.
