## Changelog : aides-agri (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur la préparation et le déploiement de la version 2 du parcours agri, avec des améliorations significatives de l'interface d'administration pour la gestion des aides. Des corrections de bugs et des optimisations ont également été apportées pour améliorer l'expérience utilisateur et la stabilité de la plateforme. De nombreuses mises à jour de dépendances ont été effectuées pour maintenir la sécurité et la performance de l'application.

### Évolutions fonctionnelles
- **Parcours agri v2 :** Déploiement de la version 2 du parcours agri, améliorant l'expérience utilisateur pour les exploitants agricoles. [#418](https://github.com/betagouv/aides-agri/pull/418)
- **Duplication d'aides :** Possibilité de dupliquer une aide existante depuis l'interface d'administration, facilitant la création d'aides similaires. [#448](https://github.com/betagouv/aides-agri/pull/448)
- **Réorganisation des champs d'aide :** Amélioration de l'organisation des champs dans l'interface d'administration pour une meilleure ergonomie. [#446](https://github.com/betagouv/aides-agri/pull/446)
- **Association de logos DDT(M) :** Scripts pour la création et l'association des logos des Directions Départementales des Territoires et de la Mer (DDT(M)). [#493](https://github.com/betagouv/aides-agri/pull/493)
- **Base juridique des aides :** Consolidation et amélioration de la gestion de la base juridique des aides. [#495](https://github.com/betagouv/aides-agri/pull/495), [#499](https://github.com/betagouv/aides-agri/pull/499)
- **Modification des fiches mères :** Modification d'une fiche mère impacte désormais également ses fiches filles. [#468](https://github.com/betagouv/aides-agri/pull/468)
- **Création de fiches mères :** Possibilité de créer une fiche mère à partir de plusieurs fiches filles. [#469](https://github.com/betagouv/aides-agri/pull/469)

### Évolutions techniques
- **Optimisation du workflow GitHub :** Amélioration du workflow GitHub pour une meilleure gestion des contributions. [#467](https://github.com/betagouv/aides-agri/pull/467)
- **Facilitation du déploiement :** Amélioration du processus de déploiement en cas de changement de schéma de base de données. [#501](https://github.com/betagouv/aides-agri/pull/501)
- **Mise à jour des dépendances :** Mises à jour de plusieurs dépendances, notamment Django, Sentry, requests, pygments, faker, gunicorn, ruff, et d'autres, pour améliorer la sécurité et la performance. (Voir les commits individuels pour plus de détails)
- **Mise à jour de django-dsfr :** Passage à la version 3.4.0 puis 3.4.2 de django-dsfr. [#459](https://github.com/betagouv/aides-agri/pull/459), [#490](https://github.com/betagouv/aides-agri/pull/490)

### Autres changements
- **Correctifs d'affichage :** Correction de bugs d'affichage de couleurs et d'alignement des filtres. [#511](https://github.com/betagouv/aides-agri/pull/511), [#515](https://github.com/betagouv/aides-agri/pull/515)
- **Correctif slug des aides :** Correction d'un bug lié au slug des aides. [#497](https://github.com/betagouv/aides-agri/pull/497)
- **Mise à jour security.txt :** Mise à jour de la date de validité du fichier security.txt. [#505](https://github.com/betagouv/aides-agri/pull/505)
- **Ajout des statistiques de mars 2026 :** Ajout des statistiques d'utilisation pour le mois de mars 2026. [#477](https://github.com/betagouv/aides-agri/pull/477)
- **Divers correctifs de dernière minute :** Plusieurs petits correctifs ont été apportés en préparation du déploiement de la v2. [#502](https://github.com/betagouv/aides-agri/pull/502), [#503](https://github.com/betagouv/aides-agri/pull/504)
