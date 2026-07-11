## Changelog : rdv-service-public (30 derniers jours, au 10 juillet 2026)

### Résumé
Cette période a été marquée par une migration vers un nouveau nom de domaine, des améliorations de l'expérience utilisateur (accessibilité, clarté des informations), des corrections de bugs et des optimisations techniques. L'équipe a également travaillé sur l'ajout de nouvelles fonctionnalités pour les agents et les administrateurs, notamment la gestion des services et des motifs.

### Évolutions fonctionnelles
- **Nouveau nom de domaine:** Migration des organisations vers le nouveau nom de domaine et ajustements associés pour une meilleure expérience utilisateur. [#6518](https://github.com/betagouv/rdv-service-public/issues/6518)
- **Recherche utilisateur:** Amélioration de la recherche d'utilisateurs dans le super admin avec l'utilisation de la recherche full-text. [#6515](https://github.com/betagouv/rdv-service-public/issues/6515)
- **Gestion des motifs:** Possibilité pour les administrateurs d'espace de créer de nouveaux services. [#6455](https://github.com/betagouv/rdv-service-public/issues/6455)
- **Création massive de motifs:** Création de 29 motifs France Service en un seul clic dans le super-admin. [#6406](https://github.com/betagouv/rdv-service-public/issues/6406)
- **Réservation en ligne:** Ajout d'instructions pour les usagers lors de la réservation en ligne. [#6431](https://github.com/betagouv/rdv-service-public/issues/6431)
- **Interface agent:** Amélioration de l'interface pour les agents, notamment avec l'utilisation de cartes DSFR pour la recherche de créneaux et les choix de motifs. [#6437](https://github.com/betagouv/rdv-service-public/issues/6437), [#6448](https://github.com/betagouv/rdv-service-public/issues/6448)
- **Affichage des informations:** Affichage du nom de l'usager connecté. [#6452](https://github.com/betagouv/rdv-service-public/issues/6452)
- **Correction d'erreurs:** Correction de bugs liés à la modification d'email utilisateur, à l'import d'événements CalDAV, et à la disponibilité des créneaux. [#6507](https://github.com/betagouv/rdv-service-public/issues/6507), [#6488](https://github.com/betagouv/rdv-service-public/issues/6488), [#6470](https://github.com/betagouv/rdv-service-public/issues/6470)
- **Accessibilité:** Corrections d'accessibilité (a11y) pour la navigation de l'agenda et les plages d'ouverture. [#6499](https://github.com/betagouv/rdv-service-public/issues/6499), [#6498](https://github.com/betagouv/rdv-service-public/issues/6498)

### Évolutions techniques
- **Refactoring CSS:** Réduction de la dépendance à Bootstrap pour le CSS. [#6457](https://github.com/betagouv/rdv-service-public/issues/6457)
- **DSFR:** Remplacement progressif des composants Bootstrap par des composants du Design System Français (DSFR) (badges, boutons, alertes, cards, accordéon). [#6467](https://github.com/betagouv/rdv-service-public/issues/6467), [#6468](https://github.com/betagouv/rdv-service-public/issues/6468), [#6489](https://github.com/betagouv/rdv-service-public/issues/6489), [#6434](https://github.com/betagouv/rdv-service-public/issues/6434)
- **API Webhooks:** Ajout d'une API de gestion des webhooks pour visioplainte. [#6517](https://github.com/betagouv/rdv-service-public/issues/6517)
- **Recherche par téléphone/ID:** Suppression de la dépendance à `tsvector` pour la recherche par téléphone et ID. [#6349](https://github.com/betagouv/rdv-service-public/issues/6349)
- **Review Apps:** Utilisation de la stack `scalingo-24` dans les review apps. [#6439](https://github.com/betagouv/rdv-service-public/issues/6439)
- **Scripts d'installation:** Mise à jour des instructions d'installation et ajout d'un fichier `mise.toml`. [#6440](https://github.com/betagouv/rdv-service-public/issues/6440)

### Autres changements
- **Sécurité:** Possibilité de désactiver l'exécution de la tâche cron de rafraîchissement des comptes sensibles via une variable d'environnement. [#6513](https://github.com/betagouv/rdv-service-public/issues/6513)
- **Agents RDV Insertion:** Marquage des agents des organisations rdv-insertion comme sensibles. [#6387](https://github.com/betagouv/rdv-service-public/issues/6387)
- **Documentation:** Mise à jour des mentions légales pour le nouveau nom de domaine. [#6442](https://github.com/betagouv/rdv-service-public/issues/6442)
- **Nettoyage de code:** Suppression d'un formulaire de création d'organisation inutilisé. [#6465](https://github.com/betagouv/rdv-service-public/issues/6465)
