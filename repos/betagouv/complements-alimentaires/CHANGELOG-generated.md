## Changelog : complements-alimentaires (30 derniers jours, au 20 mai 2026)

### Résumé
Ce mois-ci, les mises à jour se concentrent sur la maintenance technique du projet, avec de nombreuses mises à jour de dépendances pour assurer la sécurité et la stabilité de l'application. Des améliorations fonctionnelles ont également été apportées, notamment concernant la gestion des plantes inactives et l'automatisation du processus de visa.

### Évolutions fonctionnelles
- Amélioration de la gestion des plantes inactives : Possibilité de rendre les informations additionnelles facultatives pour les plantes inactives [#2896](https://github.com/betagouv/complements-alimentaires/pull/2896).
- Automatisation du processus de visa : Implémentation d'un processus de visa automatique [#2884](https://github.com/betagouv/complements-alimentaires/pull/2884).
- Export des contacts par email : Ajout de la fonctionnalité d'export des contacts par email [#2870](https://github.com/betagouv/complements-alimentaires/pull/2870).
- Correction d'un bug empêchant le mélange des paramètres lors de l'activation de l'auto-visa.
- Amélioration de l'affichage des noms d'unités avec une police de caractères de secours pour une meilleure lisibilité.

### Évolutions techniques
- Mise à jour de nombreuses dépendances : plusieurs bibliothèques Python et JavaScript ont été mises à jour vers leurs dernières versions stables (Django, psycopg2, vue, tailwindcss, etc.) pour bénéficier des correctifs de sécurité et des améliorations de performance.
- Suppression de l'utilisation de `ipdb` et de ses dépendances pour une meilleure sécurité et une réduction de la taille du code.
- Refactorisation des tests unitaires pour une meilleure granularité et maintenabilité.
- Mise à jour de la configuration CI/CD avec les dernières versions des actions GitHub.

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements techniques.
- Nettoyage du code et correction de petites anomalies.
- Mise à jour de la version de boto3 dans les requirements.txt.
- Correction de remarques issues de revues de code.
