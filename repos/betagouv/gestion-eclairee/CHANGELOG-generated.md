## Changelog : gestion-eclairee (30 derniers jours, au 22 juillet 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration du traitement des factures électroniques, notamment l'ajout de la prise en charge de nouveaux formats (UBL Invoice 2.1, 2.4) et l'optimisation de l'extraction des données. Des améliorations ont également été apportées à l'infrastructure et aux tests pour une meilleure robustesse et une plus grande facilité de maintenance.

### Évolutions fonctionnelles
- Ajout d'une vue permettant de télécharger des fichiers.
- Prise en charge du format UBL Invoice 2.1 pour le traitement des factures.
- Prise en charge du format UBL Invoice 2.4 et amélioration de la robustesse du traitement XML.
- Amélioration du traitement des factures Factur-X.
- Ajout du traitement des factures XML (testé sur UGAP).
- Ajout du pipeline de traitement XML CPRO avec extraction Factur-X et modèles Pydantic.
- Ajout du champ "ministère" au modèle Facture et implémentation du pipeline de mapping des services.
- Ajout du pipeline de traitement de l'export ODA et des champs GM au modèle Facture.

### Évolutions techniques
- Refactorisation de la gestion des téléchargements pour utiliser le stockage Django.
- Simplification du traitement concurrent.
- Amélioration de l'extraction pivot XML avec une option de répertoire plat et ajout du pipeline d'extraction des factures.
- Ajout de la concurrence au pipeline de traitement.
- Mise à jour des chemins de stockage.
- Ajout d'une dépendance pour le stockage S3.
- Utilisation de Ruff pour le linting du code.
- Ajout d'un test recette.
- Refactorisation de l'affichage des résultats des tests pour un feedback immédiat par fichier.
- Augmentation de la limite de taille des champs CSV pour le traitement des factures.
- Ajout de logging pour suivre la progression de l'exécution du pipeline.
- Ajout d'un fichier `procfile`.
- Correction du mapping des services (plusieurs commits).
- Force de la locale à "fr" pour les téléchargements.
- Installation des librairies nécessaires pour cloakbrowser.

### Autres changements
- Ajout de tests pour le traitement des lignes de facture.
- Suppression de versions obsolètes des schémas XSD UBL-Invoice.
- Refactorisation du code.
- Mise à jour du mapping des services.
- Correction du mapping des services.
