## Changelog : rdv-service-public (30 derniers jours, au 30 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'expérience utilisateur, notamment concernant la prise de rendez-vous pour les usagers et la gestion des agents. Des corrections de bugs ont été apportées pour améliorer la stabilité et la fiabilité du service, ainsi que des optimisations techniques et de sécurité. L'intégration de Visio est en cours et a reçu des améliorations.

### Évolutions fonctionnelles
- **Prise de rendez-vous usager :** Simplification et fusion des étapes de prise de rendez-vous post-connexion pour une expérience plus fluide [#6421](https://github.com/betagouv/rdv-service-public/pull/6421).
- **Recherche d'usagers :**
    - Correction de la recherche usager par numéro de téléphone finissant par 9 [#6546](https://github.com/betagouv/rdv-service-public/issues/6546).
    - Correction des redirections lors de recherches usagers pour des motifs sans service [#6560](https://github.com/betagouv/rdv-service-public/issues/6560).
    - Amélioration de la recherche textuelle d'usagers avec réduction des tests "flaky" [#6532](https://github.com/betagouv/rdv-service-public/pull/6532), [#6533](https://github.com/betagouv/rdv-service-public/pull/6533), [#6534](https://github.com/betagouv/rdv-service-public/pull/6534).
    - Utilisation de la recherche usager full-text dans le super admin [#6515](https://github.com/betagouv/rdv-service-public/pull/6515).
- **Visio :**
    - Possibilité de désactiver Visio sur une instance [#6565](https://github.com/betagouv/rdv-service-public/pull/6565).
    - Ajout de Visio et intégration des scopes nécessaires à la connexion ProConnect [#6536](https://github.com/betagouv/rdv-service-public/pull/6536), [#6543](https://github.com/betagouv/rdv-service-public/pull/6543), [#6550](https://github.com/betagouv/rdv-service-public/pull/6550).
- **Notifications :** Correction des liens de reprise de rendez-vous après annulation dans les emails et SMS [#6535](https://github.com/betagouv/rdv-service-public/pull/6535).
- **Interface Agent :**
    - Étoffer le dropdown agent avec les différents paramètres de son compte [#6549](https://github.com/betagouv/rdv-service-public/pull/6549).
    - Changement de l’emplacement du lien « Donnez votre avis » [#6548](https://github.com/betagouv/rdv-service-public/pull/6548).
    - Correction de la saisie d’une durée négative dans l'interface de création de RDV pour les agents [#6530](https://github.com/betagouv/rdv-service-public/pull/6530).
- **Collectif RDV :** Correction de la validation de la date pour les nouveaux RDV collectifs [#6556](https://github.com/betagouv/rdv-service-public/pull/6556).
- **Accessibilité :** Amélioration de l'accessibilité du menu latéral avec le DSFR et correction du focus sur l'agenda [#6499](https://github.com/betagouv/rdv-service-public/pull/6499), [#6508](https://github.com/betagouv/rdv-service-public/pull/6508), [#6512](https://github.com/betagouv/rdv-service-public/pull/6512).

### Évolutions techniques
- **Mise à jour Ruby :** Mise à jour vers Ruby 3.4.10 [#6505](https://github.com/betagouv/rdv-service-public/pull/6505).
- **Sécurité :** Correction de la vulnérabilité CVE-2026-53727 dans la gem `css_parser` [#6520](https://github.com/betagouv/rdv-service-public/pull/6520).
- **Infrastructure :**
    - Ajout d'une API de gestion des webhooks pour visioplainte [#6517](https://github.com/betagouv/rdv-service-public/pull/6517).
    - Migration d'organisations ouvertes à la main vers le nouveau nom de domaine [#6518](https://github.com/betagouv/rdv-service-public/pull/6518).
- **Logging :** Ajout du logging des paramètres des recherches de RDV usagers [#6564](https://github.com/betagouv/rdv-service-public/pull/6564).
- **Corrections API :** Correction de l'API pour les doublons de RDV avec plusieurs agents [#6559](https://github.com/betagouv/rdv-service-public/pull/6559).

### Autres changements
- **Documentation :** Ajout de documentation et d'un script pour le setup d'une VM pour les agents LLM [#6492](https://github.com/betagouv/rdv-service-public/pull/6492).
- **Monitoring :** Ajout du referer dans les messages Zammad des erreurs 404 [#6562](https://github.com/betagouv/rdv-service-public/pull/6562).
- **Maintenance :** Mise à jour de latest_login_at lors de l’utilisation de FC [#6551](https://github.com/betagouv/rdv-service-public/pull/6551).
- **Divers :** Désactivation possible d'un job CRON sensible [#6513](https://github.com/betagouv/rdv-service-public/pull/6513).
- **Correction :** Correction d'un bug empêchant la modification de l'email d'un usager [#6507](https://github.com/betagouv/rdv-service-public/pull/6507).
- **Correction :** Correction d'un problème de verticale sur le nouveau nom de domaine [#6500](https://github.com/betagouv/rdv-service-public/pull/6500).
- **Correction :** Correction d'un problème d'export des participations [#6514](https://github.com/betagouv/rdv-service-public/pull/6514).
