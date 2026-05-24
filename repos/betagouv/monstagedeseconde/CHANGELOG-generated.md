## Changelog : monstagedeseconde (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la robustesse de la plateforme, la correction de bugs et l'ajout de nouvelles fonctionnalités pour faciliter la gestion des stages et des candidatures. Des améliorations ont été apportées à la gestion des signatures, à la validation des candidatures et à la gestion des erreurs, ainsi que des optimisations de performance et des mises à jour de sécurité.

### Évolutions fonctionnelles
- Possibilité pour un élève d'avoir deux stages validés simultanément. [#839](https://github.com/betagouv/monstagedeseconde/issues/839)
- Amélioration de la gestion des conventions, notamment pour l'édition du chef d'établissement. [#808](https://github.com/betagouv/monstagedeseconde/issues/808) et [#830](https://github.com/betagouv/monstagedeseconde/issues/830)
- Suppression de l'envoi d'emails de confirmation de candidature. [#838](https://github.com/betagouv/monstagedeseconde/issues/838)
- Ajout de la prise en charge du préfixe téléphonique de la Guadeloupe. [#859](https://github.com/betagouv/monstagedeseconde/issues/859)
- Amélioration de l'affichage des offres pour les employeurs.
- Correction d'un bug empêchant la validation de candidatures sur certaines semaines.
- Ajout d'un chatbot Crisp pour l'assistance aux utilisateurs. [#879](https://github.com/betagouv/monstagedeseconde/issues/879)

### Évolutions techniques
- Mise à jour de la version de Ruby à 3.4.9. [#884](https://github.com/betagouv/monstagedeseconde/issues/884)
- Refactoring du modèle `InternshipApplication` pour améliorer la lisibilité et la maintenabilité. [#888](https://github.com/betagouv/monstagedeseconde/issues/888)
- Amélioration de la gestion des erreurs liées à l'API Sygne avec la création d'une exception dédiée. [#888](https://github.com/betagouv/monstagedeseconde/issues/888)
- Correction de problèmes de tests instables liés à l'archivage de l'année scolaire.
- Mise à jour de plusieurs dépendances (webpack-dev-server, jwt, faraday, nokogiri, etc.).
- Amélioration de la gestion des erreurs Sentry (cache, logs, etc.).
- Optimisation de la reconstruction des données de revue.
- Amélioration de la validation des adresses et de la géolocalisation des entreprises. [#817](https://github.com/betagouv/monstagedeseconde/issues/817)
- Mise en place de mesures de sécurité pour prévenir les attaques XSS.

### Autres changements
- Nettoyage du code et suppression de fichiers inutiles.
- Amélioration de la documentation.
- Correction de typos et de petites erreurs de code.
- Mise à jour des fichiers de configuration.
- Correction de problèmes liés aux tests unitaires et d'intégration.
- Amélioration de la gestion des permissions et des rôles.
- Correction de bugs mineurs dans l'interface utilisateur.
- Ajout de compétences pour l'outil d'IA Claude.
