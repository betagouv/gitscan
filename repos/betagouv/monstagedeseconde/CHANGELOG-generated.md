## Changelog : monstagedeseconde (30 derniers jours, au 2026-06-02)

### Résumé
Ce mois-ci, les évolutions de MonStageDeSeconde se sont concentrées sur l'amélioration de l'expérience utilisateur, notamment en corrigeant des bugs liés aux candidatures, à la gestion des stages et à l'affichage d'informations. Des améliorations ont également été apportées à la sécurité et à la robustesse de la plateforme, ainsi qu'à l'administration et à la gestion des données.

### Évolutions fonctionnelles
- Correction d'un bug empêchant les élèves de postuler plusieurs fois à la même offre de stage [#876](https://github.com/betagouv/monstagedeseconde/issues/876).
- Amélioration de la gestion des niveaux scolaires des élèves [#883](https://github.com/betagouv/monstagedeseconde/issues/883).
- Correction d'un problème d'affichage des URL des ressources [#872](https://github.com/betagouv/monstagedeseconde/issues/872).
- Correction d'un bug empêchant le renvoi des demandes de candidature [#898](https://github.com/betagouv/monstagedeseconde/issues/898).
- Ajout de la possibilité d'importer des élèves depuis l'interface d'administration [#880](https://github.com/betagouv/monstagedeseconde/issues/880).
- Correction d'un problème de doublons de candidatures [#1234](https://github.com/betagouv/monstagedeseconde/issues/1234).
- Correction d'un bug lié au nombre de places restantes dans les stages [#9534f8f6].
- Amélioration de la gestion des conventions de stage, notamment pour la signature [#882](https://github.com/betagouv/monstagedeseconde/issues/882) et [#893](https://github.com/betagouv/monstagedeseconde/issues/893).
- Ajout de la possibilité pour un élève d'avoir deux stages valides simultanément [#836](https://github.com/betagouv/monstagedeseconde/issues/836).
- Correction d'un problème de validation de candidature pour les élèves de lycée [#819](https://github.com/betagouv/monstagedeseconde/issues/819).
- Amélioration de l'affichage du formulaire d'entreprise publique [#831](https://github.com/betagouv/monstagedeseconde/issues/831).
- Ajout de statistiques pour les maisons d'accueil [#848](https://github.com/betagouv/monstagedeseconde/issues/848).
- Correction d'un lien cassé dans la FAQ [#841](https://github.com/betagouv/monstagedeseconde/issues/841).

### Évolutions techniques
- Mise à jour de la version de Ruby à 3.4.9 [#884](https://github.com/betagouv/monstagedeseconde/issues/884).
- Amélioration de la gestion des erreurs Sygne, avec la création d'une classe d'erreur dédiée et la mise en place de mécanismes de retry [#888](https://github.com/betagouv/monstagedeseconde/issues/888).
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Amélioration de la gestion des autorisations avec cancancan.
- Mise à jour des dépendances npm et bundler (qs, webpack-dev-server, devise, view_component, ip-address, etc.).
- Amélioration de la gestion des tests et correction de plusieurs tests défaillants.
- Correction de problèmes de sécurité XSS [#860](https://github.com/betagouv/monstagedeseconde/issues/860] et [#869](https://github.com/betagouv/monstagedeseconde/issues/869).
- Ajout d'un chatbot Crisp pour l'assistance utilisateur [#879](https://github.com/betagouv/monstagedeseconde/issues/879).
- Amélioration de la validation d'adresse et de la géolocalisation [#817](https://github.com/betagouv/monstagedeseconde/issues/817).

### Autres changements
- Ajout de compétences pour l'IA Claude afin d'améliorer l'assistance au développement.
- Suppression de fichiers inutiles.
- Mise à jour de la documentation.
- Correction de typos et amélioration de la qualité du code.
- Suppression d'un add-on tiers inutile [#120b5b14].
- Correction de problèmes de configuration et de build.
- Ajout du préfixe téléphonique de la Guadeloupe [#859](https://github.com/betagouv/monstagedeseconde/issues/859).
