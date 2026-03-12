## Changelog : infomedicament-dataeng (30 derniers jours)

### Résumé
Ce changelog présente les récentes améliorations apportées à l'outil d'ingénierie de données infomedicament-dataeng. Les évolutions se concentrent sur l'ajout de nouvelles fonctionnalités d'importation de données, notamment à partir de data.gouv.fr, ainsi que sur l'amélioration et la stabilisation du module de classification pédiatrique. Des améliorations de la qualité du code et de la configuration ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'une nouvelle commande CLI pour importer les données ASMR/SMR disponibles sur data.gouv.fr.
- Implémentation de l'importation de notices RCP (Résumé des Caractéristiques du Produit) en Python, avec une commande CLI correspondante.
- Amélioration de la classification pédiatrique : prise en compte de motifs d'indications positives, gestion des opérateurs <= et >=, et correction de priorités entre les classes pédiatriques (B > C > A).
- Possibilité de déboguer le processus de classification pédiatrique grâce à un mode debug.
- Gestion des cas où une RCP n'est pas trouvée lors de la classification pédiatrique.
- Utilisation de PostgreSQL pour gérer le mapping CIS-ATC.
- Ajout d'une option pour exporter les résultats en CSV dans un fichier local via la CLI.

### Évolutions techniques
- Ajout de linters et de tests à la CI (Continuous Integration).
- Ajout de hooks pre-commit pour assurer la qualité du code.
- Refactorisation de l'algorithme de classification pédiatrique pour une meilleure paramétrabilité via un fichier de configuration (`pediatrics_conf`).
- Normalisation des chaînes de caractères lors de l'extraction de texte (suppression des guillemets typographiques, des tirets et des symboles ≥ et ≤).
- Renommage du projet en `infomedicament-dataeng`.

### Autres changements
- Refonte de la structure du fichier README pour une meilleure clarté.
- Mise à jour de la description du projet dans le fichier README.
- Correction d'une ancienne modification datant de 18 ans.
