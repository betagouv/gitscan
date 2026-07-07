## Changelog : apistration (30 derniers jours, au 06 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations de la sécurité, notamment la gestion des sessions et la protection contre les attaques, ainsi que par des corrections de bugs et des améliorations de la documentation. Des efforts ont également été déployés pour faciliter l'intégration des éditeurs et améliorer l'expérience utilisateur sur le site. Enfin, l'ajout de l'endpoint DGFIP TVA est une nouveauté importante.

### Évolutions fonctionnelles
- Ajout d'un filtre de statut pour les habilitations des fournisseurs dans le tableau de bord des fournisseurs. [#216](https://github.com/datagouv/apistration/pull/216)
- Affichage de l'ID interne de l'utilisateur sur la page de son compte. [#217](https://github.com/datagouv/apistration/pull/217)
- Ajout de l'endpoint DGFIP TVA et de sa documentation. [#125](https://github.com/datagouv/apistration/pull/125)
- Amélioration de la gestion des erreurs et de la sécurité, notamment la correction de failles potentielles XSS et tabnapping. [#240](https://github.com/datagouv/apistration/pull/240)
- Ajout d'une fonctionnalité de redirection vers la page demandée après la connexion. [#241](https://github.com/datagouv/apistration/pull/241)
- Ajout de la possibilité de gérer les membres (ajout/suppression) des éditeurs dans l'interface d'administration. [#139](https://github.com/datagouv/apistration/pull/139)

### Évolutions techniques
- Renforcement de la sécurité des sessions avec une expiration après 12h d'inactivité et une protection anti-fixation. [#242](https://github.com/datagouv/apistration/pull/242)
- Mise à jour des dépendances : Ruby, Rails, PostgreSQL, Docker, et divers gems.
- Amélioration de la robustesse des tests et correction de fuites mémoire dans les tests. [#236](https://github.com/datagouv/apistration/pull/236)
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Amélioration de la gestion des erreurs et des pings pour les endpoints.
- Mise en place d'un système de cache plus efficace pour l'API TVA. [#233](https://github.com/datagouv/apistration/pull/233)
- Amélioration de la documentation et du changelog.

### Autres changements
- Ajout de tests pour les nouvelles fonctionnalités.
- Corrections de typos et améliorations de la qualité du code.
- Mise à jour de la documentation pour les éditeurs et l'intégration de nouvelles API.
- Amélioration de l'interface utilisateur pour les cas d'usage Simplifions.
- Ajout de données de test pour CNous. [#218](https://github.com/datagouv/apistration/pull/218)
- Suppression de code obsolète.
- Ajout d'un skill pour gérer les incidents sur Hyperping. [#235](https://github.com/datagouv/apistration/pull/235)
