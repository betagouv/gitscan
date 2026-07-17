## Changelog : gestion-eclairee (30 derniers jours, au 15 juillet 2026)

### Résumé
Ce mois-ci, le projet s'est concentré sur l'amélioration significative du traitement des factures électroniques, notamment en ajoutant la prise en charge de nouveaux formats (UBL Invoice 2.4 et 2.1, CPRO) et en renforçant la robustesse de l'extraction des données. Des optimisations ont également été apportées aux pipelines de traitement et aux tests pour une meilleure performance et fiabilité.

### Évolutions fonctionnelles
- Ajout de la prise en charge du format de facture UBL Invoice 2.4, améliorant la compatibilité avec les nouveaux standards.
- Ajout de la prise en charge du format de facture UBL Invoice 2.1.
- Implémentation d'un pipeline de traitement pour les factures CPRO avec extraction Factur-X et modèles Pydantic.
- Ajout du champ "ministère" au modèle Facture et implémentation d'un pipeline de mapping des services.
- Amélioration du traitement des factures Factur-X.
- Ajout d'un pipeline d'exportation des données ODA et ajout des champs GM au modèle Facture.
- Possibilité d'identifier les EJs complémentaires dans Chorus mais pas dans ODA (code commenté).

### Évolutions techniques
- Refonte du pipeline d'extraction XML avec une option de répertoire plat et ajout d'un pipeline d'extraction de factures.
- Simplification du traitement concurrent des fichiers.
- Refactorisation de l'export CSV vers la base de données avec une meilleure gestion des colonnes et du suivi des sources.
- Modification de la clé primaire du modèle User de UUID à BigAutoField.
- Ajout de tests unitaires pour le traitement des lignes de facture et augmentation de la limite de taille des champs CSV.
- Amélioration de l'affichage des résultats des tests pour un feedback plus rapide.
- Ajout de logs pour suivre la progression de l'exécution des pipelines.
- Mise en place d'une concurrence sur les pipelines de traitement.
- Utilisation de Ruff pour le linting et la correction automatique du code.
- Mise à jour des chemins de téléchargement pour utiliser le sous-répertoire gesec.
- Ajout d'un fichier `procfile` pour faciliter le déploiement.
- Ajout d'utilitaires de test pour le dump des tables de la base de données et la comparaison de fichiers CSV.

### Autres changements
- Ajout de dépendance pour le stockage S3.
- Refactorisation générale du code pour améliorer la lisibilité et la maintenabilité.
- Mise à jour des chemins de stockage.
- Ajout de commentaires dans le code pour clarifier certaines parties.
