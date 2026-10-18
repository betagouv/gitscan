## Changelog : mobilic (30 derniers jours, au 15 octobre 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur l'amélioration des outils de gestion et de contrôle. De nouvelles fonctionnalités de filtrage, de pagination et d'exportation de données ont été ajoutées pour faciliter le travail des administrateurs. L'interface utilisateur a également été affinée pour être plus claire et plus intuitive, tout en renforçant la stabilité technique et la performance de la plateforme.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités de gestion et de contrôle**
    - Ajout de la possibilité d'exporter les contrôles avec des colonnes d'infractions et un onglet dédié [#977](https://github.com/MTES-MCT/mobilic/pull/977).
    - Mise en place d'un registre de bugs pour les contrôles [#957](https://github.com/MTES-MCT/mobilic/pull/957).
    - Possibilité pour les salariés de recevoir des bulletins de contrôle (BDC) avec ou sans licence [#982](https://github.com/MTES-MCT/mobilic/pull/982).
    - Introduction d'un badge pour signaler les modifications de pauses [#952](https://github.com/MTES-MCT/mobilic/pull/952).
- **Améliorations de l'interface et de l'expérience utilisateur**
    - Amélioration du filtrage des activités par statut [#970](https://github.com/MTES-MCT/mobilic/pull/970) et ajout de la pagination pour les activités [#935](https://github.com/MTES-MCT/mobilic/pull/935).
    - Refonte visuelle de la bannière d'alerte pour les salariés [#964](https://github.com/MTES-MCT/mobilic/pull/964).
    - Optimisation de l'affichage des listes (incidents, filtres de statut) pour une meilleure lisibilité [#996](https://github.com/MTES-MCT/mobilic/pull/996), [#991](https://github.com/MTES-MCT/mobilic/pull/991).
    - Nettoyage de l'interface : masquage des badges de validation lorsqu'ils sont vides ou en cours de chargement [#983](https://github.com/MTES-MCT/mobilic/pull/983), [#979](https://github.com/MTES-MCT/mobilic/pull/979).
    - Clarification de certains libellés dans les formulaires pour une meilleure compréhension.
    - Corrections sur l'application PWA (ancres de navigation, mise en page des notifications).
- **Corrections diverses**
    - Correction du formulaire de contrôle pour inclure correctement le type de transport.

### Évolutions techniques
- **Performance et stabilité**
    - Optimisation des appels API pour réduire la charge lors de la consultation des détails d'une entreprise [#917](https://github.com/MTES-MCT/mobilic/pull/917).
    - Amélioration de la résilience du système de suivi (polling) lors des exports [#972](https://github.com/MTES-MCT/mobilic/pull/972).
    - Correction de problèmes de pagination et de gestion des données dans l'interface d'administration [#988](https://github.com/MTES-MCT/mobilic/pull/988).
    - Amélioration de la gestion des erreurs de rafraîchissement de jeton (refresh-token) au niveau de l'API.
- **Infrastructure et Observabilité**
    - Mise à jour de la configuration CI/CD (passage à CircleCI version 2.1) et suppression des anciens processus de déploiement Scalingo [#975](https://github.com/MTES-MCT/mobilic/pull/975), [#976](https://github.com/MTES-MCT/mobilic/pull/976).
    - Ajout de mesures de performance (temps de chargement du tableau de bord) via Sentry pour améliorer l'observabilité.

### Autres changements
- Nettoyage du code et résolution des avertissements de qualité (SonarCloud et Lint).
