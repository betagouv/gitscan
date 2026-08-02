## Changelog : rdv-service-public (30 derniers jours, au 01 août 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans la prise de rendez-vous pour les usagers et les agents, ainsi que sur la correction de bugs et l'ajout de nouvelles fonctionnalités comme l'intégration de Visio. Des efforts ont également été faits pour améliorer la sécurité et la performance du service.

### Évolutions fonctionnelles
- **Prise de rendez-vous usager :** Simplification et fusion des étapes de prise de rendez-vous pour les usagers après connexion [#6421](https://github.com/betagouv/rdv-service-public/pull/6421).
- **Recherche d'usagers :**
    - Amélioration de la recherche d'usagers par numéro de téléphone, correction d'un bug affectant les numéros finissant par 9 [#6546](https://github.com/betagouv/rdv-service-public/pull/6546).
    - Correction des redirections lors de recherches usagers pour des motifs sans service [#6560](https://github.com/betagouv/rdv-service-public/pull/6560).
    - Correction de l'ordre des agents dans les vues multi-agents [#6532](https://github.com/betagouv/rdv-service-public/pull/6532).
    - Utilisation de la recherche usager full-text dans le super admin [#6515](https://github.com/betagouv/rdv-service-public/pull/6515).
- **Visio :**
    - Ajout de la possibilité de désactiver Visio sur une instance [#6565](https://github.com/betagouv/rdv-service-public/pull/6565).
    - Intégration des scopes Visio à la connexion ProConnect (avec un revert et une nouvelle tentative) [#6543](https://github.com/betagouv/rdv-service-public/pull/6543), [#6545](https://github.com/betagouv/rdv-service-public/pull/6545).
- **Notifications :** Ajout du referer dans les messages Zammad des erreurs 404 pour faciliter le diagnostic [#6562](https://github.com/betagouv/rdv-service-public/pull/6562).
- **RDV Collectifs :** Correction de la validation de la date pour les nouveaux RDV collectifs [#6556](https://github.com/betagouv/rdv-service-public/pull/6556).
- **Interface Agent :** Étoffer le dropdown agent avec les différents paramètres de son compte [#6549](https://github.com/betagouv/rdv-service-public/pull/6549). Changement de l’emplacement du lien « Donnez votre avis » [#6548](https://github.com/betagouv/rdv-service-public/pull/6548).
- **Outlook :** Correction de la synchronisation Outlook avec les fuseaux horaires [#6527](https://github.com/betagouv/rdv-service-public/pull/6527).

### Évolutions techniques
- **Mise à jour de Ruby :** Passage à Ruby 3.4.10 [#6505](https://github.com/betagouv/rdv-service-public/pull/6505).
- **Mise à jour de Rails :** Mise à jour de Rails vers la version 8.0.5.1 [#6572](https://github.com/betagouv/rdv-service-public/pull/6572).
- **Sidemenu :** Migration du sidemenu vers le DSFR (Design System FR) [#6512](https://github.com/betagouv/rdv-service-public/pull/6512).
- **Sécurité :** Correction d'une vulnérabilité (CVE-2026-53727) dans la gem `css_parser` [#6520](https://github.com/betagouv/rdv-service-public/pull/6520).
- **API :** Ajout d'une API de gestion des webhooks pour visioplainte [#6517](https://github.com/betagouv/rdv-service-public/pull/6517).
- **Tests :** Amélioration des tests avec remplacement des `sleep` par des `expect` pour réduire les faux positifs [#6533](https://github.com/betagouv/rdv-service-public/pull/6534), [#6534](https://github.com/betagouv/rdv-service-public/pull/6534).
- **Logging :** Logging des paramètres des recherches de RDV usagers [#6564](https://github.com/betagouv/rdv-service-public/pull/6564).

### Autres changements
- **Documentation :** Ajout de documentation et d'un script pour le setup d'une VM pour les agents LLM [#6492](https://github.com/betagouv/rdv-service-public/pull/6492).
- **Migration d'organisations :** Script pour migrer les organisations ouvertes à la main vers le nouveau nom de domaine [#6518](https://github.com/betagouv/rdv-service-public/pull/6518).
- **Script :** Script pour extraire toutes les organisations du territoire historique des mairies [#6509](https://github.com/betagouv/rdv-service-public/pull/6509).
- **Correction :** Correction d'un bug empêchant la modification d'email usager [#6507](https://github.com/betagouv/rdv-service-public/pull/6507).
- **Correction :** Correction d'un problème avec l'info d'usager insupprimable [#6540](https://github.com/betagouv/rdv-service-public/pull/6540).
- **Correction :** Correction d'un bug lié à la saisie d'une durée négative dans l'interface agent [#6530](https://github.com/betagouv/rdv-service-public/pull/6530).
- **Cron Job :** Possibilité de désactiver l'exécution du CRON job de rafraîchissement des comptes sensibles via une variable d'environnement [#6513](https://github.com/betagouv/rdv-service-public/pull/6513).
- **a11y :** Ajout de balises `ul/li` pour la liste des motifs de nouveau RDV Collectif pour améliorer l'accessibilité [#6508](https://github.com/betagouv/rdv-service-public/pull/6508).
