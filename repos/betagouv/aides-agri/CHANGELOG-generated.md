## Changelog : aides-agri (30 derniers jours, au 2026-04-28)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'interface d'administration pour la gestion des aides, notamment avec l'ajout de fonctionnalités de duplication et d'organisation des champs. Des améliorations de la base de code et des dépendances ont également été apportées pour assurer la stabilité et la sécurité de la plateforme. La préparation du parcours utilisateur v2 est également en cours.

### Évolutions fonctionnelles
- **Gestion des aides :** Possibilité de dupliquer une aide existante depuis l'interface d'administration. [#448](https://github.com/betagouv/aides-agri/issues/448)
- **Interface d'administration :** Réorganisation des champs dans le back-office pour une meilleure ergonomie lors de la création et modification des aides. [#446](https://github.com/betagouv/aides-agri/issues/446)
- **Correction d'un bug :** Résolution d'un problème de duplication d'aides dans l'interface d'administration. [#449](https://github.com/betagouv/aides-agri/issues/449)
- **Base juridique des aides :** Consolidation et amélioration de la gestion de la base juridique des aides. [#495](https://github.com/betagouv/aides-agri/issues/495), [#499](https://github.com/betagouv/aides-agri/issues/499)
- **Edition des aides :** Améliorations apportées à l'outil d'édition des aides. [#498](https://github.com/betagouv/aides-agri/issues/498)
- **Slug des aides :** Correction d'un bug lié au slug des aides. [#497](https://github.com/betagouv/aides-agri/issues/497)
- **Parcours agri v2 :** Avancement du développement du nouveau parcours utilisateur. [#418](https://github.com/betagouv/aides-agri/issues/418)

### Évolutions techniques
- **Mise à jour des dépendances :** Plusieurs dépendances ont été mises à jour vers leurs dernières versions stables, notamment Django, Django-DSFR, requests, sentry-sdk, faker, gunicorn, ruff, et d'autres.
- **Optimisation du workflow GitHub :** Amélioration du workflow GitHub pour une meilleure gestion des commits et des pull requests. [#467](https://github.com/betagouv/aides-agri/issues/467)
- **Déploiement facilité :** Simplification du processus de déploiement en cas de changement de schéma de base de données. [#501](https://github.com/betagouv/aides-agri/issues/501)
- **Sécurité :** Mise à jour de la date de validité du fichier `security.txt`. [#505](https://github.com/betagouv/aides-agri/issues/505)
- **Gestion des logos :** Scripts pour la gestion des logos des Directions Départementales des Territoires et de la Mer (DDT(M)). [#493](https://github.com/betagouv/aides-agri/issues/493), [#507](https://github.com/betagouv/aides-agri/issues/507)

### Autres changements
- **Documentation :** Ajout des statistiques d'utilisation pour le mois de mars 2026. [#477](https://github.com/betagouv/aides-agri/issues/477)
- **Configuration :** Correction du système de cooldown des dépendances `uv`. [#470](https://github.com/betagouv/aides-agri/issues/470)
- **Architecture :** Possibilité de créer une fiche mère à partir de plusieurs fiches filles et de modifier une fiche mère pour impacter ses filles. [#468](https://github.com/betagouv/aides-agri/issues/468), [#469](https://github.com/betagouv/aides-agri/issues/469)
- **Déplacement d'information :** Déplacement de l'information légale en bas de la page Aide. [#466](https://github.com/betagouv/aides-agri/issues/466)
