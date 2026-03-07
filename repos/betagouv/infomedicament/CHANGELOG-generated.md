## Changelog : infomedicament (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration significative de la recherche de médicaments, notamment en intégrant la recherche par code ATC5 et en affinant l'ordre des résultats. Des améliorations ont également été apportées à la page d'information sur les médicaments avec l'ajout de nouvelles données (excipients, alertes de sécurité, etc.). Des optimisations techniques ont été réalisées pour améliorer la performance et la stabilité de l'application.

### Évolutions fonctionnelles
- **Recherche :** Possibilité de rechercher des médicaments par code ATC5. [#197](https://github.com/betagouv/infomedicament/pull/197)
- **Recherche :** L'ordre des résultats de recherche a été amélioré en fonction du type de correspondance (nom, spécialité, etc.). [#197](https://github.com/betagouv/infomedicament/pull/197)
- **Recherche :** La recherche automatique propose désormais des noms de spécialités.
- **Recherche :** Limitation du nombre de résultats de recherche à 100 médicaments pour améliorer la performance.
- **Page médicament :** Ajout d'informations sur les excipients.
- **Page médicament :** Ajout d'informations sur les Autorisations d'Utilisation Temporaire (AIP).
- **Page médicament :** Ajout d'informations sur le statut commercialisé.
- **Page médicament :** Ajout d'informations sur les alertes de sécurité.
- **Page médicament :** Ajout d'informations sur la surveillance renforcée.
- **Page médicament :** Ajout d'informations sur le statut homéopathique.
- **Page d'accueil :** Mise à jour du nombre de spécialités affichées.

### Évolutions techniques
- **Base de données :** Migration de la source de données ATC vers la base de données pour une meilleure performance et maintenabilité. [#157](https://github.com/betagouv/infomedicament/pull/157)
- **Base de données :** Refonte de la structure de la base de données pour optimiser la recherche.
- **CI/CD :** Ajout de tests Lighthouse à l'exécution des applications de revue.
- **CI/CD :** Amélioration du workflow CI pour attendre la fin du déploiement de l'application de revue Scalingo.
- **Performance :** Suppression de l'intégration coûteuse de Sentry Replay.
- **Performance :** Diminution du taux d'échantillonnage de Sentry à 10%.
- **Tests :** Ajout de tests unitaires et d'intégration.
- **Tests :** Mise à jour et correction des tests d'interface utilisateur (snapshots).
- **Refactoring :** Simplification du code de la recherche et des composants associés.
- **Refactoring :** Suppression de code inutilisé.

### Autres changements
- Correction d'un problème de blocage du script PDBM en fermant la connexion MySQL. [#191](https://github.com/betagouv/infomedicament/pull/191)
- Correction d'un problème d'ordre d'exécution des migrations de base de données. [#187](https://github.com/betagouv/infomedicament/pull/187)
- Correction d'un problème lié à un gestionnaire d'événements. [#182](https://github.com/betagouv/infomedicament/pull/182)
- Ajout d'une commande `db:update-resume` pour faciliter la mise à jour des données.
- Amélioration de la documentation et des commentaires dans le code.
- Correction de bugs mineurs et améliorations de la qualité du code.
