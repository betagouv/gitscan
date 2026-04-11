# Synthèse d'activité : MTES-MCT (derniers 7 jours)

## Résumé de l'activité
L'activité récente de l'organisation MTES-MCT est marquée par une forte concentration sur l'amélioration et l'enrichissement des fonctionnalités de ses nombreuses applications. Plusieurs projets ont bénéficié de mises à jour significatives, notamment en termes d'interface utilisateur (amélioration de l'expérience utilisateur, refonte de tableaux de bord, ajout de fonctionnalités de recherche et de filtrage), de gestion des données (ajout de nouvelles données, corrections de bugs, amélioration de la validation) et de sécurité (corrections de vulnérabilités, renforcement de l'authentification). Des efforts importants ont également été déployés pour moderniser les infrastructures techniques et améliorer la maintenance des applications. Les projets *Lucca*, *Dossier Facile*, *Monitorfish*, *Potentiel* et *Trackdéchets* sont particulièrement actifs, avec des évolutions notables pour les utilisateurs finaux.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :
- **mobilic-api** : Restriction des fournisseurs d'identité (IdP) autorisés pour les contrôleurs.
- **qualicharge** : Mise à jour des dépendances pour corriger des vulnérabilités.
- **zero-logement-vacant** : Ajout d'en-têtes de sécurité et correction de vulnérabilités.
- **td-mass-validator**: Amélioration de la validation des données pour éviter les erreurs d'import.

## Autres changements notables
Plusieurs projets ont connu des évolutions techniques majeures :
- **Docurba** : Refonte de l'architecture Django, migration vers Django 6.0, utilisation de Rclone pour la synchronisation des fichiers.
- **apilos** : Mise à jour de la configuration du pipeline CI/CD avec l'ajout de `setuptools`.
- **carbure** : Refactorisation de la gestion des certificats d'électricité.
- **dialog-integrations** : Refactorisation du code, utilisation de `ruff` pour le linting et le formatage.
- **prelevements-deau-api** : Modification de la stratégie d'authentification.
- **sparte** : Intégration du carroyage de la consommation d'espaces.
- **verseau2** : Migration vers la couche d'abstraction MASA pour les appels API et refactorisation de l'authentification.
- **zero-logement-vacant**: Refactorisation frontend avec l'utilisation de composants MUI et migration vers Web Streams.

## Dépôts les plus actifs
- **Docurba** : Amélioration de l'administration de l'application, corrections de bugs et optimisations de performance.
- **Dossier-Facile-Frontend** : Amélioration de l'accessibilité, correction de bugs et amélioration de l'expérience utilisateur.
- **Lucca** : Ajout de la gestion des adhérents et amélioration de l'importation des données.
- **Monitorfish** : Ajout de la gestion des signalements INN et amélioration de l'affichage des données sur la carte.
- **Potentiel** : Ajout de la possibilité de sélectionner les parcelles sur un plan et amélioration des filtres.
- **Trackdéchets** : Ajout de filtres avancés sur le tableau de bord et amélioration du support des fichiers d'import Excel.
- **zero-logement-vacant**: Ajout de la gestion des documents liés aux logements et refonte de l'interface de création de campagnes.
