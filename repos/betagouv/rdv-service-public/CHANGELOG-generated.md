## Changelog : rdv-service-public (30 derniers jours, au 16 juillet 2026)

### Résumé
Cette période a été marquée par une migration vers le Design System Fr (DSFR) pour améliorer l'accessibilité et la cohérence visuelle de l'application. Des corrections de bugs et des améliorations de l'expérience utilisateur ont également été apportées, notamment concernant la gestion des rendez-vous, la recherche d'utilisateurs et la gestion des organisations. Une attention particulière a été portée à la transition vers un nouveau nom de domaine.

### Évolutions fonctionnelles
- Passage du menu latéral à la version DSFR pour une meilleure accessibilité et cohérence visuelle. [#6512](https://github.com/betagouv/rdv-service-public/issues/6512)
- Amélioration de la recherche d'utilisateurs dans l'interface d'administration avec la recherche full-text. [#6515](https://github.com/betagouv/rdv-service-public/issues/6515)
- Ajout d'une API de gestion des webhooks pour visioplainte. [#6517](https://github.com/betagouv/rdv-service-public/issues/6517)
- Affichage des liens entre les détails du motif et la réservation en ligne. [#6466](https://github.com/betagouv/rdv-service-public/issues/6466)
- Simplification du parcours de rendez-vous téléphonique. [#6464](https://github.com/betagouv/rdv-service-public/issues/6464)
- Ajout de l'email du bénéficiaire au parcours de prescription. [#6436](https://github.com/betagouv/rdv-service-public/issues/6436)
- Correction de l'affichage des flashes de login. [#6487](https://github.com/betagouv/rdv-service-public/issues/6487)
- Correction d'un bug empêchant le retrait de catégorie d'un motif. [#6478](https://github.com/betagouv/rdv-service-public/issues/6478)
- Correction d'un bug sur la modification d'email usager. [#6507](https://github.com/betagouv/rdv-service-public/issues/6507)
- Amélioration du script pour merger des agents. [#6475](https://github.com/betagouv/rdv-service-public/issues/6475)

### Évolutions techniques
- Mise à jour de Ruby vers la version 3.4.10. [#6505](https://github.com/betagouv/rdv-service-public/issues/6505)
- Migration progressive vers le Design System Fr (DSFR) pour les composants d'interface utilisateur (boutons, alertes, badges, modales). [#6463](https://github.com/betagouv/rdv-service-public/issues/6463), [#6467](https://github.com/betagouv/rdv-service-public/issues/6467), [#6468](https://github.com/betagouv/rdv-service-public/issues/6468), [#6489](https://github.com/betagouv/rdv-service-public/issues/6489)
- Refactoring CSS pour réduire la dépendance à Bootstrap. [#6457](https://github.com/betagouv/rdv-service-public/issues/6457)
- Suppression de la dépendance à `tsvector` pour la recherche par téléphone et ID. [#6349](https://github.com/betagouv/rdv-service-public/issues/6349)
- Migration des organisations ouvertes vers le nouveau nom de domaine. [#6518](https://github.com/betagouv/rdv-service-public/issues/6518)
- Correction d'un problème d'import d'événements CalDAV sans DTEND. [#6488](https://github.com/betagouv/rdv-service-public/issues/6488)
- Ajout d'une variable d'environnement pour afficher les login codes sur les environnements de revue. [#6454](https://github.com/betagouv/rdv-service-public/issues/6454)

### Autres changements
- Correction d'une vulnérabilité de sécurité (CVE-2026-53727) dans la gem `css_parser`. [#6520](https://github.com/betagouv/rdv-service-public/issues/6520)
- Ajout de la possibilité de désactiver la tâche cron de rafraîchissement des comptes sensibles via une variable d'environnement. [#6513](https://github.com/betagouv/rdv-service-public/issues/6513)
- Script pour extraire les organisations du territoire historique des mairies. [#6509](https://github.com/betagouv/rdv-service-public/issues/6509)
- Marquer les agents des organisations rdv-insertion comme sensibles. [#6387](https://github.com/betagouv/rdv-service-public/issues/6387)
- Ajout d'un fichier `mise.toml` et mise à jour des instructions d'installation. [#6440](https://github.com/betagouv/rdv-service-public/issues/6440)
- Correction de bugs liés à la transition vers le nouveau nom de domaine. [#6479](https://github.com/betagouv/rdv-service-public/issues/6479), [#6480](https://github.com/betagouv/rdv-service-public/issues/6480), [#6481](https://github.com/betagouv/rdv-service-public/issues/6481), [#6484](https://github.com/betagouv/rdv-service-public/issues/6484), [#6491](https://github.com/betagouv/rdv-service-public/issues/6491)
- Revert d'une modification précédente concernant les modales du DSFR côté agent. [#6493](https://github.com/betagouv/rdv-service-public/issues/6493)
