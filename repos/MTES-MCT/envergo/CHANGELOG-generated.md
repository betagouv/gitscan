## Changelog : envergo (30 derniers jours, au 15 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des ICPE (Installations Classées pour la Protection de l'Environnement), l'optimisation des performances de l'application, et la correction de bugs pour une meilleure expérience utilisateur. Des améliorations ont également été apportées à la gestion des notifications par email et à la clarté de l'interface utilisateur.

### Évolutions fonctionnelles
- **ICPE :** Ajout d'une gestion plus fine des cas par cas pour les ICPE, incluant de nouveaux critères, des actions spécifiques et des modèles d'email adaptés. L'affichage des informations ICPE a été amélioré et rendu plus clair.
- **Notifications Email :** Amélioration de la gestion des emails, notamment en lien avec les ICPE, avec des templates mis à jour et une meilleure gestion des erreurs.
- **Interface Utilisateur :**
    - Clarification des messages d'erreur et des indications affichées aux utilisateurs.
    - Amélioration de l'affichage des haies et de leur longueur.
    - Modification du libellé "Administration" vers "Espace instruction" pour plus de clarté.
- **Gestion des pétitions :** Refonte de la gestion du contexte des pétitions pour améliorer la performance et la clarté.

### Évolutions techniques
- **Performance :** Optimisations significatives des requêtes en base de données, notamment pour l'affichage des données et le calcul des longueurs de haies. Mise en cache de données fréquemment utilisées pour réduire la charge sur la base de données.
- **Refactoring :** Plusieurs refactorings ont été effectués pour améliorer la qualité du code, notamment dans les modules liés aux conditions d'évaluation et à la gestion des ICPE.
- **Tests :** Ajout et amélioration des tests unitaires et d'intégration, notamment pour les nouvelles fonctionnalités ICPE et les calculs de longueurs de haies.
- **Dépendances :** Mise à jour des dépendances du projet.
- **Sécurité :** Suppression de fonctionnalités obsolètes liées à Brevo (anciennement Sendinblue) pour améliorer la conformité RGPD.

### Autres changements
- **Documentation :** Ajout de liens vers la documentation en ligne du PAC (Plan d'Action Climat).
- **CI/CD :** Corrections pour assurer le bon fonctionnement des pipelines CI/CD.
- **Nettoyage de code :** Suppression de code inutile et amélioration de la lisibilité du code.
- **Corrections de bugs :** Correction de plusieurs bugs mineurs affectant l'affichage et le comportement de l'application.
