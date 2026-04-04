# Synthèse d'activité : MTES-MCT (derniers 7 jours)

## Résumé de l'activité
L'activité de l'organisation MTES-MCT au cours des 7 derniers jours a été particulièrement riche, avec des améliorations significatives sur de nombreux projets.  On observe une forte concentration sur l'amélioration de l'expérience utilisateur, notamment sur les applications Dossier Facile, Potentiel, et Vizeau, avec des fonctionnalités nouvelles comme l'ajout de notes sur les parcelles, la simplification de l'invitation d'utilisateurs, et la refonte des interfaces. La sécurité a également été un axe majeur, avec des mises à jour de dépendances et des corrections de vulnérabilités sur plusieurs dépôts (qualicharge, zero-logement-vacant). Enfin, des efforts importants ont été consacrés à l'amélioration de l'infrastructure et de la maintenance des outils, notamment avec des migrations vers des versions plus récentes de technologies clés (Symfony, Node.js) et l'optimisation des processus de build et de déploiement. Les projets Monitorfish et Ecobalyse ont également bénéficié d'améliorations importantes en termes de données et de fonctionnalités.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :

- Correction de vulnérabilités et mise à jour des dépendances dans [qualicharge](/repos/MTES-MCT/qualicharge).
- Amélioration de la sécurité avec l'ajout d'en-têtes de sécurité et correction de vulnérabilités dans [zero-logement-vacant](/repos/MTES-MCT/zero-logement-vacant).
- Ajout d'une expiration sur les hash d'invitation pour renforcer la sécurité dans [trackdechets](/repos/MTES-MCT/trackdechets).
- Refactorisation de l'authentification et gestion des droits avec une couche d'abstraction et suppression du `cerbere_token` dans [verseau2](/repos/MTES-MCT/verseau2).

## Autres changements notables
Plusieurs projets ont connu des évolutions techniques majeures :

- Migration vers Symfony 7.4 dans [stop-punaises](/repos/MTES-MCT/stop-punaises).
- Refonte de l'architecture Django dans [Docurba](/repos/MTES-MCT/Docurba) avec séparation des configurations et des applications.
- Migration vers la couche d'abstraction MASA pour les appels API dans [verseau2](/repos/MTES-MCT/verseau2).
- Utilisation de l'API geo.gouv.fr côté backend pour éviter les problèmes de CORS dans [trackdechets](/repos/MTES-MCT/trackdechets).
- Migration de Highland vers Web Streams dans [zero-logement-vacant](/repos/MTES-MCT/zero-logement-vacant).
- Utilisation d'esbuild pour la construction du serveur dans [zero-logement-vacant](/repos/MTES-MCT/zero-logement-vacant).

## Dépôts les plus actifs
- [Docurba](/repos/MTES-MCT/Docurba) : Améliorations significatives de l'administration de l'application, corrections de bugs et refonte de l'architecture.
- [Dossier-Facile-Frontend](/repos/MTES-MCT/Dossier-Facile-Frontend) : Améliorations de l'accessibilité, corrections de bugs et amélioration de l'expérience utilisateur.
- [Monitorfish](/repos/MTES-MCT/monitorfish) : Ajout de la gestion des signalements INN, enrichissement des données affichées et corrections de bugs.
- [Potentiel](/repos/MTES-MCT/potentiel) : Ajout de nouvelles fonctionnalités pour la gestion des utilisateurs et des projets, ainsi que des améliorations techniques importantes.
- [Trackdechets](/repos/MTES-MCT/trackdechets) : Ajout de filtres avancés, amélioration de la sécurité et refactorisation technique.
- [Vizeau](/repos/MTES-MCT/vizeau) : Ajout de la possibilité d'ajouter des notes aux parcelles et amélioration de l'interface utilisateur.
