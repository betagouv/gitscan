## Changelog : gestion-eclairee (30 derniers jours, au 2 juillet 2026)

### Résumé
Ce mois-ci, le projet s'est concentré sur l'amélioration du traitement et de l'ingestion de factures électroniques, notamment les formats UBL Invoice et CPRO.  Des améliorations ont été apportées à la robustesse du parsing XML, à la gestion des erreurs et à l'intégration des données dans la base de données. Des optimisations ont également été réalisées pour améliorer la performance des pipelines de traitement.

### Évolutions fonctionnelles
- Ajout du support pour le format UBL Invoice 2.4 et amélioration de la robustesse du traitement XML. [#208f44c](https://github.com/betagouv/gestion-eclairee/commit/208f44c)
- Ajout du traitement pour UBL Invoice 2.1 [#4c9b840](https://github.com/betagouv/gestion-eclairee/commit/4c9b840)
- Ajout du pipeline de traitement XML CPRO avec extraction Factur-X et modèles Pydantic. [#c0a01a7](https://github.com/betagouv/gestion-eclairee/commit/c0a01a7)
- Ajout du traitement des factures XML (testé sur UGAP). [#3ed41d8](https://github.com/betagouv/gestion-eclairee/commit/3ed41d8)
- Ajout du champ "ministère" au modèle Facture et implémentation du pipeline de mapping des services. [#650bed5](https://github.com/betagouv/gestion-eclairee/commit/650bed5)
- Ajout d'un pipeline d'exportation ODA et de champs GM au modèle Facture. [#4ea4891](https://github.com/betagouv/gestion-eclairee/commit/4ea4891)
- Amélioration de la gestion des colonnes et du suivi de la source lors de l'export CSV vers la base de données. [#42cf389](https://github.com/betagouv/gestion-eclairee/commit/42cf389)
- Ajout d'utilitaires de test : dump de tables de base de données et comparaison CSV. [#23c48b3](https://github.com/betagouv/gestion-eclairee/commit/23c48b3)

### Évolutions techniques
- Refactorisation du traitement XML pivot avec option de répertoire plat et ajout du pipeline d'extraction de factures. [#160f683](https://github.com/betagouv/gestion-eclairee/commit/160f683)
- Simplification du traitement concurrent. [#1e0b6d2](https://github.com/betagouv/gestion-eclairee/commit/1e0b6d2)
- Refactorisation du modèle User pour utiliser BigAutoField comme clé primaire. [#729c0d1](https://github.com/betagouv/gestion-eclairee/commit/729c0d1)
- Ajout de logging pour suivre la progression de l'exécution du pipeline. [#b429324](https://github.com/betagouv/gestion-eclairee/commit/b429324)
- Mise en place d'une concurrence sur le pipeline. [#7a7dec1](https://github.com/betagouv/gestion-eclairee/commit/7a7dec1)
- Refactorisation générale du code et amélioration de la lisibilité. [#a6f6e5c](https://github.com/betagouv/gestion-eclairee/commit/a6f6e5c) et [#35e9ac2](https://github.com/betagouv/gestion-eclairee/commit/35e9ac2)
- Ajout d'un fichier `Procfile` pour faciliter le déploiement. [#35e9ac2](https://github.com/betagouv/gestion-eclairee/commit/35e9ac2)
- Mise en place de Django. [#047f61e](https://github.com/betagouv/gestion-eclairee/commit/047f61e)

### Autres changements
- Amélioration de l'affichage des résultats des tests pour un feedback plus rapide. [#5d138e8](https://github.com/betagouv/gestion-eclairee/commit/5d138e8)
- Augmentation de la limite de taille des champs CSV pour le traitement des factures. [#5709464](https://github.com/betagouv/gestion-eclairee/commit/5709464)
- Mise à jour des chemins de téléchargement pour utiliser le sous-répertoire `gesec`. [#ec103fd](https://github.com/betagouv/gestion-eclairee/commit/ec103fd)
- Application de corrections de style avec `ruff`. [#0ebb313](https://github.com/betagouv/gestion-eclairee/commit/0ebb313), [#24c266a](https://github.com/betagouv/gestion-eclairee/commit/24c266a), [#31ad612](https://github.com/betagouv/gestion-eclairee/commit/31ad612), [#d8c397b](https://github.com/betagouv/gestion-eclairee/commit/d8c397b), [#4d8976f](https://github.com/betagouv/gestion-eclairee/commit/4d8976f)
- Ajout de code commenté pour identifier les EJs complémentaires dans Chorus mais pas dans ODA. [#3496484](https://github.com/betagouv/gestion-eclairee/commit/3496484)
- Ajout de validations pour la longueur des EJ et gestion des SERVICES vides. [#632a865](https://github.com/betagouv/gestion-eclairee/commit/632a865)
- Ajout d'un arrondi pour les montants CPRO et exclusion de services/EJ spécifiques des vérifications. [#ebbdc3f](https://github.com/betagouv/gestion-eclairee/commit/ebbdc3f)
