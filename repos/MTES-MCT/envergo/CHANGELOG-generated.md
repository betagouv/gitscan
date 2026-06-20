## Changelog : envergo (30 derniers jours, au 17 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des données, notamment concernant les critères ICPE et les règles d'urbanisme, ainsi que sur des optimisations de performance et des corrections de bugs. Des améliorations significatives ont été apportées à l'interface utilisateur pour faciliter l'accès aux informations et la gestion des dossiers. La sécurité et la conformité RGPD ont également été renforcées.

### Évolutions fonctionnelles
- Amélioration de l'affichage et de la gestion des données relatives aux densités.
- Ajout de la gestion du "cas par cas" pour les ICPE, avec des templates et des actions spécifiques.
- Amélioration de l'affichage des données de plantation et des conditions associées.
- Correction de l'affichage des données dans les avis (html et txt).
- Amélioration de la gestion des critères ICPE et de leur visibilité en fonction des utilisateurs.
- Mise à jour des textes et libellés pour une meilleure clarté, notamment dans l'espace instruction.
- Possibilité d'importer plusieurs documents simultanément.
- Amélioration de l'interface pour la gestion des zones et des coefficients.
- Ajout d'une fonctionnalité permettant d'importer les données de l'inventaire national du patrimoine naturel (INPN).

### Évolutions techniques
- Optimisations de performance significatives au niveau des requêtes en base de données, notamment pour les pétitions et les données de Moulinette.
- Refactorisation du code pour une meilleure qualité et maintenabilité.
- Mise à jour des dépendances (Playwright, Node).
- Amélioration de la gestion des configurations et des URL.
- Suppression des informations sensibles dans les données exportées.
- Amélioration des tests unitaires et d'intégration, notamment avec Playwright.
- Renforcement de la sécurité en limitant l'accès aux URL et en gérant les secrets.
- Suppression des fonctionnalités liées au suivi des emails (Brevo) pour assurer la conformité RGPD.
- Correction de plusieurs erreurs de pre-commit.

### Autres changements
- Mise à jour de la documentation.
- Correction de problèmes de synchronisation entre les templates HTML et TXT.
- Amélioration des commentaires et de la lisibilité du code.
- Correction de bugs mineurs dans l'interface utilisateur.
- Ajout de tests pour les nouvelles fonctionnalités.
- Correction de problèmes de typographie et de grammaire dans les textes.
- Suppression de code inutile et nettoyage du codebase.
