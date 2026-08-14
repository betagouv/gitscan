## Changelog : Aidants_Connect (30 derniers jours, au 10 août 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur l'amélioration de l'accessibilité numérique pour garantir une expérience inclusive à tous les utilisateurs. Parallèlement, la gestion des données (notamment le suivi des SIRET) a été renforcée et la fiabilité du projet a été consolidée par une montée en charge importante de la couverture de tests.

### Évolutions fonctionnelles
- **Gestion des organisations** : Amélioration du suivi des données avec la possibilité de sauvegarder les SIRET invalides [#1799](https://github.com/betagouv/Aidants_Connect/issues/1799) et de gérer les doublons de SIRET [#1800](https://github.com/betagouv/Aidants_Connect/issues/1800).
- **Exports** : Enrichissement de l'export global avec de nouveaux champs dédiés au nettoyage des SIRET [#1802](https://github.com/betagouv/Aidants_Connect/issues/1802).
- **Interface** : Mise à jour de la page d'accueil [#1803](https://github.com/betagouv/Aidants_Connect/issues/1803).

### Évolutions techniques
- **Accessibilité (A11y)** : Chantier majeur de mise en conformité sur l'ensemble de l'application, incluant :
    - Corrections sémantiques (utilisation de balises de titre, paragraphes et attributs ARIA) sur les templates de formation, de notifications et d'organisations [#1797](https://github.com/betagouv/Aidants_Connect/issues/1797).
    - Optimisation de la navigation (en-tête, pied de page et menu légal) pour une meilleure gestion du focus et des liens actifs.
    - Ajustements visuels pour assurer la stabilité de l'affichage sur petits écrans.
- **API** : Mise à jour de l'intégration de l'API FNE [#1801](https://github.com/betagouv/Aidants_Connect/issues/1801).
- **Qualité et Tests** : 
    - Renforcement significatif de la suite de tests (couverture des modèles, de l'API et de FranceConnect) [#1808](https://github.com/betagouv/Aidants_Connect/issues/1808), [#1783](https://github.com/betagouv/Aidants_Connect/issues/1783).
    - Correction de plusieurs régressions et erreurs de typographie dans les tests.
