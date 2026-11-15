## Changelog : karfur (30 derniers jours, au 13/11/2026)

### Résumé
Ce mois-ci, le développement a été marqué par un effort massif de mise en conformité avec les normes d'accessibilité (RGAA) et une amélioration significative des outils de gestion. Les utilisateurs bénéficieront de notifications plus précises et d'une recherche plus fluide, tandis que l'équipe dispose de nouveaux outils pour administrer les widgets et automatiser les processus de déploiement.

### Évolutions fonctionnelles
- **Notifications** : 
    - Mise en place de l'envoi manuel de notifications push pour les démarches et les dispositifs [#4050](https://github.com/refugies-info/karfur/pull/4050).
    - Amélioration de la fiabilité des notifications (meilleur ciblage des utilisateurs actifs et gestion des erreurs d'envoi) [#4055](https://github.com/refugies-info/karfur/pull/4055).
- **Gestion des widgets** : Introduction d'une nouvelle interface d'administration via API [#4027](https://github.com/refugies-info/karfur/pull/4027) et ajout de webhooks pour automatiser la gestion du contenu et des configurations.
- **Recherche** : Amélioration de l'expérience de recherche avec une gestion plus intuitive des états vides et des erreurs.
- **Interface mobile** : Nettoyage de l'interface mobile avec la suppression de mentions obsolètes ("Date Dépassée") [#4047](https://github.com/refugies-info/karfur/pull/4047).

### Évolutions techniques
- **Accessibilité (RGAA)** : Mise en conformité majeure sur de nombreux points critiques, notamment la gestion du zoom à 200%, les contrastes, les annonces pour les lecteurs d'écran (formulaires, erreurs, messages de remerciement), et la navigation au clavier [#4049](https://github.com/refugies-info/karfur/pull/4049), [#4048](https://github.com/refugies-info/karfur/pull/4048), [#4023](https://github.com/refugies-info/karfur/pull/4023).
- **Optimisation de la recherche** : Refonte technique de la recherche utilisant SWR pour des résultats plus rapides et une meilleure gestion des données [#4019](https://github.com/refugies-info/karfur/pull/4019).
- **Sécurité et Infrastructure** : 
    - Mise à jour de l'environnement Node.js et correction de plusieurs vulnérabilités critiques (Handlebars, sanitize-html, Storybook) via des audits de sécurité réguliers [#4031](https://github.com/refugies-info/karfur/pull/4031), [#4013](https://github.com/refugies-info/karfur/pull/4013).
    - Automatisation du versioning lors des déploiements en production [#4011](https://github.com/refugies-info/karfur/pull/4011).
- **Refactoring et Nettoyage** : 
    - Suppression de fonctionnalités et de pages obsolètes (widgets abandonnés, pages d'intégration mortes) pour alléger la plateforme.
    - Refonte de la structure de données des widgets pour une meilleure gestion en base de données.

### Autres changements
- **Documentation** : Mise à jour du README pour clarifier l'importance du versioning.
- **Tests** : Renforcement de la couverture de tests, notamment sur les processus de traduction et les notifications.
