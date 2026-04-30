## Changelog : mon-entreprise (30 derniers jours, au 28 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la robustesse et de la fiabilité de la plateforme, notamment au niveau des workflows de déploiement et de la gestion des données Algolia. Des corrections ont été apportées pour améliorer l'expérience utilisateur, en particulier concernant le simulateur de choix de statut et les calculs liés aux cotisations sociales et à l'impôt sur le revenu. La décommission du simulateur RGCP a également été finalisée.

### Évolutions fonctionnelles
- Suppression du simulateur RGCP et mise à jour des règles associées. [#4433](https://github.com/betagouv/mon-entreprise/issues/4433)
- Ajout du PASS mahorais pour les travailleurs indépendants.
- Correction de la saisie des montants, quelle que soit l'unité.
- Correction de la navigation et de la prévisualisation en iframe pour l'intégration du simulateur.
- Correction du calcul des cotisations de début d'activité au régime micro-fiscal.
- Correction de la valeur de situation de famille pour le calcul de l'impôt.
- Ajout d'icônes d'aide pour la retraite complémentaire dans le comparateur.
- Amélioration de la gestion des points acquis AGIRC-ARRCO dans le comparateur.
- Correction d'un bug de scroll dans l'assistant choix-du-statut en iframe.
- Mise à jour des plafonds de CA pour l'activité entrepreneuriale.
- Mise à jour des cotisations aux caisses de retraite (PLR).
- Correction des tests sur les DROM.

### Évolutions techniques
- Refonte complète des workflows GitHub Actions pour une meilleure gestion des déploiements et des tests.
- Amélioration de l'isolation et de la gestion des scripts Algolia, notamment pour le téléchargement d'artefacts et la gestion des erreurs.
- Correction de problèmes liés à l'environnement Node.js et à la gestion des secrets.
- Correction d'un problème de FOUC (Flash of Unstyled Content) causé par l'utilisation de `navigator` dans Node.js.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité, notamment dans les composants liés à l'iframe et aux calculs de cotisations.
- Utilisation de `When(Not)Applicable` pour simplifier la logique des cotisations forfaitaires.
- Suppression de code commenté et de dépendances inutiles.
- Mise à jour des versions de Node.js et des actions CI/CD.

### Autres changements
- Mise à jour des traductions (i18n).
- Correction du formatage Prettier.
- Correction de la casse de Cipav dans la description des points acquis.
- Mise à jour du taux horaire minimum pour l'activité partielle.
- Correction de la gestion des règles obsolètes et ajout d'un bandeau d'alerte pour les informer.
- Amélioration de la gestion des erreurs et des exceptions dans le code.
- Correction de bugs mineurs et amélioration de la qualité du code.
