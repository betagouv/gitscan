## Changelog : rdv-service-public (30 derniers jours, au 28 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment pour les agents et les utilisateurs lors de la prise de rendez-vous. Des corrections de bugs ont été apportées pour améliorer la fiabilité de la recherche d'usagers et la gestion des rendez-vous. Des mises à jour techniques ont également été réalisées pour améliorer la sécurité et la performance de la plateforme.

### Évolutions fonctionnelles
- **Prise de rendez-vous :** Fusion des étapes de prise de rendez-vous pour les utilisateurs connectés, simplifiant ainsi le processus. [#6421](https://github.com/betagouv/rdv-service-public/pull/6421)
- **Recherche d'usagers :** Correction de la recherche d'usagers par numéro de téléphone se terminant par un 9. [#6546](https://github.com/betagouv/rdv-service-public/issues/6546)
- **Redirections :** Correction des redirections lors de la recherche d'usagers pour des motifs sans service. [#6560](https://github.com/betagouv/rdv-service-public/issues/6560)
- **Validation de date :** Correction de la validation de la date lors de la création de rendez-vous collectifs. [#6556](https://github.com/betagouv/rdv-service-public/issues/6556)
- **Modification d'email usager :** Correction de la modification d'email usager. [#6507](https://github.com/betagouv/rdv-service-public/issues/6507)
- **Liens de reprise de RDV :** Correction des liens pour permettre la reprise de rendez-vous après annulation (via email et SMS). [#6535](https://github.com/betagouv/rdv-service-public/issues/6535)
- **Synchronisation Outlook :** Correction de la synchronisation Outlook avec les fuseaux horaires. [#6527](https://github.com/betagouv/rdv-service-public/issues/6527)
- **Agent :** Affichage des différents paramètres du compte agent dans un dropdown. [#6549](https://github.com/betagouv/rdv-service-public/issues/6549)
- **Agent :** Correction de l'ordre des agents dans les vues multi-agents. [#6532](https://github.com/betagouv/rdv-service-public/issues/6532)
- **Agent :** Utilisation des modales du DSFR côté agent. [#6463](https://github.com/betagouv/rdv-service-public/pull/6463)
- **Agent LLM :** Ajout de documentation et d'un script pour le setup d'une VM pour les agents LLM. [#6492](https://github.com/betagouv/rdv-service-public/issues/6492)

### Évolutions techniques
- **Ruby :** Mise à jour vers Ruby 3.4.10. [#6505](https://github.com/betagouv/rdv-service-public/pull/6505)
- **Sécurité :** Correction d'une vulnérabilité (CVE-2026-53727) dans la gem `css_parser`. [#6520](https://github.com/betagouv/rdv-service-public/pull/6520)
- **Recherche :** Utilisation de la recherche usager full-text dans le super admin. [#6515](https://github.com/betagouv/rdv-service-public/issues/6515)
- **DSFR :** Passage du sidemenu au Design System Fr. [#6512](https://github.com/betagouv/rdv-service-public/pull/6512)
- **Alertes :** Remplacement des alertes Bootstrap par des alertes DSFR. [#6489](https://github.com/betagouv/rdv-service-public/pull/6489)
- **Infrastructure :**  Correction pour les organisations ANTS ajoutées avec le mauvais nom de domaine. [#6502](https://github.com/betagouv/rdv-service-public/issues/6502)
- **Infrastructure :** Migration d'organisations ouvertes à la main vers le nouveau nom de domaine. [#6518](https://github.com/betagouv/rdv-service-public/pull/6518)

### Autres changements
- **Documentation :** Ajout de liens entre les détails du motif et la réservation en ligne. [#6466](https://github.com/betagouv/rdv-service-public/pull/6466)
- **Accessibilité :** Améliorations de l'accessibilité (a11y) pour la plage d’ouverture et la navigation de l’agenda. [#6498](https://github.com/betagouv/rdv-service-public/issues/6498) et [#6499](https://github.com/betagouv/rdv-service-public/issues/6499)
- **Configuration :** Ajout de `mise.toml` et mise à jour des instructions d'installation. [#6440](https://github.com/betagouv/rdv-service-public/pull/6440)
- **Sécurité :** Ajout d'une option pour désactiver l'exécution de la tâche cron de renouvellement des comptes sensibles. [#6513](https://github.com/betagouv/rdv-service-public/issues/6513)
- **Agents :** Marquer les agents des organisations rdv-insertion comme sensibles. [#6387](https://github.com/betagouv/rdv-service-public/issues/6387)
- **API :** Ajout d'une API de gestion des webhooks pour visioplainte. [#6517](https://github.com/betagouv/rdv-service-public/pull/6517)
- **Divers :** Ajustement de logos et de la direction de la publication pour le site vitrine côté État. [#6483](https://github.com/betagouv/rdv-service-public/pull/6483)
