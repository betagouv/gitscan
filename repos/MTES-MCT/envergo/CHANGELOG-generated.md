## Changelog : envergo (30 derniers jours, au 2026-06-02)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives des performances de l'application, notamment au niveau des requêtes en base de données et de l'affichage des données cartographiques. Des corrections ont également été apportées pour améliorer l'expérience utilisateur, notamment dans la gestion des conditions d'évaluation et l'affichage des données relatives aux haies et aux espèces. La sécurité et la conformité RGPD ont également été renforcées.

### Évolutions fonctionnelles
- Amélioration de l'affichage des données relatives aux haies, avec une simplification de la topologie pour une meilleure performance et une correction du calcul de la densité des haies.
- Clarification de l'affichage des données relatives aux haies et aux espèces, avec des messages plus clairs et une meilleure organisation de l'information.
- Ajout d'un message d'avertissement lorsque des espèces sensibles sont détectées.
- Amélioration de l'interface utilisateur pour l'espace instruction, avec un changement de terminologie pour une meilleure clarté.
- Correction d'un bug lié à l'affichage des valeurs flottantes dans les tests.
- Mise en place d'une gestion améliorée des jetons expirés.
- Correction d'un problème d'affichage dans les détails des conditions de plantation.
- Amélioration de l'affichage des messages et des erreurs.

### Évolutions techniques
- Optimisation des performances des requêtes en base de données, notamment pour l'affichage des zones et des données de Moulinette.
- Mise en cache de divers résultats de requêtes pour réduire la charge sur la base de données.
- Refactorisation du code pour améliorer la qualité et la maintenabilité, notamment dans la gestion des conditions d'évaluation et des données relatives aux haies.
- Suppression de code obsolète et de fonctionnalités inutilisées, notamment concernant la gestion des événements Brevo et le modèle RecipientStatus.
- Amélioration de la sécurité en protégeant l'accès aux données des espèces derrière une authentification.
- Mise à jour des dépendances du projet.
- Correction de plusieurs erreurs et avertissements dans le code.
- Amélioration de la gestion des erreurs et des exceptions.

### Autres changements
- Documentation mise à jour pour refléter les changements apportés au code.
- Corrections de tests unitaires pour assurer la qualité du code.
- Ajout de commentaires pour améliorer la lisibilité du code.
- Amélioration de la configuration du projet.
- Correction de problèmes de linting et de style de code.
- Suppression de l'affichage de sections sans données.
- Ajout de tests pour les nouvelles fonctionnalités.
- Correction de bugs liés à la validation des formulaires.
- Amélioration de la gestion des événements Brevo pour la conformité RGPD.
