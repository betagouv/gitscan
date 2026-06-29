## Changelog : gestion-eclairee (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, le projet a connu une avancée significative dans le traitement et l'ingestion de données de dépenses publiques, notamment via l'ajout de pipelines pour les formats CPRO et Factur-X (UGAP).  L'infrastructure a été renforcée pour supporter des volumes de données plus importants et une meilleure gestion des erreurs. Des améliorations ont également été apportées aux tests et à la qualité du code.

### Évolutions fonctionnelles
- Ajout du traitement des fichiers XML de factures (format UGAP) [#5709464](https://github.com/betagouv/gestion-eclairee/commit/5709464).
- Implémentation d'un pipeline pour le traitement des fichiers CPRO XML, incluant l'extraction Factur-X et la définition de modèles Pydantic [#c0a01a7](https://github.com/betagouv/gestion-eclairee/commit/c0a01a7).
- Ajout du champ "ministère" au modèle Facture et implémentation d'un pipeline de mapping des services [#650bed5](https://github.com/betagouv/gestion-eclairee/commit/650bed5).
- Ajout d'un pipeline d'exportation des données ODA et ajout des champs GM au modèle Facture [#4ea4891](https://github.com/betagouv/gestion-eclairee/commit/4ea4891).
- Amélioration de l'export CSV vers la base de données avec une meilleure gestion des colonnes et du suivi de la source des données [#42cf389](https://github.com/betagouv/gestion-eclairee/commit/42cf389).
- Ajout d'utilitaires de test pour le dump de tables de base de données et la comparaison de fichiers CSV [#23c48b3](https://github.com/betagouv/gestion-eclairee/commit/23c48b3).

### Évolutions techniques
- Refactorisation de l'extraction XML pivot avec une option de répertoire plat et ajout d'un pipeline d'extraction de factures [#160f683](https://github.com/betagouv/gestion-eclairee/commit/160f683).
- Mise en place d'une concurrence pour l'exécution des pipelines [#7a7dec1](https://github.com/betagouv/gestion-eclairee/commit/7a7dec1).
- Changement de la clé primaire du modèle User de UUID à BigAutoField et suppression du champ UUID du modèle de base [#729c0d1](https://github.com/betagouv/gestion-eclairee/commit/729c0d1).
- Initialisation d'une application Django et ajout des dépendances nécessaires [#73f32ad](https://github.com/betagouv/gestion-eclairee/commit/73f32ad, #047f61e](https://github.com/betagouv/gestion-eclairee/commit/047f61e, #4ef8ee5](https://github.com/betagouv/gestion-eclairee/commit/4ef8ee5).
- Ajout d'un fichier `procfile` pour faciliter le déploiement [#35e9ac2](https://github.com/betagouv/gestion-eclairee/commit/35e9ac2).
- Refactorisation du code avec l'outil Ruff pour améliorer la qualité et la lisibilité [#5c266a5](https://github.com/betagouv/gestion-eclairee/commit/5c266a5, #31ad612](https://github.com/betagouv/gestion-eclairee/commit/31ad612, #d8c397b](https://github.com/betagouv/gestion-eclairee/commit/d8c397b).

### Autres changements
- Ajout de logs pour suivre la progression de l'exécution des pipelines [#b429324](https://github.com/betagouv/gestion-eclairee/commit/b429324).
- Mise à jour des chemins de téléchargement pour utiliser un sous-répertoire "gesec" [#ec103fd](https://github.com/betagouv/gestion-eclairee/commit/ec103fd).
- Ajout de code commenté pour identifier les EJ complémentaires dans Chorus mais pas dans ODA [#3496484](https://github.com/betagouv/gestion-eclairee/commit/3496484).
- Refactorisation de l'affichage des résultats des tests pour un feedback plus rapide par fichier [#5d138e8](https://github.com/betagouv/gestion-eclairee/commit/5d138e8).
- Augmentation de la limite de taille des champs CSV pour le traitement des factures [#5709464](https://github.com/betagouv/gestion-eclairee/commit/5709464).
