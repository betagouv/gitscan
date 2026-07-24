## Changelog : rdv-service-public (30 derniers jours, au 22 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment en corrigeant des bugs liés à la gestion des rendez-vous, à l'intégration avec des services tiers (ProConnect, Outlook, ANCT), et à l'accessibilité. Des efforts ont également été faits pour moderniser l'interface utilisateur avec le Design System Fr (DSFR) et pour améliorer la sécurité et la robustesse de la plateforme.

### Évolutions fonctionnelles
- Correction d'un bug empêchant la saisie d'une durée négative lors de la création d'un rendez-vous par un agent. [#6530](https://github.com/betagouv/rdv-service-public/issues/6530)
- Correction de l'affichage de l'ordre des agents dans les vues multi-agents. [#6532](https://github.com/betagouv/rdv-service-public/issues/6532)
- Correction des liens de reprise de rendez-vous après annulation, tant par email que par SMS. [#6535](https://github.com/betagouv/rdv-service-public/issues/6535)
- Amélioration de la synchronisation Outlook avec les fuseaux horaires. [#6527](https://github.com/betagouv/rdv-service-public/issues/6527)
- Ajout du menu latéral basé sur le DSFR dans les liens d’évitements. [#6528](https://github.com/betagouv/rdv-service-public/issues/6528)
- Correction d'un bug lié à la suppression d'informations d'usager. [#6540](https://github.com/betagouv/rdv-service-public/issues/6540)
- Ajout d'une API de gestion des webhooks pour visioplainte. [#6517](https://github.com/betagouv/rdv-service-public/issues/6517)
- Ajout de liens entre les détails du motif et la réservation en ligne. [#6466](https://github.com/betagouv/rdv-service-public/issues/6466)
- Correction d'un bug de retrait de catégorie sur un motif. [#6478](https://github.com/betagouv/rdv-service-public/issues/6478)
- Affichage du bon message d’erreur lorsque le créneau n’est plus disponible. [#6470](https://github.com/betagouv/rdv-service-public/issues/6470)
- Correction pour les créations de comptes sur le nouveau nom de domaine. [#6484](https://github.com/betagouv/rdv-service-public/issues/6484)

### Évolutions techniques
- Mise à jour vers Ruby 3.4.10. [#6505](https://github.com/betagouv/rdv-service-public/issues/6505)
- Passage du sidemenu au DSFR. [#6512](https://github.com/betagouv/rdv-service-public/issues/6512)
- Utilisation de la recherche usager full-text dans le super admin. [#6515](https://github.com/betagouv/rdv-service-public/issues/6515)
- Correction d'une vulnérabilité (CVE-2026-53727) dans la gem `css_parser`. [#6520](https://github.com/betagouv/rdv-service-public/issues/6520)
- Refactoring CSS pour limiter la dépendance à Bootstrap. [#6457](https://github.com/betagouv/rdv-service-public/issues/6457)
- Amélioration de la robustesse des tests avec remplacement des `sleep` par des `expect`. [#6533](https://github.com/betagouv/rdv-service-public/issues/6533)
- Limitation de la flakiness du test de recherche textuelle d'usagers. [#6534](https://github.com/betagouv/rdv-service-public/issues/6534)
- Suppression de la dépendance à `tsvector` pour la recherche par téléphone et ID. [#6349](https://github.com/betagouv/rdv-service-public/issues/6349)

### Autres changements
- Ajout de documentation et d'un script pour le setup d'une VM pour les agents LLM. [#6492](https://github.com/betagouv/rdv-service-public/issues/6492)
- Ajout d'une option pour désactiver l'exécution de la tâche cron de rafraîchissement des comptes sensibles. [#6513](https://github.com/betagouv/rdv-service-public/issues/6513)
- Script pour extraire toutes les organisations du territoire historique des mairies. [#6509](https://github.com/betagouv/rdv-service-public/issues/6509)
- Ajout d'un mock numéro ANTS RDVSPUB020 avec des appointments. [#6476](https://github.com/betagouv/rdv-service-public/issues/6476)
- Amélioration du script pour merger des agents. [#6475](https://github.com/betagouv/rdv-service-public/issues/6475)
- Marquer comme sensibles les agents des organisations rdv-insertion. [#6387](https://github.com/betagouv/rdv-service-public/issues/6387)
- Ajout de mise.toml et mise à jour des instructions d'installation. [#6440](https://github.com/betagouv/rdv-service-public/issues/6440)
- Correction d'un revert précédent lié à l'ajout des scopes Visio à la connexion ProConnect. [#6545](https://github.com/betagouv/rdv-service-public/issues/6545)
