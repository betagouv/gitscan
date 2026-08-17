## Changelog : fonds-vert-espace-laureat (30 derniers jours, au 14 août 2026)

### Résumé
Ce mois a été marqué par une refonte majeure du module de gestion des métriques. L'accent a été mis sur la capacité des utilisateurs à identifier, corriger et valider les anomalies de données de manière intuitive. L'interface a été considérablement simplifiée et harmonisée avec le design system (DSFR) pour offrir une expérience de suivi plus fluide et professionnelle.

### Évolutions fonctionnelles

**Gestion des métriques et des anomalies**
- **Correction simplifiée** : Possibilité de corriger directement les valeurs depuis les cartes de métriques et via un nouvel éditeur de listes structuré.
- **Suivi des anomalies** : Les anomalies sont désormais propagées directement sur les lignes de métriques et peuvent être filtrées via une grille dédiée pour faciliter leur traitement.
- **Persistance des données** : Les corrections effectuées sont désormais enregistrées en base de données, garantissant la fiabilité des révisions.
- **Importation** : Finalisation du processus d'importation initiale des données du Fonds Vert.
- **Mode Démo** : Ajout de fonctionnalités de réinitialisation des données de base pour faciliter les tests et les démonstrations.

**Interface Utilisateur (UI/UX)**
- **Refonte visuelle** : Amélioration de la lisibilité des cartes thématiques (meilleur contraste, icônes standardisées, regroupement des valeurs et des unités).
- **Notifications** : Mise en conformité des messages de succès (toasts) avec les standards du DSFR.
- **Ergonomie des formulaires** : Optimisation des modales de correction et de l'espacement des tableaux pour une navigation plus claire.

### Évolutions techniques

**Architecture et données**
- **Modélisation des données** : Séparation entre les données brutes et les données de confiance ("trusted shapes") pour une meilleure intégrité.
- **Gestion des révisions** : Implémentation d'un système de révisions atomiques et typées pour assurer la traçabilité des modifications.
- **Optimisation du pipeline** : Refactorisation du pipeline d'importation local et optimisation du chargement des cibles de correction.

**Infrastructure et Qualité**
- **CI/CD** : Mise à jour de la chaîne d'outils npm pour les tests Playwright.
- **Docker** : Clarification de la gestion des ports dans la configuration Docker.
- **Tests** : Renforcement de la couverture de tests, notamment sur la persistance des corrections et les comportements de traitement des métriques.
