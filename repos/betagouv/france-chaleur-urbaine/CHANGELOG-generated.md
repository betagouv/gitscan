## Changelog : france-chaleur-urbaine (30 derniers jours, au 16/09/2026)

### Résumé
Ce mois-ci, le service a été enrichi de nouvelles fonctionnalités de simulation (gestion des espaces extérieurs, précision accrue de l'altitude, nouveaux indicateurs de pertinence) et d'une meilleure communication automatisée avec les utilisateurs (emails de relance et de refus). L'interface utilisateur et la fiabilité des données (DPE, réseaux) ont également été renforcées.

### Évolutions fonctionnelles
- **Simulateur** : intégration de nouveaux critères (espaces extérieurs, éligibilité aux réseaux de froid, sobriété énergétique) et amélioration de l'ergonomie (badges de notification pour les paramètres à compléter, nouveau design du bloc de paramètres, réorganisation des prérequis).
- **Simulateur** : précision accrue des résultats grâce à l'utilisation de l'altitude précise des bâtiments (via l'API IGN) et affichage de la pertinence des solutions par un système d'étoiles.
- **Cartographie et réseaux** : ajout d'infobulles sur la liste des réseaux, affichage du nom des gestionnaires de réseaux et rétablissement de l'affichage des propriétés au clic sur la carte.
- **Gestion des demandes** : automatisation de l'envoi d'emails lorsque les demandes de chaleur renouvelable ne sont pas réalisables et simplification des messages de relance.
- **Statistiques** : filtrage des demandes non validées pour garantir la cohérence des données affichées.
- **Comparateur** : correction des labels pour une meilleure clarté.

### Évolutions techniques
- **Données et API** : optimisation de la récupération des données ECFR via un système de cache plus stable pour réduire la dépendance aux API externes [#1287](https://github.com/betagouv/france-chaleur-urbaine/pull/1287) et mise à jour des données DPE 2026.
- **Analytics** : déploiement du suivi Posthog pour le module PAC et synchronisation avec le plan de tracking [#1302](https://github.com/betagouv/france-chaleur-urbaine/pull/1302).
- **Maintenance et architecture** : suppression de la permission nationale [#1289](https://github.com/betagouv/france-chaleur-urbaine/pull/1289), nettoyage des couches de tests et des commandes de migration "oneshot".
- **Correctifs** : ajustement des règles de calcul Publicodes (gestion des maximums/minimums) [#1297](https://github.com/betagouv/france-chaleur-urbaine/pull/1297).

### Autres changements
- Mise à jour de la documentation.
