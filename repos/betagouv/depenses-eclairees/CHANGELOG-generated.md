## Changelog : depenses-eclairees (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la robustesse du traitement des fichiers (Excel, XLSX, PDF), la qualité de l'extraction de données (RIB, IBAN, SIRET) grâce à des corrections OCR et des validations, ainsi que sur l'amélioration des métriques d'évaluation de la qualité de l'IA. Des optimisations ont également été apportées à l'interface d'administration et à la gestion des files d'attente de traitement.

### Évolutions fonctionnelles
- Amélioration de l'affichage des données CCAP et AE dans l'interface utilisateur.
- Ajout de fonctions pour lister les erreurs de différents types (faux positifs, faux négatifs).
- Amélioration de l'interface d'administration avec des filtres et une meilleure présentation des données.
- Ajout de métriques (précision, rappel) pour évaluer la qualité de l'extraction des données.
- Possibilité de filtrer les batches bloqués dans l'interface d'administration.
- Amélioration de la gestion des fichiers Excel volumineux, avec un seuil de 2Mo et une gestion des fichiers plus grands.
- Reconstruction de l'IBAN à partir des autres codes présents sur les RIB.
- Validation du SIRET via l'algorithme Luhn.

### Évolutions techniques
- Refactorisation de la définition des schémas de données.
- Amélioration de la gestion des erreurs de décodage JSON avec une logique de nouvelle tentative.
- Optimisation du traitement des fichiers XLSX pour éviter les problèmes de mémoire.
- Mise en place d'une file d'attente dédiée pour le traitement OCR.
- Amélioration de la gestion des permissions avec la prise en charge de caractères joker.
- Suppression de la dépendance à Jupyter et remplacement par IPython.
- Amélioration de la gestion des erreurs et ajout de détails dans les logs pour le module OCR.
- Refactorisation des tests end-to-end pour une meilleure clarté et maintenabilité.
- Ajout de métriques d'évaluation de la qualité (détection, précision, hallucinations).
- Amélioration de la gestion des fichiers ZIP en ignorant les répertoires `__MACOSX`.

### Autres changements
- Mise à jour des dépendances.
- Nettoyage du code et suppression de code inutilisé.
- Correction de bugs mineurs et amélioration de la documentation.
- Correction de schémas DC4 et alignement des schémas RIB.
- Suppression du paramètre `--force-analyze` de la commande cron.
- Amélioration des prompts pour l'extraction de dates.
