## Changelog : complements-alimentaires (30 derniers jours)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'accessibilité du site, notamment en corrigeant des points soulevés par les normes RGAA. Des améliorations ont également été apportées à l'interface utilisateur, en particulier pour les tableaux et les formulaires, afin de les rendre plus conviviales et accessibles. Enfin, des mises à jour de dépendances ont été effectuées pour assurer la sécurité et la stabilité de l'application.

### Évolutions fonctionnelles
- Amélioration de l'accessibilité des champs de saisie de quantités avec des labels plus explicites. [#2712, #2714, #2715, #2716, #2717, #2718, #2719]
- Correction des titres hiérarchiques de la section "composition info" sur les vues "pro" et "bepias". [#2721]
- Amélioration de l'accessibilité des sélecteurs d'entreprises avec des labels conformes aux normes RGAA. [#2723]
- Remplacement des cases à cocher par des interrupteurs (toggle switches) pour la conformité RGAA 11.2 dans la section "Composition". [#2720]
- Ajout de la possibilité de modifier les déclarations sans entreprises mandatées. [#2734]
- Amélioration de la gestion des erreurs affichées lors de la soumission de formulaires. [#2753]
- Correction d'erreurs sur l'onglet "Soumettre". [#2753]

### Évolutions techniques
- Mise à jour de plusieurs dépendances : Django (6.0.2 -> 6.0.3), pypdf (6.6.2 -> 6.7.1 -> 6.7.2 -> 6.7.4 -> 6.7.5), pillow (12.1.0 -> 12.1.1), ruff (0.14.6 -> 0.14.14), pre-commit (4.5.0 -> 4.5.1), vue-router (4.6.4 -> 5.0.1), @vueuse/core (14.1.0 -> 14.2.0 -> 14.2.1), @babel/core (7.28.6 -> 7.29.0),  soupsieve (2.8 -> 2.8.3), numpy (2.3.5 -> 2.4.2), pandas (2.3.3 -> 3.0.1), phonenumbers (9.0.21 -> 9.0.24), regex (2025.11.3 -> 2026.1.15), reportlab (4.4.4 -> 4.4.10), botocore (1.42.25 -> 1.42.44), qs (6.14.1 -> 6.14.2), @gouvminint/vue-dsfr (8.14.0 -> 8.15.0).
- Mise à jour de la configuration GitHub Actions (workflows `main.yml` et `dependabot.yml`). [#2771]
- Mise à jour de la base de données PostgreSQL dans les workflows GitHub Actions. [#2736]
- Suppression de variables inutilisées. [#2780]

### Autres changements
- Correction du nom de la balise `doctype` pour permettre la génération de nonce.
- Amélioration de la structure des en-têtes sur la page d'accueil et les pages d'historique.
- Suppression de la balise `<i>` obsolète.
- Nettoyage du code et suppression de code inutilisé.
- Ajout d'une migration pour la suppression de l'ANR. [#2689]
- Correction de la structure des breadcrumbs. [#2731]
- Amélioration de l'accessibilité des tableaux. [#2738]
- Ajout de la validation du type MIME des pièces jointes. [#2754]
- Suppression de l'ANR. [#2689]
